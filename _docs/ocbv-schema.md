---
title: OCBV — Conversational Building Vocabulary
layout: post
category: docs
permalink: /docs/ocbv-schema/
date: 2026-07-04
---

# OCBV — the Conversational Building Vocabulary

Brick Schema models a building's *technical fabric* — points, sensors, equipment, locations — for
machines. It does **not** model what a human actually asks: *"where's the prayer room?", "is it stuffy
on floor 5?", "the toilet is leaking, who do I tell?"*.

The **OntoSage Conversational Building Vocabulary (OCBV)** — `input/ontosage_schema.ttl`, CC-BY-4.0 —
adds exactly that layer. It is the schema that makes a building *talkable-to*, and a standalone,
publication-ready artifact you can cite and reuse.

## It extends Brick — and never contradicts it

OCBV declares only `ontosage:` (`http://ontosage.org/capabilities#`) and `hbco:`
(`http://ontosage.org/hbco#`) terms. Where it touches the physical building it **references** Brick as
the property range (`ontosage:locatedIn → brick:Location`, `hbco:mapsToBrickClass → a Brick sensor
class`), and it aligns to Brick/REC/BOT/SOSA with SKOS mapping properties only (`skos:relatedMatch` /
`closeMatch`, never `owl:equivalent*`). So loading OCBV alongside a Brick model **adds** conversational
triples and invalidates nothing.

## Modules — one file, the whole conversational layer

| Module | What it models |
|---|---|
| **A — Capabilities** | `ontosage:Capability → Amenity` (PrayerRoom, Cafe, Lift, ToiletFacility, ShowerFacility, StudyArea…) and `→ KnowledgeTopic` (InformationTopic, Procedure, MaintenanceIssue); Brick-bridge object properties; 13 datatype properties (the guided-form fields) |
| **B — Conversation concepts (HBCO)** | `hbco:Concept`, `hbco:mapsToBrickClass`, `hbco:layTerm` — lay word → Brick sensor ("stuffy" → CO₂), so plain language resolves to live data |
| **C — Stakeholder roles** | `ontosage:StakeholderRole` (Occupant, FacilityManager, Researcher, SustainabilityOfficer, SafetyOfficer…) — frames answers, **explicitly not RBAC** |
| **D — Question-intent grammar** | `ontosage:QuestionIntent` (Locate, Quantify, Trend, Compare, Anomaly, Forecast, Comfort, Discover, Procedure, Report) |
| **E — Report intake** | `ontosage:Report → FaultReport / Complaint / SafetyReport / Feedback / Suggestion` |
| **F — Answer provenance** | `ontosage:SourceType` + `groundedIn` + `isSimulated` — the vocabulary behind honest, auditable answers |
| **G — Competency questions + example SPARQL** | `ontosage:competencyQuestion` + `ontosage:exampleSparql` annotations per class |
| **H / I / J** | Brick/REC/BOT/SOSA alignment; SHACL validation shapes; worked examples |

Every term carries `rdfs:label` + `rdfs:comment` + `skos:definition` + `skos:example` so each is
individually retrievable when the schema is chunked into a vector store.

## The schema is the source of truth for authoring *and* answering

### It drives the console

The console's **Ontology** tab is where OCBV lives in practice — building identity, the semantic search
index, building capabilities, named graphs, TTL upload, and a SPARQL browser, all in one place:

![Admin console Ontology tab]({{ '/admin-portal-screenshots/09-ontology.png' | relative_url }})
*Building identity (namespace/prefix), the semantic index, building capabilities (+Add capability),
named graphs, Upload TTL, and the SPARQL browser.*

The **"Add capability"** form is generated from the schema:

- the **Type** dropdown = the OCBV subclasses of `ontosage:Amenity` / `ontosage:KnowledgeTopic`
  (`get_capability_classes()`), and
- the **fields shown** = the datatype properties whose `rdfs:domain` applies to the selected type
  (`get_capability_form_schema()`) — an Amenity shows `locationText`; a Procedure shows `steps`; a
  MaintenanceIssue shows `priority`.

**Add a class or property to `ontosage_schema.ttl` and it appears in the form after a reload — no code
change.** (It falls back to a built-in list if GraphDB is unreachable, so the console never breaks.)

![Add-capability form generated from the OCBV schema]({{ '/admin-portal-screenshots/09b-add-capability.png' | relative_url }})
*The console's "Add capability" form is generated from OCBV: the Type dropdown lists the schema's
subclasses, and it shows "Fields for this type (from the OCBV schema)". Saved as `ontosage:Amenity`
triples in `input/<bldg>_capabilities.ttl`, answerable immediately — no Turtle, no restart.*

### It feeds the RAG / LLM

The semantic index's indexed text now includes each term's comment, definition, example, lay-terms and
**competency questions**. So a plain-English question — *"the toilet is leaking, who do I tell"* —
matches `ontosage:MaintenanceIssue`, and the retriever's bounded-context step then hands that term's
`ontosage:exampleSparql` to the LLM as a **copy-adaptable query template**. The schema literally teaches
the model how to answer.

## Authoring instances — no Turtle required

Stakeholders don't write RDF. An amenity or a knowledge topic is authored via the guided form (below),
or by dropping a `<bldg>_capabilities.ttl` file into `input/`. A worked example of what the form
produces:

```turtle
bldg:PrayerRoom_104 a ontosage:PrayerRoom, ontosage:Amenity ;
    rdfs:label "Multi-faith prayer & reflection room" ;
    ontosage:layTerms "prayer room, quiet room, where can i pray, faith room" ;
    ontosage:locationText "Floor 1, room 1.04" ;
    ontosage:locatedIn bldg:Room_1.04 ;          # <- Brick alignment
    ontosage:capabilityCategory "AMENITIES" .

bldg:Issue_WaterLeak a ontosage:MaintenanceIssue, ontosage:KnowledgeTopic ;
    rdfs:label "Water leak / leakage" ;
    ontosage:layTerms "leak, leaking, water on the floor, flooding, dripping" ;
    ontosage:reportTo "Estates FM helpdesk (estates@example.ac.uk / 029 2087 6026)" ;
    ontosage:priority "URGENT" .
```

Both are answerable immediately — no restart.

## See also

- [Admin console]({{ '/docs/admin-console/' | relative_url }}) — the schema-driven "Add capability" form in the GUI.
- [Onboard a building]({{ '/docs/onboarding-building/' | relative_url }}) — where OCBV instances fit in the bigger picture.
