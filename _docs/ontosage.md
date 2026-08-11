---
layout: post
title: Full Technical Reference
date: 2026-07-11
category: docs
permalink: /docs/ontosage/
---

# OntoSage — Full Technical Reference

> **Start elsewhere if you're new.** For an overview read the
> [Introduction]({{ '/docs/introduction/' | relative_url }}) and
> [Architecture]({{ '/docs/architecture/' | relative_url }}); for the conversational schema see
> [OCBV]({{ '/docs/ocbv-schema/' | relative_url }}); to administer a building use the
> [Admin console]({{ '/docs/admin-console/' | relative_url }}). This page is the **deep operator +
> contributor reference** — source layout, every phase, and the routing internals — kept for depth.
> Where it mentions the older `capability.yaml` surface, that role is now filled by the
> [OCBV vocabulary]({{ '/docs/ocbv-schema/' | relative_url }}) (`input/<bldg>_capabilities.ttl` +
> `ontosage_schema.ttl`).

**Comprehensive operator + contributor reference for the OntoSage agentic-AI framework for smart buildings, covering every architectural change from Phase 11 through the Phase 18 production-hardening + libredwg geometry pipeline.**

> **TL;DR:** A user types a question in plain English. OntoSage classifies the intent (LLM), blends the user's stacked personas (registry), routes to the right pipeline (Python + audit-logged), and returns a structured answer. As of 2026-05-30, the **94/95 live-survey baseline (99% clean pass)** covers sensor data, capability KB, floor plans, spatial geometry, reports, exports, anomalies, multi-intent compound queries, multi-persona blended priors, and the per-request multi-tenant infrastructure already shipped as forward-compat for Onto-community v2.

---

## 1. What OntoSage is

OntoSage is an open-source, **building-agnostic** agentic-AI framework for talking to a building in
plain English. It is not built for one site: connect a building's ontology and the databases holding
its readings, and it answers questions about that building with no code changes. A deployment serves
**one active building at a time**, fusing four data surfaces into a single chat endpoint:

| Surface | What it holds | Where it lives |
|---|---|---|
| **Ontology graph** | Sensor URIs, zones, equipment hierarchy (Brick Schema + BACnet TTL) + the OCBV conversational vocabulary | GraphDB (port 7200) |
| **Time-series store** | Per-sensor readings keyed by UUID; routed per sensor by `ref:storedAt`, so one building can span several databases (a shipped example uses MySQL and PostgreSQL together) | MySQL / PostgreSQL / … — pluggable adapter per backend |
| **Floor plans** | Room polygons, areas, adjacency, MEP blocks | PDF (text) + AutoCAD DWG (geometry) → JSON manifests + Qdrant |
| **Capabilities & documents** | Amenities, policies, contacts, procedures — authored as `ontosage:Amenity` / `KnowledgeTopic` / `Policy` **triples**; a `Policy` names its governing document via `ontosage:documentRef` | OCBV schema + `input/<bldg>_capabilities.ttl` + `documents/` → GraphDB + Qdrant |

A single `POST /chat` endpoint returns natural-language answers, markdown tables, structured reports, exports (CSV/JSON), or visualizations (PNG plots). Ask it about *itself* — "what can you do?" — and it answers from live configuration as the framework it is.

**Grounded, never fabricated.** Every figure traces to a live triple or row. Ask about a floor, space,
amenity or measurement the building does not have and OntoSage says so and tells you what to add — it
will not substitute another sensor's reading, present an unrelated document as the answer, put a
confident verdict on a raw unscaled value, or (even when the existence check times out under load)
guess. The honesty guarantee is enforced by a stack of building-agnostic guards, not per-building tuning.

The next major release (**Onto-community**) will serve multiple buildings concurrently; v1 (today) is single-tenant by design, with the per-building infrastructure (registry caches, BuildingContextResolver, per-building Qdrant collections, persona overlays) already in place as forward-compatibility.

---

## 2. Architecture — hub-and-spoke LangGraph

`orchestrator/workflow/` (a Python package after Phase 17 — was a single 3,220-line file) defines a LangGraph state machine. Every request flows through:

```
                       POST /chat
                            │
                            ▼
                    ┌───────────────┐
                    │   dialogue    │ ← LLM classifies intent + extracts entities
                    └───────┬───────┘     persona priors surfaced into prompt (Phase 16B)
                            │
                            │ _route_from_dialogue (Python, audit-logged — Phase 13A)
                            ▼
   ┌───────┬────────────┬─────────┬─────────────┬───────────┬───────┬──────┐
   ▼       ▼            ▼         ▼             ▼           ▼       ▼      ▼
 sparql  capability  floor_plan spatial_q   control   maintenance export planner
   │      │           │          │           │           │           │     │
   ▼      └───────────┴──────────┴───────────┴───────────┴───────────┘     │
  sql                                                                       │
   │                                                                        │
   ▼                                                                        │
analytics ───► visualization                                                │
   │                                                                        │
   └────────────────────────────────────► response ◄────────────────────────┘
                                              │
                                              ▼
                                            client
```

