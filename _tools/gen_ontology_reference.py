#!/usr/bin/env python3
"""Generate the OntoSage ontology reference for the documentation site.

Reads the schema-level ontology files of an OntoSage checkout and writes:

* ``_ontology/class/<Local>.md``      one page per class
* ``_ontology/property/<Local>.md``   one page per property
* ``_ontology/vocabulary/<slug>.md``  one page per controlled vocabulary
* the GENERATED blocks of ``_docs/ontology-browser.md``
* the GENERATED block of ``_docs/ontology-extensions.md`` (alignment with Brick and others)
* the GENERATED block of ``_docs/ontology-relationships.md`` (relationship usage counts,
  computed from one building's TTL files when they can be found)

Only schema-level content is published: classes, properties, SKOS concepts, controlled-
vocabulary individuals and SHACL shapes. Building instance data (rooms, sensors, UUIDs) is
never written. A subject that is neither is counted and reported as "left out".

Run from the site root::

    python _tools/gen_ontology_reference.py                 # --source ../OntoSage
    python _tools/gen_ontology_reference.py --source PATH --building bldg1
    python _tools/gen_ontology_reference.py --skip-building # no usage counts

The script deletes and rewrites ``_ontology/`` only, and replaces text only between
``<!-- BEGIN GENERATED: name -->`` and ``<!-- END GENERATED: name -->`` markers in the three
hand-written pages. Output is sorted, so a re-run over unchanged sources changes nothing.

Development notes inside schema comments (where a term came from, tracker references) are
removed sentence by sentence before publication; ``--report FILE`` lists every change.

Requires rdflib (7.x) and PyYAML.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import re
import shutil
import sys
import textwrap
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple

import yaml
from rdflib import BNode, Graph, Literal, Namespace, URIRef
from rdflib.namespace import OWL, RDF, RDFS, SKOS, XSD

# ─────────────────────────────────────────────────────────────────────────────
# Constants
# ─────────────────────────────────────────────────────────────────────────────

SITE_ROOT = Path(__file__).resolve().parent.parent
OUT_DIR_NAME = "_ontology"
BROWSER_PAGE = Path("_docs") / "ontology-browser.md"
RELATIONSHIPS_PAGE = Path("_docs") / "ontology-relationships.md"
EXTENSIONS_PAGE = Path("_docs") / "ontology-extensions.md"

ONTO = "http://ontosage.org/capabilities#"
HBCO = "http://ontosage.org/hbco#"
OUR_NS = (ONTO, HBCO)
ONTOLOGY_IRI = URIRef("http://ontosage.org/ontology")

SH = Namespace("http://www.w3.org/ns/shacl#")
DCTERMS = Namespace("http://purl.org/dc/terms/")
O = Namespace(ONTO)
H = Namespace(HBCO)

BRICK = "https://brickschema.org/schema/Brick#"
REF = "https://brickschema.org/schema/Brick/ref#"
BRICK_EXPLORER = "https://ontology.brickschema.org/1.4/#"
GITHUB_BLOB = "https://github.com/suhasdevmane/OntoSage/blob/main/"

#: Prefixes, in the order the namespaces table lists them. The first two are OntoSage's own.
PREFIXES: List[Tuple[str, str, str]] = [
    ("ontosage", ONTO, "OntoSage Conversational Building Vocabulary (OCBV) terms"),
    ("hbco", HBCO, "Human-Building Conversation Ontology: lay-term concepts"),
    ("brick", BRICK, "Brick Schema 1.4"),
    ("ref", REF, "Brick external references (timeseries linkage)"),
    (
        "ashrae",
        "http://data.ashrae.org/standard223#",
        "ASHRAE Standard 223P; OntoSage's TTL binds it to the prefix ashrae:",
    ),
    ("rec", "https://w3id.org/rec#", "RealEstateCore"),
    ("bot", "https://w3id.org/bot#", "Building Topology Ontology"),
    ("sosa", "http://www.w3.org/ns/sosa/", "Sensor, Observation, Sample, Actuator"),
    ("qudt", "http://qudt.org/schema/qudt/", "QUDT quantities and units"),
    ("rdf", str(RDF), "RDF"),
    ("rdfs", str(RDFS), "RDF Schema"),
    ("owl", str(OWL), "Web Ontology Language"),
    ("xsd", str(XSD), "XML Schema datatypes"),
    ("skos", str(SKOS), "Simple Knowledge Organization System"),
    ("sh", str(SH), "SHACL shapes"),
    ("dcterms", str(DCTERMS), "Dublin Core terms"),
    ("vann", "http://purl.org/vocab/vann/", "Vocabulary annotation"),
]

#: Files read, relative to the OntoSage checkout. All are schema-level by design.
SOURCE_FILES = [
    "ontology/ontosage_schema.ttl",
    "ontology/hbco_core.ttl",
    "ontology/hbco_mappings.ttl",
    "ontology/measurand_kinds.ttl",
    "ontology/ontosage_capabilities.ttl",
]
RECORD_DIR = "ontology/record_documents"

PROPERTY_TYPES = {
    OWL.ObjectProperty: "object",
    OWL.DatatypeProperty: "datatype",
    OWL.AnnotationProperty: "annotation",
}

#: Controlled vocabularies: (slug, title, member class, intro sentence).
VOCABULARIES = [
    (
        "question-intents",
        "Question intents",
        O.QuestionIntent,
        "The kinds of question a stakeholder asks, each with cue phrases and the source types "
        "that usually answer it.",
    ),
    (
        "stakeholder-roles",
        "Stakeholder roles",
        O.StakeholderRole,
        "Conversational personas. A role frames how an answer is phrased; it does not grant or "
        "restrict access (that is RBAC, a separate mechanism).",
    ),
    (
        "source-types",
        "Answer source types",
        O.SourceType,
        "The kinds of system an answer can be grounded in.",
    ),
    (
        "capability-categories",
        "Capability categories",
        SKOS.Concept,
        "SKOS concepts used as `ontosage:capabilityCategory` values and as the categories a "
        "stakeholder role `ontosage:asksAbout`.",
    ),
]

LAY_PREDICATES = {O.layTerms, H.layTerm, O.qualifierTerms, O.intentPattern}
#: Literal values never altered by the publication filter: they are vocabulary, not prose.
UNSANITISED = LAY_PREDICATES | {O.exampleSparql, H.conceptId, RDFS.label, SKOS.prefLabel}

RELATIONSHIP_PREDICATES: List[Tuple[str, str]] = [
    # (group, IRI)
    ("Composition and location", BRICK + "hasLocation"),
    ("Composition and location", BRICK + "isLocationOf"),
    ("Composition and location", BRICK + "hasPart"),
    ("Composition and location", BRICK + "isPartOf"),
    ("Points and equipment", BRICK + "hasPoint"),
    ("Points and equipment", BRICK + "isPointOf"),
    ("Points and equipment", BRICK + "feeds"),
    ("Points and equipment", BRICK + "isFedBy"),
    ("Points and equipment", BRICK + "controls"),
    ("Points and equipment", BRICK + "measures"),
    ("Points and equipment", BRICK + "isAssociatedWith"),
    ("Points and equipment", BRICK + "hasUnit"),
    ("Points and equipment", "http://qudt.org/schema/qudt/hasUnit"),
    ("Timeseries linkage", REF + "hasExternalReference"),
    ("Timeseries linkage", "http://data.ashrae.org/standard223#hasExternalReference"),
    ("Timeseries linkage", BRICK + "hasExternalReference"),
    ("Timeseries linkage", REF + "hasTimeseriesId"),
    ("Timeseries linkage", BRICK + "hasTimeseriesId"),
    ("Timeseries linkage", REF + "storedAt"),
]

# ─────────────────────────────────────────────────────────────────────────────
# Publication filter: development notes inside rdfs:comment literals
# ─────────────────────────────────────────────────────────────────────────────

#: Phrase substitutions applied before sentence filtering.
_SUBSTITUTIONS = [
    (re.compile(r"\s*\((?:[^()]*\bMaster Report\b[^()]*|Table \d+)\)"), ""),
    (re.compile(r"\bthe Master Report's\b"), "the"),
    (re.compile(r"\bthe Master Report requires\b"), "OntoSage requires"),
    (re.compile(r"\s*\([^()]*\bcorpus\b[^()]*\)", re.IGNORECASE), ""),
    (re.compile(r",?\s+in the whole corpus", re.IGNORECASE), ""),
    # Phrases that cite the development question catalogues, reworded to the rule they state.
    (re.compile(r"\bthe catalogues are explicit that a planned figure"), "a planned figure"),
    (re.compile(r"\bwhich the catalogues want REPORTED"), "which should be REPORTED"),
    (
        re.compile(r"\bthe catalogues require conflicting originals to be preserved"),
        "conflicting originals are preserved",
    ),
    (re.compile(r"\bthe catalogues ask about SERVICE health, and "), ""),
    (re.compile(r"\bthe catalogues limit person-level detail to an authorised case, and "), ""),
    (
        re.compile(
            r"\bV\d+-T\d+ holds identity at role level and the catalogues forbid exposing who "
            r"holds what, so"
        ),
        "identity is held at role level, so",
    ),
    (
        re.compile(
            r"\bThe catalogues ask what a restricted area requires and forbid exposing who holds "
            r"what, so the answerable form is"
        ),
        "The answerable form is",
    ),
]
#: A sentence matching this is a development note and is not published.
_NOTE_SENTENCE = re.compile(
    r"(\b(?:the|this|whole|survey|seed|stakeholder) corpus\b"
    r"|\bcatalogues?\b"
    r"|stakeholder capture"
    r"|\bunanswered\b"
    r"|\bcomputed at \d"
    r"|\bAdded (?:because|after)\b"
    r"|\bmeasured live\b"
    r"|\b(?:BUG|CAVEAT|TODO|FIX|NOTE|KNOWN)-\d+"
    r"|\bV\d+-T\d+\b"
    r"|\bMaster Report\b"
    r"|\bthe paper\b"
    r"|\d[\d,]* (?:stakeholder )?questions\b)",
    re.IGNORECASE,
)
_SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z\"'(])")


def sanitise_text(text: str) -> str:
    """Remove development notes from a schema literal; return the published text."""
    out = text
    for pattern, repl in _SUBSTITUTIONS:
        out = pattern.sub(repl, out)
    if not _NOTE_SENTENCE.search(out):
        return out
    sentences = _SENTENCE_SPLIT.split(out.strip())
    kept = [s for s in sentences if not _NOTE_SENTENCE.search(s)]
    return " ".join(kept).strip()


# ─────────────────────────────────────────────────────────────────────────────
# Graph helpers
# ─────────────────────────────────────────────────────────────────────────────


def in_our_ns(term) -> bool:
    """True for an IRI in the ontosage: or hbco: namespace."""
    return isinstance(term, URIRef) and str(term).startswith(OUR_NS)


def local_name(term) -> str:
    """The local part of an IRI."""
    s = str(term)
    for sep in ("#", "/"):
        if sep in s:
            s = s.rsplit(sep, 1)[-1]
    return s


def curie(term) -> str:
    """A compact name for an IRI, or the IRI in angle brackets."""
    s = str(term)
    best = None
    for prefix, ns, _ in PREFIXES:
        if s.startswith(ns) and len(s) > len(ns):
            if best is None or len(ns) > len(best[1]):
                best = (prefix, ns)
    if best:
        return f"{best[0]}:{s[len(best[1]):]}"
    return f"<{s}>"


def sort_key(term) -> str:
    """Case-insensitive sort key for a term."""
    return curie(term).lower()


def canonicalise_bnodes(g: Graph) -> Graph:
    """Rename blank nodes by a hash of their content, so serialisation order is stable."""
    memo: Dict[BNode, str] = {}

    def sig(b: BNode, stack: Tuple[BNode, ...] = ()) -> str:
        if b in memo:
            return memo[b]
        if b in stack:
            return "cycle"
        parts = []
        for p, o in g.predicate_objects(b):
            ov = "_:" + sig(o, stack + (b,)) if isinstance(o, BNode) else o.n3()
            parts.append(p.n3() + " " + ov)
        h = "b" + hashlib.sha1("\n".join(sorted(parts)).encode("utf-8")).hexdigest()[:16]
        memo[b] = h
        return h

    out = Graph(bind_namespaces="none")
    for s, p, o in g:
        s2 = BNode(sig(s)) if isinstance(s, BNode) else s
        o2 = BNode(sig(o)) if isinstance(o, BNode) else o
        out.add((s2, p, o2))
    return out


def bnode_closure(g: Graph, subjects: Iterable) -> Set:
    """The subjects plus every blank node reachable from them."""
    seen: Set = set()
    todo = list(subjects)
    while todo:
        s = todo.pop()
        if s in seen:
            continue
        seen.add(s)
        for o in g.objects(s, None):
            if isinstance(o, BNode) and o not in seen:
                todo.append(o)
    return seen


def turtle_for(g: Graph, subjects: Iterable) -> str:
    """Serialise the triples of the given subjects (and their blank nodes) as Turtle."""
    sub = Graph(bind_namespaces="none")
    for prefix, ns, _ in PREFIXES:
        sub.bind(prefix, ns)
    for s in bnode_closure(g, subjects):
        for t in g.triples((s, None, None)):
            sub.add(t)
    if len(sub) == 0:
        return ""
    text = sub.serialize(format="turtle")
    return text.strip() + "\n"


# ─────────────────────────────────────────────────────────────────────────────
# Markdown helpers
# ─────────────────────────────────────────────────────────────────────────────


def liquid_safe(text: str) -> str:
    """Neutralise Liquid delimiters in prose."""
    return (
        text.replace("{{", "&#123;&#123;")
        .replace("{%", "&#123;%")
        .replace("}}", "&#125;&#125;")
        .replace("%}", "%&#125;")
    )


def md(text: str) -> str:
    """Escape free text for a Markdown paragraph."""
    t = " ".join(str(text).split())
    t = t.replace("\\", "\\\\")
    t = t.replace("<", "&lt;").replace(">", "&gt;")
    t = t.replace("*", "\\*").replace("_", "\\_")
    t = t.replace("[", "\\[").replace("]", "\\]")
    t = t.replace("$$", "\\$\\$")
    return liquid_safe(t)


def cell(text: str) -> str:
    """Escape free text for a Markdown table cell."""
    return md(text).replace("|", "\\|")


def code(text: str) -> str:
    """An inline code span (text must not contain a backtick)."""
    t = str(text).replace("`", "'")
    return "`" + liquid_safe(t) + "`"


def url(path: str) -> str:
    """A site-relative URL through Jekyll's relative_url filter."""
    return "{{ '" + path + "' | relative_url }}"


