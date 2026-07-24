---
title: API Reference
layout: post
category: docs
permalink: /docs/api-reference/
date: 2026-07-10
---

# API reference

The orchestrator serves a REST + WebSocket API on port **8000**. Every response uses a common envelope
(`status`, `data`/`message`, `trace_id`); every data and admin endpoint is
[permission-gated]({{ '/docs/security-rbac/' | relative_url }}) — send `Authorization: Bearer <token>`.

This is an orientation map, not an exhaustive OpenAPI dump. The live schema is at
`http://localhost:8000/docs`.

## Auth

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/auth/register` | Create a user |
| `POST` | `/auth/login` | Get a session token |
| `POST` | `/auth/logout` | Invalidate the session |
| `GET` | `/auth/me` | Current user + role + permissions |

```bash
curl -s -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin@yourorg.com","password":"<pw>"}'
# → data.session_token
```

## Chat

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/chat` | Ask a question (native envelope) — requires `sensor:read` |
| `POST` | `/chat/stream` | Server-sent streaming variant |
| `WS` | `/stream` | WebSocket streaming |
| `POST` | `/v1/chat/completions` | OpenAI-compatible endpoint (used by OpenWebUI) |
| `GET` | `/v1/models` | OpenAI-compatible model list |

```bash
curl -s -X POST http://localhost:8000/chat \
  -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
  -d '{"message":"how many CO2 sensors are there?","session_id":"demo"}'
```

`message` (1–2000 chars) and `session_id` are required; `building_id` is an optional override.

## Conversations & history

| Method | Path | Purpose |
|---|---|---|
| `GET` | `/conversations/{user_id}` | List a user's conversations |
| `GET` | `/conversation/{conversation_id}` | Fetch one conversation |
| `DELETE` | `/conversation/{conversation_id}` | Delete a conversation |
| `GET`/`POST`/`DELETE` | `/history/{username}` | Chat history CRUD |

## Reports & floor plans

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/api/v1/report` | File a fault / complaint / safety / feedback report |
| `GET` | `/api/v1/floor-plans` | List floor plans |
| `GET` | `/api/v1/floor-plans/{building}/{floor}/manifest` | Room polygons + areas + adjacency |
| `GET` | `/api/v1/floor-plans/{building}/{floor}/svg` | Rendered floor SVG |
| `POST` | `/api/v1/floor-plans/reingest` | Rebuild floor-plan manifests |

## Admin — ontology (`system:admin`)

| Method | Path | Purpose |
|---|---|---|
| `GET` | `/api/v1/admin/ontology/graphs` | List named graphs |
| `POST` | `/api/v1/admin/ontology/validate` | Validate TTL text |
| `POST` | `/api/v1/admin/ontology/upload` | Upload TTL into a named graph |
| `DELETE` | `/api/v1/admin/ontology/graphs/{graph_id}` | Drop a named graph |
| `POST` | `/api/v1/admin/ontology/sparql` | SPARQL SELECT browser |

The console's Ontology tab exposes the same `/ontology/*` endpoints as a UI — named graphs, TTL upload,
and a live SPARQL browser:

![SPARQL browser with live results]({{ '/admin-portal-screenshots/09c-sparql-results.png' | relative_url }})
*A `SELECT ?class (COUNT(?s) …)` query returning live class counts from the graph, above the named-graph
list and Upload-TTL panel.*

## Admin — capabilities & schema-driven form (`system:admin`)

| Method | Path | Purpose |
|---|---|---|
| `GET` | `/api/v1/admin/capabilities` | List capabilities **+ `types`, `types_by_kind`, `form_fields`, `types_source`** (schema-derived) |
| `POST` | `/api/v1/admin/capabilities` | Create an amenity / knowledge topic |
| `DELETE` | `/api/v1/admin/capabilities/{local_name}` | Remove one |

## Admin — semantic index / reindex (`system:admin`)

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/api/v1/admin/reindex` | Enqueue a reindex job (capability / documents / floor_plans / ontology_similarity) |
| `GET` | `/api/v1/admin/reindex` | List jobs |
| `GET` | `/api/v1/admin/reindex/{job_id}` | Job status |
| `GET` | `/api/v1/admin/reindex/similarity-status` | Similarity-index status (BUILDING / BUILT) |

## Admin — documents & floor-plan upload (`config:write`)

Pure-GUI onboarding: upload knowledge files straight from the console — no host-side file drop. Each
writes into the **active** building's `input/` (resolved from `BUILDING_ID`, building-agnostic) and
re-indexes automatically. Uploads are `multipart/form-data`.

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/api/v1/admin/documents/upload` | Upload a `.md`/`.txt`/`.pdf` → `input/documents/` → document KB |
| `GET` | `/api/v1/admin/documents` | List documents in the active building |
| `DELETE` | `/api/v1/admin/documents/{name}` | Remove a document + re-index |
| `POST` | `/api/v1/admin/floor-plans/upload` | Upload a PDF/DWG (`floor`, optional `label`) → manifest registry |
| `GET` | `/api/v1/admin/floor-plans/files` | List floor-plan files in the active building |

```bash
# add a document (re-indexed into documents_<bldg>)
curl -s -X POST http://localhost:8000/api/v1/admin/documents/upload \
  -H "Authorization: Bearer $TOKEN" -F "file=@wifi_policy.md"

# add a floor plan for floor 3 (defaults label to the active building id)
curl -s -X POST http://localhost:8000/api/v1/admin/floor-plans/upload \
  -H "Authorization: Bearer $TOKEN" -F "floor=3" -F "file=@floor3.pdf"
```

## Admin — building identity & databases (`system:admin`)

| Method | Path | Purpose |
|---|---|---|
| `GET` | `/api/v1/admin/building/config` | Read namespace / prefix / name |
| `PUT` | `/api/v1/admin/building/config` | Set namespace / prefix / name → `building.yaml` |
| `GET` | `/api/v1/admin/databases` | Registered time-series databases |
| `POST` | `/api/v1/admin/databases/{db_key}/sensors` | Register sensors (persist to `input/` + index) |
| `POST` | `/api/v1/admin/databases/{db_key}/sensors/csv` | Bulk-register sensors from CSV |
| `GET` | `/api/v1/admin/databases/answerability` | Which sensors have **both halves** (ontology + rows) |

## Health & ops

| Method | Path | Auth | Purpose |
|---|---|---|---|
| `GET` | `/health` | none | Dependency status **+ `build.sha` / `build.time`** |
| `GET` | `/ping` | none | Liveness |
| `GET` | `/health/aggregate` | — | Rolled-up health |
| `GET` | `/metrics` | — | Prometheus metrics |

```bash
curl -s http://localhost:8000/health | python -m json.tool
```

## See also

- [Quick start]({{ '/docs/quickstart/' | relative_url }}) — worked auth + chat calls.
- [Security & RBAC]({{ '/docs/security-rbac/' | relative_url }}) — which permission each endpoint needs.
- Live OpenAPI: `http://localhost:8000/docs`.
