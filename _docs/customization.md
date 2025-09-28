---
layout: post
title: Customization
date: 2025-09-28
---

# Customization for New Buildings

Step-by-step to adapt OntoBot to a new site.

## 1) Ontologies and TTLs

- Prepare/build TTLs for devices, locations, and relationships.
- Load TTLs into Jena Fuseki.
- Align your entity names in Rasa with ontology terms.

## 2) Sensors and mapping

- Export device list and create a UUID→sensor name mapping.
- Store mappings under `rasa-ui/shared_data/` or integrate a registry query in actions.

## 3) Data sources

- SQL: adjust queries in actions to your schema.
- SPARQL: configure Fuseki dataset and credentials; optionally enable NL2SPARQL.

## 4) Rasa training

- Update intents/entities in `rasa-ui/data/` to include building-specific vocabulary.
- Re-train with docker compose’s `rasa-train` profile or use the Editor (6080).

## 5) Analytics thresholds

- UK defaults included; override via request params (`acceptable_range`, `thresholds`).
- Add custom analyses by editing `microservices/blueprints/analytics_service.py` and registering in the dispatcher.

## 6) Visualisation (optional)

- Enable Abacws API/Visualiser in compose.
- Add your building model and update device/location overlays.
- Set `API_HOST` for the visualiser to point to your API container.

## 7) Frontend UX

- Customize labels and shortcuts for common building queries.
- Keep action names/intents aligned with Rasa config.
