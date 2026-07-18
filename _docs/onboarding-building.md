---
title: Onboard a Building
layout: post
category: docs
permalink: /docs/onboarding-building/
date: 2026-07-06
---

# Onboard a building

OntoSage serves **one active building at a time**. Onboarding means giving it that building's two
halves — the **ontology** (what exists) and the **time-series** (what it reads) — plus optional
conversational extras. No code changes; everything is `input/` + `.env` + the console.

## The mental model: both halves or no answer

```
A question is answerable when …
  (a) the sensor is a triple in GraphDB          — "there is a CO₂ sensor in room 3.04"
  AND
  (b) its readings are rows in a registered DB    — linked by ref:hasTimeseriesId + ref:storedAt
```

A DB full of rows with no ontology is invisible; an ontology with no rows has nothing to read. Provide
both. This is exactly why toggling a synthetic source **on** in the console writes Brick triples *and*
database rows in one step:

![Data Sources tab — toggle a source to unlock its questions]({{ '/admin-portal-screenshots/02-data-sources.png' | relative_url }})
*Each source unlocks a set of questions when enabled; every answer is then tagged with the provenance
system that produced it (legend on the right).*

## The `input/` folder (flat layout is canonical)

The active building's files sit **directly** under `input/`:

| File | Required | Purpose |
|---|---|---|
| `building.yaml` | ✅ | Building id, name, **ontology namespace + prefix**, actuation block |
| `*.ttl` (e.g. `bldg1_*.ttl`) | ✅ | Brick/BACnet model + sensor `ref:` links; auto-uploaded to GraphDB |
| `ontosage_schema.ttl` | ✅ (shipped) | The [OCBV vocabulary]({{ '/docs/ocbv-schema/' | relative_url }}) |
| `database_registry.yaml` | ✅ | Maps each `ref:storedAt` key → a real DB connection + adapter |
| `<bldg>_capabilities.ttl` | optional | Amenities / knowledge topics (or author via the console) |
| `*.dwg` / `*.pdf` | optional | Floor-plan geometry + text |
| `documents/` | optional | Policy / manual PDFs for the document KB |
| `concepts.ttl`, `feeds.yaml`, `rules.yaml`, `channels.yaml`, `intents.yaml`, `personas/` | optional | Lay-term overlay, live feeds, ECA alerts, notifications, per-building intents/personas |

> **Sensor readings never live in `input/`.** `input/` is metadata/config only. Readings go in a
> database and are referenced from the ontology.

## Path A — scripted (a whole new building)

```bash
# 1. Generate a config skeleton
python scripts/onboard_building.py --building-id bldg2 --non-interactive

# 2. Drop bldg2's TTL, register its DB in database_registry.yaml, load its rows

# 3. Make bldg2 the active building (validates TTL @prefix ↔ ontology_namespace)
python scripts/swap_building.py --to bldg2 --dry-run     # validate first
python scripts/swap_building.py --to bldg2 --archive     # apply + archive old + flush cache
docker compose restart orchestrator                      # TTL validator runs first; hard-fails on mismatch
```

The swap refuses to proceed if `building.yaml` is missing required keys, `building_id` ≠ the declared
id, or a TTL prefix disagrees with `ontology_namespace` — so the building can never boot half-configured.

## Path B — the console (incremental, no code)

For adding sensors, amenities, or fixing the building identity on a running system, use the
[admin console]({{ '/docs/admin-console/' | relative_url }}) — mostly its **Ontology** and **Databases**
tabs:

1. **Ontology → Building identity** — set namespace / prefix / name (writes `building.yaml`). Do this
   **first** for a new building, before loading triples.
2. **Databases → Guided setup / Register sensors** — connect the DB and describe its sensors; each gets
   a `ref:storedAt bldg:<key>` triple so its queries route to that backend.
3. **Ontology → + Add capability** — author amenities from the schema-driven form.
4. **Ontology → Upload TTL** — paste/validate/upload larger TTL, and browse with the SPARQL browser.

The **Guided setup** wizard on the Databases tab walks the whole no-code flow end to end:

![Guided-setup wizard — connect, describe sensors, verify]({{ '/admin-portal-screenshots/08b-guided-setup.png' | relative_url }})
*"Connect a data source — no code, three steps: connect a database, describe its sensors as triples,
then verify OntoSage can answer about them."*

Once connected, you can preview the actual time-series rows — the *other* half of an answerable
question:

![Database data preview — time-series rows]({{ '/admin-portal-screenshots/08c-db-data.png' | relative_url }})
*`energy_data` holding 132,688 rows across 8 sensors, each row a timestamped value keyed by sensor UUID.*

Everything persists to `input/`, so a later `docker compose up -d` reproduces the same building.

## Verifying it worked

```bash
# Ontology loaded?  (structural question — SPARQL only)
curl -s -X POST http://localhost:8000/chat -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"message":"how many temperature sensors are there?","session_id":"probe"}'

# Both halves?  (needs ontology + rows)
curl -s -X POST http://localhost:8000/chat -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"message":"what is the temperature on floor 1 right now?","session_id":"probe"}'
```

If the structural one answers but the live one says *"no data"*, half (b) is missing — the sensor is in
the graph but its rows/registration aren't there yet.

## See also

- [Configuration]({{ '/docs/configuration/' | relative_url }}) — every `.env` and `input/` knob.
- [OCBV vocabulary]({{ '/docs/ocbv-schema/' | relative_url }}) — authoring capabilities.
- [Architecture]({{ '/docs/architecture/' | relative_url }}) — the two-half answer model in depth.