The 17 graph nodes auto-register from `orchestrator/intents/intent_definitions.yaml` (Phase 13B). Shared infrastructure stages (`dialogue`, `sparql`, `sql`, `analytics`, `response`) and downstream-only nodes (`anomaly`, `report`, `document`) stay hardcoded because they aren't 1:1 with any intent.

### Source layout (post Phase 17)

```
orchestrator/
├── workflow/                       # Phase 17 — was a single 3,220-line file
│   ├── __init__.py                 #   25 lines — re-exports WorkflowOrchestrator
│   ├── _orchestrator.py            # 3,012 lines — node implementations
│   ├── _graph.py                   #  187 lines — WorkflowGraphMixin._build_graph
│   └── _routing.py                 #  115 lines — WorkflowRoutingMixin
├── intents/
│   ├── registry.py                 # IntentDefinition, IntentRegistry
│   └── intent_definitions.yaml     # 22 intents — single source of truth
├── agents/                         # 16 single-purpose agents
├── services/
│   ├── building_context.py         # Phase 10/11A — per-request building resolver
│   ├── ttl_validator.py            # Phase 12B — startup TTL ↔ namespace check
│   ├── multi_intent_detector.py    # Phase 14 — compound query decomposition
│   ├── dwg_pipeline.py             # Phase 18E — libredwg-driven DWG → geometry
│   └── …
└── auth_manager.py                 # Phase 18A — fail-closed on Postgres down

shared/
├── persona_registry.py             # Phase 14A — get_blended_priors()
├── pipeline_context.py             # Phase 17 — typed view over intermediate_results
└── …

input/                              # The ACTIVE building's files sit directly here (flat layout)
├── building.yaml
├── *.ttl                           # Brick/BACnet + <id>_capabilities.ttl (Amenity/KnowledgeTopic/Policy triples)
├── database_registry.yaml          # backends keyed by ref:storedAt (MySQL, PostgreSQL, …)
├── intents.yaml                    # optional per-building intent overlay
├── personas/                       # optional per-building persona overlay
├── documents/                      # optional manuals/policies (linked from Policy triples via documentRef)
└── *.dwg, *.pdf                    # optional floor plans

ontology/                           # shared, building-independent TTL (mounted read-only)
├── ontosage_schema.ttl             # the OCBV vocabulary — one copy for every building
└── hbco_core.ttl, hbco_mappings.ttl

scripts/
└── swap_building.py                # Phase 12C — safe building-swap CLI
```

### Storage layer

| Store | Port | Role |
|---|---|---|
| **GraphDB** | 7200 | RDF ontology (Brick/BACnet TTL); SPARQL agent target |
| **MySQL** | 3306 | Time-series sensor readings keyed by UUID |
| **PostgreSQL** | 5433 | User accounts, Argon2id password+salt, RBAC roles |
| **Redis** | 6379 | Conversation state (1h TTL), `resp_cache:*`, session tokens |
| **Qdrant** | 6333 | `floor_plans`, `capability_<bldg>`, `user_memory` collections |
| **MongoDB** | 27017 | Full chat-history transcripts (OpenWebUI) |
| **rag-service** | 8001 | Semantic fallback when SPARQL returns empty |
| **code-executor** | 8002 | Sandboxed Python for the analytics agent |

---

## 3. The 22 intents

All intents live in `orchestrator/intents/intent_definitions.yaml`. Each declares `name`, `description`, `examples`, `pipeline_group` (`data` | `standalone` | `meta`), and optionally `route_target`, `node_method` (Phase 13B), `aliases`, `cacheable`.

