---
title: Configuration
layout: post
category: docs
permalink: /docs/configuration/
date: 2026-07-20
---

# Configuration

OntoSage reads its configuration from four places. Nothing about a particular building is
written into the code.

| Place | What it holds | Who reads it |
|---|---|---|
| `.env` (repository root) | Secrets, model providers, feature flags, service addresses | `docker compose` (for `${...}` interpolation) and the orchestrator's `Settings` class in `shared/config.py` |
| `docker-compose.yml` | Service definitions, ports, volumes, and an `environment:` block per service | Docker Compose |
| `input/` | The active building: `building.yaml`, Turtle files, database registry, documents, floor plans, optional overlays | The orchestrator, GraphDB (read-only import) and the data publisher |
| `config/` | Building-independent operational config: alert thresholds, recipes, goals, access tiers, evidence policy | The orchestrator (mounted read-only) |

`shared/config.py` defines every typed setting (146 of them) with its default. A smaller set of
behaviour switches is read straight from the process environment by the module that uses it;
those are listed below with the module defaults.

## How a value is resolved

1. **The compose file's `environment:` block wins.** For the orchestrator, several values are
   set there explicitly and override `.env`. In the shipped bldg1 compose file these include
   `OLLAMA_NUM_PARALLEL=1`, `BUILDING_CONFIG_FILE`, `EXPORTS_DIR`, `SENSOR_MAP_PATH` and the
   service host names. Many others are written as `${NAME:-default}`, so `.env` supplies the value
   and the compose default applies only when `.env` leaves it out; `RESPONSE_CACHE_FUZZY`,
   `EMBEDDING_MODEL_LOCAL` and `SECRET_KEY` are among them.
2. **Then `.env`.** It is loaded into the container with `env_file`, and the orchestrator also
   reads the mounted `/app/.env` directly.
3. **Then the default in `shared/config.py`** (or in the reading module, for environment-only
   switches).

> **`SECRET_KEY`.** The compose files pass `SECRET_KEY` from `.env` to the orchestrator; if
> `ONTOSAGE_SECRET_KEY` is set it wins. With neither set, the placeholder is passed and
> `STRICT_SECRETS=true` refuses to start. Sessions are random tokens held in Redis, so nothing
> signs with this key today, but set a real value anyway.

**Applying a change.** `.env` is read when the container is created. After editing it, recreate
the orchestrator:

```bash
docker compose up -d orchestrator     # recreate: re-reads .env
```

`docker compose restart` keeps the old environment and is not enough. Orchestrator source code is
bind-mounted, so a code change needs only a restart; a dependency change or a different local
embedding model needs an image rebuild (`docker compose build orchestrator`).

The admin console's **Settings (.env)** tab edits the same file with secrets masked, and shows
the recreate command after a save. See [Admin console]({{ '/docs/admin-console/' | relative_url }}).

## Minimum settings before first boot

```bash
# Language model: choose one (see "Model provider" below)
MODEL_PROVIDER=local                 # local | openai | cloud | hosted
EMBEDDING_PROVIDER=local             # local | openai

# Secrets that STRICT_SECRETS refuses to boot on while they hold a default or CHANGE-ME value
STRICT_SECRETS=true
SECRET_KEY=<random string>
POSTGRES_USER_PASSWORD=<real password>
GRAPHDB_PASSWORD=<real password>
MYSQL_PASSWORD=<password of your host MySQL user>
PIPELINE_API_KEY=<random string>     # Open WebUI sends it to /v1/chat/completions

# First admin account, created at startup if it does not exist (12+ character password)
ADMIN_USERNAME=<admin user name>
ADMIN_PASSWORD=<12+ characters>

# Plain HTTP on localhost: the session cookie must not be marked Secure
COOKIE_SECURE=false
```

`STRICT_SECRETS` compares every setting whose name contains `PASSWORD`, `SECRET`, `API_KEY`,
`TOKEN` or `PRIVATE_KEY` with its shipped default, rejects values that start with `CHANGE-ME`,
`CHANGE_ME`, `CHANGEME`, `YOUR_` or `YOUR-`, and, where `.env.example` is readable, rejects
credential variables that still equal its value. An empty value is allowed: it means "this
integration is not configured". The error names every offending setting.

## Feature flags

Switches that turn a behaviour on or off. The defaults below are the **code defaults**. The
per-building templates (`.env1.example` and so on), the compose file and a deployment's own
`.env` may set them differently, and a running deployment often does (a bldg1 deployment, for
example, may run `ARBITER_V2_ROUTING=live` and `DATASOURCE_TOGGLES_ENABLED=true`). Check your
`.env`, or the console's Settings tab, for the values actually in force.

