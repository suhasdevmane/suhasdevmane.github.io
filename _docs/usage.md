---
layout: post
title: Usage
date: 2025-09-28
---

# Usage

This guide covers how to use OntoBot’s services end-to-end.

## Services at a glance

- Rasa (5005): NLU/Dialogue
- Action Server (5055): business logic, data fetch, analytics calls
- Duckling (8000): entity extraction
- Analytics (6001): time-series analysis
- File server (8080): serves generated artifacts
- Jena Fuseki (3030): SPARQL store (optional)
- Rasa Editor (6080): tweak NLU data live
- Frontend (3000): chat UI

## Conversational flow

1) User asks a question in the frontend.
2) Rasa detects intent/entities; a custom action runs.
3) Action queries DB/knowledge, maps UUID→sensor names.
4) Action builds standardized flat or nested payload and (optionally via Decider) posts to `/analytics/run`.
5) Analytics returns unit-aware results with defaults; action replies and may attach artifacts via the file server.

## Analytics payloads

- Flat: `{ sensorName: [ {datetime|timestamp, reading_value}, ... ] }`
- Nested: `{ groupId: { key: { timeseries_data: [ {datetime, reading_value}, ... ] } } }`

Analytics accepts both, normalizes timestamps, and merges groups when needed.

## Customizing for a new building

- Ontologies/TTLs: add your building TTLs and align device/location terms with Rasa entities.
- Sensor mapping: create/maintain UUID→name mapping used by actions.
- Thresholds: pass `acceptable_range` / `thresholds` to analytics per request to override defaults (UK guidelines built-in).
- SQL schema: update actions’ queries to match your tables; adjust SELECT/ joins accordingly.
- NL2SPARQL: enable the T5 service and train/fine-tune on your ontology if using SPARQL.
- Visualiser/API: enable Abacws API & Visualiser if you need a 3D dashboard; set `API_HOST`.

## Testing

- Health: open the service health URLs listed above.
- Analytics smoke test:

```powershell
python microservices/test_analytics_smoke.py
```

It posts a realistic payload to each analysis and prints a summary.