| Intent | Pipeline group | Default route | Node method |
|---|---|---|---|
| `general` | meta | response | shared |
| `greeting` | meta | response | shared |
| `clarification` | meta | response | shared |
| `planner` | meta | planner | `_planner_node` |
| `metadata` | data | sparql | shared pipeline |
| `discovery` | data | sparql | shared pipeline |
| `sensor_data` | data | sparql | shared pipeline |
| `analytics` | data | sparql | shared pipeline |
| `compare` (alias `comparison`) | data | sparql | shared pipeline |
| `trend` | data | sparql | shared pipeline |
| `recommend` | data | sparql | shared pipeline |
| `anomaly` | data | sparql | downstream `_anomaly_node` |
| `report` | data | **planner** (override) | downstream `_report_node` |
| `export` | data | **export** (override) | `_export_node` |
| `compliance` | data | sparql | shared pipeline |
| `visualization` | data | **visualization** (override) | `_visualization_node` |
| `floor_plan` | standalone | floor_plan | `_floor_plan_node` |
| `spatial_query` | standalone | spatial_query | `_spatial_query_node` |
| `capability` | standalone | capability | `_capability_node` |
| `control` | standalone | control | `_control_node` |
| `maintenance` | standalone | maintenance | `_maintenance_node` |
| `lab_booking` (bldg1 overlay) | standalone | (no node → safety net to response) | — |

---

## 4. Routing pipeline (smart-Python + smart-LLM hybrid)

```
LLM dialogue_agent classifies intent
            │
            ▼
_route_from_dialogue (workflow/_orchestrator.py)
            │
   ┌────────┴────────────────────────┐
   │ Contextual overrides (4):       │
   │  1. floor_plan ↔ comparison     │
   │     (compare+data keywords)     │
   │  2. floor_plan keyword detect   │
   │  3. discovery + spatial words   │
   │     → sparql (not response)     │
   │  4. analytics-family +          │
   │     cached data → analytics     │
   └────────┬────────────────────────┘
            │
            ▼
   registry.route_target_for(intent)
            │
            ▼
   Phase 10G safety net:
   target not registered → "response"
            │
            ▼
   LangGraph dispatches
            │
            ▼
   state.intermediate_results["route_decision"] = {
     intent_from_dialogue, intent_after_overrides,
     overrides_applied, final_node, decision_source
   }
```

**Why hybrid?** LLMs are smart at classifying ambiguous queries but unpredictable on edge cases. Python is fast and deterministic but rigid. Phase 13A combined them: LLM picks the intent **label**, Python resolves the **graph node**, an **audit trail** records every decision. The 4 contextual overrides catch known LLM weak spots (floor_plan vs comparison confusion, discovery vs SPARQL, etc.).

---

## 5. Multi-tenant + multi-persona + multi-intent

### 5.1 Multi-tenant (forward-compat for Onto-community v2)

v1 serves one building via `BUILDING_ID`. The code is already multi-tenant ready:

| Mechanism | Where | Phase |
|---|---|---|
| `IntentRegistry` keyed by `building_id` via `lru_cache` | `intents/registry.py` | 11A |
| `BuildingContextResolver.resolve(building_id)` | `services/building_context.py` | 10A/11A |
| Per-building Qdrant collection (`capability_<bldg>`) | `services/capability_indexer.py` | 5/14 |
| Per-building persona overlays | `shared/persona_loader.py` | 5/11C |
| Per-request SPARQL `ContextVar` | `agents/sparql_agent.py` | 15A |
| Storage adapter filter (`storage.databases`) | `services/adapters/registry.py` | 2 |

### 5.2 Multi-persona blending (Phase 14A + 16B)

A single turn can stack multiple personas:

```jsonc
POST /chat
{
  "message": "what should I look at this week?",
  "session_id": "...",
  "personas": ["facility_manager", "sustainability_officer"]
}
```

The `PersonaRegistry.get_blended_priors(personas)` merges:

| Field | Blend rule |
|---|---|
| `top_domains` | Rank-vote (1st=8pts, 2nd=7pts, …); ties keep first-encountered persona's order |
| `borda_topics` | Same rank-voting |
| `lookup_share` | Arithmetic mean |
| `default_complexity` | Max of `{SIMPLE < MODERATE < COMPLEX}` |
| `clarification_threshold` | Min (more willing to clarify) |

Phase 16B surfaces the blended priors into the LLM dialogue prompt so intent classification is persona-informed. Backward-compatible: legacy `persona: "facility_manager"` (single string) still works; when `personas` is present, `state.persona` is back-filled with `personas[0]`.

### 5.3 Multi-intent decomposition (Phase 14B + 16A)

A single user message can mix multiple intents:

```
"show me floor 3 layout and also tell me how many rooms are there"
```

Two-stage gate:

1. **Heuristic** (`MultiIntentDetector._passes_heuristic`):
   - length ≥ `MULTI_INTENT_MIN_LENGTH` (default **50 chars** after Phase 16A; was 80)
   - explicit connective from `_CONNECTIVE_PHRASES` ("and also", "tell me", "1.", "first/then/finally", etc.)
   - keywords from ≥ 2 distinct `INTENT_DOMAINS` sets
