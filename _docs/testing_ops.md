---
layout: post
title: Testing & Operations
date: 2025-09-28
---

# Testing & Operations

## Health checks

- Analytics: `/health` on 6001
- Rasa: `/version` on 5005
- Action server: `/health` on 5055
- Duckling: root page contains "Duckling" on 8000
- File server: `/health` on 8080
- Fuseki: `/$/ping` on 3030

## Smoke tests

Run the analytics smoke test:

```powershell
python microservices/test_analytics_smoke.py
```

This posts sample payloads to each analysis and reports pass/fail.

## Logs

```powershell
docker-compose logs -f microservices
docker-compose logs -f action_server
docker-compose logs -f rasa
```

## Troubleshooting

- Ports busy: change host port mappings in docker-compose.
- Service unhealthy: hit health URL and check container logs.
- Payload errors: verify flat/nested shapes; ensure `{datetime, reading_value}` exist.
- Networking: containers use `ontobot-network`.
