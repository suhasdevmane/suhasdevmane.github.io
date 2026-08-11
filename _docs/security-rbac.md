---
title: Security & RBAC
layout: post
category: docs
permalink: /docs/security-rbac/
date: 2026-07-09
---

# Security & RBAC

OntoSage is built to run in front of real building data, so **every data and config endpoint is
authenticated and permission-gated**. There is no unauthenticated data path.

## Authentication

- **Passwords** are hashed with **Argon2id** (never stored or logged in plaintext).
- **Sessions** are Redis-backed bearer tokens (7-day lifetime). Log in at `POST /auth/login`; send the
  token as `Authorization: Bearer <token>` (or the session cookie).
- **Login lockout** throttles repeated failures; rate limiting is proxy-aware.
- **No default admin.** The first admin is created from `ADMIN_USERNAME` / `ADMIN_PASSWORD` at startup;
  passwords must be **12+ characters**.
- **`STRICT_SECRETS=true`** refuses to boot if any secret still equals its shipped default, and secrets
  are masked in the settings repr.

![Admin console sign-in modal]({{ '/admin-portal-screenshots/00-login.png' | relative_url }})
*The admin console's read-only views load without a login; admin actions require a `system:admin`
account.*

## RBAC — 6 roles × permissions

Every protected endpoint declares a required permission via `require_permission("<perm>")`. The
dependency resolves the session, returns **401** if unauthenticated and **403** if the role lacks the
permission, and injects a `UserContext`.

Permissions are `resource:action` strings — e.g. `sensor:read`, `analytics:read`, `metadata:read`,
`config:write`, `building:write`, `control:write`, `system:admin`, `system:health`.

| Role | Gets | Typical user |
|---|---|---|
| **admin** | **all** permissions incl. `system:admin` (ontology CRUD, reindex, user mgmt) | System administrator |
| **facility_manager** | all data reads + `config:write`, `building:write`, `device:control`, `control:write` | Building/estates manager |
| **analyst** | all data reads + `building:read` | Researcher / data analyst |
| **operator** | sensor/analytics/anomaly/trend reads + `device:control` | Ops / maintenance operator |
| **occupant** | `sensor:read`, `metadata:read` | Building occupant |
| **readonly** | `metadata:read`, `system:health` only | Guest / kiosk / unauthenticated default |

Guests default to **readonly** — they can see structure but not readings.

Roles are assigned per account on the console's **Users & Access** tab, which also controls which data
sources each role may query:

![Admin console Users & Access tab]({{ '/admin-portal-screenshots/10-users-access.png' | relative_url }})
*Each account has a role dropdown (admin, facility_manager, occupant…); + Add user creates accounts. A
role left unconfigured is unrestricted (opt-in), and `admin` always has full access.*

Ontology management (`upload/validate/drop TTL`, SPARQL browser) and the semantic-index reindex all
require **`system:admin`** — the [admin console]({{ '/docs/admin-console/' | relative_url }}) is admin-only.

## Roles are not personas

This trips people up, so it's worth stating flatly:

- **RBAC roles** decide *what you are allowed to access*. Enforced, server-side, non-negotiable.
- **Personas** ([stakeholder framing]({{ '/docs/stakeholder-guide/' | relative_url }})) only bias
  *classification and wording*. A persona can never grant access a role forbids.

An "occupant persona" phrasing does not give occupant-role permissions, and an admin asking as a
"visitor" still has admin access. Keep them mentally separate.

## Managing users

Accounts live in the **Admin Console → Users & Access**. Creating one takes a username, a
password of 12+ characters (with a show/hide toggle so you can confirm what you typed) and a
role. Every row carries a **Password** button for setting a new one.

Stored passwords are one-way **Argon2id** hashes: an existing password can never be
displayed — not to an admin, not to anyone with the database — only replaced. A reset also
signs out that user's active sessions, because a shared or leaked password is the usual
reason to reset one.

Creating a user, changing a role, and resetting a password all apply to the **next request**:
no restart, no re-login, no cache flush. The **Role → Data-source access** matrix on the same
tab decides which data sources each role may draw on when answering; a role left fully
unticked is unrestricted, since access control is opt-in.

## Role-aware answers in the chat UI

Open WebUI authenticates to OntoSage with a single shared API key, so by itself it cannot say
*who* is asking — every chat request would arrive as the same least-privilege identity.
Enabling `ENABLE_FORWARD_USER_INFO_HEADERS` on Open WebUI and `TRUST_FORWARDED_USER` on the
orchestrator resolves the signed-in person to their OntoSage account, so **their** role
shapes the answer:

```
"Set the temperature setpoint in zone 5.28 to 21 degrees"

  readonly          → "You don't have permission to control building systems…"
  facility_manager  → "Command queued for approval (ID: b2160acc)…"
```

Same request, same API key, different answers.

Anyone who signs in without an OntoSage account is served at **readonly** — enough to explore
the building, nothing more. To grant a role, create an account whose username matches their
sign-in email or its local part (`alice@example.com` → `alice`).

> **Trust boundary.** A forwarded identity header is only as trustworthy as whoever can set
> it: anyone holding the pipeline key could claim to be any user. `TRUST_FORWARDED_USER` is
> **off by default**, and with it off the header is ignored entirely. Enable it only where the
> proxy is the sole key holder on a trusted network — the default Docker deployment — and keep
> the API port off the public internet.

## Read-only by design

OntoSage answers; it does not operate the building. Actuation requests are declined at the routing layer,
and even the `control:write` permission only reaches a **simulated** actuation gateway (logged, not wired
to a live BMS) unless a real driver is explicitly configured. This is a deliberate safety boundary.

Every mutating admin action is recorded, so config changes are accountable:

![Admin console Audit tab]({{ '/admin-portal-screenshots/12-audit.png' | relative_url }})
*The audit log — timestamp, user, HTTP method, path, and outcome for each capability edit, building-config
change, reindex, sensor upload, and TTL upload.*

## Hardening checklist for production

- [ ] `STRICT_SECRETS=true` and every default secret replaced (`SECRET_KEY`, `GRAPHDB_PASSWORD`,
      `MYSQL_PASSWORD`, `POSTGRES_USER_PASSWORD`).
- [ ] Strong 12+ char admin password; no shared accounts.
- [ ] `TRUST_FORWARDED_USER` enabled **only** where the chat proxy is the sole holder of
      `PIPELINE_API_KEY` on a trusted network — that key otherwise becomes an impersonation key.
- [ ] Self-registration on the chat UI closed once your users exist, unless open sign-up is
      intended (new sign-ups land at readonly by design).
- [ ] TLS terminated at your reverse proxy; the console (`:3001`) and API (`:8000`) not exposed raw.
- [ ] Backend stores (GraphDB, MySQL, Postgres, Redis, Qdrant, Mongo) not published to the public
      internet.
- [ ] Confirm `/health` reports the expected `build.sha` so you know exactly what's running.

## See also

- [Configuration]({{ '/docs/configuration/' | relative_url }}) — where these settings live.
- [Stakeholder guide]({{ '/docs/stakeholder-guide/' | relative_url }}) — personas vs. roles.
- [API reference]({{ '/docs/api-reference/' | relative_url }}) — auth + admin endpoints.
