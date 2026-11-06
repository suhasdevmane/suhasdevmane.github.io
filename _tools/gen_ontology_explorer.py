#!/usr/bin/env python3
"""Build the interactive OntoSage ontology explorer (``explorer/`` on the site).

The explorer is a static site made by rdf-toolkit, the tool ontology.brickschema.org is built
with: a class tree, a search box and one page per term. This script feeds it the SAME graph the
reference pages are generated from (``gen_ontology_reference.Model``): schema-level content
only, development notes removed. Building instance data is never written.

It writes an rdf-toolkit project to ``_tools/explorer/project/`` and, unless ``--project-only``
is given, runs rdf-toolkit in Docker to produce ``explorer/``:

* ``ontosage.ttl``  the OntoSage Conversational Building Vocabulary (``ontosage:``)
* ``hbco.ttl``      the Human-Building Conversation Ontology (``hbco:``)
* ``brick.ttl``     an excerpt of Brick 1.4: only the Brick classes and properties OntoSage
                    names, with their superclass chains, so OntoSage's classes sit in the tree
                    where they attach to Brick. It is not the whole of Brick.
* ``vocab/*.ttl``   rdf, rdfs, owl, skos and shacl, vendored in ``_tools/explorer/vocab/``.

Run from the site root::

    docker build -t ontosage-rdf-toolkit _tools/explorer    # once
    python _tools/gen_ontology_explorer.py                  # --source ../OntoSage

Requires rdflib (7.x), PyYAML and Docker.
"""

from __future__ import annotations

import argparse
import collections
import html
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple

from rdflib import BNode, Graph, Literal, URIRef
from rdflib.namespace import OWL, RDF, RDFS, SKOS

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gen_ontology_reference as gor  # noqa: E402

TOOLS = Path(__file__).resolve().parent / "explorer"
PROJECT_DIR = TOOLS / "project"
VOCAB_DIR = TOOLS / "vocab"
OUT_DIR_NAME = "explorer"
IMAGE = "ontosage-rdf-toolkit"
SITE_TITLE = "OntoSage Ontology Explorer"

ONTO_DOC = str(gor.ONTOLOGY_IRI)
HBCO_DOC = "http://ontosage.org/hbco"
BRICK_DOC = "https://brickschema.org/schema/Brick"

#: Document IRI -> file, for the vendored vocabularies.
VOCAB_FILES = {
    "http://www.w3.org/1999/02/22-rdf-syntax-ns": "vocab/rdf.ttl",
    "http://www.w3.org/2000/01/rdf-schema": "vocab/rdfs.ttl",
    "http://www.w3.org/2002/07/owl": "vocab/owl.ttl",
    "http://www.w3.org/2004/02/skos/core": "vocab/skos.ttl",
    "http://www.w3.org/ns/shacl": "vocab/shacl.ttl",
}

#: Brick predicates copied into the excerpt. Everything else Brick says is left out.
BRICK_KEEP = {RDFS.label, SKOS.definition, RDFS.comment}


def split_by_namespace(m: gor.Model) -> Dict[str, Graph]:
    """The published graph, as one graph per OntoSage document (blank nodes follow their owner)."""
    out = {ONTO_DOC: new_graph(), HBCO_DOC: new_graph()}
    g = m.g
    for s in set(g.subjects()):
        if isinstance(s, BNode):
            continue
        doc = HBCO_DOC if str(s).startswith(gor.HBCO) else ONTO_DOC
        for t in gor.bnode_closure(g, [s]):
            for p, o in g.predicate_objects(t):
                out[doc].add((t, p, o))
    return out