def raw_block(lang: str, body: str) -> str:
    """A fenced code block wrapped in raw tags so Liquid leaves it alone."""
    return "{% raw %}\n```" + lang + "\n" + body.rstrip("\n") + "\n```\n{% endraw %}\n"


def front_matter(title: str, permalink: str) -> str:
    """Front matter for a generated page."""
    return (
        "---\n"
        f"title: {json.dumps(title, ensure_ascii=False)}\n"
        "layout: post\n"
        f"permalink: {permalink}\n"
        "---\n\n"
    )


# ─────────────────────────────────────────────────────────────────────────────
# The model
# ─────────────────────────────────────────────────────────────────────────────


class Model:
    """Everything the pages need, read once from the sources."""

    def __init__(self, source: Path):
        self.source = source
        self.file_graphs: Dict[str, Graph] = {}
        self.left_out: Dict[str, collections.Counter] = {}
        self.kept_triples: Dict[str, int] = {}
        self.sanitised: List[Tuple[str, str, str, str]] = []
        self.warnings: List[str] = []
        self._load()
        self._index()

    # ── loading ──────────────────────────────────────────────────────────────

    def _load(self) -> None:
        union = Graph(bind_namespaces="none")
        self.defined_in: Dict[object, Set[str]] = collections.defaultdict(set)
        for rel in SOURCE_FILES:
            path = self.source / rel
            if not path.exists():
                self.warnings.append(f"missing source file {rel}")
                continue
            g = Graph(bind_namespaces="none")
            g.parse(path, format="turtle")
            keep = self._schema_subjects(g)
            closure = bnode_closure(g, keep)
            dropped: collections.Counter = collections.Counter()
            kept = 0
            for s, p, o in g:
                if s in closure:
                    union.add((s, p, o))
                    kept += 1
                    if not isinstance(s, BNode):
                        self.defined_in[s].add(rel)
                elif not isinstance(s, BNode):
                    types = sorted(curie(t) for t in g.objects(s, RDF.type)) or ["untyped"]
                    dropped[", ".join(types)] += 1
            self.file_graphs[rel] = g
            self.kept_triples[rel] = kept
            self.left_out[rel] = dropped
        union = canonicalise_bnodes(union)
        self.raw = union
        self.g = self._sanitise(union)

    def _schema_subjects(self, g: Graph) -> Set:
        """Subjects of g that are schema-level (never building instances)."""
        schema_types = {
            OWL.Class,
            OWL.ObjectProperty,
            OWL.DatatypeProperty,
            OWL.AnnotationProperty,
            OWL.Ontology,
            SH.NodeShape,
            SKOS.ConceptScheme,
            SKOS.Concept,
        }
        vocab_types = {
            O.QuestionIntent,
            O.StakeholderRole,
            O.SourceType,
            O.Measurand,
            H.Concept,
            H.CompositeConcept,
        }
        keep: Set = set()
        for s in set(g.subjects()):
            if isinstance(s, BNode):
                continue
            types = set(g.objects(s, RDF.type))
            if s == ONTOLOGY_IRI or types & schema_types:
                keep.add(s)
            elif in_our_ns(s) and (not types or types & vocab_types):
                # an annotation on an OntoSage term, or a controlled-vocabulary member
                keep.add(s)
            elif str(s).startswith((BRICK, REF)) and not types:
                # statements OntoSage makes about an upstream class (measured quantity kind)
                keep.add(s)
        return keep

    def _sanitise(self, g: Graph) -> Graph:
        out = Graph(bind_namespaces="none")
        for s, p, o in g:
            if isinstance(o, Literal) and "\r" in str(o):
                # a checkout with CRLF line endings puts \r inside multi-line literals
                o = Literal(str(o).replace("\r\n", "\n").replace("\r", "\n"), lang=o.language, datatype=o.datatype)
            if isinstance(o, Literal) and p not in UNSANITISED and o.datatype in (None, XSD.string):
                new = sanitise_text(str(o))
                if new != str(o):
                    self.sanitised.append((curie(s), curie(p), str(o), new))
                    if not new:
                        continue
                    o = Literal(new, lang=o.language, datatype=o.datatype)
            out.add((s, p, o))
        return out

    # ── indexes ──────────────────────────────────────────────────────────────

    def _index(self) -> None:
        g = self.g
        declared = {c for c in g.subjects(RDF.type, OWL.Class) if in_our_ns(c)}
        referenced = set()
        for p in (RDFS.subClassOf, RDFS.domain, RDFS.range, SH.targetClass, RDF.type):
            for s, o in g.subject_objects(p):
                if in_our_ns(o):
                    referenced.add(o)
        props = {}
        for t, kind in PROPERTY_TYPES.items():
            for p in g.subjects(RDF.type, t):
                if in_our_ns(p):
                    props[p] = kind
        undeclared = {c for c in referenced if c not in declared and c not in props}
        # an individual (e.g. a vocabulary member) is referenced by rdf:type of nothing;
        # only keep undeclared terms that are used as a CLASS
        used_as_class = set()
        for p in (RDFS.subClassOf, RDFS.domain, RDFS.range, SH.targetClass):
            used_as_class |= {o for o in g.objects(None, p)}
        for s, o in g.subject_objects(RDF.type):
            used_as_class.add(o)
        undeclared = {c for c in undeclared if c in used_as_class}
        self.declared_classes = declared
        self.undeclared_classes = undeclared
        self.classes = sorted(declared | undeclared, key=sort_key)
        self.props = props
        self.prop_list = sorted(props, key=sort_key)

        self.parents: Dict[URIRef, List[URIRef]] = {}
        self.children: Dict[URIRef, List[URIRef]] = collections.defaultdict(list)
        for c in self.classes:
            ps = sorted(
                [o for o in g.objects(c, RDFS.subClassOf) if isinstance(o, URIRef)], key=sort_key
            )
            self.parents[c] = ps
            for p in ps:
                self.children[p].append(c)
        for k in self.children:
            self.children[k] = sorted(set(self.children[k]), key=sort_key)

        # page slugs: local name, prefixed only on a (case-insensitive) clash
        self.slug: Dict[URIRef, str] = {}
        for group in (self.classes, self.prop_list):
            seen = collections.Counter(local_name(t).lower() for t in group)
            for t in group:
                ln = local_name(t)
                pre = curie(t).split(":", 1)[0]
                self.slug[t] = f"{pre}-{ln}" if seen[ln.lower()] > 1 else ln

        # vocabulary members
        self.vocab_member: Dict[URIRef, Tuple[str, str]] = {}
        self.vocab_lists: Dict[str, List[URIRef]] = {}
        for slug, _title, cls, _intro in VOCABULARIES:
            members = sorted(
                {s for s in g.subjects(RDF.type, cls) if isinstance(s, URIRef)}, key=sort_key
            )
            self.vocab_lists[slug] = members
            for m in members:
                self.vocab_member[m] = (slug, local_name(m))
        concepts = sorted(
            {s for s in g.subjects(RDF.type, H.Concept)}
            | {s for s in g.subjects(RDF.type, H.CompositeConcept)},
            key=lambda t: local_name(t).lower(),
        )
        self.concepts = [c for c in concepts if isinstance(c, URIRef)]
        for c in self.concepts:
            self.vocab_member[c] = ("hbco-concepts", local_name(c))
        self.measurands = sorted(
            {s for s in g.subjects(RDF.type, O.Measurand) if isinstance(s, URIRef)}, key=sort_key
        )
        for m in self.measurands:
            self.vocab_member[m] = ("measurands", local_name(m))
        self.shapes = sorted(
            {s for s in g.subjects(RDF.type, SH.NodeShape) if isinstance(s, URIRef)}, key=sort_key
        )
        for s in self.shapes:
            self.vocab_member[s] = ("shacl-shapes", local_name(s))
        self.schemes = sorted(
            {s for s in g.subjects(RDF.type, SKOS.ConceptScheme)}, key=sort_key
        )

        # record document mappings
        self.mappings = self._load_mappings()

    def _load_mappings(self) -> List[dict]:
        out = []
        d = self.source / RECORD_DIR
        if not d.is_dir():
            self.warnings.append(f"missing {RECORD_DIR}")
            return out
        for path in sorted(d.glob("*.yaml")):
            raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
            raw["_file"] = f"{RECORD_DIR}/{path.name}"
            out.append(raw)
        return out

    # ── queries ──────────────────────────────────────────────────────────────

    def ancestors(self, c: URIRef) -> List[Tuple[URIRef, int]]:
        """Ancestors with their distance; external parents included one level deep."""
        out: Dict[URIRef, int] = {}
        frontier = [(c, 0)]
        while frontier:
            node, dist = frontier.pop(0)
            for p in self.parents.get(node, []):
                if p not in out:
                    out[p] = dist + 1
                    if p in self.parents:
                        frontier.append((p, dist + 1))
        return sorted(out.items(), key=lambda kv: (kv[1], sort_key(kv[0])))

    def descendants(self, c: URIRef) -> Set[URIRef]:
        """All descendants of a class."""
        out: Set[URIRef] = set()
        todo = list(self.children.get(c, []))
        while todo:
            x = todo.pop()
            if x not in out:
                out.add(x)
                todo.extend(self.children.get(x, []))
        return out

    def chains(self, c: URIRef) -> List[List[URIRef]]:
        """Every superclass path from a root down to c."""
        ps = self.parents.get(c, [])
        if not ps:
            return [[c]]
        out = []
        for p in ps:
            if p in self.parents:
                for ch in self.chains(p):
                    out.append(ch + [c])
            else:
                out.append([p, c])
        return out

    def literals(self, s, p) -> List[str]:
        """String values of s p, sorted."""
        return sorted({str(o) for o in self.g.objects(s, p)}, key=lambda x: x.lower())

    def first(self, s, p) -> str:
        """The first string value of s p, or ''."""
        vals = self.literals(s, p)
        return vals[0] if vals else ""

    def label(self, t) -> str:
        """Human label of a term."""
        return self.first(t, RDFS.label) or self.first(t, SKOS.prefLabel) or local_name(t)

    def sources_of(self, t) -> List[str]:
        """Source files declaring a term."""
        return sorted(self.defined_in.get(t, set()))

    def was_sanitised(self, subjects: Iterable) -> bool:
        names = {curie(s) for s in subjects}
        return any(row[0] in names for row in self.sanitised)