| Flag | Default | Effect |
|---|---|---|
| `COREFERENCE_REWRITE_ENABLED` | `true` | Rewrites a follow-up ("and humidity there?") into a standalone question before classification. |
| `MULTI_INTENT_ENABLED` | `true` | Splits a compound question into parts and answers each. Needs at least `MULTI_INTENT_MIN_LENGTH` characters (50). |
| `REFERENT_VALIDATION_ENABLED` | `true` | Checks that a named room, zone, floor or sensor exists in the graph before a data lane answers. Turning it off permits answers about places that do not exist. |
| `ANSWER_RELEVANCE_GATE` | `true` | One extra model call checks that an answer from the listed lanes responds to the question; a non-responsive answer is replaced by an honest decline. Fails open. |
| `SEMANTIC_CONCEPT_MATCH` | `true` | When no lay term matches, the model may pick one of the building's own concepts (or none). Fails open. |
| `ABSENCE_SECOND_CHANCE` (env) | `true` | An answer that says the building holds nothing gets one more look in the registers before it is published. |
| `REGISTER_PROJECTION_ANSWER` (env) | `true` | Simple who/when/which/how-many questions about a register are answered from its rows in code rather than narrated. |
| `DOCUMENT_RELEVANCE_GATE` (env) | `on` | Keeps an uploaded-document passage only when it is about the question. `off` restores score-only retrieval. |
| `CLAIM_BINDING_MODE` / `CLAIM_BINDING_ENABLED` (env) | `record` | Checks that each figure in an answer appears in that turn's evidence. `record` counts only; `enforce` (or `CLAIM_BINDING_ENABLED=true`) removes an unsupported sentence and says so; `off` disables it. |
| `ENTITY_ENRICHMENT_ENABLED` | `true` | At startup, gives an untyped time-series point a Brick class and label derived from its name (`config/entity_enrichment.yaml`). |
| `ARBITER_FACETS_ENABLED` | `true` | The ranking (deliberation) lane uses record fields, space properties, capacity and bookings as well as sensors. |
| `ARBITER_V2_ROUTING` | `shadow` | Routing rule that sends multi-criteria "choose a space" questions to the ranking lane. `off`, `shadow` (log only) or `live`. |
| `PROTECT_ENFORCE` | `shadow` | Access-policy decision point at every data fetch. `off`, `shadow` (log verdicts, enforce nothing) or `on`. The `.env.example` template sets `off`. See [Security & RBAC]({{ '/docs/security-rbac/' | relative_url }}). |
| `DATASOURCE_TOGGLES_ENABLED` | `false` | Loads `input/datasources.yaml`: switchable synthetic data sources, the `/api/v1/datasources` API, the Sources footer with provenance chips under answers, and the role-to-data-source access check. `.env1.example` sets `true`. The "How I know this" evidence panel does not depend on this flag. |
| `GOAL_PLANNER_ENABLED` | `false` | Intended to decompose an open goal ("make the building eco-friendly") into measurable sub-questions. `services/goal_planner.py` exists but nothing in the pipeline calls it, so the flag has no effect in the current code; the orchestrator logs a warning at start-up when it is set. |
| `RESPONSE_SYNTHESIS_ENABLED` | `false` | One extra grounded model pass rewrites the drafted answer into a single persona-aware reply. |
| `STRUCTURED_PLAN_ENABLED` | `false` | The model fills a JSON schema (provider-enforced) for intent classification and the ranking-lane compile, instead of free-text JSON. |
| `RESPONSE_CACHE_ENABLED` | `true` | Redis cache of answers (`resp_cache:*`, `RESPONSE_CACHE_TTL` seconds). |
| `RESPONSE_CACHE_FUZZY` (env) | `false` | Serves a near-identical question from the cache. Leave it off: questions that differ by one word read as near-identical text, and with it on "which rooms on floor 2 are *unoccupied*" would be served the answer to "… *occupied*" (similarity 0.90 against a 0.85 threshold). Room and floor numbers are guarded; words are not. |
| `CQIR_COMPILE_CACHE` (env) | `true` | Caches the ranking lane's compiled plan (24 h). |
| `AGENT_MEMORY_ENABLED` / `CROSS_SESSION_MEMORY_ENABLED` (env) | `true` / `true` | Per-user memory across turns and across conversations. |
| `I18N_ENABLED` (env) | `true` | Detects the language of incoming questions. |
| `DELIBERATE_CLARIFY_OFF` (env) | off | When set, the ranking lane never asks its clarifying question and proceeds on stated assumptions. For experiments only. |
| `LIVE_DATA_ENABLED`, `WEATHER_ENABLED`, `WEB_SEARCH_ENABLED` | `true` | Live weather (Open-Meteo) and web search for general-knowledge questions. |
| `GRAPHDB_USE_SIMILARITY` | `true` | Uses GraphDB's similarity index as a retrieval fallback when SPARQL returns nothing. |
| `TTL_VALIDATION_SHACL` | `false` | SHACL Brick conformance check of each Turtle file at startup (adds 5 to 30 s per file). |
| `WATCHDOG_ENABLED` (env) | `true` | A thread that logs container memory and event-loop lag every `WATCHDOG_INTERVAL_S` seconds. |
| `ENABLE_SIGNUP` | `false` | Allows `POST /auth/register`; new accounts get the `occupant` role. `.env.example` sets `true`. |
| `TRUST_FORWARDED_USER` | `false` | Uses the user identity header Open WebUI forwards on `/v1/*`, so that user's role applies. `.env.example` sets `true`. |
| `STRICT_SECRETS` | `true` | Refuses to start while any credential holds a default or placeholder. |
| `COOKIE_SECURE` | `true` | Marks the session cookie Secure. Must be `false` over plain HTTP. |
| `AUTO_BACKUP_ENABLED` | `true` | Encrypted backup after answers, only when `BACKUP_PASSPHRASE` is set. |

