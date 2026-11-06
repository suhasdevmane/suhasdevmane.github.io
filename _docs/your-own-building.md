---
title: Use Your Own Building
layout: post
category: docs
permalink: /docs/your-own-building/
date: 2026-07-11
---

# Use OntoSage with your own building

This page takes you from a fresh clone to your own building answering questions. It is for
someone with a building model (or the knowledge to write one) and a database of readings. It
covers choosing an identity, creating the building's files, connecting its data, starting it, and
checking both halves of the answer path.

OntoSage ships with three buildings: `bldg1` (Cardiff University's Abacws), `bldg2` and `bldg3`.
They are test fixtures. They let a fresh clone show a working system and let portability be
tested on more than one model. Nothing in the core code knows them. Your building uses the same
slots, and onboarding it means adding data and configuration, never code. If you find yourself
editing Python to make your building work, report it as a defect.

---

## The two halves

A question about a reading is answerable when both halves exist:

```
(a) the thing is a triple in the graph          "there IS a CO2 sensor in Room 1.01"
        AND
(b) its readings are rows in a registered store  linked by ref:hasTimeseriesId + ref:storedAt
```

A database full of readings with no graph is invisible: OntoSage cannot know what the series
measure. A graph with no readings answers structural questions (*"how many CO2 sensors are
there?"*) but not *"what is it now?"*. When a half is missing, OntoSage says so instead of
offering a number from somewhere else.

---

## Step 1: choose an identity

Pick three values and keep them identical everywhere they appear:

| Value | Example | Used for |
|---|---|---|
| Building id | `riverside` | `BUILDING_ID`, the folder name when parked, `volumes/riverside/` |
| Namespace | `http://riverside.example/building#` | Every instance IRI; must match `@prefix bldg:` in every TTL file |
| Project name | `ontosage_riverside` | `COMPOSE_PROJECT_NAME`: containers and images |

**Use a new id.** All per-building state (GraphDB, Qdrant, Redis, Postgres, Mongo, uploaded
files' records) lives in `volumes/<BUILDING_ID>/`. A new id starts from empty stores. Reusing
`bldg1` would load your triples into Abacws's graph, and counts and *"what is in this
building"* answers would mix two buildings. If you must reuse an id, stop the stack and delete
`volumes/<id>/` first.

**Use a namespace you control**, ending in `#` or `/`. The readiness check treats one that starts
with `http://example.org/` as unset.

---

## Step 2: create your building's set

In a fresh clone no building is active: the repository holds `bldg1/`, `bldg2/` and `bldg3/`, a
`docker-compose.bldg<N>.yml` for each, and `.env<N>.example` templates. Create a fourth set beside
them, so the fixtures stay intact:

```bash
mkdir -p riverside/documents
cp bldg1/Brick_v1.4.ttl "bldg1/Brick+extensions.ttl" riverside/
cp docker-compose.bldg1.yml docker-compose.riverside.yml
cp .env1.example .env.riverside
```

If `bldg1` is the active building at the time, copy from `input/` and `docker-compose.yml`
instead. On Windows PowerShell use `New-Item -ItemType Directory` and `Copy-Item`.

### `riverside/building.yaml`

```yaml
building_id: riverside
building_name: Riverside House
ontology_namespace: "http://riverside.example/building#"
ontology_prefix: bldg
timezone: "Europe/London"

storage:
  databases:
    - riverside_iaq
```

`storage.databases` lists the database keys whose adapters are built (Step 4). The demonstration
buildings' `building.yaml` files show the other optional blocks (actuation, floor-plan aliases,
evidence policy).

### `.env.riverside`

Set the identity, the time-series database and every secret. The template marks each credential
`CHANGE-ME`, and with `STRICT_SECRETS=true` the orchestrator refuses to start while any credential
is still a placeholder or a shipped default.

```bash
BUILDING_ID=riverside
BUILDING_NAME=Riverside House
BUILDING_NAMESPACE=http://riverside.example/building#
BUILDING_PREFIX=bldg
BUILDING_TIMEZONE=Europe/London
MYSQL_DATABASE=riverside_sensordb
COMPOSE_PROJECT_NAME=ontosage_riverside
```

Set `SECRET_KEY` to a random value. The compose file passes it to the orchestrator, unless
`ONTOSAGE_SECRET_KEY` is also set, which then takes its place.

The model provider (`MODEL_PROVIDER`, `OLLAMA_MODEL` and related keys) and the admin account
(`ADMIN_USERNAME`, `ADMIN_PASSWORD`) are covered in
[Configuration]({{ '/docs/configuration/' | relative_url }}). Every `.env*` file is ignored by
git; keep it that way.

### `riverside/env.building`

Copy the same seven identity lines into `riverside/env.building`. It travels with the folder, so a
parked building still says which building it is.

---

## Step 3: write the graph

Write your building as TTL files in `riverside/`: the building, floors and rooms, points with
their units, one timeseries reference per point, equipment, and optionally capabilities, records
and lay terms. [Write TTL for Your Building]({{ '/docs/write-ttl/' | relative_url }}) is the
tutorial, with a snippet and a check for each step.

OntoSage reads the classes you already use. A model written in Brick needs the least work; the
TTL rules that matter are the ones in that tutorial (the `bldg:` prefix, labels people can name,
IRIs for relations, and one complete reference per point).

Before you go further, run the offline check against the folder, from the repository root with
the orchestrator's Python requirements installed (`pip install -r orchestrator/requirements.txt`):

```bash
STRICT_SECRETS=false python scripts/swap_building.py --to riverside --dry-run --input-root .
```

It must report the TTL files as validated, with no `[FAIL]` line. `STRICT_SECRETS=false` lets the
script load OntoSage's settings before `.env` holds real secrets; it affects this command only.
In PowerShell, run `$env:STRICT_SECRETS = "false"` first.

---

## Step 4: connect the readings

Add a `riverside/database_registry.yaml` with one entry per store, keyed by the name your TTL's
`ref:storedAt` uses:

```yaml
databases:
  riverside_iaq:                    # matches ref:storedAt bldg:riverside_iaq
    type: mysql_narrow              # rows of (uuid, datetime, value)
    table: iaq_readings
    host: "${MYSQL_HOST:-mysql}"
    port: "${MYSQL_PORT:-3306}"
    user: "${MYSQL_USER}"
    password: "${MYSQL_PASSWORD}"
    database: "${MYSQL_DATABASE}"
    nature: real                    # real | synthetic, shown as provenance
    note: "Riverside BMS historian"
```

- **Narrow tables** (`type: mysql_narrow` with `table:`) hold rows of `uuid`, `datetime`,
  `value`. Several can coexist, one per modality. This shape scales.
- **Wide tables** (`type: mysql`) hold one column per series identifier. MySQL limits a row to
  about 1,017 columns, so large estates outgrow them.
- PostgreSQL, TimescaleDB and Cassandra are supported, and a building can use several stores at
  once: each point's `ref:storedAt` key chooses its store.
  [Data Sources]({{ '/docs/data-sources/' | relative_url }}) lists the adapters.

Store times in UTC. The database must be reachable from the orchestrator container: the
demonstration compose file points `MYSQL_HOST` at `host.docker.internal`, which is the Docker
host.

You can also register connections and sensors later from the admin console's Databases tab,
without editing these files; see
[Onboard a Building]({{ '/docs/onboarding-building/#onboard-through-the-admin-console' | relative_url }}).

**Remove the demonstration publisher for a real building.** The compose file you copied contains
a `data-publisher` service that writes generated readings so the fixtures have recent data.
Delete that service from `docker-compose.riverside.yml` so nothing synthetic is ever written into
your store.

---

## Step 5: activate and start

Activation is the rename described in
[Onboard a Building]({{ '/docs/onboarding-building/#activate-park-and-swap-buildings' | relative_url }}).
If another building is active, stop it and park it first. Then:

```bash
mv riverside input
mv .env.riverside .env
mv docker-compose.riverside.yml docker-compose.yml

docker compose up -d
curl -s http://127.0.0.1:8000/health      # repeat until it returns 200
```

The first start builds the images, creates the GraphDB repository and loads every TTL file; a
large model can take several minutes. If the orchestrator keeps restarting, a TTL file failed the
start-up check and the log names it:

```bash
docker compose logs --tail=50 orchestrator | grep ttl_validator
```

To switch back to a demonstration building later, park your set as `riverside/`,
`.env.riverside` and `docker-compose.riverside.yml` and activate the other.

---

## Step 6: verify both halves

Open the admin console at `http://127.0.0.1:3001`, sign in as the admin, and use **Ask (test)**,
or ask in the chat interface:

```
Half (a), the graph:       "How many temperature sensors are in this building?"
Half (b), the readings:    "What is the temperature in Room 1.01 right now?"
```

Then compare declared and populated sensors. The Ontology tab's **Sensor data coverage** line
states how many datasource-linked sensors have readings and how many reported in the last 24
hours; each connection's **Verify** button on the Databases tab gives the same figures per store.
A sensor that is in the graph and never has readings has a wrong `ref:hasTimeseriesId`, a wrong
`ref:storedAt` key, or no rows. The SPARQL checks in
[Write TTL]({{ '/docs/write-ttl/#check-your-graph-with-sparql' | relative_url }}) find which.

---

## Pitfalls

| Symptom | Cause | Fix |
|---|---|---|
| The orchestrator keeps restarting; the log mentions `@prefix bldg:` | A TTL file without the prefix, or with a namespace that differs from `building.yaml` (often a trailing `#`) | Make them identical; run the dry-run check; start again |
| The orchestrator refuses to start and lists secrets | `STRICT_SECRETS=true` and a credential is still `CHANGE-ME` or a default | Set real values in `.env` |
| Structural questions work; readings never do | Missing `ref:storedAt`, a key not in `database_registry.yaml` or not in `storage.databases`, a wrong identifier, or no rows | Run the SPARQL checks; check the key in both YAML files |
| Answers mention a building you never loaded | A reused `BUILDING_ID` whose `volumes/<id>/` still holds the old graph | Use a new id, or stop the stack and delete that folder |
| A room exists but questions about it are declined | Its label and IRI lack the number or words people use | See [names the referent check can find]({{ '/docs/write-ttl/#names-the-referent-check-can-find' | relative_url }}) |
| Rows added to a wide table are not found for a few minutes | The wide-table adapter caches the table's columns for 5 minutes | Load data before start-up, or restart the orchestrator |
| A wide table refuses more sensors | MySQL's limit of about 1,017 columns per row | Move those series to a narrow `(uuid, datetime, value)` table |
| `.env` changes have no effect | `docker compose restart` keeps the environment the container was created with | Use `docker compose up -d` |
| A fix in the source does not appear | The service's image predates it | `docker compose build <service>` then `docker compose up -d` |

---

## Prefer clicking to editing?

Identity, TTL upload, database connections, sensor registration, capabilities, documents and
floor plans can all be set from the admin console at `http://127.0.0.1:3001`, with every change
saved to the active building's `input/` folder. The console still needs an active building to
attach to, so Steps 1, 2 and 5 come first: an identity, a set of files, and a running stack. See
[Onboard a Building]({{ '/docs/onboarding-building/' | relative_url }}) and
[Admin Console]({{ '/docs/admin-console/' | relative_url }}).

## See also

- [Quick Start]({{ '/docs/quickstart/' | relative_url }}): run a demonstration building first.
- [Write TTL for Your Building]({{ '/docs/write-ttl/' | relative_url }}): the graph, step by step.
- [Edit TTL in a Running System]({{ '/docs/edit-ttl/' | relative_url }}): changing it later.
- [Onboard a Building]({{ '/docs/onboarding-building/' | relative_url }}): swapping, console onboarding, readiness.
- [Configuration]({{ '/docs/configuration/' | relative_url }}): every environment variable.
- [OCBV Schema]({{ '/docs/ocbv-schema/' | relative_url }}): the capability vocabulary.