# ─────────────────────────────────────────────────────────────────────────────
# Links
# ─────────────────────────────────────────────────────────────────────────────


def page_path(m: Model, t: URIRef) -> Optional[str]:
    """Site path of a generated page for a term, or None."""
    if t in m.slug and t in m.props:
        return f"/ontology/property/{m.slug[t]}/"
    if t in m.slug:
        return f"/ontology/class/{m.slug[t]}/"
    if t in m.vocab_member:
        slug, anchor = m.vocab_member[t]
        return f"/ontology/vocabulary/{slug}/#{anchor}"
    return None


def external_url(t: URIRef) -> Optional[str]:
    """Where an upstream term is documented."""
    s = str(t)
    if s.startswith(BRICK):
        return BRICK_EXPLORER + "brick:" + s[len(BRICK) :]
    if s.startswith(REF):
        return BRICK_EXPLORER + "ref:" + s[len(REF) :]
    if s.startswith(("https://w3id.org/", "http://www.w3.org/ns/sosa/", "http://qudt.org/")):
        return s
    return None


def link(m: Model, t) -> str:
    """A Markdown link (or code span) for a term."""
    if isinstance(t, Literal):
        return code(str(t))
    if isinstance(t, BNode):
        # An anonymous class such as `rdfs:domain [ owl:unionOf ( A B C ) ]` reads as "A or B or C".
        from rdflib.collection import Collection

        for kind, joiner in ((OWL.unionOf, " or "), (OWL.intersectionOf, " and ")):
            head = m.g.value(t, kind)
            if head is not None:
                try:
                    members = list(Collection(m.g, head))
                except Exception:
                    members = []
                if members:
                    return joiner.join(link(m, x) for x in members)
        return "(blank node)"
    path = page_path(m, t)
    if path:
        if "#" in path:
            base, anchor = path.split("#", 1)
            return f"[{code(curie(t))}]({url(base)}#{anchor})"
        return f"[{code(curie(t))}]({url(path)})"
    ext = external_url(t)
    if ext:
        return f"[{code(curie(t))}]({ext})"
    return code(curie(t))


def source_links(m: Model, t) -> str:
    """Links to the source files of a term."""
    files = m.sources_of(t)
    if not files:
        return "not declared in the schema files"
    return ", ".join(f"[{code(f)}]({GITHUB_BLOB}{f})" for f in files)


def breadcrumb(*parts: str) -> str:
    """The breadcrumb line at the top of a generated page."""
    first = f"[Ontology Browser]({url('/docs/ontology-browser/')})"
    return " › ".join([first, *parts]) + "\n\n"


# ─────────────────────────────────────────────────────────────────────────────
# Page writers
# ─────────────────────────────────────────────────────────────────────────────


#: An example written as a triple ("bldg:X ontosage:p bldg:Y .") is shown as code.
_TRIPLE_LIKE = re.compile(r"^[A-Za-z][\w-]*:\S+\s+[A-Za-z][\w-]*:\S+")


def definition_block(m: Model, t) -> str:
    """Definition, description and examples of a term."""
    out = []
    defs = m.literals(t, SKOS.definition)
    comments = m.literals(t, RDFS.comment)
    if defs:
        out.append("## Definition\n\n" + "\n\n".join(md(d) for d in defs) + "\n")
        if comments:
            out.append("## Description\n\n" + "\n\n".join(md(c) for c in comments) + "\n")
    elif comments:
        out.append("## Definition\n\n" + "\n\n".join(md(c) for c in comments) + "\n")
    else:
        out.append("## Definition\n\nThe schema gives no definition for this term.\n")
    examples = m.literals(t, SKOS.example)
    if examples:
        out.append(
            "## Examples\n\n"
            + "".join(f"- {code(e) if _TRIPLE_LIKE.match(e) else md(e)}\n" for e in examples)
        )
    return "\n".join(out)


