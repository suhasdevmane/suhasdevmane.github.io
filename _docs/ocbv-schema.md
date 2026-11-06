---
title: OCBV — Conversational Building Vocabulary
layout: post
category: docs
permalink: /docs/ocbv-schema/
date: 2026-07-18
---

This page introduces the OntoSage Conversational Building Vocabulary (OCBV): what it adds to a
Brick model, how its modules are organised, and how the admin console and the retrieval step
use it. It is for building owners and administrators deciding what to put in a building's TTL.
The term-by-term reference is the [Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}).

## What OCBV is

Brick models a building's technical fabric (points, sensors, equipment, locations) for machines.
It does not model what people ask a building: *"where's the prayer room?"*, *"is it stuffy on
floor 5?"*, *"the toilet is leaking, who do I tell?"*, *"which permits are open?"*.

OCBV adds that layer. It is one file in the OntoSage repository,
[`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl),
published under CC BY 4.0, with its terms in two namespaces: `ontosage:`
(`http://ontosage.org/capabilities#`) and `hbco:` (`http://ontosage.org/hbco#`). Three smaller
files sit beside it in `ontology/`: `hbco_mappings.ttl` (the lay-term concepts),
`measurand_kinds.ttl` (what each sensor class measures, and the physical range of a reading)
and `record_documents/` (mappings that turn a building's register documents into triples). The
orchestrator loads the TTL files into GraphDB at startup whichever building is active, and the
document indexer reads the mappings; a building does not copy any of them into its own folder.

## It extends Brick and does not contradict it

OCBV declares only `ontosage:` and `hbco:` terms. Where it touches the physical building it uses
Brick classes as the domain or range of its properties (`ontosage:locatedIn` points at a
`brick:Location`, `hbco:mapsToBrickClass` at a Brick sensor class), and where Brick 1.4 lacks a
class it subclasses the nearest Brick one in its own namespace. Alignments to REC, BOT and SOSA
use SKOS mapping properties (`skos:relatedMatch`, `skos:closeMatch`), never
`owl:equivalentClass`, so loading OCBV beside a Brick model adds triples and invalidates
nothing. The details, with the full list of Brick classes OCBV specialises, are in
[How OntoSage Extends Brick]({{ '/docs/ontology-extensions/' | relative_url }}).

## Modules

The file is organised in lettered modules. The main ones:

| Module | What it models |
|---|---|
| **A: Capabilities** | `ontosage:Capability` → `ontosage:Amenity` (prayer room, café, lift, toilet, drinking water, assembly point, parking, first aid and others) and → `ontosage:KnowledgeTopic` (information topic, procedure, policy, maintenance issue); class-level lay terms; the properties an answer is built from (`locationText`, `answerText`, `steps`, `reportTo`, `documentRef`, `openingHours` and others). Module A2 adds the building's own description (owner, operator, address, purpose) on the `brick:Building` instance. |
| **B: Conversation concepts (HBCO)** | `hbco:Concept`, `hbco:layTerm`, `hbco:mapsToBrickClass`: a lay word mapped to the sensor classes whose readings answer it ("stuffy" → CO2). |
| **C: Stakeholder roles** | `ontosage:StakeholderRole` (occupant, visitor, facility manager, researcher and others). Frames how an answer is phrased; it is not an access-control role. |
| **D: Question intents** | `ontosage:QuestionIntent` (locate, quantify, trend, compare, anomaly, forecast, comfort, discover, procedure, report). |
| **E: Report intake** | `ontosage:Report` → fault report, complaint, safety report, feedback, suggestion. |
| **F: Answer provenance** | `ontosage:SourceType` and `ontosage:groundedIn`. A fact stated in a triple (`Src_Ontology`) and a passage retrieved from a document (`Src_Document`) are separate source types, because they are different strengths of evidence. |
| **G: Competency questions** | `ontosage:competencyQuestion` and `ontosage:exampleSparql` annotations on the classes they serve. |
| **H, I** | Standards alignment; capability categories as SKOS concepts; SHACL shapes. |
| **J to S** | Interval records and records of the building's registers (permits, work orders, bookings, contracts, tariffs and others), forecast skill, access policies, sensor metadata and calibration, served zones, service state and potability, waste and targets, the organisation that runs the building. |

The full module list is in
[How OntoSage Extends Brick]({{ '/docs/ontology-extensions/' | relative_url }}#what-each-ontology-file-adds),
and the controlled vocabularies are listed under
[Vocabularies]({{ '/docs/ontology-browser/' | relative_url }}#vocabularies) in the browser.
Every declared class and property has an `rdfs:label`; every declared class and most
properties have an `rdfs:comment`, and the core terms also carry `skos:definition` and
`skos:example`.

## The schema drives capability authoring

The console's **Ontology** tab lists the named graphs the schema and the building's files are
loaded into, beside TTL upload and a SPARQL browser:

![Named graphs in the console's Ontology tab]({{ '/assets/images/screenshots/admin-ontology-graphs.png' | relative_url }})
*The named graphs in the active building's repository, one per loaded TTL file.*

Capabilities (amenities and knowledge topics) are added in one of two ways:

- **Edit the building's `<id>_capabilities.ttl`** (or any TTL file in its input folder) and
  restart the orchestrator. The file is loaded into its own named graph at startup.
- **Call the admin API**, `POST /api/v1/admin/capabilities`, with an administrator's session
  token. The orchestrator builds the Turtle, validates it, appends it to `<id>_capabilities.ttl`
  and re-syncs that file's named graph, so no restart is needed:

  ```bash
  curl -s -X POST http://localhost:8000/api/v1/admin/capabilities \
    -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
    -d '{"id": "PrayerRoom_104", "type": "PrayerRoom", "label": "Multi-faith prayer room",
         "floor": "1", "location": "Floor 1, room 1.04",
         "lay_terms": "prayer room, quiet room, where can i pray"}'
  ```

  `GET /api/v1/admin/capabilities` lists the existing capabilities, and `DELETE
  /api/v1/admin/capabilities/<local name>` removes one. See
  [API Reference]({{ '/docs/api-reference/' | relative_url }}).

The console's Add capability dialog (Ontology tab) is a third route: it calls the same API and
draws the form from the schema rules below.

The API takes its rules from the schema in GraphDB (`orchestrator/services/capability_admin.py`):

- **`type`** must be a subclass of `ontosage:Amenity` or `ontosage:KnowledgeTopic` in the
  `ontosage:` namespace (`get_capability_classes`). Add such a class to the schema and the API
  accepts it after a reload, with no code change. The new instance is typed with the chosen
  class and with `ontosage:Amenity` or `ontosage:KnowledgeTopic`.
- **The fields** map to a fixed set of thirteen datatype properties: `lay_terms` →
  `ontosage:layTerms`, `location` → `locationText`, `floor` → `onFloor`, `category` →
  `capabilityCategory`, `opening_hours` → `openingHours`, and `note`, `answer_text`,
  `info_url`, `contact_email`, `contact_phone`, `report_to`, `steps` and `priority` to the
  properties of the same name. `GET /api/v1/admin/capabilities` also returns, in
  `form_fields`, which of these apply to which type, read from each property's `rdfs:domain`
  (`get_capability_form_schema`): `locationText` applies to an Amenity, `steps` to a Procedure,
  `priority` to a MaintenanceIssue. A new property in the schema is not accepted by the API
  unless it is one of these; `documentRef`, `effectiveDate` and `policyOwner` are written in
  TTL.

If GraphDB cannot be reached, the type and field lists fall back to built-in ones.

## The schema feeds retrieval

The GraphDB similarity index that finds terms from a question
(`orchestrator/services/ontology_manager.py`) indexes, for every typed IRI, its label, type
name, local name, `rdfs:comment`, `skos:definition`, `skos:example`, `ontosage:layTerms` and
`ontosage:competencyQuestion`. A plain-English question such as *"the toilet is leaking, who do
I tell"* can therefore match `ontosage:MaintenanceIssue`. The retrieval step then fetches the
triples within two hops of the matched terms for the language model that writes SPARQL, and for
a schema class those include its `ontosage:exampleSparql`, a query of the right shape to adapt.

## Authoring instances

Instances are authored in a TTL file in the building's input folder, or through
`POST /api/v1/admin/capabilities` as above. The schema's own worked examples (Module J of
`ontosage_schema.ttl`, shortened) show the shape:

```turtle
bldg:PrayerRoom_104 a ontosage:PrayerRoom, ontosage:Amenity ;
    rdfs:label "Multi-faith prayer & reflection room" ;
    ontosage:layTerms "prayer room, quiet room, where can i pray, faith room" ;
    ontosage:locationText "Floor 1, room 1.04" ;
    ontosage:onFloor "1" ;
    ontosage:locatedIn bldg:Room_1.04 ;          # <- Brick alignment
    ontosage:capabilityCategory "AMENITIES" .

bldg:Issue_WaterLeak a ontosage:MaintenanceIssue, ontosage:KnowledgeTopic ;
    rdfs:label "Water leak / leakage" ;
    ontosage:layTerms "leak, leaking, leakage, water on the floor, flooding, dripping" ;
    ontosage:answerText "Report water leaks to Estates immediately so they can isolate the supply." ;
    ontosage:priority "URGENT" ;
    ontosage:capabilityCategory "MAINTENANCE" .
```

A file in the building's folder must also declare the building's prefix (`@prefix bldg: <…> .`
with the `ontology_namespace` from `building.yaml`), or the orchestrator refuses to start. See
[How OntoSage Extends Brick]({{ '/docs/ontology-extensions/' | relative_url }}#adding-your-own-terms).

### A policy names the document that sets it out

Some answers are long-form: a fire-safety procedure, a data-protection policy. A
`ontosage:Policy` (or any knowledge topic) carries the short answer and names the file that
holds the rest with `ontosage:documentRef`. From the reference building's
`bldg1_capabilities.ttl`, shortened:

```turtle
bldg:Cap_fire_safety a ontosage:InformationTopic,
        ontosage:KnowledgeTopic,
        ontosage:Policy ;
    rdfs:label "Fire Safety"@en ;
    ontosage:answerText """Fire safety features include: (1) Automatic smoke and heat detectors on every floor; …""" ;
    ontosage:capabilityCategory "INFORMATION" ;
    ontosage:documentRef "fire_safety.md" ;
    ontosage:layTerms "fire, fire alarm, evacuation, emergency exit, fire escape, smoke detector, …" .
```

When a question matches the topic by lay term, the capability lane
(`orchestrator/agents/capability_agent.py`) searches only the named file in the building's
`documents/` folder for the detail, so similarity only orders passages within a document already
known to be the right one. Without the link, which document answers depends on a similarity
threshold tuned for one set of documents and one embedding model. The triple holds the structure
and the short answer, the document holds the long form, and `documentRef` joins them.
`ontosage:effectiveDate` and `ontosage:policyOwner` can be added to say which version is quoted
and who owns it.

## See also

- [Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}): every OCBV class, property
  and vocabulary, generated from the TTL.
- [Ontology Relationships]({{ '/docs/ontology-relationships/' | relative_url }}): how a
  building graph connects spaces, sensors, readings, capabilities and records.
- [How OntoSage Extends Brick]({{ '/docs/ontology-extensions/' | relative_url }}): namespaces,
  alignment, per-building files and adding your own terms.
- [Admin console]({{ '/docs/admin-console/' | relative_url }}): the Ontology tab, named graphs
  and the SPARQL browser.
- [Onboard a building]({{ '/docs/onboarding-building/' | relative_url }}): where OCBV instances
  fit in the bigger picture.