## Settings reference

"(env)" marks a switch read directly from the environment rather than through `Settings`.
Secret defaults are not reproduced here: each shipped default is refused by `STRICT_SECRETS`.

### Model provider

`MODEL_PROVIDER` and `EMBEDDING_PROVIDER` are chosen independently. Code reaches models only
through `llm_manager` and these settings.

| Setting | Default | Meaning |
|---|---|---|
| `MODEL_PROVIDER` | `hosted` | `local` (Ollama), `openai` (OpenAI API), `cloud` (Ollama Cloud) or `hosted` (an OpenAI-compatible GPU gateway). The shipped templates also select `hosted`, which needs a gateway you can reach; on your own machine choose `local`, `openai` or `cloud`. With `openai` and no `OPENAI_API_KEY`, the orchestrator falls back to `local`. |
| `OLLAMA_BASE_URL` | `http://localhost:11434` | Ollama endpoint. The compose file defaults it to `http://host.docker.internal:11434`, a native Ollama on the Docker host. |
| `OLLAMA_MODEL` | `gpt-oss:20b` | Local model. It must already be pulled (`ollama pull gpt-oss:20b`). About 16 GB of GPU memory keeps it fully on the GPU. |
| `OLLAMA_NUM_CTX` (env) | `8192` | Context window passed to Ollama. `.env.example` sets `16384`, which avoids empty completions on long prompts. |
| `OLLAMA_NUM_PREDICT` (env) | `8192` | Most tokens one local call may generate; `0` means unlimited. |
| `OLLAMA_KEEP_ALIVE` (env) | `30m` | How long Ollama keeps the model loaded. |
| `OLLAMA_CLOUD_BASE_URL` | `https://ollama.com/v1` | Ollama Cloud endpoint (`MODEL_PROVIDER=cloud`). |
| `OLLAMA_CLOUD_MODEL` | `gpt-oss:120b-cloud` | Ollama Cloud model. |
| `OLLAMA_CLOUD_API_KEY` | empty | Ollama Cloud key; required for `cloud`. |
| `LLM_REASONING_EFFORT` | empty | `low`, `medium` or `high` for models that accept it; empty uses the model default. |
| `OPENAI_API_KEY` | empty | Required for `openai` (language model, embeddings or speech). |
| `OPENAI_MODEL` | `o3-mini` | OpenAI model for longer tasks (analytics, reports). The compose file defaults it to `gpt-4o-mini` when `.env` is silent. |
| `OPENAI_MODEL_FAST` | `gpt-4o-mini` | OpenAI model for short, frequent calls (classification, rewriting). |
| `OPENAI_TEMPERATURE` | `0.1` | Sampling temperature. |
| `HOSTED_LLM_BASE_URL` | a private gateway | OpenAI-compatible endpoint for `hosted`. Set your own. |
| `HOSTED_LLM_API_KEY` | empty | Key for the hosted gateway; required for `hosted`. |
| `HOSTED_LLM_MODEL` | `gpt-oss:20b` | Model served by the gateway. |
| `HOSTED_LLM_TIMEOUT_S` | `660` | Deadline per hosted request, queue time included. |
| `HOSTED_LLM_MAX_CONCURRENCY` | `4` | Hosted requests kept in flight at once. |
| `HOSTED_PIPELINE_CONCURRENCY` | `4` | Chat turns run at once on the hosted gateway (a local model runs one at a time). |
| `HOSTED_LLM_MAX_TOKENS` | `4096` | Token budget floor per hosted call (reasoning plus visible text). |
| `HOSTED_PROBE_TTL_S`, `HOSTED_PROBE_TIMEOUT_S` (env) | `20`, `5` | Reachability probe for the gateway, so a dead link is refused quickly. |
| `HOSTED_BLIP_S` (env) | `60` | An outage younger than this is waited out once; an older one fails at once. |