2. **LLM decomposition** returns 2–5 sub-intents validated against `VALID_INTENTS`.

When triggered, `state.current_intent` is rewritten to `"planner"` and the enhanced PlannerAgent fans out each sub-intent. Example decomposes to:

```python
[SubIntent(intent="floor_plan",    sub_query="floor 3 layout"),
 SubIntent(intent="spatial_query", sub_query="how many rooms on floor 3")]
```

---

## 6. Adding stuff via YAML (no code changes)

### Add a new intent (2 steps)

```yaml
# orchestrator/intents/intent_definitions.yaml (or input/<bldg>/intents.yaml)
- name: my_intent
  description: |-
    What this intent handles. Include trigger phrases.
  examples:
    - '"trigger query 1"'
  pipeline_group: standalone
  node_method: _my_node_fn
```

```python
# orchestrator/workflow/_orchestrator.py
async def _my_node_fn(self, state: ConversationState) -> ConversationState:
    state.intermediate_results["my_result"] = ...
    return state
```

Restart. Done. Graph wiring + routing dispatch auto-generated.

### Add a new persona

```yaml
# input/<bldg>/personas/safety_officer.yaml
name: safety_officer
top_domains: [FIRE_SAFETY, OCCUPANCY, THERMAL]
default_complexity: MODERATE
clarification_threshold: 0.40
borda_topics: [Fire Safety, Occupancy, Air Quality]
aliases: [fire_officer, safety]
```

### Swap to a new building

```bash
# 1. Drop files under input/<new>/  (building.yaml, *.ttl, *.dwg, *.pdf, …)
# 2. Validate
python scripts/swap_building.py --to <new> --dry-run
# 3. Apply (updates .env, archives old, flushes resp_cache)
python scripts/swap_building.py --to <new> --archive
# 4. Restart
docker-compose restart orchestrator
```

TTL validator hard-fails on `@prefix bldg:` ↔ `ontology_namespace` mismatch.

---

## 7. Phase changelog (11 → 18)

| Phase | Theme | Key change |
|---|---|---|
| **11A-C** | Multi-tenant intent + SPARQL bctx | `IntentRegistry` keyed by `building_id`; SPARQL agent uses per-request `bctx` from `BuildingContextResolver`; `input/_defaults/` loader added |
| **12A-D** | Single-building convention enforcement | `bldg2` moved to `tests/fixtures/`; `ttl_validator.py` hard-fails on prefix mismatch; `swap_building.py` CLI with archive + cache flush |
| **13A-E** | Routing diagnostics + auto-wire | `state.route_decision` audit trail; `_build_graph` iterates registry; adding an intent = 2 steps (down from 5) |
| **14A-D** | Multi-persona + multi-intent | `personas: List[str]` field; `get_blended_priors()` rank-vote merge; multi-intent decomposition verified live |
| **15A-E** | SPARQL ContextVar + swap cache flush | `ContextVar` threads per-request bctx through every SPARQL helper; swap CLI flushes only `resp_cache:*`; state round-trip tests |
| **16A-D** | Threshold tuning + persona-aware prompt + CI | `MULTI_INTENT_MIN_LENGTH 80→50`; LLM prompt sees blended priors; CI runs 13 test files |
| **17A-D** | `workflow.py` package split | 3,220-line monolith → `workflow/{__init__,_orchestrator,_graph,_routing}.py`; mixin-based, zero behavior change |
| **18A** | Auth fail-closed | When Postgres degraded, return *"service unavailable"* instead of misleading *"invalid password"* |
| **18B** | Postgres connect retry | 5 attempts with 2→4→8→16→30s exponential backoff |
| **18C** | Base image CVE remediation | All 7 Dockerfiles → `python:3.12-slim-trixie` (clears 1 critical + 13 high CVEs) |
| **18D** | wkhtmltopdf → weasyprint | Python-native PDF backend; pdfkit kept as legacy fallback |
| **18E** | libredwg source build | Multi-stage Dockerfile: `libredwg 0.13.3` from source; runtime gains `dwg2dxf` + 12 MB |

---

## 8. Test coverage

### Deterministic suite (CI)

**981 tests pass · 8 skip · 0 fail** on the Python 3.10 / 3.11 / 3.12 matrix, from a clean checkout
with no active building and no `.env` — exactly what CI sees. Selected files:

| File | Tests | Coverage |
|---|---|---|
| `test_routing_accuracy.py` | 29 | All intents + override scenarios + audit invariants |
| `test_routing_contract.py` | 51 | Every question-shape → intent rule + precedence + a scan proving no building literal |
| `test_grounding_guard.py` | 47 | Unrelated-passage refusal; typed-referent existence gate; verb-inflection matching; the "I don't hold that fact" caveat |
| `test_absent_referent_metrics.py` | 18 | A place the building lacks is declined, not answered with whole-building figures — even when the existence check times out |
| `test_plausibility.py` | 11 | No verdict over a value outside every plausible unit-range for its measurand |
| `test_self_description.py` | 16 | "What is OntoSage / what can you do" from live config as a building-agnostic framework — never a bare-LLM claim, never a building literal |
| `test_ontology_inventory.py` | 18 | "What equipment/sensors does this building have" from the graph's own Brick classes |
| `test_entity_label_resolution.py` | 12 | A prose-named sensor resolves to the one asked about, across two naming conventions |
| `test_embedding_standardisation.py` | 14 | Retrieval floor + vector width derived from the loaded model |
| `test_embedding_consistency.py` | 9 | Boot sweep drops any Qdrant collection at a mismatched width, for any building |
| `test_agents_building_agnostic.py` | 2 | Source scan: no agent names a building in code |
| `test_survey_aligned_phases.py` | 64 | Capability + persona + workflow wiring |
| `services/test_ttl_validator.py` | 10 | TTL parse + prefix/namespace + SHACL gating |

A **cross-building regression harness** (`scripts/regression_harness.py`) fills 14 behavioural checks
from the active building's own graph and compares them to a recorded baseline — so the same set proves
any building, including one onboarded tomorrow, and flags an honest decline that becomes an answer as a
fabrication risk.

### Live survey (`scripts/survey_live_test.py`)

**Phase 18 + libredwg baseline (2026-05-30):**

```
RESULTS: 94/95 PASS  ·  1 WARN  ·  0 FAIL  ·  (99% clean pass)
Latency: avg 16.7s · median 9.2s · max 71.2s
```

| Category | Result |
|---|---|
| Temperature, CO2, Humidity, Anomaly | All PASS |
| Discovery / Ontology / Analytics | All PASS |
| **Floor Plan / Spatial** | **4/4 PASS** (was 3/4 in every prior baseline — Phase 18E delivered T7-SP2 + T7-SP3) |
| Capability KB (12 questions) | 12/12 PASS |
| Routing edge cases | 4/4 PASS |
| Reports / Export | 4/4 PASS |
| Personas / Multi-hop reasoning | All PASS |
| Control (must decline) | 3/3 PASS |
| Robustness / SQL injection / out-of-scope | 6/6 PASS |
| Non-tech persona (T15) | 14/15 PASS (1 WARN: maintenance "report broken light") |
| Tech expert (T16) | 17/17 PASS |

---

## 9. Known issues

| # | Issue | Status |
|---|---|---|
| 10.1 | Argon2 salt fragility | **FIXED Phase 18A** — diagnosis revised; salt was already in Postgres, real bug was silent Redis fallback. Auth now fails closed honestly |
| 10.2 | Postgres connect race | **FIXED Phase 18B** — 5-attempt exponential backoff in lifespan |
| 10.3 | DWG geometry missing | **FIXED Phase 18E** — libredwg source build; all 6 floors ingest at startup; building total 20,370.2 m² queryable |
| 10.4 | Maintenance "report broken light" | Open — T15-S5 WARN; agent's nominal-create path needs missing-field detection |

---

## 10. Quick reference

### Live smoke

```bash
TOKEN=$(curl -s -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"...","password":"..."}' \
  | python -c "import sys,json; print(json.load(sys.stdin)['data']['session_token'])")

curl -s -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" -H "Authorization: $TOKEN" \
  -d '{
    "message":"What is the total area of floor 1?",
    "session_id":"smoke",
    "personas":["facility_manager","sustainability_officer"]
  }' | python -m json.tool
```

### Inspect routing decision

```bash
docker exec redis-memory-store redis-cli GET conversation:conv_<session_id>:<user>
# Look for the "route_decision" key in intermediate_results
```

### Run the live survey

```bash
python scripts/survey_live_test.py
```

---

## License + provenance

OntoSage is MIT-licensed. The Phase 11-18 work was developed against Cardiff University's Abacws building (`bldg1`) with `bldg2` as a multi-tenant fixture. Brick Schema is BSD-licensed. libredwg is GPLv3.

The single-building-at-a-time design is intentional for v1. The future **Onto-community** release will support multiple buildings simultaneously; the per-building infrastructure (registry caches, `BuildingContextResolver`, per-building Qdrant collections, persona overlays, SPARQL `ContextVar`) is the forward-compatible foundation already in place.