def lay_terms_block(m: Model, t) -> str:
    """Lay terms and qualifier terms declared on a term."""
    out = []
    for p, title, note in (
        (
            O.layTerms,
            "Lay terms",
            "Plain-language phrases declared on this term with `ontosage:layTerms`. A question "
            "that contains one of them can be matched to this term.",
        ),
        (
            O.qualifierTerms,
            "Qualifier terms",
            "Terms that name this class only when used of it, declared with "
            "`ontosage:qualifierTerms`.",
        ),
        (H.layTerm, "Lay terms", "Declared with `hbco:layTerm`."),
    ):
        vals = m.literals(t, p)
        if vals:
            out.append(
                f"## {title}\n\n{note} ({len(vals)})\n\n" + ", ".join(code(v) for v in vals) + "\n"
            )
    return "\n".join(out)


def alignments_block(m: Model, t) -> str:
    """SKOS mappings and related terms."""
    rows = []
    for p in (SKOS.exactMatch, SKOS.closeMatch, SKOS.relatedMatch, SKOS.related):
        for o in sorted(m.g.objects(t, p), key=sort_key):
            rows.append(f"| {code(curie(p))} | {link(m, o)} |\n")
    if not rows:
        return ""
    return "## Alignments\n\n| Mapping | Term |\n|---|---|\n" + "".join(rows)


def competency_block(m: Model, t) -> str:
    """Competency questions and example SPARQL."""
    out = []
    cqs = m.literals(t, O.competencyQuestion)
    if cqs:
        out.append("## Competency questions\n\n" + "".join(f"- {md(q)}\n" for q in cqs))
    for q in m.literals(t, O.exampleSparql):
        body = textwrap.dedent(q.strip("\n")).strip()
        out.append("## Example SPARQL\n\n" + raw_block("sparql", body))
    return "\n".join(out)


def turtle_block(m: Model, subjects: List) -> str:
    """The Turtle section of a page."""
    text = turtle_for(m.g, subjects)
    if not text:
        return "## Turtle\n\nNo triples in the schema files have this term as their subject.\n"
    note = ""
    if m.was_sanitised(subjects):
        note = (
            "Development notes were removed from one or more text values below; the source "
            "file holds the full text.\n\n"
        )
    return "## Turtle\n\n" + note + raw_block("turtle", text)


def mapping_rows_for_class(m: Model, c: URIRef) -> List[dict]:
    """Record document mappings whose target class is c."""
    out = []
    for mp in m.mappings:
        cls = expand(mp.get("class", ""))
        if cls == c:
            out.append(mp)
    return out


def expand(name: str) -> Optional[URIRef]:
    """Expand a CURIE used in a mapping file."""
    if not name or ":" not in name:
        return None
    pre, loc = name.split(":", 1)
    for prefix, ns, _ in PREFIXES:
        if prefix == pre:
            return URIRef(ns + loc)
    return None


def write_class_page(m: Model, c: URIRef, out_dir: Path) -> None:
    """One class page."""
    g = m.g
    parts = [front_matter(curie(c), f"/ontology/class/{m.slug[c]}/")]
    parts.append(breadcrumb(f"[Classes]({url('/docs/ontology-browser/')}#class-hierarchy)", md(local_name(c))))
    deprecated = any(str(v).lower() == "true" for v in g.objects(c, OWL.deprecated))
    rows = [
        f"| IRI | {code(str(c))} |\n",
        f"| Label | {cell(m.label(c))} |\n",
        f"| Defined in | {source_links(m, c)} |\n",
    ]
    if deprecated:
        rows.append("| Status | deprecated |\n")
    parts.append("| Field | Value |\n|---|---|\n" + "".join(rows) + "\n")
    if c in m.undeclared_classes:
        users = sorted(
            {s for p in (RDFS.subClassOf, RDFS.domain, RDFS.range) for s in g.subjects(p, c)},
            key=sort_key,
        )
        parts.append(
            "This class is used in the schema but not declared with `rdf:type owl:Class` in "
            f"the schema files. {len(users)} term(s) refer to it.\n\n"
        )
    parts.append(definition_block(m, c) + "\n")
    lay = lay_terms_block(m, c)
    if lay:
        parts.append(lay + "\n")

    # hierarchy
    parts.append("## Class hierarchy\n\n")
    chains = m.chains(c)
    if chains == [[c]]:
        parts.append("Superclasses: none (a root class).\n\n")
    else:
        parts.append("Superclasses:\n\n")
        for ch in chains:
            parts.append("- " + " › ".join(link(m, x) if x != c else f"**{code(curie(x))}**" for x in ch) + "\n")
        parts.append("\n")
    kids = m.children.get(c, [])
    if kids:
        desc = m.descendants(c)
        parts.append(f"Direct subclasses ({len(kids)}; {len(desc)} descendants in all):\n\n")
        parts.append("".join(f"- {link(m, k)} {cell(m.label(k))}\n" for k in kids) + "\n")
    else:
        parts.append("Subclasses: none.\n\n")

    # properties with this class (or an ancestor) as domain
    anc = [(c, 0)] + m.ancestors(c)
    prows = []
    for owner, dist in anc:
        for p in sorted(g.subjects(RDFS.domain, owner), key=sort_key):
            if p not in m.props:
                continue
            ranges = sorted(g.objects(p, RDFS.range), key=sort_key)
            rng = ", ".join(link(m, r) for r in ranges) or "not declared"
            where = "this class" if owner == c else link(m, owner)
            prows.append(f"| {link(m, p)} | {m.props[p]} | {rng} | {where} |\n")
    parts.append("## Properties\n\n")
    if prows:
        parts.append(
            "Properties whose `rdfs:domain` is this class or one of its superclasses.\n\n"
            "| Property | Kind | Range | Domain |\n|---|---|---|---|\n" + "".join(prows) + "\n"
        )
    else:
        parts.append("No property declares this class (or a superclass) as its domain.\n\n")

    rrows = []
    for p in sorted(g.subjects(RDFS.range, c), key=sort_key):
        if p not in m.props:
            continue
        doms = sorted(g.objects(p, RDFS.domain), key=sort_key)
        dom = ", ".join(link(m, d) for d in doms) or "any"
        rrows.append(f"| {link(m, p)} | {m.props[p]} | {dom} |\n")
    if rrows:
        parts.append(
            "## Used as the range of\n\n| Property | Kind | Domain |\n|---|---|---|\n"
            + "".join(rrows)
            + "\n"
        )

    # shapes
    shapes = [s for s in m.shapes if any(t in [x for x, _ in anc] for t in g.objects(s, SH.targetClass))]
    if shapes:
        parts.append("## SHACL shapes\n\n")
        for s in shapes:
            tgt = ", ".join(link(m, t) for t in g.objects(s, SH.targetClass))
            parts.append(f"- {link(m, s)} targets {tgt}\n")
            for b in sorted(g.objects(s, SH.property), key=str):
                parts.append(f"  - {shape_constraint(m, b)}\n")
        parts.append("\n")

    # quantity kind
    qk = sorted(g.objects(c, O.measuresQuantityKind), key=sort_key)
    if qk:
        parts.append(
            "## Measured quantity\n\n`ontosage:measuresQuantityKind` "
            + ", ".join(link(m, q) for q in qk)
            + "\n\n"
        )

    al = alignments_block(m, c)
    if al:
        parts.append(al + "\n")

    for mp in mapping_rows_for_class(m, c):
        rt = str(mp.get("record_type", ""))
        parts.append(
            "## Record document mapping\n\n"
            f"Record documents of type {code(rt)} are lifted into instances of this class "
            f"([mapping]({url('/ontology/vocabulary/record-document-mappings/')}#{rt})).\n\n"
        )

    for slug, title, cls, _ in VOCABULARIES:
        if cls == c:
            n = len(m.vocab_lists[slug])
            parts.append(
                f"## Members\n\nThe schema declares {n} members of this class: see "
                f"[{title}]({url('/ontology/vocabulary/' + slug + '/')}).\n\n"
            )
    if c in (H.Concept, H.CompositeConcept):
        n = sum(1 for x in m.concepts if (x, RDF.type, c) in g)
        extra = ""
        if c == H.Concept:
            k = sum(1 for x in m.concepts if (x, RDF.type, H.CompositeConcept) in g)
            extra = f", and {k} typed with its subclass `hbco:CompositeConcept`"
        parts.append(
            f"## Members\n\n`ontology/hbco_mappings.ttl` declares {n} individuals typed with this "
            f"class directly{extra}: see "
            f"[HBCO concepts]({url('/ontology/vocabulary/hbco-concepts/')}).\n\n"
        )
    if c == O.Measurand:
        parts.append(
            f"## Members\n\nThe schema declares {len(m.measurands)} measurands: see "
            f"[Measurands]({url('/ontology/vocabulary/measurands/')}).\n\n"
        )

    comp = competency_block(m, c)
    if comp:
        parts.append(comp + "\n")
    parts.append(turtle_block(m, [c]))
    (out_dir / "class" / f"{m.slug[c]}.md").write_text("".join(parts), encoding="utf-8", newline="\n")


