---
title: Architecture
layout: post
category: docs
permalink: /docs/architecture/
date: 2026-07-03
---

# Architecture

OntoSage is a **LangGraph hub-and-spoke state machine**. Every request flows through a dialogue node
(intent classification), a deterministic Python router, one or more agent nodes (spokes), and a
response node — with a full routing audit trail written to Redis.

## The pipeline

```
User question (natural language)
        │
        ▼
[Co-reference rewrite]  — "and humidity there?" → "average humidity on floor 3"
        │
        ▼
dialogue agent  — LLM classifies intent + extracts entities (persona priors injected)
        │
        ▼
_route_from_dialogue  — deterministic, audit-logged Python router
        │
   ┌────┴───────────────┬───────────┬──────────┬───────────┬──────────┐
   ▼        ▼            ▼           ▼          ▼           ▼          ▼
 sparql  capability  floor_plan  spatial   control   maintenance   planner
   │       (Qdrant)                                                   │
   ▼                                                                  │
  sql  (routes by ref:storedAt → adapter → time-series DB)            │
   │                                                                  │
   ▼                                                                  │
analytics ──► visualization                                           │
   │                                                                  │
   └───────────────────────► response ◄─────────────────────────────┘
                                │
                                ▼   [persist conversation memory]
                             client
```

- **Nodes auto-register** from `orchestrator/intents/intent_definitions.yaml` — adding an intent is a
  YAML entry + one method, no graph edits.
- **dialogue** classifies the intent and extracts entities; it also runs the co-reference rewrite and a
  capability semantic-router probe.
- **sparql** generates + executes SPARQL against GraphDB, with a semantic RAG fallback (rag-service on
  8001) when a query returns empty.
- **sql** fetches time-series by UUID, routing to the right backend via the adapter registry.
- **analytics** writes Python that runs in a sandboxed `code-executor` (8002); **forecast** adds
  multi-model projections.
- **floor_plan / spatial** answer from PDF/DWG floor-plan manifests (no LLM for geometry).
- **capability** answers off-ontology amenity/procedure/policy questions from the
  [OCBV]({{ '/docs/ocbv-schema/' | relative_url }}) graph + document KB.

## Why a smart-Python + smart-LLM hybrid?

LLMs are good at classifying ambiguous questions but unpredictable on edge cases; Python is fast and
deterministic but rigid. OntoSage combines them: the **LLM picks the intent label**, **Python resolves
the graph node** (with a handful of contextual overrides for known LLM weak spots), and an **audit
trail** (`state.intermediate_results["route_decision"]`) records every decision — so routing is both
smart and debuggable.

## The two-half answer model

Every time-series question needs **both halves**:

```
NL question → SPARQL on GraphDB   (finds the sensor + its UUID + which DB it is ref:storedAt)
           → SQL routes by ref:storedAt → that DB's adapter → rows by UUID → answer
```

A database with rows but no ontology triples is invisible; a sensor in the ontology with no rows has no
data. [Onboarding a source]({{ '/docs/onboarding-building/' | relative_url }}) means providing both —
which is why enabling a source in the console writes triples *and* rows together, and every answer is
then tagged with the system that produced it:

![Data Sources tab with provenance legend]({{ '/admin-portal-screenshots/02-data-sources.png' | relative_url }})
*Toggling a source unlocks its questions; the provenance legend (right) names each source system, and
`simulated` marks synthetic data injected to demonstrate a capability a real BMS wouldn't expose.*

## Storage layer

| Store | Port | Role |
|---|---|---|
| **GraphDB** | 7200 | Brick/BACnet RDF ontology + OCBV; the SPARQL agent's target; hosts the similarity index for semantic retrieval |
| **MySQL** | 3306 | Time-series sensor readings keyed by UUID (wide `sensor_data` + narrow `(uuid, datetime, value)` tables) |
| **PostgreSQL** | 5433 | User accounts, Argon2id passwords, RBAC roles, turn-memory, user reports |
| **Redis** | 6379 | Conversation state (count-bounded), response cache, embedding cache, session tokens, async job queue |
| **Qdrant** | 6333 | `capability_<bldg>`, `documents_<bldg>`, `floor_plans`, `user_memory` vector collections |
| **MongoDB** | 27017 | Full chat transcripts (OpenWebUI) |
| **rag-service** | 8001 | GraphDB-backed semantic retrieval for SPARQL generation |
| **code-executor** | 8002 | Sandboxed Python for the analytics agent |

## Models & providers

`shared/config.py` is the single source of truth. `MODEL_PROVIDER` = `openai` / `local` (Ollama) /
`cloud`; `EMBEDDING_PROVIDER` (`openai` 1536-d / `local` bge/MiniLM) is independent — so you can run
fully offline or on the API, and swap either without touching the other.

## Conversation memory & co-reference

- **Memory** (`turn_memory.py`): Redis holds recent state (count-bounded); Postgres keeps per-turn
  summaries + carry-forward of forecast/analytics results (so *"now plot that"* works).
- **Co-reference**: follow-ups (*"…humidity there?"*) are rewritten to self-contained queries before
  classification.

## Deeper

The [full technical reference]({{ '/docs/ontosage/' | relative_url }}) covers the source layout,
every intent, the routing overrides, the multi-persona/multi-intent model, forecasting, and the
phase-by-phase changelog.