def brick_excerpt(m: gor.Model, brick_path: Path) -> Graph:
    """The Brick classes and properties OntoSage names, with their named ancestors."""
    b = Graph(bind_namespaces="none")
    b.parse(brick_path, format="turtle")
    used: Set[URIRef] = set()
    for s, p, o in m.g:
        for t in (s, p, o):
            if isinstance(t, URIRef) and str(t).startswith(gor.BRICK):
                used.add(t)

    classes: Set[URIRef] = set()
    props: Set[URIRef] = set()
    todo: List[URIRef] = sorted(used)
    while todo:
        t = todo.pop()
        types = set(b.objects(t, RDF.type))
        if OWL.Class in types:
            if t in classes:
                continue
            classes.add(t)
            todo.extend(o for o in b.objects(t, RDFS.subClassOf) if is_brick(o))
        elif types & {OWL.ObjectProperty, OWL.DatatypeProperty, RDF.Property}:
            if t in props:
                continue
            props.add(t)
            todo.extend(o for o in b.objects(t, RDFS.subPropertyOf) if is_brick(o))

    out = new_graph()
    doc = URIRef(BRICK_DOC)
    out.add((doc, RDF.type, OWL.Ontology))
    out.add((doc, RDFS.label, Literal("Brick (excerpt)")))
    out.add(
        (
            doc,
            RDFS.comment,
            Literal(
                "Only the Brick 1.4 classes and properties that OntoSage names, with their "
                "superclass chains, so that OntoSage's classes appear where they attach to "
                "Brick. The complete Brick ontology is at https://ontology.brickschema.org/."
            ),
        )
    )
    for c in classes:
        out.add((c, RDF.type, OWL.Class))
        for o in b.objects(c, RDFS.subClassOf):
            if o in classes:
                out.add((c, RDFS.subClassOf, o))
    for p in props:
        for t in b.objects(p, RDF.type):
            if t in (OWL.ObjectProperty, OWL.DatatypeProperty, RDF.Property):
                out.add((p, RDF.type, t))
        for o in b.objects(p, RDFS.subPropertyOf):
            if o in props:
                out.add((p, RDFS.subPropertyOf, o))
        for o in b.objects(p, OWL.inverseOf):
            if o in props:
                out.add((p, OWL.inverseOf, o))
    for t in classes | props:
        for pred in BRICK_KEEP:
            for o in b.objects(t, pred):
                if isinstance(o, Literal):
                    out.add((t, pred, o))
    return out


def is_brick(t) -> bool:
    """True for a named Brick term."""
    return isinstance(t, URIRef) and str(t).startswith(gor.BRICK)


def new_graph() -> Graph:
    """An empty graph with OntoSage's prefixes bound."""
    g = Graph(bind_namespaces="none")
    for prefix, ns, _ in gor.PREFIXES:
        g.bind(prefix, ns)
    return g


def root_classes(m: gor.Model, extra: Iterable[URIRef]) -> List[str]:
    """Tree roots: OntoSage classes with no OntoSage or Brick superclass, then Brick's root."""
    known = set(m.classes) | set(extra)
    roots = []
    for c in m.classes:
        if not str(c).startswith(gor.OUR_NS):
            continue
        parents = [p for p in m.g.objects(c, RDFS.subClassOf) if isinstance(p, URIRef)]
        if not any(p in known for p in parents):
            roots.append(str(c))
    return sorted(roots, key=lambda s: s.lower())


#: Domains that make a property apply to every class. rdf-toolkit lists a property under every
#: class in its domain, so owl:sameAs, rdfs:label and the like would appear in the property
#: table of every OntoSage class. These domain statements are dropped from the DISPLAYED copy
#: of the standard vocabularies only; the vendored files are unchanged.
UNIVERSAL_DOMAINS = {OWL.Thing, RDFS.Resource}


def copy_vocab(src: Path, dst: Path) -> None:
    """Copy a standard vocabulary into the project, without its universal-domain statements."""
    g = Graph(bind_namespaces="none")
    g.parse(src, format="turtle")  # the parser binds the file's own @prefix lines
    for s, o in list(g.subject_objects(RDFS.domain)):
        if o in UNIVERSAL_DOMAINS:
            g.remove((s, RDFS.domain, o))
    g.serialize(dst, format="turtle", encoding="utf-8")