def shape_constraint(m: Model, b) -> str:
    """One-line description of a SHACL property constraint."""
    g = m.g
    bits = []
    for p, name in ((SH.path, "path"), (SH.minCount, "min"), (SH.maxCount, "max"), (SH.datatype, "datatype")):
        for o in g.objects(b, p):
            bits.append(f"{name} {link(m, o) if isinstance(o, URIRef) else code(str(o))}")
    msg = m.first(b, SH.message)
    return "; ".join(bits) + (f". {md(msg)}" if msg else "")


def write_property_page(m: Model, p: URIRef, out_dir: Path) -> None:
    """One property page."""
    g = m.g
    parts = [front_matter(curie(p), f"/ontology/property/{m.slug[p]}/")]
    parts.append(breadcrumb(f"[Properties]({url('/docs/ontology-browser/')}#property-index)", md(local_name(p))))
    doms = sorted(g.objects(p, RDFS.domain), key=sort_key)
    rngs = sorted(g.objects(p, RDFS.range), key=sort_key)
    supers = sorted(g.objects(p, RDFS.subPropertyOf), key=sort_key)
    inverses = sorted(set(g.objects(p, OWL.inverseOf)) | set(g.subjects(OWL.inverseOf, p)), key=sort_key)
    subs = sorted(g.subjects(RDFS.subPropertyOf, p), key=sort_key)
    dom_txt = ", ".join(link(m, d) for d in doms) or "not declared (any subject)"
    if len(doms) > 1:
        dom_txt += " (RDFS reads several domains as their intersection)"
    rows = [
        f"| IRI | {code(str(p))} |\n",
        f"| Label | {cell(m.label(p))} |\n",
        f"| Kind | {m.props[p]} property |\n",
        f"| Domain | {dom_txt} |\n",
        f"| Range | {', '.join(link(m, r) for r in rngs) or 'not declared'} |\n",
        f"| Inverse | {', '.join(link(m, i) for i in inverses) or 'none declared'} |\n",
        f"| Sub-property of | {', '.join(link(m, s) for s in supers) or 'none'} |\n",
    ]
    if subs:
        rows.append(f"| Sub-properties | {', '.join(link(m, s) for s in subs)} |\n")
    rows.append(f"| Defined in | {source_links(m, p)} |\n")
    if any(str(v).lower() == "true" for v in g.objects(p, OWL.deprecated)):
        rows.append("| Status | deprecated |\n")
    parts.append("| Field | Value |\n|---|---|\n" + "".join(rows) + "\n")
    parts.append(definition_block(m, p) + "\n")
    al = alignments_block(m, p)
    if al:
        parts.append(al + "\n")

    users = sorted({s for s in g.subjects(p, None) if isinstance(s, URIRef)}, key=sort_key)
    if users:
        parts.append(
            f"## Used in the schema\n\n{len(users)} schema term(s) carry this property:\n\n"
            + "".join(f"- {link(m, u)}\n" for u in users)
            + "\n"
        )
    rows = []
    for mp in m.mappings:
        for col, spec in sorted((mp.get("columns") or {}).items()):
            if isinstance(spec, dict) and expand(str(spec.get("predicate", ""))) == p:
                rt = str(mp.get("record_type", ""))
                rows.append(
                    f"| [{code(rt)}]({url('/ontology/vocabulary/record-document-mappings/')}#{rt}) "
                    f"| {code(col)} | {code(spec.get('datatype', 'xsd:string'))} |\n"
                )
    if rows:
        parts.append(
            "## Used in record document mappings\n\n"
            "| Record type | Column | Datatype |\n|---|---|---|\n" + "".join(sorted(rows)) + "\n"
        )
    parts.append(turtle_block(m, [p]))
    (out_dir / "property" / f"{m.slug[p]}.md").write_text("".join(parts), encoding="utf-8", newline="\n")


def write_simple_vocab(m: Model, slug: str, title: str, cls: URIRef, intro: str, out_dir: Path) -> None:
    """A vocabulary page for a small set of individuals."""
    g = m.g
    members = m.vocab_lists[slug]
    parts = [front_matter(title, f"/ontology/vocabulary/{slug}/")]
    parts.append(breadcrumb(f"[Vocabularies]({url('/docs/ontology-browser/')}#vocabularies)", md(title)))
    parts.append(
        f"{intro} Members are instances of {link(m, cls)}. "
        f"The schema declares {len(members)}.\n\n"
    )
    if cls == SKOS.Concept:
        for sch in m.schemes:
            parts.append(f"Concept scheme: {code(curie(sch))} ({cell(m.label(sch))}).\n\n")
    parts.append("| Member | Label |\n|---|---|\n")
    for x in members:
        parts.append(f"| [{code(curie(x))}](#{local_name(x)}) | {cell(m.label(x))} |\n")
    parts.append("\n")
    skip = {RDF.type, RDFS.label, RDFS.comment, SKOS.prefLabel, OWL.deprecated}
    for x in members:
        parts.append(f"## {md(m.label(x))} {{#{local_name(x)}}}\n\n")
        rows = [f"| IRI | {code(str(x))} |\n"]
        if any(str(v).lower() == "true" for v in g.objects(x, OWL.deprecated)):
            rows.append("| Status | deprecated |\n")
        for pr in sorted({pp for pp in g.predicates(x, None)} - skip, key=sort_key):
            vals = sorted(g.objects(x, pr), key=lambda o: str(o).lower())
            rendered = ", ".join(link(m, v) if isinstance(v, URIRef) else cell(str(v)) for v in vals)
            rows.append(f"| {link(m, pr)} | {rendered} |\n")
        parts.append("| Field | Value |\n|---|---|\n" + "".join(rows) + "\n")
        for cmt in m.literals(x, RDFS.comment):
            parts.append(md(cmt) + "\n\n")
    parts.append(turtle_block(m, list(members) + list(m.schemes if cls == SKOS.Concept else [])))
    (out_dir / "vocabulary" / f"{slug}.md").write_text("".join(parts), encoding="utf-8", newline="\n")


def write_concepts_page(m: Model, out_dir: Path) -> None:
    """The HBCO lay-term concepts."""
    g = m.g
    comps = [c for c in m.concepts if (c, RDF.type, H.CompositeConcept) in g]
    atoms = [c for c in m.concepts if c not in comps]
    n_terms = sum(len(m.literals(c, H.layTerm)) for c in m.concepts)
    brick_classes = sorted({o for c in m.concepts for o in g.objects(c, H.mapsToBrickClass)}, key=sort_key)
    parts = [front_matter("HBCO concepts", "/ontology/vocabulary/hbco-concepts/")]
    parts.append(breadcrumb(f"[Vocabularies]({url('/docs/ontology-browser/')}#vocabularies)", "HBCO concepts"))
    parts.append(
        "The Human-Building Conversation Ontology (HBCO) maps the words occupants use for the "
        "indoor environment to the Brick sensor classes whose readings answer them. Each "
        f"concept is an individual of {link(m, H.Concept)}; a "
        f"{link(m, H.CompositeConcept)} combines several. The concept resolver matches a "
        "question against the lay terms, then uses `hbco:mapsToBrickClass` to find sensors "
        "and `hbco:requiresRecipe` to choose how to evaluate the readings.\n\n"
        f"Source: [{code('ontology/hbco_mappings.ttl')}]({GITHUB_BLOB}ontology/hbco_mappings.ttl). "
        f"It declares {len(m.concepts)} concepts ({len(atoms)} atomic, {len(comps)} composite) "
        f"with {n_terms} lay terms, mapped to {len(brick_classes)} distinct sensor or point "
        f"classes ({sum(1 for b in brick_classes if str(b).startswith(BRICK))} in the Brick "
        "namespace, the rest OntoSage's own).\n\n"
    )
    parts.append("## Index\n\n| Concept | Type | Maps to | Recipe |\n|---|---|---|---|\n")
    for c in m.concepts:
        kind = "composite" if c in comps else "atomic"
        bc = ", ".join(link(m, o) for o in sorted(g.objects(c, H.mapsToBrickClass), key=sort_key))
        rec = ", ".join(code(r) for r in m.literals(c, H.requiresRecipe))
        parts.append(f"| [{code(curie(c))}](#{local_name(c)}) | {kind} | {bc} | {rec} |\n")
    parts.append("\n")
    for heading, group in (("Composite concepts", comps), ("Atomic concepts", atoms)):
        parts.append(f"## {heading}\n\n")
        for c in group:
            parts.append(f"### {md(m.label(c))} {{#{local_name(c)}}}\n\n")
            rows = [
                f"| IRI | {code(str(c))} |\n",
                f"| Concept ID | {code(m.first(c, H.conceptId))} |\n",
            ]
            bc = ", ".join(link(m, o) for o in sorted(g.objects(c, H.mapsToBrickClass), key=sort_key))
            rows.append(f"| Maps to Brick class | {bc or 'none'} |\n")
            rec = ", ".join(code(r) for r in m.literals(c, H.requiresRecipe))
            if rec:
                rows.append(f"| Recipe | {rec} |\n")
            conf = m.first(c, H.confidence)
            if conf:
                rows.append(f"| Confidence | {cell(conf)} |\n")
            parents = sorted(g.objects(c, H.componentOf), key=sort_key)
            if parents:
                rows.append(f"| Component of | {', '.join(link(m, x) for x in parents)} |\n")
            kids = sorted(g.subjects(H.componentOf, c), key=sort_key)
            if kids:
                rows.append(f"| Components | {', '.join(link(m, x) for x in kids)} |\n")
            terms = m.literals(c, H.layTerm)
            rows.append(f"| Lay terms ({len(terms)}) | {', '.join(code(t) for t in terms)} |\n")
            parts.append("| Field | Value |\n|---|---|\n" + "".join(rows) + "\n")
    (out_dir / "vocabulary" / "hbco-concepts.md").write_text("".join(parts), encoding="utf-8", newline="\n")