### Model calls: timeouts and retries

| Setting | Default | Meaning |
|---|---|---|
| `LLM_TIMEOUT_S` (env) | `60` | Deadline for one model call. `.env.example` sets `180`. |
| `LLM_TRANSPORT_TIMEOUT_S` (env) | derived | HTTP client deadline; empty means `LLM_TIMEOUT_S × 1.5 + 15`. |
| `LLM_SLOW_CALL_WARN_S` (env) | `60` | Log a completed call at WARNING when it took this long. |
| `LLM_MAX_RETRIES`, `LLM_BACKOFF_BASE_S`, `LLM_BACKOFF_FACTOR` (env) | `3`, `1.0`, `2.0` | Retry policy for failed calls. |
| `LLM_RUNNER_RESTART_WAIT_S` (env) | `10.0` | Wait for a crashed local model runner to respawn before retrying. |
| `OPENAI_RETRY_DELAY_S`, `OPENAI_RATE_LIMIT_DELAY` (env) | `20.0`, `1.0` | Back-off after an OpenAI rate-limit response. |
| `WORKFLOW_TIMEOUT_S` | `0` | Deadline for a whole turn. `0` derives it from the model timeout (at least 120 s); an explicit value shorter than one model call produces a warning at boot. |
| `REQUEST_TIMEOUT_SECS` | `150` | Ceiling for a single pipeline execution before a timeout response. |

### Embeddings and retrieval

| Setting | Default | Meaning |
|---|---|---|
| `EMBEDDING_PROVIDER` | `local` | `local` (sentence-transformers) or `openai`. Falls back to `local` without an OpenAI key. |
| `EMBEDDING_MODEL_LOCAL` | `BAAI/bge-large-en-v1.5` | Local embedding model. It is downloaded into the image at build time and the container runs with the Hugging Face hub offline, so a different model needs an image rebuild. |
| `EMBEDDING_DIMENSION_LOCAL` | `1024` | Declared width of the local model. |
| `EMBEDDING_MODEL_OPENAI` | `text-embedding-3-small` | OpenAI embedding model. |
| `EMBEDDING_DIMENSION_OPENAI` | `1536` | Declared width of the OpenAI model. |
| `DOCUMENT_SCORE_FLOOR` | unset | Minimum cosine score for a document passage. Unset derives it from the loaded model (0.55 for bge-large). |
| `DOCUMENT_RELEVANCE_MARGIN` (env) | `0.10` | How far a passage must score above the runner-up under the document relevance gate. |
| `EMBEDDING_CACHE_TTL_SECONDS` | `86400` | Lifetime of cached embeddings (`cache:embed:*`). |
| `AGENT_MEMORY_EMBED_MODEL` (env) | `text-embedding-3-small` | Embedding model for per-user memory (the templates set `text-embedding-3-large`). |
| `GRAPHDB_SIMILARITY_INDEX` | `bldg_index` | Name of the GraphDB similarity index. |
| `ONTOLOGY_QUERY_MODE` | `semantic` | `semantic`, `sparql` or `hybrid`. |
| `USE_SEMANTIC_ONTOLOGY` | `true` | Enables retrieval-backed ontology querying. |
| `ONTOLOGY_DETECT_THRESHOLD` (env) | `0.75` | Confidence needed before a question is treated as being about the building's own model. |
| `TBOX_COLLECTION`, `ABOX_COLLECTION` | `brick_schema`, `building_instances` | Qdrant collection names. |

