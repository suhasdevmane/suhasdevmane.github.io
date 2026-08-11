---
title: Introduction
layout: post
category: docs
permalink: /docs/introduction/
date: 2026-07-01
---

# What is OntoSage?

**OntoSage is a building-agnostic framework for talking to a building in plain English.** It is not
built for any one site: connect a building's Brick/BACnet ontology and the databases holding its
sensor readings, and OntoSage answers questions about *that* building — grounded in live data, framed
for the person asking, and able to span several intents in a single turn. Onboarding a new building is
configuration and data — a Brick TTL, database credentials, optional documents and floor plans — with
no code changes. A single deployment serves one active building at a time; the same code serves the
next building unchanged.

Ask OntoSage what it is — *"what can you do?"*, *"how do you work?"* — and it answers from its own live
configuration as the framework it is, never claiming to be a generic chatbot.

No SQL, no SPARQL, no schema knowledge required from the user. Ask *"is it stuffy on floor 5?"* and
OntoSage resolves "stuffy" to the CO₂ sensors, fetches their live readings, and answers in plain terms.
Ask a follow-up — *"and what about humidity there?"* — and it remembers you meant floor 5. Ask about a
space or building it does not have — *"how many sensors are in the swimming pool?"* — and it says it
cannot find that, rather than answering with another sensor's readings.

## Key features at a glance

| | Feature | What it means |
|---|---|---|
| 🏢 | **Zero core-code changes to onboard a building** | The core and `shared/` carry no building literals. A new building is *config + data only* — a Brick TTL, a registered database, optional documents/floor plans. The same code serves `bldg1`, `bldg2`, or yours unchanged. |
| 🖥️ | **Full onboarding from the Admin Console** | Set building identity, upload TTL, connect a database and register sensors, add documents and floor-plan PDFs/DWGs, author capabilities, browse SPARQL — all in the browser, no host-side editing. Dropping a file in `input/` and doing it in the GUI are equivalent. |
| 🎯 | **Grounded, never fabricated** | Every figure traces to a live triple or row. If the sensor or data isn't there, OntoSage says "no data" — it never invents a value. |
| 🧩 | **Agentic & multi-intent** | A LangGraph state machine classifies intent, rewrites follow-ups, decomposes compound questions, and routes each part to the right agent (SPARQL → SQL → analytics / floor-plan / capability), then fuses one answer. |
| 💬 | **Zero-knowledge to expert** | Lay terms resolve ("stuffy" → CO₂) for anyone; experts still get Brick classes, the SPARQL browser, and the full API. |
| 🔌 | **Multiple, pluggable datasources — even within one building** | Each sensor's `ref:storedAt` routes its readings to the right backend, so different sensors in the *same* building can live in different databases. A shipped example serves one building from **MySQL and PostgreSQL at once**. The registry has connection templates for ~50 stores; a new backend is a new adapter, never an agent edit. |
| 🤖 | **Answers about itself** | Ask *"what is OntoSage / what can you do / how do you work"* and it answers from live configuration as a building-agnostic framework — the capability list comes from the active building's own intent registry, so it can never drift from what the system actually does. |
| ⚙️ | **Local or API models, independently** | Run fully local on Ollama (`gpt-oss:20b`) or via OpenAI; the LLM and the embedding backend switch independently. |
| 🔒 | **Admin-controlled access (RBAC)** | Every data/config endpoint is gated — 6 roles × 20 permissions. Personas frame answers; they never grant access. |
| 🐳 | **One command to boot** | `docker compose up -d` brings up the whole stack; config lives in `.env` + `input/`. |

## The four surfaces it fuses

A single `POST /chat` endpoint answers over four data surfaces:

| Surface | What it holds | Where it lives |
|---|---|---|
| **Ontology graph** | Sensor URIs, zones, equipment hierarchy (Brick Schema + BACnet TTL) + the OCBV conversational layer | GraphDB (7200) |
| **Time-series store** | Per-sensor readings keyed by UUID | MySQL (3306) — pluggable to Postgres / Timescale / Influx |
| **Floor plans** | Room polygons, areas, adjacency, MEP blocks | PDF (text) + AutoCAD DWG (geometry) → JSON manifests + Qdrant |
| **Capabilities & documents** | Amenities, policies, contacts, how-to procedures — authored as `ontosage:Amenity` / `KnowledgeTopic` / `Policy` triples; a `Policy` names the document that sets it out in full via `ontosage:documentRef`, so the long form is read from *that* file rather than a similarity guess | The **OCBV** schema + `input/<bldg>_capabilities.ttl` + `documents/` → GraphDB + Qdrant |

The [admin console]({{ '/docs/admin-console/' | relative_url }}) shows all four surfaces and the running
system at a glance:

![Admin console Overview]({{ '/admin-portal-screenshots/01-overview.png' | relative_url }})
*One deployment, one active building: provider, enabled data sources, embedding model, users/roles, and
service health.*

## What makes it different — the design principles

Each of these is a deliberate commitment:

1. **One building at a time.** A deployment serves a single active building; the multi-building
   machinery is forward-compatibility, not a live multi-tenant mode.
2. **TTL-first — the ontology is the source of truth.** If a fact can be an RDF triple, it lives in the
   Brick/BACnet ontology (or the [OCBV vocabulary]({{ '/docs/ocbv-schema/' | relative_url }})), not a
   sidecar file or a code constant. Questions are answered via SPARQL first.
3. **No hardcoding — building-agnostic core.** Core code carries no building-specific literals; every
   figure is computed live, so it never drifts stale, and the same code runs for any building.
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
9. **Multiple datasources, pluggable — even within one building.** Each sensor's `ref:storedAt` routes
   its readings to its own backend, so one building can run several database technologies at once
   (a shipped example uses MySQL and PostgreSQL together). A new backend is a new adapter.
10. **Local or API models, independently.** Language and embedding models each switch between OpenAI and
    local Ollama — fully offline for privacy or on the API for capability.
11. **`docker compose up -d` is all you need.**

## What it will *not* do

- **Actuate the building.** Requests to open windows, change setpoints, or email someone are politely
  **declined** — OntoSage is a read/answer layer, not a BMS controller.
- **Invent data.** Ask about a floor, wing, amenity, asset or measurement the building does not have —
  *"the swimming pool"*, *"floor 42"*, *"the methane concentration"* — and OntoSage names what does
  exist instead, or says plainly that it can't find that, and tells you what to add to make it
  answerable. It will not quietly substitute another sensor's reading, present an unrelated document as
  the answer, or pass a raw unscaled number off as a confident verdict. Even when the check that
  confirms a place exists cannot complete under load, it refuses rather than guessing — a
  plausible-sounding wrong number is worse than no number, because you can't tell it apart from a right
  one.
- **Answer about a different building.** A deployment is single-building by design; a reference to some
  other building is treated as "not here."
- **Pretend to be a generic chatbot.** Asked how it works, it describes itself as the framework it is —
  it will not claim to be "a large language model."

## Where to go next

- [**Quick start**]({{ '/docs/quickstart/' | relative_url }}) — boot the stack and ask your first question.
- [**Architecture**]({{ '/docs/architecture/' | relative_url }}) — how a question flows through the pipeline.
- [**OCBV vocabulary**]({{ '/docs/ocbv-schema/' | relative_url }}) — the schema that makes a building talkable-to.
- [**Stakeholder guide**]({{ '/docs/stakeholder-guide/' | relative_url }}) — which questions can be answered.