def write_project(m: gor.Model, brick: Graph) -> Dict[str, int]:
    """Write the rdf-toolkit project folder; return triple counts per file."""
    if PROJECT_DIR.exists():
        assert PROJECT_DIR.name == "project" and PROJECT_DIR.parent == TOOLS
        shutil.rmtree(PROJECT_DIR)
    (PROJECT_DIR / "vocab").mkdir(parents=True)
    for src in sorted(VOCAB_DIR.glob("*.ttl")):
        copy_vocab(src, PROJECT_DIR / "vocab" / src.name)

    graphs = split_by_namespace(m)
    files ={ONTO_DOC: "ontosage.ttl", HBCO_DOC: "hbco.ttl", BRICK_DOC: "brick.ttl"}
    counts = {}
    for doc, g in list(graphs.items()) + [(BRICK_DOC, brick)]:
        path = PROJECT_DIR / files[doc]
        g.serialize(path, format="turtle", encoding="utf-8")
        counts[files[doc]] = len(g)

    brick_classes = {s for s in brick.subjects(RDF.type, OWL.Class)}
    roots = root_classes(m, brick_classes)
    brick_roots = sorted(
        str(c)
        for c in brick_classes
        if not any(o in brick_classes for o in brick.objects(c, RDFS.subClassOf))
    )
    package = {
        "private": True,
        "name": "ontosage-ontology-explorer",
        "rdf:files": {**{k: v for k, v in files.items()}, **VOCAB_FILES},
        "rdf:prefixes": {prefix: ns for prefix, ns, _ in gor.PREFIXES},
    }
    config = {
        "siteOptions": {
            "title": SITE_TITLE,
            "roots": roots + brick_roots,
            "expand": [],
            "cleanUrls": False,
        }
    }
    (PROJECT_DIR / "package.json").write_text(json.dumps(package, indent=2) + "\n", encoding="utf-8")
    (PROJECT_DIR / "rdfconfig.json").write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
    counts["roots"] = len(roots)
    counts["brick_roots"] = len(brick_roots)
    return counts


def run_toolkit(base: str) -> int:
    """Run rdf-toolkit in Docker over the project folder; write explorer/."""
    out = gor.SITE_ROOT / OUT_DIR_NAME
    if out.exists():
        assert out.name == OUT_DIR_NAME and out.parent == gor.SITE_ROOT
        shutil.rmtree(out)
    out.mkdir()
    cmd = [
        "docker", "run", "--rm",
        "-v", f"{PROJECT_DIR.as_posix()}:/project:ro",
        "-v", f"{out.as_posix()}:/out",
        IMAGE, "make", "site", "--project", "/project", "--output", "/out", "--base", base,
    ]
    return subprocess.call(cmd)


def find_brick(source: Path) -> Optional[Path]:
    """Brick_v1.4.ttl from the active building, or from a parked one."""
    candidates = [source / "input" / "Brick_v1.4.ttl"] + sorted(source.glob("bldg*/Brick_v1.4.ttl"))
    return next((p for p in candidates if p.exists()), None)


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", default="../OntoSage", help="OntoSage checkout (relative to the site root)")
    ap.add_argument("--base", default="/explorer/", help="URL path the explorer is served under")
    ap.add_argument("--project-only", action="store_true", help="write the project folder, do not run rdf-toolkit")
    args = ap.parse_args(argv)

    source = Path(args.source)
    if not source.is_absolute():
        source = (gor.SITE_ROOT / source).resolve()
    if not (source / "ontology").is_dir():
        print(f"error: {source} has no ontology/ folder", file=sys.stderr)
        return 2
    brick = find_brick(source)
    if brick is None:
        print("error: Brick_v1.4.ttl not found under input/ or bldg*/", file=sys.stderr)
        return 2

    m = gor.Model(source)
    excerpt = brick_excerpt(m, brick)
    counts = write_project(m, excerpt)
    print(" ".join(f"{k}={v}" for k, v in counts.items()) + f" sanitised_values={len(m.sanitised)}")
    for w in m.warnings:
        print(f"warning: {w}")
    if args.project_only:
        return 0
    rc = run_toolkit(args.base)
    if rc != 0:
        print(f"error: rdf-toolkit exited {rc}", file=sys.stderr)
        return rc
    report = postprocess(m, excerpt, gor.SITE_ROOT / OUT_DIR_NAME, args.base)
    print(" ".join(f"{k}={v}" for k, v in report.items()))
    return 1 if report["unresolved_links"] else 0


# ─────────────────────────────────────────────────────────────────────────────
# Post-processing of rdf-toolkit's output
# ─────────────────────────────────────────────────────────────────────────────

DOCS_HOME = "/"
REFERENCE_HOME = "/docs/ontology-browser/"
SOURCE_URL = "https://github.com/suhasdevmane/OntoSage/tree/main/ontology"
ISSUES_URL = "https://github.com/suhasdevmane/OntoSage/issues"
BRICK_SITE = "https://ontology.brickschema.org/"
RDF_TOOLKIT_URL = "https://github.com/ektrah/rdf-toolkit"