def write_measurands_page(m: Model, out_dir: Path) -> None:
    """Measurands and the Brick classes mapped to them."""
    g = m.g
    mapped = sorted(
        {(s, o) for s, o in g.subject_objects(O.measuresQuantityKind)}, key=lambda so: sort_key(so[0])
    )
    parts = [front_matter("Measurands", "/ontology/vocabulary/measurands/")]
    parts.append(breadcrumb(f"[Vocabularies]({url('/docs/ontology-browser/')}#vocabularies)", "Measurands"))
    parts.append(
        f"A {link(m, O.Measurand)} is a quantity a sensor can measure, at the granularity that "
        "tells one gas from another. Each carries the physical range a reading can take (a value "
        "outside it is not treated as a measurement) and a typical range. "
        f"{link(m, O.measuresQuantityKind)} states which measurand a sensor class measures, "
        "independent of where Brick places the class in its hierarchy.\n\n"
        f"Source: [{code('ontology/measurand_kinds.ttl')}]({GITHUB_BLOB}ontology/measurand_kinds.ttl). "
        f"It declares {len(m.measurands)} measurands and {len(mapped)} class-to-measurand "
        "statements.\n\n"
    )
    parts.append(
        "## Measurands\n\n| Measurand | Label | Unit | Physical range | Typical range | Decimals | "
        "Measured by |\n|---|---|---|---|---|---|---|\n"
    )
    for x in m.measurands:
        unit = m.first(x, O.physicalUnit)
        pr = f"{m.first(x, O.physicalMin)} to {m.first(x, O.physicalMax)}"
        tr = f"{m.first(x, O.typicalMin)} to {m.first(x, O.typicalMax)}"
        dec = m.first(x, O.typicalDecimals)
        by = sorted(g.subjects(O.measuresQuantityKind, x), key=sort_key)
        parts.append(
            f'| <span id="{local_name(x)}"></span>{code(local_name(x))} | {cell(m.label(x))} | {cell(unit)} | '
            f"{cell(pr) if unit else ''} | {cell(tr) if unit else ''} | {cell(dec)} | "
            f"{', '.join(link(m, b) for b in by)} |\n"
        )
    parts.append("\n## Band sources\n\nWhere each physical range comes from, as the schema states it.\n\n")
    for x in m.measurands:
        src = m.first(x, O.bandSource)
        cm = m.first(x, RDFS.comment)
        if src or cm:
            parts.append(f"- **{md(m.label(x))}** ({code(local_name(x))}): {md(src or cm)}\n")
    parts.append("\n## Sensor classes and what they measure\n\n| Class | Measures |\n|---|---|\n")
    for s, o in mapped:
        parts.append(f"| {link(m, s)} | {link(m, o)} |\n")
    parts.append("\n")
    props = sorted({p for p in m.props if (p, RDFS.domain, O.Measurand) in g}, key=sort_key)
    if props:
        parts.append("## Properties of a measurand\n\n" + "".join(f"- {link(m, p)}: {cell(m.label(p))}\n" for p in props) + "\n")
    (out_dir / "vocabulary" / "measurands.md").write_text("".join(parts), encoding="utf-8", newline="\n")


def write_shapes_page(m: Model, out_dir: Path) -> None:
    """The SHACL shapes."""
    g = m.g
    parts = [front_matter("SHACL shapes", "/ontology/vocabulary/shacl-shapes/")]
    parts.append(breadcrumb(f"[Vocabularies]({url('/docs/ontology-browser/')}#vocabularies)", "SHACL shapes"))
    parts.append(
        f"The schema declares {len(m.shapes)} SHACL node shapes. Each targets a class and states "
        "the constraints an instance should meet.\n\n"
    )
    for s in m.shapes:
        parts.append(f"## {md(m.label(s))} {{#{local_name(s)}}}\n\n")
        tgt = ", ".join(link(m, t) for t in g.objects(s, SH.targetClass))
        parts.append(f"{code(curie(s))} targets {tgt}.\n\n| Path | Min | Max | Datatype | Message |\n|---|---|---|---|---|\n")
        for b in sorted(g.objects(s, SH.property), key=str):
            path = ", ".join(link(m, o) for o in g.objects(b, SH.path))
            mn = m.first(b, SH.minCount)
            mx = m.first(b, SH.maxCount)
            dt = ", ".join(code(curie(o)) for o in g.objects(b, SH.datatype))
            parts.append(f"| {path} | {cell(mn)} | {cell(mx)} | {dt} | {cell(m.first(b, SH.message))} |\n")
        parts.append("\n" + turtle_block(m, [s]).replace("## Turtle", "### Turtle") + "\n")
    (out_dir / "vocabulary" / "shacl-shapes.md").write_text("".join(parts), encoding="utf-8", newline="\n")


def write_mappings_page(m: Model, out_dir: Path) -> None:
    """Record document mappings (YAML) shipped with the ontology."""
    parts = [front_matter("Record document mappings", "/ontology/vocabulary/record-document-mappings/")]
    parts.append(
        breadcrumb(f"[Vocabularies]({url('/docs/ontology-browser/')}#vocabularies)", "Record document mappings")
    )
    parts.append(
        "A record document is a Markdown file in a building's `documents/` folder with YAML "
        "front matter that names a `record_type`. The mapping for that record type, shipped "
        f"with the ontology in [{code(RECORD_DIR + '/')}]({GITHUB_BLOB.replace('/blob/', '/tree/')}{RECORD_DIR}), "
        "says which class each table row becomes and which predicate each column becomes. "
        f"There are {len(m.mappings)} mappings. "
        f"See [Ontology Relationships]({url('/docs/ontology-relationships/')}#records-and-record-documents) "
        "for how lifting works.\n\n"
    )
    parts.append("| Record type | Class | IRI template |\n|---|---|---|\n")
    for mp in m.mappings:
        rt = str(mp.get("record_type", ""))
        cls = expand(str(mp.get("class", "")))
        parts.append(
            f"| [{code(rt)}](#{rt}) | {link(m, cls) if cls else ''} | {code(mp.get('iri_template', ''))} |\n"
        )
    parts.append("\n")
    for mp in m.mappings:
        rt = str(mp.get("record_type", ""))
        cls = expand(str(mp.get("class", "")))
        parts.append(f"## {md(rt)} {{#{rt}}}\n\n")
        parts.append(
            f"Class {link(m, cls) if cls else code(mp.get('class', ''))}; IRI template "
            f"{code(mp.get('iri_template', ''))}"
            + (f"; label column {code(mp['label_column'])}" if mp.get("label_column") else "")
            + f". Mapping file: [{code(mp['_file'])}]({GITHUB_BLOB}{mp['_file']}).\n\n"
        )
        parts.append("| Column | Predicate | Datatype | Required | Links to | Values |\n|---|---|---|---|---|---|\n")
        for col, spec in (mp.get("columns") or {}).items():
            if not isinstance(spec, dict):
                continue
            pred = expand(str(spec.get("predicate", "")))
            if pred is not None and in_our_ns(pred) and pred not in m.props:
                m.warnings.append(f"mapping {rt}: predicate {spec.get('predicate')} is not declared")
            values = spec.get("values") or {}
            vtxt = "; ".join(
                f"{k}: {', '.join(str(v) for v in (vs or []))}" for k, vs in values.items()
            )
            parts.append(
                f"| {code(col)} | {link(m, pred) if pred else code(spec.get('predicate', ''))} | "
                f"{code(spec.get('datatype', 'xsd:string'))} | {'yes' if spec.get('required') else ''} | "
                f"{code(spec['link']) if spec.get('link') else ''} | {cell(vtxt)} |\n"
            )
        parts.append("\n")
    (out_dir / "vocabulary" / "record-document-mappings.md").write_text(
        "".join(parts), encoding="utf-8", newline="\n"
    )


# ─────────────────────────────────────────────────────────────────────────────
# Browser page blocks
# ─────────────────────────────────────────────────────────────────────────────


def block_summary(m: Model) -> str:
    """Counts, all computed."""
    g = m.g
    kinds = collections.Counter(m.props.values())
    lay_classes = [c for c in m.declared_classes if list(g.objects(c, O.layTerms))]
    n_lay = sum(len(m.literals(c, O.layTerms)) for c in m.declared_classes)
    ext_parents = sorted(
        {p for c in m.declared_classes for p in m.parents.get(c, []) if not in_our_ns(p)}, key=sort_key
    )
    comps = sum(1 for c in m.concepts if (c, RDF.type, H.CompositeConcept) in g)
    version = m.first(ONTOLOGY_IRI, OWL.versionInfo)
    rows = [
        ("Ontology IRI", code(str(ONTOLOGY_IRI))),
        ("Version (`owl:versionInfo`)", code(version) if version else "not stated"),
        ("Licence", ", ".join(f"<{x}>" for x in sorted(str(v) for v in g.objects(ONTOLOGY_IRI, DCTERMS.license)))),
        ("Classes declared", str(len(m.declared_classes))),
        ("Classes used but not declared", ", ".join(link(m, c) for c in sorted(m.undeclared_classes, key=sort_key)) or "none"),
        ("Object properties", str(kinds.get("object", 0))),
        ("Datatype properties", str(kinds.get("datatype", 0))),
        ("Annotation properties", str(kinds.get("annotation", 0))),
        ("Classes carrying lay terms", f"{len(lay_classes)} ({n_lay} lay terms)"),
        ("Brick classes specialised", ", ".join(link(m, p) for p in ext_parents)),
        ("HBCO concepts", f"{len(m.concepts)} ({len(m.concepts) - comps} atomic, {comps} composite)"),
        ("Measurands", str(len(m.measurands))),
        ("SHACL node shapes", str(len(m.shapes))),
        ("Record document mappings", str(len(m.mappings))),
    ]
    for slug, title, _cls, _ in VOCABULARIES:
        rows.append((title, str(len(m.vocab_lists[slug]))))
    out = "| Field | Value |\n|---|---|\n" + "".join(f"| {a} | {b} |\n" for a, b in rows)
    return out


