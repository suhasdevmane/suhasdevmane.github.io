---
title: Use Your Own Building
layout: post
category: docs
permalink: /docs/your-own-building/
date: 2026-08-04
---

# Use OntoSage with your own building

OntoSage ships with three buildings — `bldg1` (Cardiff University's Abacws), `bldg2` and `bldg3`.
**They are test fixtures.** They exist so that a fresh clone demonstrates a working system within
minutes, and so portability is provable on more than one model rather than merely claimed. Nothing
in the core code knows they exist.

Your building uses **exactly the same slots**. Onboarding it means replacing data and configuration —
never code. If you find yourself editing Python to make your building work, that is a bug worth
reporting, not a step.

---

## What a building actually is

A building in OntoSage is a trio of files, and "being active" is simply having the canonical names:

```
 <data folder>     <env file>    <compose file>
  input/             .env         docker-compose.yml     ← the ACTIVE building
  bldg2/             .env2        docker-compose.bldg2.yml   (parked)
  bldg3/             .env3        docker-compose.bldg3.yml   (parked)
```

Only one building is active at a time. Everything the system knows about it comes from those three
places plus the databases you register.

---

## The two halves — the rule that explains every "no data" answer

A question is answerable when **both halves** exist:

```
(a) the thing is a triple in the ontology        →  "there IS a CO₂ sensor in room 3.04"
        AND
(b) its readings are rows in a registered DB     →  linked by ref:hasTimeseriesId + ref:storedAt
```

A database full of readings with no ontology is invisible — OntoSage cannot know what those columns
mean. An ontology with no readings can answer *structural* questions ("how many CO₂ sensors are
there?") but not *live* ones ("what is it now?"). When a half is missing OntoSage says so plainly
rather than inventing a number, and tells you which half to add.

---

## Step 1 — Activate a slot and claim it as yours

```bash
git clone https://github.com/suhasdevmane/OntoSage.git
cd OntoSage

# activate a slot (bldg1 is the conventional choice)
mv bldg1 input                                  # the building-data folder
mv docker-compose.bldg1.yml docker-compose.yml  # its services
cp .env1.example .env                           # its settings — then edit for YOUR building
```

Env files hold secrets, so the real ones are **never committed**: the repo ships only
`.env1.example` / `.env2.example` / `.env3.example`, each pre-filled with that building's identity
and with every credential replaced by a `CHANGE-ME` placeholder. Copy one, then replace the
placeholders — `STRICT_SECRETS=true` refuses to boot while any remain.

> **Windows PowerShell**
> `Move-Item bldg1 input; Move-Item docker-compose.bldg1.yml docker-compose.yml; Copy-Item .env1.example .env`

### Choose a NEW `BUILDING_ID`

This is the one decision that causes real confusion if you get it wrong. Per-building state — GraphDB,
Qdrant, Redis, Postgres, Mongo — lives in `volumes/<BUILDING_ID>/`.

* **A new id** gives you brand-new, empty stores: a genuinely clean start. **Do this.**
* **Reusing `bldg1`** inherits Abacws's populated graph. Your triples are *added alongside* it, so
  counts and "what exists in this building" answers silently mix two buildings.

If you must reuse an id, wipe its state first:

```bash
docker compose down
rm -rf volumes/bldg1
```

### Set the identity in `.env`

```bash
BUILDING_ID=riverside_hq                            # drives volumes/<id>/ and log lines
BUILDING_NAME=Riverside HQ                          # appears in answers
BUILDING_NAMESPACE=http://example.org/riverside#    # MUST equal @prefix bldg: in your TTL
BUILDING_PREFIX=bldg
BUILDING_TIMEZONE=Europe/London                     # interprets "today" / "yesterday"
MYSQL_DATABASE=riverside_sensordb                   # your time-series database
COMPOSE_PROJECT_NAME=ontosage_riverside             # namespaces containers and networks
```

Mirror the same values into `input/env.building` — that file travels with the folder, so the identity
is never lost when the building is parked.

Set real secrets too. `STRICT_SECRETS=true` refuses to boot while any password is still a shipped
default: `SECRET_KEY`, `GRAPHDB_PASSWORD`, `MYSQL_PASSWORD`, `POSTGRES_USER_PASSWORD`,
`PIPELINE_API_KEY`, plus `OPENAI_API_KEY` (or `MODEL_PROVIDER=local` with `OLLAMA_MODEL` to stay
fully offline).

---

## Step 2 — Put your building's data in `input/`

Remove the fixture's building files and add yours. **Three files are shared schema, not building
data — keep them:**

| Keep (OntoSage's vocabulary) | Replace (your building) |
|---|---|
| `Brick_v1.4.ttl` | `<your_id>.ttl` — your Brick/BACnet model |
| `Brick+extensions.ttl` | `building.yaml` — id, name, `ontology_namespace` |
| `ontosage_schema.ttl` (OCBV) | `env.building` — identity mirror |
| | `database_registry.yaml` — your database connections |
| | `<your_id>_capabilities.ttl` — amenities / topics *(optional)* |
| | `<label> floor <N>.pdf` / `.dwg` — floor plans *(optional)* |
| | `documents/` — manuals, policies *(optional)* |
| | `personas/` — persona priors *(optional)* |

```bash
cd input
rm -f bldg1_*.ttl equipment_linkage.ttl "Abacws floor"*.pdf "Abacws floor"*.dwg
rm -rf documents personas
# …then copy in your own model and config
```

File names are yours to choose: the uploader ingests **any** `*.ttl` in `input/`, and floor plans are
matched by the `<label> floor <N>.<ext>` pattern.

### Your TTL must satisfy three rules

Each of these caused a real, day-long onboarding failure during development — they are the difference
between "it works" and "the graph loads but nothing answers".

```turtle
@prefix bldg:  <http://example.org/riverside#> .   # 1. byte-identical to ontology_namespace
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix ref:   <https://brickschema.org/schema/Brick/ref#> .
@base          <http://example.org/riverside#> .   # 2. REQUIRED. Without @base, a single
                                                   #    relative IRI makes GraphDB reject
                                                   #    the ENTIRE file as malformed.

bldg:Room_204_Temp a brick:Air_Temperature_Sensor ;
    rdfs:label "Room 204 Temperature" ;
    brick:hasExternalReference [
        a ref:TimeseriesReference ;
        ref:hasTimeseriesId "8f3c…-uuid" ;         # the column name / uuid in YOUR database
        ref:storedAt        bldg:database1 ] .     # 3. an IRI, NOT "database1" in quotes.
                                                   #    A string literal cannot join, so every
                                                   #    live query silently returns nothing.
```

OntoSage reads your existing classes as they are — Brick, RealEstateCore, ASHRAE 223P, Haystack-in-RDF,
or a custom vocabulary. It does not require you to remodel your building.

---

## Step 3 — Connect your data sources

Register each database under the key your TTL's `ref:storedAt` points at, in
`input/database_registry.yaml`:

```yaml
databases:
  database1:                                   # ← matches ref:storedAt bldg:database1
    type: mysql                                # mysql | mysql_narrow | postgresql | timescaledb |
                                               # influxdb | mongodb | sqlite | cassandra | …
    host: "${MYSQL_HOST:-host.docker.internal}"
    port: "${MYSQL_PORT:-3306}"
    user: "${MYSQL_USER}"
    password: "${MYSQL_PASSWORD}"
    database: "${MYSQL_DATABASE}"
    nature: real                               # real | synthetic — surfaced as provenance
    note: "Riverside BMS historian"
```

Two table shapes are supported:

* **Wide** (`type: mysql`) — one column per sensor uuid. Simple, but MySQL caps a row at ~1017
  columns, so large estates outgrow it.
* **Narrow** (`type: mysql_narrow` with `table:`) — rows of `(uuid, datetime, value)`. Preferred at
  scale, and several modality tables can coexist.

A building may span **several backends at once** — each `ref:storedAt` key routes independently, so
energy can live in Postgres while IAQ stays in MySQL. Adding a backend type is a new adapter, never a
change to the agents.

This is not theoretical: a building shipped with the repo answers from **MySQL and PostgreSQL in the
same conversation**, with the adapter chosen per sensor.

![A reading served from MySQL]({{ '/admin-portal-screenshots/answer-mysql-reading.png' | relative_url }})
![The same building, a reading served from PostgreSQL]({{ '/admin-portal-screenshots/answer-postgres-reading.png' | relative_url }})
*Two questions, one building, two database technologies. Nothing in either question says which backend
to use — the sensor's `ref:storedAt` decides, and the person asking never sees the difference.*

---

## Step 4 — Build and start

```bash
docker compose down                 # if something is already running
docker compose build orchestrator   # first build, or after pulling code changes
docker compose up -d
curl http://localhost:8000/health   # wait for "healthy"
```

On boot OntoSage ingests every `*.ttl` in `input/` (re-uploading only what changed), builds a sensor
map from the live graph, and indexes floor plans and documents. A large ontology can take several
minutes to warm GraphDB on first start; ontology initialisation retries by itself, so no manual
restart is needed.

> **Remove the demo publisher for a real building.** The `data-publisher` service fabricates readings
> so the fixtures have something to show. For a building with real telemetry, stop or delete that
> service so nothing ever writes synthetic values into your historian.

---

## Step 5 — Verify both halves

```
Half 1 — ontology loaded?      "How many temperature sensors are in this building?"
Half 2 — readings connected?   "What is the current temperature in Room 204?"
```

The inventory answer reports **declared vs reporting** sensors — for example *"1,318 declared in the
building model, 683 reported data in the last 24 h"*. That single line is the fastest way to see how
much of your model is genuinely wired to data. A sensor that exists in the graph but never reports
has a wrong `ref:hasTimeseriesId`, a wrong `ref:storedAt`, or no rows.

---

## Pitfalls we hit for real

| Symptom | Cause | Fix |
|---|---|---|
| Orchestrator refuses to boot, complains about the namespace | `@prefix bldg:` ≠ `ontology_namespace` | Make them byte-identical, trailing `#` included |
| GraphDB rejects the whole TTL as malformed | Relative IRIs and no `@base` | Add `@base` matching your namespace |
| Structural questions work; live values never do | `ref:storedAt` missing, or refs written as quoted **strings** instead of IRIs | Both properties required; `ref:storedAt` must be an IRI matching a registry key |
| Answers mention a building you never loaded | Reused a `BUILDING_ID` whose `volumes/<id>/` still holds the old graph | Use a new id, or delete that state directory |
| "UUIDs missing / no readings" right after seeding | The adapter caches table columns for 5 minutes | Seed before boot, or restart the orchestrator |
| A wide table refuses more sensors | MySQL's ~1017-column row limit | Move those sensors to a narrow `(uuid, datetime, value)` table |

---

## Prefer clicking to editing?

Everything above is also available in the **Admin Console** at `http://localhost:3001` — building
identity, TTL upload and validation, database registration, sensor mapping, capabilities, documents
and floor plans — with no host-side file editing. See [Admin Console]({{ site.baseurl }}/docs/admin-console/).

## See also

- [Quick Start]({{ site.baseurl }}/docs/quickstart/) — get the fixtures running first
- [Onboard a Building]({{ site.baseurl }}/docs/onboarding-building/) — the console and CLI paths in detail
- [Configuration]({{ site.baseurl }}/docs/configuration/) — every environment variable
- [OCBV Schema]({{ site.baseurl }}/docs/ocbv-schema/) — the conversational vocabulary layer