#: rdf-toolkit writes blank-node pages to "_/", which Jekyll does not publish.
BNODE_DIR = "bnode"

_A_TAG = re.compile(r'<a ([^>]*?)href="(http://ontosage\.org/[^"]*)"([^>]*)>')
_DATA_HREF = re.compile(r'data-href="([^"]*)"')
_FOOTER_TAIL = re.compile(r"<details><summary>Terms of use</summary>.*?</footer>", re.DOTALL)
_LOGO = '<p class="logo">' + SITE_TITLE + "</p>"
_HOME_SECTION = "<main><section><h1>" + SITE_TITLE + "</h1></section>"

EXTRA_CSS = """
nav .logo-sub { margin: 0 0 1em 0; font-size: 0.85em; }
nav .logo-sub a { color: inherit; opacity: 0.75; text-decoration: none; }
nav .logo-sub a:hover { opacity: 1; text-decoration: underline; }
main section.home p, main section.home li { max-width: 46em; line-height: 1.6; }
main section.home code { font-size: 0.95em; }
"""


def esc(text: str) -> str:
    """Escape text for HTML."""
    return html.escape(str(text), quote=True)


def internal(href: str, text: str) -> str:
    """A link the explorer's click handler follows (it navigates to data-href)."""
    return f'<a href="{esc(href)}" data-href="{esc(href)}">{text}</a>'


def external(href: str, text: str) -> str:
    """A link the click handler leaves alone (it skips links that carry rel)."""
    return f'<a href="{esc(href)}" rel="external">{text}</a>'


_PROPS_OPEN = "<section><h2>Properties</h2>"
_PROPS_CLOSE = "</table></section>"


def drop_universal_rows(text: str, base: str) -> Tuple[str, int]:
    """Remove property rows inherited from rdfs:Resource (rdf:type, rdfs:label, skos:prefLabel...).

    rdf-toolkit's RDFS engine gives every class rdfs:Resource as a superclass and the RDFS
    vocabulary's properties that domain, so every class page lists the same ten generic rows
    above its own properties. They say nothing about the class. A section left empty goes too.
    """
    start = text.find(_PROPS_OPEN)
    if start < 0:
        return text, 0
    end = text.find(_PROPS_CLOSE, start)
    if end < 0:
        return text, 0
    end += len(_PROPS_CLOSE)
    section = text[start:end]
    head, sep, rest = section.partition("<tbody>")
    if not sep:
        return text, 0
    body, _, tail = rest.partition("</tbody>")
    marker = f'(inherited from <a class="rdf-pname-ln rdf-iri" href="{RDFS.Resource}" data-href="{base}rdfs/Resource.html">'
    rows = [r for r in re.split(r"(?=<tr>)", body) if r]
    kept = [r for r in rows if marker not in r]
    dropped = len(rows) - len(kept)
    if not dropped:
        return text, 0
    new_section = "" if not kept else head + "<tbody>" + "".join(kept) + "</tbody>" + tail
    return text[:start] + new_section + text[end:], dropped


def footer_html() -> str:
    """The OntoSage footer that replaces rdf-toolkit's generic one."""
    return (
        "<details><summary>About this explorer</summary>"
        "<p>These pages are generated from the OntoSage schema files "
        f"({external(SOURCE_URL, 'ontology/ on GitHub')}). Only schema-level content is published: "
        "classes, properties, concepts and controlled vocabularies. No building's rooms, sensors "
        "or readings are included.</p>"
        "<p>The Brick terms shown are an excerpt: only the Brick classes and properties OntoSage "
        f"names, with their superclasses. The complete Brick ontology is at {external(BRICK_SITE, 'ontology.brickschema.org')}.</p>"
        "<p>The tree and the class summaries are inferred from the Turtle by "
        f"{external(RDF_TOOLKIT_URL, 'rdf-toolkit')} (MIT licence). Check a definition against the "
        "Turtle before relying on it. Search runs in your browser; nothing you type is sent anywhere.</p>"
        "</details>"
        "<details><summary>Report a problem</summary>"
        f"<p>Open an issue in the {external(ISSUES_URL, 'OntoSage repository')} and name the term.</p>"
        "</details>"
        "</footer>"
    )


