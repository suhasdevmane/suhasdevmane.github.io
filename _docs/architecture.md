---
layout: post
title: Architecture
date: 2025-09-28
---

# Architecture

OntoBot is orchestrated by Docker Compose and consists of modular services:

- Rasa: NLU and dialogue (5005)
- Action Server: custom logic, data-layer, analytics calls (5055)
- Duckling: entity extraction (8000)
- Analytics microservices: time-series analytics (6001 host → 6000 container)
- Decider service: selects analytics for a user question (6009)
- File server: serves artifacts and provides small utilities (8080)
- Jena Fuseki: SPARQL endpoint (3030)
- Rasa Editor: light admin/UX (6080)
- Frontend: chat UI (3000)
- Optional: Abacws API and Visualiser (8091/8090), NL2SPARQL (6005), Ollama (11434)

## Data flow

1) User → Frontend → Rasa
2) Rasa → Action Server (custom action)
3) Action → Data stores (SQL/SPARQL/files) and builds a standardized payload
4) Action → (optional) Decider → selected `analysis_type`
5) Action → Analytics `/analytics/run` with payload
6) Analytics → unit-aware results with UK defaults
7) Action → Formats response + artifacts → File server → Frontend renders

## Compose mapping

Service names in code use internal DNS names (e.g., `microservices:6000`) while host access uses mapped ports (e.g., `localhost:6001`). See repo `docker-compose.yml` for the definitive mapping.