def block_namespaces(m: Model) -> str:
    """Prefix table."""
    used = set()
    for s, p, o in m.g:
        for t in (s, p, o):
            if isinstance(t, URIRef):
                used.add(curie(t).split(":", 1)[0])
    out = "| Prefix | Namespace | Used for |\n|---|---|---|\n"
    for prefix, ns, what in PREFIXES:
        if prefix in used or prefix in ("ontosage", "hbco", "ref", "ashrae"):
            out += f"| {code(prefix + ':')} | {code(ns)} | {cell(what)} |\n"
    return out


def block_sources(m: Model) -> str:
    """Per-file counts and what was left out."""
    out = "| File | Triples published | Triples left out |\n|---|---|---|\n"
    for rel in SOURCE_FILES:
        if rel not in m.file_graphs:
            out += f"| {code(rel)} | missing | |\n"
            continue
        dropped = sum(m.left_out[rel].values())
        out += f"| [{code(rel)}]({GITHUB_BLOB}{rel}) | {m.kept_triples[rel]} | {dropped} |\n"
    out += f"| [{code(RECORD_DIR + '/*.yaml')}]({GITHUB_BLOB.replace('/blob/', '/tree/')}{RECORD_DIR}) | {len(m.mappings)} mappings | |\n"
    dropped_all = collections.Counter()
    for c in m.left_out.values():
        dropped_all.update(c)
    out += "\n"
    if dropped_all:
        out += "Triples left out, by the type of their subject:\n\n" + "".join(
            f"- {code(k)}: {v}\n" for k, v in sorted(dropped_all.items())
        )
    else:
        out += (
            "No triple was left out: every subject in these files is a class, a property, a "
            "SKOS concept, a shape, a vocabulary member, or a statement about an upstream class.\n"
        )
    n_changed = len({(a, b) for a, b, _, _ in m.sanitised})
    out += (
        f"\n{n_changed} text values (mostly `rdfs:comment`) contained development notes; those "
        "sentences are omitted from the published pages. The source files hold the full text.\n"
    )
    return out


def block_hierarchy(m: Model) -> str:
    """Nested class list."""
    lines: List[str] = []

    def walk(c: URIRef, depth: int, seen: Tuple[URIRef, ...]) -> None:
        note = ""
        if c in m.undeclared_classes:
            note = " (used, not declared)"
        lines.append("  " * depth + f"- {link(m, c)} {cell(m.label(c))}{note}\n")
        if c in seen:
            return
        for k in m.children.get(c, []):
            walk(k, depth + 1, seen + (c,))

    roots = [c for c in m.classes if not m.parents.get(c)]
    lines.append("Classes rooted in OntoSage's own namespaces:\n\n")
    for r in roots:
        walk(r, 0, ())
    lines.append("\nClasses that specialise a Brick class:\n\n")
    ext = sorted(
        {p for c in m.classes for p in m.parents.get(c, []) if not in_our_ns(p)}, key=sort_key
    )
    for e in ext:
        lines.append(f"- {link(m, e)} (Brick)\n")
        for k in m.children.get(e, []):
            walk(k, 1, ())
    return "".join(lines)


def block_properties(m: Model) -> str:
    """Property index table."""
    g = m.g
    out = "| Property | Kind | Domain | Range | Label |\n|---|---|---|---|---|\n"
    for p in m.prop_list:
        doms = ", ".join(link(m, d) for d in sorted(g.objects(p, RDFS.domain), key=sort_key)) or "any"
        rngs = ", ".join(link(m, r) for r in sorted(g.objects(p, RDFS.range), key=sort_key)) or "not declared"
        out += f"| {link(m, p)} | {m.props[p]} | {doms} | {rngs} | {cell(m.label(p))} |\n"
    return out


def block_vocabularies(m: Model) -> str:
    """List of vocabulary pages."""
    rows = []
    for slug, title, cls, intro in VOCABULARIES:
        rows.append((title, slug, len(m.vocab_lists[slug]), f"members of {code(curie(cls))}"))
    rows.append(("HBCO concepts", "hbco-concepts", len(m.concepts), "lay-term concepts mapped to Brick classes"))
    rows.append(("Measurands", "measurands", len(m.measurands), "quantity kinds with physical and typical ranges"))
    rows.append(("SHACL shapes", "shacl-shapes", len(m.shapes), "validation shapes"))
    rows.append(("Record document mappings", "record-document-mappings", len(m.mappings), "YAML lifting rules for record documents"))
    out = "| Vocabulary | Members | What it holds |\n|---|---|---|\n"
    for title, slug, n, what in rows:
        out += f"| [{title}]({url('/ontology/vocabulary/' + slug + '/')}) | {n} | {what} |\n"
    return out


def first_sentence(text: str) -> str:
    """The first sentence of a definition."""
    parts = _SENTENCE_SPLIT.split(" ".join(text.split()), maxsplit=1)
    return parts[0] if parts else ""


def block_object_properties(m: Model) -> str:
    """Every OntoSage object property with domain, range and the first sentence of its comment."""
    g = m.g
    out = "| Property | Domain | Range | Meaning |\n|---|---|---|---|\n"
    for p in m.prop_list:
        if m.props[p] != "object":
            continue
        doms = ", ".join(link(m, d) for d in sorted(g.objects(p, RDFS.domain), key=sort_key)) or "any"
        rngs = ", ".join(link(m, r) for r in sorted(g.objects(p, RDFS.range), key=sort_key)) or "not declared"
        text = m.first(p, SKOS.definition) or m.first(p, RDFS.comment) or m.label(p)
        out += f"| {link(m, p)} | {doms} | {rngs} | {cell(first_sentence(text))} |\n"
    return out


def block_alignment(m: Model) -> str:
    """How the schema touches upstream ontologies: subclassing, SKOS mappings, Brick domains."""
    g = m.g
    out = ["OntoSage classes that specialise an upstream class (`rdfs:subClassOf`):\n\n"]
    out.append("| Upstream class | OntoSage subclasses |\n|---|---|\n")
    ext = collections.defaultdict(list)
    for c in m.declared_classes:
        for p in m.parents.get(c, []):
            if not in_our_ns(p):
                ext[p].append(c)
    for p in sorted(ext, key=sort_key):
        kids = ", ".join(link(m, k) for k in sorted(ext[p], key=sort_key))
        out.append(f"| {link(m, p)} | {kids} |\n")
    out.append("\nSKOS mappings to other ontologies (non-entailing):\n\n")
    out.append("| OntoSage term | Mapping | Upstream term |\n|---|---|---|\n")
    for pred in (SKOS.exactMatch, SKOS.closeMatch, SKOS.relatedMatch, SKOS.broadMatch, SKOS.narrowMatch):
        for s, o in sorted(g.subject_objects(pred), key=lambda so: (sort_key(so[0]), sort_key(so[1]))):
            if in_our_ns(s) and not in_our_ns(o):
                out.append(f"| {link(m, s)} | {code(curie(pred))} | {link(m, o)} |\n")
    conf = sorted(g.objects(ONTOLOGY_IRI, DCTERMS.conformsTo), key=str)
    if conf:
        out.append(
            "\nThe ontology header declares `dcterms:conformsTo` "
            + ", ".join(f"<{c}>" for c in conf)
            + ".\n"
        )
    out.append("\nOntoSage properties whose domain or range is a Brick class:\n\n")
    out.append("| Property | Kind | Domain | Range |\n|---|---|---|---|\n")
    for p in m.prop_list:
        doms = sorted(g.objects(p, RDFS.domain), key=sort_key)
        rngs = sorted(g.objects(p, RDFS.range), key=sort_key)
        if any(str(x).startswith(BRICK) for x in doms + rngs):
            out.append(
                f"| {link(m, p)} | {m.props[p]} | {', '.join(link(m, d) for d in doms) or 'any'} | "
                f"{', '.join(link(m, r) for r in rngs) or 'not declared'} |\n"
            )
    mapped = sorted({s for s in g.subjects(O.measuresQuantityKind, None) if str(s).startswith(BRICK)}, key=sort_key)
    out.append(
        f"\n`ontology/measurand_kinds.ttl` also states, with {link(m, O.measuresQuantityKind)}, "
        f"which measurand {len(mapped)} Brick sensor and meter classes measure "
        f"(see [Measurands]({url('/ontology/vocabulary/measurands/')})). These are statements "
        "about Brick classes, made in OntoSage's namespace; the Brick file itself is not edited.\n"
    )
    return "".join(out)


# ─────────────────────────────────────────────────────────────────────────────
# Relationship usage (counted from one building's TTL files)
# ─────────────────────────────────────────────────────────────────────────────

SCHEMA_SUBJECT_NS = (
    "https://brickschema.org/",
    "https://w3id.org/",
    "http://data.ashrae.org/",
    "http://ontosage.org/",
    "http://www.w3.org/",
    "http://qudt.org/",
)


