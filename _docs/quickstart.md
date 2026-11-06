---
title: Quick Start
layout: post
category: docs
permalink: /docs/quickstart/
date: 2026-07-02
---

# Quick start

This page takes a fresh clone to a first answer using the bundled test building `bldg1`. Running
your own building follows the same steps; see
[Use your own building]({{ '/docs/your-own-building/' | relative_url }}).

## 0. Prerequisites

| What | Why | Check |
|---|---|---|
| Docker Engine or Docker Desktop with Compose v2 | Every service except MySQL runs in Compose | `docker compose version` |
| **MySQL 8 on the host**, port 3306 | Time-series readings. The MySQL service in the shipped compose file is commented out; the orchestrator reaches the host through `host.docker.internal:3306` | `mysql -h 127.0.0.1 -P 3306 -e "SHOW DATABASES"` |
| A language model | Reads the question and writes the reply. One of: Ollama on the host with `gpt-oss:20b` pulled (about 16 GB of GPU memory keeps it fully on the GPU), an OpenAI API key, or an Ollama Cloud key | `curl -s http://127.0.0.1:11434/api/tags` for Ollama |
| Memory | GraphDB is given up to 8 GB of heap and the orchestrator container a limit of 8 GB (`ORCHESTRATOR_MEM_LIMIT`) | |

## 1. Activate a building

OntoSage serves one building at a time. The active building is whichever folder is named
`input/`, with `.env` and `docker-compose.yml` beside it. A fresh clone has every building
parked, so these do not exist yet. Activating is renaming:

```bash
git clone https://github.com/suhasdevmane/OntoSage.git
cd OntoSage

mv bldg1 input                                  # the building's data
mv docker-compose.bldg1.yml docker-compose.yml  # its services
cp .env1.example .env                           # its settings, with bldg1's identity filled in
```

On Windows PowerShell:

```powershell
Move-Item bldg1 input
Move-Item docker-compose.bldg1.yml docker-compose.yml
Copy-Item .env1.example .env
```

`.env2.example` and `.env3.example` do the same for `bldg2` and `bldg3`. Your `.env` is ignored
by git; only the templates are in the repository.

## 2. Fill in `.env`

The template ships with placeholders, and `STRICT_SECRETS=true` refuses to start while any of
them remain. Set at least:

```bash
# Choose the language model. The template says "hosted", a private GPU gateway;
# use one of these instead:
MODEL_PROVIDER=local                  # Ollama on this machine (OLLAMA_MODEL=gpt-oss:20b)
# MODEL_PROVIDER=openai               # with OPENAI_API_KEY=<key>
# MODEL_PROVIDER=cloud                # with OLLAMA_CLOUD_API_KEY=<key>
EMBEDDING_PROVIDER=local              # bge-large-en-v1.5, built into the image

# Secrets (replace every CHANGE-ME value)
SECRET_KEY=<random string>
POSTGRES_USER_PASSWORD=<password>
GRAPHDB_PASSWORD=<password>
PIPELINE_API_KEY=<random string>      # Open WebUI uses it to reach OntoSage

# Your host MySQL account (see step 3)
MYSQL_USER=ontosage
MYSQL_PASSWORD=<password>
MYSQL_DATABASE=sensordb

# First admin account, created at startup if it does not exist
ADMIN_USERNAME=<admin user name>
ADMIN_PASSWORD=<12 or more characters>
```

`COOKIE_SECURE=false` is already set in the template, which is right for plain HTTP on
localhost. Generate random strings with, for example,
`python -c "import secrets; print(secrets.token_urlsafe(32))"`. Every setting is described on
[Configuration]({{ '/docs/configuration/' | relative_url }}).

## 3. Prepare MySQL

Create the database and a user the containers can reach. The user needs to create tables and
insert rows, because synthetic data sources write their own tables:

```sql
CREATE DATABASE sensordb;
CREATE USER 'ontosage'@'%' IDENTIFIED BY '<password>';
GRANT ALL PRIVILEGES ON sensordb.* TO 'ontosage'@'%';
```

MySQL must accept connections from Docker (on Linux, check `bind-address`). Then create the
narrow time-series tables, one per measured quantity:

```bash
mysql -u root -p sensordb < data/mysql-init/create_all_narrow_timeseries_tables.sql
```

bldg1's recorded readings are not part of the repository. With empty tables, structural questions
answer from the graph and reading questions report that no readings were found. Step 6 shows how
to generate synthetic readings.

## 4. Start the stack

```bash
docker compose up -d
docker compose logs -f orchestrator
```

The first boot builds the orchestrator image (it includes the embedding model, about 1.3 GB),
warms GraphDB and loads the building's Turtle files; allow several minutes. Ontology
initialisation retries by itself. Then:

```bash
curl -s http://127.0.0.1:8000/health | python -m json.tool
```

`data.status` should read `healthy`, and `data.building_id` should be `bldg1`. If the
orchestrator exits at once, its log names the cause: usually a remaining placeholder secret or a
building identity that disagrees between `.env`, `input/building.yaml` and the Turtle prefixes.

## 5. Ask in the chat interface

Open **Open WebUI** at `http://127.0.0.1:3000`. The first account created there becomes the
Open WebUI administrator. The model `ontobot-pipeline` is preselected.

Who you are to OntoSage depends on `TRUST_FORWARDED_USER`. With it on, Open WebUI forwards your
email and OntoSage uses the role of the matching OntoSage account; an email it has not seen gets
a new `readonly` account, which an admin can promote. With it off, everyone chats as one shared
`readonly` identity. See [Security & RBAC]({{ '/docs/security-rbac/' | relative_url }}).

Questions to start with, all from the repository's own question banks:

