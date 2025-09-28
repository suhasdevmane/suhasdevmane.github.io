---
layout: post
title: Data & Payloads
date: 2025-09-28
---

# Data & Payloads

## Sensor payloads

Analytics accepts two formats:

- Flat

```json
{
  "Air_Temperature_Sensor": [
    {"datetime": "2025-02-10 05:31:59", "reading_value": 22.5}
  ]
}
```

- Nested

```json
{
  "1": {
    "Air_Temperature_Sensor": {
      "timeseries_data": [
        {"datetime": "2025-02-10 05:31:59", "reading_value": 22.5}
      ]
    }
  }
}
```

Timestamps are normalized; duplicate groups are merged.

## UUID → name mapping

Map device UUIDs to human-readable names in actions before calling analytics. Store mappings in `rasa-ui/shared_data/` or query your device registry.

## SQL schema notes

- Update actions’ SQL to reflect your tables and columns (sensor table, readings table, joins by foreign keys or device IDs).
- Ensure you produce `{datetime, reading_value}` pairs per series.

## SPARQL endpoints and TTLs

- Load your building ontology TTLs into Jena Fuseki.
- Align Rasa entities and action logic with ontology terms (rooms, floors, sensors).
- If using NL2SPARQL, train/fine-tune on your ontology’s predicates and patterns.