def nav_html(base: str) -> str:
    """The navigation title, linked, with a way back to the documentation."""
    return (
        f'<p class="logo">{internal(base, esc(SITE_TITLE))}</p>'
        f'<p class="logo-sub"><a href="{DOCS_HOME}" rel="home">&larr; OntoSage documentation</a></p>'
    )


def home_html(m: gor.Model, excerpt: Graph, hrefs: Dict[str, str]) -> str:
    """The body of the explorer's home page."""

    def term(iri: URIRef) -> str:
        href = hrefs.get(str(iri))
        label = f"<code>{esc(gor.curie(iri))}</code>"
        return internal(href, label) if href else label

    def in_ns(terms: Iterable[URIRef], ns: str) -> int:
        return sum(1 for t in terms if str(t).startswith(ns))

    n_onto, n_hbco = in_ns(m.declared_classes, gor.ONTO), in_ns(m.declared_classes, gor.HBCO)
    p_onto, p_hbco = in_ns(m.prop_list, gor.ONTO), in_ns(m.prop_list, gor.HBCO)
    n_brick_c = len(set(excerpt.subjects(RDF.type, OWL.Class)))
    n_brick_p = len(
        {s for t in (OWL.ObjectProperty, OWL.DatatypeProperty, RDF.Property) for s in excerpt.subjects(RDF.type, t)}
    )
    brick_props = f" and {n_brick_p} properties" if n_brick_p else ""
    version = m.g.value(gor.ONTOLOGY_IRI, OWL.versionInfo)
    modified = m.g.value(gor.ONTOLOGY_IRI, gor.DCTERMS.modified)
    starts = ", ".join(
        term(gor.O[x]) for x in ("Capability", "Record", "QuestionIntent", "StakeholderRole", "Measurand")
    )
    stamp = []
    if version:
        stamp.append(f"schema version {esc(version)}")
    if modified:
        stamp.append(f"last modified {esc(modified)}")
    return (
        '<main><section class="home">'
        f"<h1>{esc(SITE_TITLE)}</h1>"
        "<p>The OntoSage schema: the classes, properties and lay-language concepts OntoSage adds "
        "on top of Brick so that a building can be asked questions in plain English. Browse the "
        "tree on the left, or search for a term or for an everyday word such as "
        "<em>stuffy</em>, <em>bathroom</em> or <em>parking</em>.</p>"
        "<h2>What is here</h2><ul>"
        f"<li><code>ontosage:</code> the OntoSage Conversational Building Vocabulary: {n_onto} "
        f"classes and {p_onto} properties. Good places to start: {starts}.</li>"
        f"<li><code>hbco:</code> the Human-Building Conversation Ontology: {n_hbco} classes, "
        f"{p_hbco} properties and {len(m.concepts)} concepts that map everyday words to Brick "
        f"sensor classes. Start at {term(gor.H.Concept)}.</li>"
        f"<li><code>brick:</code> an excerpt of Brick 1.4: the {n_brick_c} classes{brick_props} "
        "that OntoSage names, with their superclasses, so each OntoSage class "
        f"appears where it attaches to Brick. The complete Brick ontology is at "
        f"{external(BRICK_SITE, 'ontology.brickschema.org')}.</li>"
        "</ul>"
        "<p>Concepts, question intents, stakeholder roles, measurands and the other controlled "
        "vocabularies are individuals, not classes; their links lead to the "
        f"{internal(REFERENCE_HOME, 'ontology reference')} in the documentation, which also "
        "explains how the terms are used.</p>"
        f"<p>Generated from the Turtle files in {external(SOURCE_URL, 'ontology/')}"
        + (f" ({', '.join(stamp)})" if stamp else "")
        + ". Only schema-level content is published; no building's rooms, sensors or readings "
        "are included.</p>"
        "</section>"
    )


