---
title: Introduction
layout: post
category: docs
permalink: /docs/introduction/
date: 2026-07-01
---

# What is OntoSage?

**OntoSage is an agentic conversational layer over one smart building's own data.** Connect a
building's Brick/BACnet ontology and its time-series database, and you can then *ask it anything in
plain English* — and get answers that are grounded in live data, framed for the person asking, and
able to span several intents in a single turn.

No SQL, no SPARQL, no schema knowledge required from the user. Ask *"is it stuffy on floor 5?"* and
OntoSage resolves "stuffy" to the CO₂ sensors, fetches their live readings, and answers in plain terms.
Ask a follow-up — *"and what about humidity there?"* — and it remembers you meant floor 5.

## The four surfaces it fuses

A single `POST /chat` endpoint answers over four data surfaces:

| Surface | What it holds | Where it lives |
|---|---|---|
| **Ontology graph** | Sensor URIs, zones, equipment hierarchy (Brick Schema + BACnet TTL) + the OCBV conversational layer | GraphDB (7200) |
| **Time-series store** | Per-sensor readings keyed by UUID | MySQL (3306) — pluggable to Postgres / Timescale / Influx |
| **Floor plans** | Room polygons, areas, adjacency, MEP blocks | PDF (text) + AutoCAD DWG (geometry) → JSON manifests + Qdrant |
| **Capability KB** | Off-ontology amenities, policies, contacts, how-to procedures | The **OCBV** schema + `input/<bldg>_capabilities.ttl` → GraphDB + Qdrant |

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
9. **Multiple datasources, pluggable.** Time-series routes by an ontology reference to the right
   backend. A new backend is a new adapter.
10. **Local or API models, independently.** Language and embedding models each switch between OpenAI and
    local Ollama — fully offline for privacy or on the API for capability.
11. **`docker compose up -d` is all you need.**

## What it will *not* do

- **Actuate the building.** Requests to open windows, change setpoints, or email someone are politely
  **declined** — OntoSage is a read/answer layer, not a BMS controller.
- **Invent data.** If a sensor isn't modelled or its readings aren't loaded, it says so.
- **Answer about a different building.** v1 is single-building by design.

## Where to go next

- [**Quick start**]({{ '/docs/quickstart/' | relative_url }}) — boot the stack and ask your first question.
- [**Architecture**]({{ '/docs/architecture/' | relative_url }}) — how a question flows through the pipeline.
- [**OCBV vocabulary**]({{ '/docs/ocbv-schema/' | relative_url }}) — the schema that makes a building talkable-to.
- [**Stakeholder guide**]({{ '/docs/stakeholder-guide/' | relative_url }}) — which questions can be answered.
