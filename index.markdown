---
layout: home
title: OntoSage
description: Agentic AI for smart buildings — ask your building anything in plain English.
---

# OntoSage — Agentic AI for Smart Buildings

**Ask your building anything in plain English. Get sensor-grounded, persona-aware, multi-intent answers.**

OntoSage is an **agentic conversational layer over one smart building's own data** — *connect a
building's data, then ask it anything in plain English.* A facility manager opens the chat and asks
*"show me floor 3 and tell me how many rooms are there"*; OntoSage decomposes it, routes each part to
the right agent, and returns the floor map **and** the room count in one grounded answer — no SQL, no
SPARQL, no schema knowledge required.

Behind the scenes: a LangGraph state machine over a Brick/BACnet knowledge graph (GraphDB), live
time-series (MySQL, pluggable), floor-plan geometry (PDF/DWG), and the **OntoSage Conversational
Building Vocabulary (OCBV)** — the schema that makes a building *talkable-to*.

---

## Start here

| Guide | For |
|---|---|
| [**Introduction**]({{ '/docs/introduction/' | relative_url }}) | What OntoSage is and the design principles behind it |
| [**Quick start**]({{ '/docs/quickstart/' | relative_url }}) | Boot the whole stack with `docker compose up -d` and ask your first question |
| [**Architecture**]({{ '/docs/architecture/' | relative_url }}) | The LangGraph hub-and-spoke pipeline, storage layer, and model providers |

## Talking to the building

| Guide | For |
|---|---|
| [**OCBV — Conversational Building Vocabulary**]({{ '/docs/ocbv-schema/' | relative_url }}) | The schema that extends Brick so people can talk to the building — and how it drives both authoring *and* answering |
| [**Stakeholder guide**]({{ '/docs/stakeholder-guide/' | relative_url }}) | Which questions can be answered, and what data each one needs |

## Running & administering

| Guide | For |
|---|---|
| [**Admin console**]({{ '/docs/admin-console/' | relative_url }}) | The `:3001` console — building identity, schema-driven capability authoring, sensor registration, semantic-index status |
| [**Onboard a building**]({{ '/docs/onboarding-building/' | relative_url }}) | Connect a new building: namespace, TTL, database, capabilities — no code |
| [**Configuration**]({{ '/docs/configuration/' | relative_url }}) | The `.env` + `input/` surface, model providers, and every knob |
| [**Security & RBAC**]({{ '/docs/security-rbac/' | relative_url }}) | Authentication, the 6 roles × permissions, and how roles differ from personas |
| [**API reference**]({{ '/docs/api-reference/' | relative_url }}) | The chat, auth, and admin endpoints |
| [**Full technical reference**]({{ '/docs/ontosage/' | relative_url }}) | The deep architecture + phase-by-phase changelog |

---

## Design principles

Every one of these is a deliberate commitment, not an accident of implementation:

1. **One building at a time.** A deployment serves a single active building; the multi-building
   machinery is forward-compatibility, not a live multi-tenant mode.
2. **TTL-first — the ontology is the source of truth.** If a fact can be an RDF triple, it lives in the
   Brick/BACnet ontology. Questions are answered via SPARQL first; SQL/analytics handle only live
   time-series and things RDF can't express.
3. **No hardcoding — building-agnostic core.** No building-specific literals in core code; every figure
   in an answer is computed live from the graph or the floor plans, so it can never drift stale — and
   the same code runs unchanged for any building.
4. **Honest, grounded answers — never fabricate.** Every number traces to live data. If a referent
   doesn't exist or the data isn't loaded, OntoSage says so plainly.
5. **Any stakeholder, any purpose.** One interface serves facility managers, occupants, researchers,
   sustainability/safety officers, executives, visitors, students, and admins. Personas frame answers;
   they don't gate access.
6. **Zero-knowledge to expert.** Lay terms resolve to the right sensors; experts still get Brick
   classes, RDF types, and a live SPARQL browser.
7. **Admin-controlled access (RBAC).** Every data/config endpoint is permission-gated; ontology
   management is admin-only. Roles are separate from personas.
8. **Connect data, get answers.** A question is answerable when the sensor is in the ontology *and* its
   readings are in a registered database — both halves, no code.
9. **Multiple datasources, pluggable.** Time-series routes by an ontology reference to the right
   backend (MySQL today; Postgres/Timescale/Influx ready). A new backend is a new adapter.
10. **Local or API models, independently.** Language and embedding models each switch between OpenAI and
    local Ollama — run fully offline for privacy or on the API for capability.
11. **`docker compose up -d` is all you need.** The entire stack boots with one command; config lives in
    `.env` and the `input/` folder.

---

## What's new

- **OCBV 2.0** — the single, publication-ready *Conversational Building Vocabulary* over Brick:
  capabilities, conversation concepts, stakeholder roles, question-intent grammar, report intake,
  answer provenance, competency questions + example SPARQL. [Read →]({{ '/docs/ocbv-schema/' | relative_url }})
- **Schema-driven console** — the "Add capability" dropdown *and* form fields are generated live from
  the OCBV schema; add a class/property to the TTL and it appears in the form, no code change.
- **Schema-fed RAG** — the schema's descriptions and example SPARQL are indexed so a plain-English
  question matches the right term and hands its query template to the LLM.
- **TTL-first sensor registration** — GUI-registered sensors persist to `input/`, survive restarts, and
  auto-trigger a debounced, self-healing semantic-index rebuild.
- **Building-identity GUI** — set the ontology namespace/prefix from the console.

---

**Ready?** Start with the [Quick start]({{ '/docs/quickstart/' | relative_url }}), then explore the
[OCBV vocabulary]({{ '/docs/ocbv-schema/' | relative_url }}) — the heart of how OntoSage lets people
talk to a building.
