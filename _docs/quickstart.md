---
title: Quick Start
layout: post
category: docs
permalink: /docs/quickstart/
date: 2026-07-02
---

# Quick start

The entire stack boots with one command. Configuration lives in `.env` and the `input/` folder — no
build steps outside Docker.

## 1. Configure and start

```bash
git clone https://github.com/suhasdevmane/OntoSage.git
cd OntoSage
cp .env.example .env          # then edit — see below

docker compose up -d          # boots every service
docker compose logs -f orchestrator
```

Minimum `.env` to set before first start:

```bash
# Admin account (created on startup; no default admin exists)
ADMIN_USERNAME=admin@yourorg.com
ADMIN_PASSWORD=<strong-password-12+chars>

# Refuse to boot on default secrets (recommended)
STRICT_SECRETS=true
SECRET_KEY=<random-64-char>
GRAPHDB_PASSWORD=<real-password>
MYSQL_PASSWORD=<real-password>
POSTGRES_USER_PASSWORD=<real-password>

# Model providers (each independent) — openai | local | cloud
MODEL_PROVIDER=local          # local = Ollama, offline
EMBEDDING_PROVIDER=local
```

See [Configuration]({{ '/docs/configuration/' | relative_url }}) for the full surface.

## 2. Authenticate

```bash
TOKEN=$(curl -s -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin@yourorg.com","password":"<password>"}' \
  | python -c "import sys,json; print(json.load(sys.stdin)['data']['session_token'])")
```

## 3. Ask questions

```bash
# Structural — answered from the ontology alone (SPARQL, no time-series)
curl -s -X POST http://localhost:8000/chat \
  -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
  -d '{"message":"how many CO2 sensors are there?","session_id":"demo"}'

# Live reading — needs ontology + time-series
curl -s -X POST http://localhost:8000/chat \
  -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
  -d '{"message":"what is the temperature on floor 3 right now?","session_id":"demo"}'

# Multi-intent in one turn
curl -s -X POST http://localhost:8000/chat \
  -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
  -d '{"message":"show me floor 3 and tell me how many rooms are there","session_id":"demo"}'
```

## 4. Open the web interfaces

| Interface | URL | What |
|---|---|---|
| **Chat UI** | `http://localhost:3000` | OpenWebUI — full multi-turn conversation |
| **Admin console** | `http://localhost:3001` | [config-panel]({{ '/docs/admin-console/' | relative_url }}) — building identity, capabilities, sensors, ontology, reindex, health |
| **GraphDB** | `http://localhost:7200` | SPARQL workbench |
| **Qdrant** | `http://localhost:6333/dashboard` | Vector store dashboard |

The admin console's Overview tab gives you the whole deployment at a glance:

![Admin console Overview]({{ '/admin-portal-screenshots/01-overview.png' | relative_url }})
*Provider, enabled data sources, active building, embedding model, users/roles, and service health — with
quick-action buttons into each flow. See the [Admin console]({{ '/docs/admin-console/' | relative_url }}) guide.*

## 5. Health & build provenance

```bash
curl -s http://localhost:8000/health | python -m json.tool
```

The response reports each dependency's status plus `build.sha` / `build.time` — the exact commit each
image was built from. The console's Health tab shows the same live status visually:

![Admin console Health tab]({{ '/admin-portal-screenshots/11-health.png' | relative_url }})
*Overall health, request latency, every dependency (Postgres, MySQL, GraphDB, Redis, Qdrant,
rag-service, code-executor), and the LLM/MySQL circuit breakers.*

Build images with the commit stamped in:

```bash
GIT_SHA=$(git rev-parse --short HEAD) BUILD_TIME=$(date -u +%FT%TZ) docker compose build
docker compose up -d orchestrator graphdb-rag-service   # 'up -d' (recreate), not 'restart'
```

## Next

- [Onboard your own building]({{ '/docs/onboarding-building/' | relative_url }}) — namespace, TTL, database, capabilities.
- [Admin console]({{ '/docs/admin-console/' | relative_url }}) — do it all from the GUI, no code.
