---
title: Configuration
layout: post
category: docs
permalink: /docs/configuration/
date: 2026-07-08
---

# Configuration

OntoSage is configured from exactly two places: **`.env`** (secrets, providers, feature flags) and the
**`input/`** folder (the building's data + config). `shared/config.py` is the single source of truth —
nothing is hardcoded per building.

You can edit the entire `.env` surface from the console's **Settings (.env)** tab (secrets masked),
rather than hand-editing files:

![Admin console Settings .env tab]({{ '/admin-portal-screenshots/07-settings-env.png' | relative_url }})
*The environment editor — every key with masked secrets, a filter, and a config backup/restore panel.
Changes apply after an orchestrator recreate.*

## `.env` — the operational surface

### Secrets (set these before first boot)

```bash
STRICT_SECRETS=true            # refuse to boot on any default secret (recommended)
SECRET_KEY=<random 64 chars>
GRAPHDB_PASSWORD=<real>
MYSQL_PASSWORD=<real>
POSTGRES_USER_PASSWORD=<real>

ADMIN_USERNAME=admin@yourorg.com
ADMIN_PASSWORD=<12+ chars>      # first admin, created on startup
```

### Model & embedding providers (independent)

```bash
MODEL_PROVIDER=local            # local (Ollama) | openai | cloud
OPENAI_API_KEY=<key>            # if MODEL_PROVIDER/EMBEDDING_PROVIDER = openai
OLLAMA_BASE_URL=http://ollama:11434

EMBEDDING_PROVIDER=local        # local (bge/MiniLM) | openai — chosen independently
```

Language and embedding models switch separately, so you can run the LLM on the API while keeping
embeddings local, or go fully offline. Always go through `MODEL_PROVIDER` / `EMBEDDING_PROVIDER` — never
hardcode a model. The console's **AI & Models** tab is the friendly front end for these keys:

![Admin console AI & Models tab]({{ '/admin-portal-screenshots/04-ai-models.png' | relative_url }})
*Pick the LLM provider (Local Ollama / Ollama Cloud / OpenAI) + model, and the embedding backend
(bge-large 1024-d or OpenAI 1536-d). Switching embeddings invalidates the Qdrant index — re-index after.*

### Active building

```bash
BUILDING_ID=bldg1               # which building under input/ is live
# Namespace/prefix are read from input/building.yaml (ontology_namespace / ontology_prefix)
# and can be set from the Admin console's Building-identity tab.
```

### Feature flags (common)

```bash
COREFERENCE_REWRITE_ENABLED=true    # rewrite follow-ups to standalone questions
MULTI_INTENT_ENABLED=true           # decompose compound questions
GOAL_PLANNER_ENABLED=false          # mandate decomposition ("make it eco-friendly")
CONVERSATION_MAX_MESSAGES=20        # count-bounded Redis memory
CONVERSATION_TTL=0                  # 0 = no time-expiry, count-bounded only
```

## `input/` — the building's data

The flat layout (files directly under `input/`) is canonical. See
[Onboard a building]({{ '/docs/onboarding-building/' | relative_url }}) for the full table. In short:

| File | Role |
|---|---|
| `building.yaml` | id, name, **ontology namespace + prefix**, actuation block |
| `*.ttl` | Brick/BACnet model + sensor `ref:` links (auto-uploaded) |
| `ontosage_schema.ttl` | the [OCBV vocabulary]({{ '/docs/ocbv-schema/' | relative_url }}) |
| `database_registry.yaml` | `ref:storedAt` key → real DB + adapter |
| `<bldg>_capabilities.ttl` | amenities / knowledge topics |
| `documents/`, `*.pdf`, `*.dwg` | document KB + floor plans |
| `concepts.ttl`, `feeds.yaml`, `rules.yaml`, `channels.yaml`, `intents.yaml`, `personas/` | optional overlays |

Anything absent = that feature is silently skipped. A `building.yaml` that disagrees with its TTL's
prefix, or an id mismatch, is caught by the TTL validator at boot and hard-fails — so a building never
runs half-configured.

Live feeds (`feeds.yaml`) and notification channels (`channels.yaml`) surface on the console's
**Integrations** tab, where you can see what's active and test-send a channel:

![Admin console Integrations tab]({{ '/admin-portal-screenshots/06-integrations.png' | relative_url }})
*Three `rest_poll` weather feeds polling Open-Meteo every 300s into `bldg:database1`, plus a `log`
notification channel with Test-send.*

## Where each store listens

| Store | Port | Role |
|---|---|---|
| Orchestrator API | 8000 | `/chat`, `/auth`, `/api/v1/admin/*` |
| Admin console (config-panel) | 3001 | GUI administration |
| Chat UI (OpenWebUI) | 3000 | Conversation |
| GraphDB | 7200 | Ontology + OCBV + similarity index |
| MySQL | 3306 | Time-series |
| PostgreSQL | 5433 | Users / RBAC / turn-memory / reports |
| Redis | 6379 | Conversation state, caches, sessions, job queue |
| Qdrant | 6333 | Vector collections |
| MongoDB | 27017 | Chat transcripts |
| rag-service | 8001 | SPARQL-gen retrieval |
| code-executor | 8002 | Sandboxed analytics Python |

## Build provenance

Images stamp the commit they were built from. Build with:

```bash
GIT_SHA=$(git rev-parse --short HEAD) BUILD_TIME=$(date -u +%FT%TZ) docker compose build
docker compose up -d          # 'up -d' recreates containers; 'restart' reuses the old image
```

`GET /health` then reports `build.sha` / `build.time` so you can confirm exactly what's running.

## See also

- [Security & RBAC]({{ '/docs/security-rbac/' | relative_url }}) — the secret + auth settings.
- [Onboard a building]({{ '/docs/onboarding-building/' | relative_url }}) — the `input/` folder in full.