| Ask | What it exercises |
|---|---|
| *What can you do?* | OntoSage describes itself from the active building's configuration |
| *How many sensors does the building have?* | Structural answer from the graph alone |
| *What is the current temperature in zone 5.28?* | Graph plus a time-series read |
| *Show me floor 3 plan.* | Floor plan |
| *Where is the prayer room?* | Amenity triples |
| *Compare air quality between floor 1 and floor 5.* | Two-sided comparison over readings |
| *Show me the swimming pool temperature* | A referent the building does not have: the answer says so instead of using another sensor |

![A live reading in the chat interface]({{ '/assets/images/screenshots/chat-live-reading.png' | relative_url }})
*A reading answered in Open WebUI.*

When a turn has an evidence record, the answer ends with a collapsible "How I know this" panel
naming the sources behind it:

![The evidence panel under an answer]({{ '/assets/images/screenshots/chat-evidence-panel.png' | relative_url }})
*The evidence panel lists where each figure came from.*

![An honest decline]({{ '/assets/images/screenshots/chat-decline.png' | relative_url }})
*A question the building's data cannot answer is declined, not guessed.*

What happens behind each answer is described in
[How OntoSage answers]({{ '/docs/how-it-answers/' | relative_url }}) and
[Checks and honest answers]({{ '/docs/checks-and-honesty/' | relative_url }}).

## 6. Open the admin console

Open `http://127.0.0.1:3001` and sign in with `ADMIN_USERNAME` and `ADMIN_PASSWORD`.

- **Health** shows every dependency.
- **Data Sources** (when `DATASOURCE_TOGGLES_ENABLED=true`, as in the bldg1 template) lists
  synthetic sources. **Regenerate** writes synthetic readings into a source's table and the
  switch turns its questions on.
- **Ask (test)** runs a question and shows the routed intent, with provenance chips when the
  data-source feature is on.

The `data-publisher` service also appends generated readings every 30 seconds to bldg1's
tables, so questions about "now" have recent rows during development. See
[Admin console]({{ '/docs/admin-console/' | relative_url }}).

## 7. Use the API directly

```bash
TOKEN=$(curl -s -X POST http://127.0.0.1:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"<admin user name>","password":"<password>"}' \
  | python -c "import sys,json; print(json.load(sys.stdin)['data']['session_token'])")

curl -s -X POST http://127.0.0.1:8000/chat \
  -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
  -d '{"message":"How many sensors does the building have?","session_id":"demo"}'
```

The OpenAI-compatible endpoint that Open WebUI uses takes the pipeline key instead:

```bash
curl -s http://127.0.0.1:8000/v1/chat/completions \
  -H "Authorization: Bearer $PIPELINE_API_KEY" -H "Content-Type: application/json" \
  -d '{"model":"ontobot-pipeline","messages":[{"role":"user","content":"What can you do?"}]}'
```

All routes are listed in the [API reference]({{ '/docs/api-reference/' | relative_url }}).

## Interfaces

| Interface | Address | Notes |
|---|---|---|
| Chat (Open WebUI) | `http://127.0.0.1:3000` | Multi-turn conversation |
| Admin console | `http://127.0.0.1:3001` | Configuration, data sources, ontology, users |
| API and OpenAPI page | `http://127.0.0.1:8000/docs` | |
| GraphDB workbench | `http://127.0.0.1:7200` | SPARQL against the building graph |
| Qdrant dashboard | `http://127.0.0.1:6333/dashboard` | Vector collections |
| Adminer | `http://127.0.0.1:8093` | Browse MySQL and PostgreSQL |

Every port is bound to `127.0.0.1`. To let other people use the chat interface, put a reverse
proxy with TLS in front of port 3000 and read the checklist on
[Security & RBAC]({{ '/docs/security-rbac/' | relative_url }}). Chart and export links point at
`STATIC_BASE_URL` (by default the file server on port 8080), so set it to an address remote users
can reach.

## After a change

- Edited `.env`: `docker compose up -d orchestrator` (recreate; `restart` keeps the old
  environment).
- Changed data or Turtle and want to re-test: flush the four Redis caches listed on
  [Configuration]({{ '/docs/configuration/' | relative_url }}#caches), or a stored answer from
  before the change comes back.
- Stamp the build so `/health` shows which commit is running:
  `GIT_SHA=$(git rev-parse --short HEAD) BUILD_TIME=$(date -u +%FT%TZ) docker compose build orchestrator`.

## Switch to another building

Stop the stack first (renaming folders while containers run breaks the mounts), then park the
active building under its own id and activate another:

```bash
docker compose down
mv input bldg1 && mv .env .env1 && mv docker-compose.yml docker-compose.bldg1.yml
mv bldg2 input && mv docker-compose.bldg2.yml docker-compose.yml && cp .env2.example .env
# fill in .env, then
docker compose up -d
```

`BUILDING_ID` in `.env`, `building_id` in `input/building.yaml` and `input/env.building` must
agree. Each building keeps its own state in `volumes/<BUILDING_ID>/`. `bldg2` also reads from
TimescaleDB and Cassandra, which run from an optional overlay:
`docker compose -f docker-compose.yml -f docker-compose.timeseries-backends.yml up -d`, seeded
with `python scripts/seed_timeseries_backends.py`. See
[Data sources]({{ '/docs/data-sources/' | relative_url }}).

## Next

- [Use your own building]({{ '/docs/your-own-building/' | relative_url }})
- [Onboard a building]({{ '/docs/onboarding-building/' | relative_url }}) from the admin console
- [Stakeholder guide]({{ '/docs/stakeholder-guide/' | relative_url }}): what people can ask