def search_entries(m: gor.Model, hrefs: Dict[str, str]) -> List[dict]:
    """Search entries for individuals and for every lay term, pointing at their pages."""
    out: List[dict] = []
    for t, _ in sorted(m.vocab_member.items(), key=lambda kv: gor.sort_key(kv[0])):
        href = gor.page_path(m, t)
        if not href:
            continue
        desc = m.first(t, SKOS.definition) or m.first(t, RDFS.comment) or m.label(t)
        out.append(
            {"href": href, "id": str(t), "name": gor.curie(t), "description": desc, "deprecated": False}
        )
    pairs = set()
    for pred in (gor.O.layTerms, gor.H.layTerm):
        for s, o in m.g.subject_objects(pred):
            if isinstance(s, URIRef) and isinstance(o, Literal):
                pairs.add((" ".join(str(o).split()), s))
    for word, s in sorted(pairs, key=lambda p: (p[0].lower(), gor.sort_key(p[1]))):
        href = hrefs.get(str(s)) or gor.page_path(m, s)
        if not href:
            continue
        out.append(
            {
                "href": href,
                "id": str(s),
                "name": f"{word} → {gor.curie(s)}",
                "description": "",
                "deprecated": False,
            }
        )
    return out


def postprocess(m: gor.Model, excerpt: Graph, out: Path, base: str) -> Dict[str, int]:
    """Make rdf-toolkit's output fit this site; return counts of what changed."""
    report = collections.Counter()

    # blank-node pages: Jekyll does not publish a folder whose name starts with "_"
    bdir = out / "_"
    if bdir.is_dir():
        bdir.rename(out / BNODE_DIR)

    index_path = out / "index.json"
    entries = json.loads(index_path.read_text(encoding="utf-8"))
    hrefs = {e["id"]: e["href"] for e in entries if e.get("href")}

    unresolved: Set[str] = set()
    # IRIs with no term page of their own: the namespaces, and a concept scheme (its members'
    # vocabulary page lists them all)
    others = {ns: REFERENCE_HOME + "#namespaces-and-prefixes" for ns in gor.OUR_NS}
    for slug, members in m.vocab_lists.items():
        for c in members:
            for s in m.g.objects(c, SKOS.inScheme):
                others.setdefault(str(s), f"/ontology/vocabulary/{slug}/")

    def fix_link(mt: "re.Match[str]") -> str:
        before, iri, after = mt.group(1), mt.group(2), mt.group(3)
        dh = _DATA_HREF.search(before + after)
        if dh:
            report["links_to_explorer"] += 1
            return f'<a {before}href="{dh.group(1)}"{after}>'
        target = gor.page_path(m, URIRef(iri)) or others.get(iri)
        if target:
            report["links_to_reference"] += 1
            return f'<a {before}href="{target}" data-href="{target}"{after}>'
        unresolved.add(iri)
        return mt.group(0)

    footer = footer_html()
    nav = nav_html(base)
    home = home_html(m, excerpt, hrefs)
    for page in sorted(out.rglob("*.html")):
        text = page.read_text(encoding="utf-8")
        new = text.replace(f'"{base}_/', f'"{base}{BNODE_DIR}/')
        new = _A_TAG.sub(fix_link, new)
        new = _FOOTER_TAIL.sub(lambda _: footer, new, count=1)
        new = new.replace(_LOGO, nav, 1)
        if page != out / "rdfs" / "Resource.html":
            new, dropped = drop_universal_rows(new, base)
            report["generic_rows_dropped"] += dropped
        if page == out / "index.html":
            new = new.replace(_HOME_SECTION, home, 1)
            report["home_written"] = int(home in new)
        if new != text:
            page.write_text(new, encoding="utf-8", newline="\n")
            report["pages_changed"] += 1
        report["pages"] += 1
        report["footers_left"] += int("Terms of use</summary>" in new)

    for e in entries:
        if e.get("href", "").startswith(f"{base}_/"):
            e["href"] = f"{base}{BNODE_DIR}/" + e["href"][len(base) + 2 :]
    added = search_entries(m, hrefs)
    report["search_entries"] = len(entries)
    report["search_entries_added"] = len(added)
    index_path.write_text(
        json.dumps(entries + added, ensure_ascii=False, separators=(",", ":")), encoding="utf-8", newline="\n"
    )

    css = out / "style.css"
    css.write_text(css.read_text(encoding="utf-8") + EXTRA_CSS, encoding="utf-8", newline="\n")

    report["unresolved_links"] = len(unresolved)
    for iri in sorted(unresolved):
        print(f"warning: no page for <{iri}>; link left pointing at the IRI")
    return dict(report)


if __name__ == "__main__":
    sys.exit(main())