Once the local model is loaded, the vector width is taken from the model itself, not only from
`EMBEDDING_DIMENSION_LOCAL`. Changing the embedding model or provider invalidates the existing
vector collections, because vectors of different widths cannot be compared. Rebuild the indexes
afterwards (`POST /api/v1/admin/reindex`, or the console's Ontology tab).

### Active building

| Setting | Default | Meaning |
|---|---|---|
| `BUILDING_ID` | `bldg1` | Identifier of the active building. Per-building state lives in `volumes/<BUILDING_ID>/`; compose refuses to start when it is unset. Must equal `building_id` in `input/building.yaml`. |
| `BUILDING_NAME` | `Building` | Display name. |
| `BUILDING_NAMESPACE` | `http://example.org/building#` | Instance namespace. Must end with `#` or `/` and match `ontology_namespace` in `building.yaml` and the `@prefix bldg:` of every Turtle file; a mismatch stops the boot. |
| `BUILDING_PREFIX` | `bldg` | SPARQL prefix for the namespace. |
| `BUILDING_TIMEZONE` | `Europe/London` | IANA zone used to interpret "today", "yesterday" and named days. Stores hold UTC. |
| `COMPOSE_PROJECT_NAME` | (template) | Compose project, for example `ontosage_bldg1`; keeps containers and networks per building. |
| `BUILDING_CONFIG_FILE` | `config/building_config.yaml` | Legacy building YAML path; the compose file points it into `input/`. |
| `SENSOR_MAP_PATH` | `input/.sensor_map.cache.json` | Per-building sensor map cache, rebuilt from the live graph at boot when missing or stale. |
| `ALERT_THRESHOLDS_PATH` | `/app/config/alert_thresholds.yaml` | Threshold definitions for the alert monitor. |

### Service connections

| Setting | Default | Meaning |
|---|---|---|
| `GRAPHDB_URL` | `http://graphdb:7200` | GraphDB REST endpoint. |
| `GRAPHDB_HOST`, `GRAPHDB_PORT` | `graphdb`, `7200` | Host and port for direct connections and start-up checks. |
| `GRAPHDB_REPOSITORY` | `bldg` | Repository name. The same for every building: isolation comes from the namespace and `volumes/<BUILDING_ID>/`. |
| `GRAPHDB_USER`, `GRAPHDB_PASSWORD` | `admin`, (secret) | GraphDB credentials. |
| `QDRANT_URL` | `http://qdrant:6333` | Vector store. |
| `REDIS_URL`, `REDIS_HOST`, `REDIS_PORT` | `redis://redis:6379/0`, `redis`, `6379` | Conversation state, sessions, caches, job queue. |
| `RAG_SERVICE_URL`, `RAG_SERVICE_HOST`, `RAG_SERVICE_PORT` | `http://rag-service:8001`, `rag-service`, `8001` | Retrieval service used as the SPARQL fallback. |
| `CODE_EXECUTOR_URL`, `CODE_EXECUTOR_HOST`, `CODE_EXECUTOR_PORT` | `http://code-executor:8002`, `code-executor`, `8002` | Sandboxed Python for analytics. It sits on an internal network with no route out. |
| `CODE_EXECUTOR_TIMEOUT`, `CODE_EXECUTOR_MEMORY_LIMIT`, `CODE_EXECUTOR_CPU_LIMIT` | `30`, `1g`, `1.0` | Limits per execution. |
| `POSTGRES_USER_HOST`, `POSTGRES_USER_PORT`, `POSTGRES_USER_DB`, `POSTGRES_USER_USER`, `POSTGRES_USER_PASSWORD` | `postgres-user-data`, `5432`, `ontobot`, `ontobot`, (secret) | The Postgres that holds users, roles, conversations, turn memory, reports and the audit log. |
| `MYSQL_HOST`, `MYSQL_PORT`, `MYSQL_USER`, `MYSQL_PASSWORD`, `MYSQL_DATABASE` | `mysql`, `3306`, `root`, (secret), `sensordb` | Time-series MySQL. The bldg1 compose file points the orchestrator at `host.docker.internal:3306`, a MySQL on the Docker host. |
| `MYSQL_ROOT_PASSWORD` | (template) | Only for a containerised MySQL's own initialisation. |
| `OPENWEBUI_URL` | `http://open-webui:8080` | Where the orchestrator reaches Open WebUI's API for account sync. |
| `STATIC_BASE_URL` | `http://localhost:8000` | Base URL put in front of chart and export links. The compose file defaults it to `http://localhost:8080`, the artefact file server. Set it to a reachable address when users are not on the host. |
| `BMS_ENDPOINT` | empty | Building management system endpoint. Empty keeps actuation on the simulated driver; the real switch is the `actuation:` block in `building.yaml`. |

**Additional time-series backends.** Connections in `input/database_registry.yaml` take their
credentials from variables such as `PG_HOST`, `PG_PORT`, `PG_USER`, `PG_PASSWORD`, `PG_DATABASE`,
`TIMESCALE_*`, `MONGO_*`, `INFLUX_URL`, `INFLUX_TOKEN`, `INFLUX_ORG`, `INFLUX_BUCKET`,
`SQLITE_PATH`, `CASSANDRA_*` and `REDIS_TS_*`. Only connections listed under
`storage.databases` in `building.yaml` are initialised. See
[Data sources]({{ '/docs/data-sources/' | relative_url }}).

### Security and access

| Setting | Default | Meaning |
|---|---|---|
| `SECRET_KEY` | (secret) | Signing secret, checked by `STRICT_SECRETS`. Compose passes it from `.env` unless `ONTOSAGE_SECRET_KEY` is set (see above). |
| `STRICT_SECRETS` | `true` | Refuse to start on default or placeholder credentials. |
| `COOKIE_SECURE` | `true` | Secure flag on the session cookie. |
| `PIPELINE_API_KEY` | (secret) | Bearer key for `/v1/*`, the WebSocket proxy mode and `/api/v1/me/memory`. Comma-separate several keys to rotate. The shipped default is never accepted. |
| `ADMIN_USERNAME`, `ADMIN_PASSWORD` | empty | Bootstrap admin, created at startup when both are set and the account does not exist. Never overwrites an existing account. Password 12+ characters. |
| `ENABLE_SIGNUP` | `false` | Self-registration on `POST /auth/register`. |
| `TRUST_FORWARDED_USER` | `false` | Trust the forwarded identity header on `/v1/*`. |
| `FORWARDED_USER_HEADER` | `X-OpenWebUI-User-Email` | Header carrying that identity. |
| `OPENWEBUI_ADMIN_EMAIL`, `OPENWEBUI_ADMIN_PASSWORD` | empty | An existing Open WebUI admin account. When set, creating an OntoSage account also creates the matching Open WebUI account. |
| `LOGIN_MAX_ATTEMPTS`, `LOGIN_LOCKOUT_SECONDS` | `5`, `900` | Per-account lockout after failed logins. |
| `RATE_LIMIT_REQUESTS`, `RATE_LIMIT_WINDOW_S` (env) | `60`, `60` | Per-IP request limit. `/ping` and `/health` are exempt. |
| `TRUSTED_PROXY_CIDRS` | empty | Proxies allowed to set `X-Forwarded-For` for rate limiting. Empty trusts only the direct peer. |
| `CORS_ORIGINS` | `*` | Allowed origins. With `*`, credentialed cross-origin requests are disabled; list explicit origins to enable them. |
| `PROTECT_ENFORCE` | `shadow` | Access-policy enforcement stage (`off`, `shadow`, `on`). |

### Conversation and memory

| Setting | Default | Meaning |
|---|---|---|
| `CONVERSATION_TTL` | `0` | Expiry of the Redis working copy in seconds; `0` means none. The full history stays in Postgres. |
| `CONVERSATION_MAX_MESSAGES` | `400` | Messages kept in the Redis working copy. Trimming is not data loss. |
| `MAX_CONVERSATION_HISTORY` | `400` | Prior messages one turn may carry. |
| `AGENT_MEMORY_MAX`, `AGENT_MEMORY_TOP_K` (env) | `200`, `5` | Per-user memory size and recall depth. |
| `I18N_DETECT_CONFIDENCE`, `I18N_SKIP_SHORT` (env) | `0.85`, `10` | Language detection threshold, and the length below which it is skipped. |
| `DEEPL_API_KEY`, `GOOGLE_TRANSLATE_KEY` (env) | empty | Optional translation providers. Without them, replies are in English. |

### Answering pipeline

| Setting | Default | Meaning |
|---|---|---|
| `MULTI_INTENT_MIN_LENGTH` | `50` | Minimum question length before compound-question splitting is tried. |
| `PLANNER_MAX_STEPS` | `6` | Most steps in a multi-step plan. |
| `SEMANTIC_CONCEPT_TIMEOUT_S` | `8.0` | Time allowed for the semantic concept match. |
| `ANSWER_RELEVANCE_GATE_LANES` | data lanes | Comma list of lanes the relevance gate judges. Lanes that write state or files are never judged. |
| `ANSWER_RELEVANCE_TIMEOUT_S` | `8.0` | Time allowed for the relevance check; on expiry the answer stands. |
| `ONTOSAGE_PLUGINS` (env) | empty | Comma-separated plugin modules loaded at startup. |

### Caches

| Setting | Default | Meaning |
|---|---|---|
| `RESPONSE_CACHE_TTL` (env) | `3600` | Lifetime of a cached answer in seconds. |
| `RESPONSE_CACHE_MIN_SIMILARITY` (env) | `0.85` | Similarity needed for a fuzzy cache hit. |

Four Redis key families hold cached decisions: `resp_cache:*` (answers), `cache:sparql*` (query
rows), `cache:intent:*` (routing decisions) and `cqir_compile:*` (ranking-lane plans). After
changing data or code, flush all four before re-testing, or a stored answer from before the
change is returned:

```bash
docker exec redis-memory-store sh -c 'for p in "resp_cache:*" "cache:sparql*" "cache:intent:*" "cqir_compile:*"; do redis-cli --scan --pattern "$p" | xargs -r redis-cli DEL; done'
```

### General knowledge and live data

| Setting | Default | Meaning |
|---|---|---|
| `WEB_SEARCH_PROVIDER` | `duckduckgo` | `duckduckgo` (no key), `tavily` (needs `TAVILY_API_KEY`) or `none`. |
| `WEB_SEARCH_MAX_RESULTS` | `5` | Results passed to the summariser. |
| `WEB_SEARCH_TIMEOUT_S` | `8.0` | Timeout per live fetch. |
| `TAVILY_API_KEY` | empty | Tavily key. |

### Background jobs and monitoring

| Setting | Default | Meaning |
|---|---|---|
| `ALERT_POLL_INTERVAL_SECS` | `60` | How often the alert monitor polls readings for threshold breaches. |
| `ANOMALY_SCAN_INTERVAL_SECS` | `3600` | Background anomaly sweep; `0` disables it. |
| `READINESS_CHECK_INTERVAL_SECS` | `0` | Scheduled room-readiness checks before timetabled sessions; `0` disables the schedule (the check still works on request). |
| `READINESS_LEAD_MINUTES` | `30` | How far ahead of a session the scheduled check runs. |
| `WATCHDOG_INTERVAL_S` (env) | `30` | Watchdog log interval. |
| `WATCHDOG_MEM_WARN_GIB` (env) | `0` | Memory warning level; `0` means 60% of the container limit, or 6 GiB without one. |
| `WATCHDOG_LOOP_LAG_WARN_S` (env) | `30` | Event-loop lag that triggers a warning. |

### Backups

| Setting | Default | Meaning |
|---|---|---|
| `BACKUP_PASSPHRASE` | unset | Encrypts every backup archive (AES-256-GCM, 12+ characters). Unset disables automatic backups. Losing it makes existing archives unreadable. |
| `AUTO_BACKUP_DIR` | `/app/volumes/backups` | Container path, mounted from `volumes/<BUILDING_ID>/backups`. |
| `AUTO_BACKUP_MIN_INTERVAL_S` | `600` | At most one automatic backup per interval. |
| `AUTO_BACKUP_KEEP` | `96` | Number of archives kept. |

### Output directories and logging

| Setting | Default | Meaning |
|---|---|---|
| `EXPORTS_DIR` | `/app/outputs/exports` | Generated export files. |
| `QUERY_RESULTS_DIR` | `/app/outputs/query_results` | Saved SPARQL results. |
| `OUTPUT_DATA_DIR` | `outputs/data` | Analytics output files. |
| `DOCS_OUTPUT_DIR` (env) | `/app/outputs/documents` | Generated documents (reports). |
| `LOG_FORMAT` (env) | timestamp, trace id, logger, level, message | Python logging format. |

### Compose-level variables

These are read by `docker-compose.yml`, not by the orchestrator code.

| Variable | Default | Meaning |
|---|---|---|
| `ONTOSAGE_SECRET_KEY` | unset | If set, passed to the orchestrator as `SECRET_KEY` in place of `.env`'s `SECRET_KEY`. |
| `ORCHESTRATOR_MEM_LIMIT` | `8g` | Memory limit of the orchestrator container. |
| `GIT_SHA`, `BUILD_TIME` | `unknown` | Build arguments stamped into the image and reported by `/health`. |
| `MCP_USERNAME` + `MCP_PASSWORD`, or `MCP_PIPELINE_KEY`; `MCP_TRANSPORT`, `MCP_DEFAULT_PERSONA` | empty; `streamable-http`, `general` | The optional MCP server (`--profile mcp`), at `http://127.0.0.1:8003/mcp`. It signs in as an OntoSage account (use a non-admin role) or with the pipeline key; `MCP_AUTH_TOKEN` is the old name of `MCP_PIPELINE_KEY`. |

### Declared but not read by the current code

These remain in `Settings` or `.env.example` for compatibility and have no effect on the
orchestrator today: `LOG_LEVEL` (logging runs at INFO), `MAX_RETRY_ATTEMPTS`,
`REPORT_INTAKE_ENABLED`, `CAPABILITIES_TTL_FIRST`, `ADMIN_USERNAMES`, `RAG_SYSTEM`,
`FUSEKI_HOST`, `FUSEKI_PORT`, `FUSEKI_URL`, `BRICK_TBOX_FILE`, `BUILDING_ABOX_FILE`,
`ONTOLOGY_COLLECTION`, `STT_PROVIDER`, `WHISPER_MODEL_LOCAL` and `WHISPER_STT_URL` (the speech
service is commented out in the shipped compose file), and `.env.example` entries for services
that are commented out (`POSTGRES_*` for ThingsBoard, `PGADMIN_*`, `API_*`, `PG_THINGSBOARD_*`,
`ABACWS_DEBUG`), together with `QDRANT_*_COLLECTION`, `SIMILARITY_THRESHOLD`, `RAG_TOP_K`,
`MAX_UPLOAD_SIZE_MB`, `ALLOWED_AUDIO_FORMATS` and `CAPABILITY_SEMANTIC_ROUTING_ENABLED`.
`RBAC_ENABLED` only affects the start-up check of `SECRET_KEY`; permission checks always run.

## `input/`: the building's data and per-building config

The active building's files sit directly under `input/`. A fresh clone keeps each building
parked in its own folder (`bldg1/`, `bldg2/`, `bldg3/`); activating one renames it to `input/`
(see [Quick start]({{ '/docs/quickstart/' | relative_url }})).

| File | Role |
|---|---|
| `building.yaml` | Required. `building_id`, `building_name`, `ontology_namespace`, `ontology_prefix`, `timezone`, `storage.databases` (which registry connections are active), `provenance`, `actuation`. |
| `env.building` | The identity block to copy into `.env` for this building. |
| `<id>_*.ttl` | The building model: Brick classes, spaces, points and their time-series links. Uploaded to GraphDB at startup into named graphs; files are skipped when their hash is unchanged. |
| `<id>_capabilities.ttl` | Amenities and knowledge topics. |
| `database_registry.yaml` | Maps each `ref:storedAt` key to a database connection and adapter. |
| `datasources.yaml` | Switchable synthetic data sources (used when `DATASOURCE_TOGGLES_ENABLED=true`). |
| `role_datasource_access.yaml` | Which data sources each role may use. See [Security & RBAC]({{ '/docs/security-rbac/' | relative_url }}). |
| `documents/` | Policies, manuals and contact sheets as `.md`, `.txt` or `.pdf`. A PDF is read through its text layer; a scanned PDF without one is reported as not indexed. |
| `*.pdf`, `*.dwg` | Floor plans, one per floor. |
| `concepts.ttl`, `feeds.yaml`, `rules.yaml`, `channels.yaml`, `intents.yaml`, `recipes.yaml`, `benchmarks.csv`, `personas/` | Optional overlays: lay terms, live feeds, alert rules, notification channels, extra intents, recipes, benchmarks, personas. Absent means the feature is skipped. `benchmarks.csv` is validated but nothing reads it yet, and start-up says so. |

The Turtle validator runs at startup. A `building.yaml` whose namespace disagrees with a Turtle
file's `@prefix bldg:`, or whose `building_id` differs from `BUILDING_ID`, stops the boot. Check
new Turtle offline before a restart; see [Write TTL for your building]({{ '/docs/write-ttl/' | relative_url }})
and [Onboard a building]({{ '/docs/onboarding-building/' | relative_url }}).

Live feeds and notification channels appear on the console's **Integrations** tab, where a
channel can be test-sent:

![Admin console Integrations tab]({{ '/admin-portal-screenshots/06-integrations.png' | relative_url }})
*Weather feeds polling Open-Meteo into a registered database, and a `log` notification channel
with Test-send.*

## Ports

Every published port is bound to `127.0.0.1`. Nothing is reachable from another machine unless
you add a reverse proxy or tunnel.

| Service | Host port | Role |
|---|---|---|
| Open WebUI | 3000 | Chat interface |
| Admin console (`config-panel`) | 3001 | Administration GUI |
| Orchestrator API | 8000 | `/chat`, `/v1/*`, `/auth/*`, `/api/v1/*`, `/health` |
| rag-service | 8001 | Retrieval fallback |
| code-executor | 8002 | Sandboxed analytics |
| GraphDB | 7200 (7300 gRPC) | Graph store and workbench |
| Qdrant | 6333 (6334 gRPC) | Vector store |
| Redis | 6379 | State, sessions, caches |
| PostgreSQL (users and memory) | 5433 | Users, roles, conversations, reports, audit |
| MongoDB | 27017 | Chat transcripts |
| File server | 8080 | Charts, exports and floor-plan renders |
| Adminer | 8093 | Database browser |
| Prometheus, Grafana | 9090, 3002 | `--profile monitoring` only |
| MCP server | 8003 | `--profile mcp` only |
| Demo MySQL | 3399 | `--profile demo` only |
| MySQL (time series) | 3306 | **On the Docker host**, not a container |

## Build provenance

The image records the commit it was built from:

```bash
GIT_SHA=$(git rev-parse --short HEAD) BUILD_TIME=$(date -u +%FT%TZ) docker compose build orchestrator
docker compose up -d orchestrator
```

`GET /health` then reports `build.sha` and `build.time`, plus `code_sha` and `mounted_sha` (the
commit of the bind-mounted source). A difference between the two means the running image and
the checkout disagree.

## See also

- [Quick start]({{ '/docs/quickstart/' | relative_url }}): the minimum steps from a fresh clone.
- [Security & RBAC]({{ '/docs/security-rbac/' | relative_url }}): what the secrets and access settings protect.
- [Data sources]({{ '/docs/data-sources/' | relative_url }}): the database registry and adapters.
- [Admin console]({{ '/docs/admin-console/' | relative_url }}): the Settings, AI & Models and Integrations tabs.