def find_building_dir(source: Path, building: str) -> Optional[Path]:
    """The building's file set: active in input/ or parked in <building>/."""
    active = source / "input" / "building.yaml"
    if active.exists():
        try:
            bid = (yaml.safe_load(active.read_text(encoding="utf-8")) or {}).get("building_id")
        except yaml.YAMLError:
            bid = None
        if bid == building:
            return source / "input"
    parked = source / building
    if (parked / "building.yaml").exists():
        return parked
    return None


def block_usage(m: Model, bdir: Path, building: str) -> str:
    """Counts of relationship predicates on instance subjects."""
    files = [
        p
        for p in sorted(bdir.glob("*.ttl"))
        if not any(t in p.name.lower() for t in ("brick", "rec", "s223", "schema"))
    ]
    wanted = {iri for _, iri in RELATIONSHIP_PREDICATES}
    object_props = sorted((p for p, k in m.props.items() if k == "object"), key=sort_key)
    wanted |= {str(p) for p in object_props}
    lay = [O.layTerms, H.layTerm]
    wanted |= {str(p) for p in lay}
    counts: collections.Counter = collections.Counter()
    per_file: Dict[str, Set[str]] = collections.defaultdict(set)
    #: predicates in OntoSage's namespaces, used with an IRI object, that the schema does not declare
    undeclared: collections.Counter = collections.Counter()
    undeclared_types: collections.Counter = collections.Counter()
    for f in files:
        g = Graph(bind_namespaces="none")
        g.parse(f, format="turtle")
        for s, p, o in g:
            if isinstance(s, URIRef) and str(s).startswith(SCHEMA_SUBJECT_NS):
                continue
            ps = str(p)
            if ps in wanted:
                counts[ps] += 1
                per_file[ps].add(f.name)
            elif in_our_ns(p) and p not in m.props and not isinstance(o, Literal):
                undeclared[ps] += 1
            if p == RDF.type and in_our_ns(o) and o not in m.slug:
                undeclared_types[str(o)] += 1
    out = (
        f"Counted by `_tools/gen_ontology_reference.py` over the {len(files)} building TTL files "
        f"of `{building}` (Brick and schema files excluded; only triples whose subject is a "
        "building entity are counted).\n\n"
        "| Group | Relationship | Triples | Files |\n|---|---|---|---|\n"
    )
    for group, iri in RELATIONSHIP_PREDICATES:
        out += f"| {group} | {link(m, URIRef(iri))} | {counts.get(iri, 0)} | {len(per_file.get(iri, ()))} |\n"
    for p in object_props:
        n = counts.get(str(p), 0)
        if n:
            out += f"| OntoSage | {link(m, p)} | {n} | {len(per_file[str(p)])} |\n"
    for p in lay:
        out += f"| Lay terms | {link(m, p)} | {counts.get(str(p), 0)} | {len(per_file.get(str(p), ()))} |\n"
    unused = [p for p in object_props if not counts.get(str(p))]
    out += (
        f"\n{len(unused)} of the {len(object_props)} OntoSage object properties are not used in "
        "this building's TTL files. Some are written at run time (record document lifting writes "
        "the record links), some are used only in the shared ontology files, and some belong to "
        "features this building does not use: "
        + ", ".join(link(m, p) for p in unused)
        + ".\n"
    )
    if undeclared or undeclared_types:
        out += (
            "\nThe building's files also use OntoSage-namespace terms that the schema files do not "
            "declare. They load and can be queried, but have no page here: "
            + ", ".join(
                f"{code(curie(URIRef(k)))} ({v})"
                for k, v in sorted(list(undeclared.items()) + list(undeclared_types.items()))
            )
            + ".\n"
        )
    return out


# ─────────────────────────────────────────────────────────────────────────────
# Marker replacement
# ─────────────────────────────────────────────────────────────────────────────


def replace_block(text: str, name: str, body: str) -> str:
    """Replace the text between the BEGIN/END GENERATED markers for name."""
    begin = f"<!-- BEGIN GENERATED: {name} -->"
    end = f"<!-- END GENERATED: {name} -->"
    i = text.find(begin)
    j = text.find(end)
    if i < 0 or j < 0 or j < i:
        raise SystemExit(f"markers for '{name}' not found or out of order")
    return text[: i + len(begin)] + "\n" + body.rstrip("\n") + "\n" + text[j:]


BROWSER_SKELETON = """---
title: Ontology Browser
layout: post
category: docs
permalink: /docs/ontology-browser/
date: 2026-07-20
---

<!-- BEGIN GENERATED: summary -->
<!-- END GENERATED: summary -->

<!-- BEGIN GENERATED: namespaces -->
<!-- END GENERATED: namespaces -->

<!-- BEGIN GENERATED: sources -->
<!-- END GENERATED: sources -->

## Class hierarchy

<!-- BEGIN GENERATED: hierarchy -->
<!-- END GENERATED: hierarchy -->

## Property index

<!-- BEGIN GENERATED: properties -->
<!-- END GENERATED: properties -->

## Vocabularies

<!-- BEGIN GENERATED: vocabularies -->
<!-- END GENERATED: vocabularies -->
"""


# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────


def check_brick_terms(m: Model, source: Path) -> None:
    """Warn about brick: terms the schema uses that Brick 1.4 does not define."""
    candidates = [source / "input" / "Brick_v1.4.ttl"] + sorted(source.glob("bldg*/Brick_v1.4.ttl"))
    path = next((p for p in candidates if p.exists()), None)
    if path is None:
        m.warnings.append("Brick_v1.4.ttl not found; brick: terms not checked")
        return
    b = Graph(bind_namespaces="none")
    b.parse(path, format="turtle")
    known = {s for s in b.subjects() if isinstance(s, URIRef)}
    used = set()
    for s, p, o in m.g:
        for t in (s, p, o):
            if isinstance(t, URIRef) and str(t).startswith(BRICK):
                used.add(t)
    for t in sorted(used - known, key=sort_key):
        m.warnings.append(f"{curie(t)} is used but not defined in {path.name}")


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", default="../OntoSage", help="OntoSage checkout (relative to the site root)")
    ap.add_argument("--building", default="bldg1", help="building whose TTL files are counted for relationship usage")
    ap.add_argument("--skip-building", action="store_true", help="leave the relationship usage block unchanged")
    ap.add_argument("--report", help="write every text value the publication filter changed to this file")
    args = ap.parse_args(argv)

    source = Path(args.source)
    if not source.is_absolute():
        source = (SITE_ROOT / source).resolve()
    if not (source / "ontology").is_dir():
        print(f"error: {source} has no ontology/ folder", file=sys.stderr)
        return 2

    m = Model(source)
    check_brick_terms(m, source)
    if args.report:
        lines = []
        for s, p, old, new in sorted(m.sanitised):
            lines.append(f"## {s} {p}\nOLD: {old}\nNEW: {new}\n")
        Path(args.report).write_text("\n".join(lines), encoding="utf-8")

    out_dir = SITE_ROOT / OUT_DIR_NAME
    if out_dir.exists():
        assert out_dir.name == OUT_DIR_NAME and out_dir.parent == SITE_ROOT
        shutil.rmtree(out_dir)
    for sub in ("class", "property", "vocabulary"):
        (out_dir / sub).mkdir(parents=True)

    for c in m.classes:
        write_class_page(m, c, out_dir)
    for p in m.prop_list:
        write_property_page(m, p, out_dir)
    for slug, title, cls, intro in VOCABULARIES:
        write_simple_vocab(m, slug, title, cls, intro, out_dir)
    write_concepts_page(m, out_dir)
    write_measurands_page(m, out_dir)
    write_shapes_page(m, out_dir)
    write_mappings_page(m, out_dir)

    browser = SITE_ROOT / BROWSER_PAGE
    text = browser.read_text(encoding="utf-8") if browser.exists() else BROWSER_SKELETON
    for name, body in (
        ("summary", block_summary(m)),
        ("namespaces", block_namespaces(m)),
        ("sources", block_sources(m)),
        ("hierarchy", block_hierarchy(m)),
        ("properties", block_properties(m)),
        ("vocabularies", block_vocabularies(m)),
    ):
        text = replace_block(text, name, body)
    browser.write_text(text, encoding="utf-8", newline="\n")

    ext_page = SITE_ROOT / EXTENSIONS_PAGE
    if ext_page.exists():
        etext = ext_page.read_text(encoding="utf-8")
        etext = replace_block(etext, "alignment", block_alignment(m))
        ext_page.write_text(etext, encoding="utf-8", newline="\n")

    rel = SITE_ROOT / RELATIONSHIPS_PAGE
    if rel.exists():
        rtext = rel.read_text(encoding="utf-8")
        rtext = replace_block(rtext, "object-properties", block_object_properties(m))
        rel.write_text(rtext, encoding="utf-8", newline="\n")
    if not args.skip_building and rel.exists():
        bdir = find_building_dir(source, args.building)
        if bdir is None:
            m.warnings.append(f"building {args.building} not found; usage block left unchanged")
        else:
            rtext = rel.read_text(encoding="utf-8")
            rtext = replace_block(rtext, "usage", block_usage(m, bdir, args.building))
            rel.write_text(rtext, encoding="utf-8", newline="\n")

    n_pages = sum(1 for _ in out_dir.rglob("*.md"))
    print(
        f"classes={len(m.classes)} properties={len(m.prop_list)} "
        f"vocabulary_pages={len(VOCABULARIES) + 4} pages_written={n_pages} "
        f"sanitised_values={len(m.sanitised)}"
    )
    for w in m.warnings:
        print(f"warning: {w}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
