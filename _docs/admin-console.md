---
title: Admin Console
layout: post
category: docs
permalink: /docs/admin-console/
date: 2026-07-19
---

# Admin console

The admin console is served by the `config-panel` service at **`http://127.0.0.1:3001`**. It is
a static page (HTML and plain JavaScript, source in `config-panel/html/`) behind nginx, which
forwards `/api`, `/auth`, `/health` and `/chat` to the orchestrator on the same origin. There is
no build step.

Every action calls the same permission-checked endpoints listed in the
[API reference]({{ '/docs/api-reference/' | relative_url }}). The page itself loads without signing
in; anything that reads or changes configuration needs a session, and most tabs need an account
with `system:admin`.

> `frontend/` in the repository holds an older React admin portal. No compose service serves it;
> the console described here is the one to use.

The console has **13 tabs**, in this order: Overview, Data Sources, Ask (test), AI & Models,
Services, Integrations, Settings (.env), Databases, Ontology, Users & Access, Health, Audit, Guide.
The page header has a light/dark theme switch, a Help button and a pill showing whether the
data-source feature is on.

> **About the screenshots.** Images in `admin-portal-screenshots/` were taken in July 2026 on the
> same 13-tab layout; button labels and badge wording have changed slightly since. The Overview
> and Ontology tab images (under `assets/images/screenshots/`) come from the current build.
> Figures shown in any screenshot belong to the building that was active at the time.

## Signing in

Click **Sign in** at the bottom of the sidebar. The console keeps the session token in the
browser and shows *signed in · &lt;user&gt;*. The first admin account comes from
`ADMIN_USERNAME` and `ADMIN_PASSWORD` in `.env` (see [Security & RBAC]({{ '/docs/security-rbac/' | relative_url }})).

![Admin console sign-in modal]({{ '/admin-portal-screenshots/00-login.png' | relative_url }})
*The sign-in dialog. Admin actions need a `system:admin` account.*

Without signing in you can see the Overview tiles that come from public endpoints, the data-source
list, Health and the Guide. Ask (test) needs any signed-in account.

**When a change needs a restart.** After a change that is read at boot (`.env`, building
identity), a notice appears with the command `docker compose up -d orchestrator` and a copy
button. The **Restart service** button restarts the orchestrator process, which reloads code but
does **not** re-read `.env`; for `.env` changes use the recreate command.

## Overview

Tiles for the number of enabled data sources (and whether the feature is on), services healthy
out of those `/health` reports, the active building, and, when signed in as admin, the language
model provider and model, the embedding model and its width, and the number of user accounts and
roles. Buttons below jump to the common flows: **Connect data**, **Try a question**,
**Manage data sources**, **AI & Models** and **How to use this console**.

![Admin console Overview tab]({{ '/assets/images/screenshots/admin-overview.png' | relative_url }})
*Overview tiles: data sources, services, active building, language model, embeddings, users.*

## Data Sources

Works when `DATASOURCE_TOGGLES_ENABLED=true`. Each card is a synthetic data source defined in
`input/datasources.yaml` (occupancy, energy, noise, indoor air quality, light, equipment, water,
complaints and others). Switching a source **on** loads its Brick triples into its own named
graph, so the matching questions become answerable; **off** clears that graph, and those
questions are declined with a message naming the source.

- **Regenerate** writes fresh synthetic readings into the source's table; **Preview** shows a
  sample series without writing; **Capabilities** lists the questions the source makes
  answerable.
- **Enable all**, **Reset (clean slate)** (switch everything off and flush the answer cache) and
  **+ Add source**.
- The side panel has a **provenance legend** (which system each answer chip refers to) and a
  **live data provenance** summary, counted from the active building's graph: which backend each
  sensor reads from and whether that backend holds real or synthetic data.

Switching sources needs `config:write`.

![Admin console Data Sources tab]({{ '/admin-portal-screenshots/02-data-sources.png' | relative_url }})
*Source cards with their switches and the provenance legend.*

## Ask (test)

Runs a question through the real pipeline (`POST /chat`) and shows the answer, the routed
intent and, when `DATASOURCE_TOGGLES_ENABLED=true`, the provenance chips of the sources it used. Use it to confirm that a change took effect,
for example that switching a source on makes its question answerable. Suggested questions are
offered as buttons ("What is the noise level on floor 5?", "How many temperature sensors are
there?").

![Ask tab with an answer]({{ '/admin-portal-screenshots/03b-ask-answer.png' | relative_url }})
*An answer with its source chips and the routed intent.*

## AI & Models

Shows and sets the language model provider and model, and the embedding backend. The tab offers
**Local Ollama**, a **Hosted gateway (OpenAI-compatible)**, **Ollama Cloud** and **OpenAI**. For
local Ollama, **Fetch installed** lists the models actually present; for the hosted gateway,
**Fetch served** lists the models it serves; **Test connection** checks the endpoint. API keys
are shown only as *set* or *not set*. **Save** writes `.env`; the change applies after the orchestrator is
recreated, because model clients are built at boot. Switching the embedding backend changes the
vector width and invalidates existing indexes, so rebuild them afterwards (Ontology tab, Semantic
search index).

![Admin console AI & Models tab]({{ '/admin-portal-screenshots/04-ai-models.png' | relative_url }})
*Provider choice, model, endpoint test, and the embedding backend.*

## Services

Cards for the attached tools, each with a live online or offline status and an **Open** button
that launches the tool's own interface in a new tab: GraphDB workbench, Qdrant dashboard,
Adminer, the artefact file server, the orchestrator's OpenAPI page, the rag-service, Open WebUI
and Ollama, and optional tools (Grafana, Prometheus, the MCP server, pgAdmin) that run only when
they are enabled in the compose file.

![Admin console Services tab]({{ '/admin-portal-screenshots/05-services.png' | relative_url }})
*Attached tools with live status.*

## Integrations

Read-only view of live data feeds (`input/feeds.yaml`) and notification channels
(`input/channels.yaml`), with **Test-send** for a channel. Feeds and channels are edited in their
YAML files, which keep their inline documentation.

![Admin console Integrations tab]({{ '/admin-portal-screenshots/06-integrations.png' | relative_url }})
*Weather feeds and a notification channel.*

## Settings (.env)

- **Config backup & restore**: download a bundle of console-managed configuration (data
  sources, database connections, role access, switch states). `.env` secrets are never included.
  Restore validates every file before writing any.
- **Environment (.env)**: every key of the root `.env` as an editable table with a filter.
  Values of keys that look like secrets are masked; leave a masked field alone to keep its value,
  or type a new one to replace it. **+ Add credential** adds a key. **Save changes** writes the
  file; recreate the orchestrator to apply.

See [Configuration]({{ '/docs/configuration/' | relative_url }}) for what each key does.

## Databases

One card per database connection: the curated registry (`input/database_registry.yaml`) plus
connections added here (`database_registry.custom.yaml`; the curated file is never rewritten).
Badges show **curated**, **real** or **synthetic**, and **active** (listed under
`storage.databases` in `building.yaml`) or dormant. **Active only** filters the list.

Per connection:

- **Test**: connect and time a trivial query.
- **Data**: row count, distinct sensors and recent rows of a table.
- **Register sensors**: describe the connection's sensors as triples, by a points form, CSV or
  Brick Turtle. Each sensor gets its real time-series id and `ref:storedAt bldg:<key>`, so its
  questions are routed to this database. Registration applies immediately.
- **Verify**: compares sensors declared in the graph with ids that actually have rows.

**+ Add connection** stores credentials in `.env` and the entry in the custom registry, and
reloads the adapters so the connection can be used straight away. **Guided setup** walks through
connect, describe sensors and verify in one flow. **Load demo database** pre-fills a connection
to the optional `demo-mysql` service (start it first with
`docker compose --profile demo up -d demo-mysql`).

![Admin console Databases tab]({{ '/admin-portal-screenshots/08-databases.png' | relative_url }})
*Connection cards with their badges and actions.*

![Databases guided setup]({{ '/admin-portal-screenshots/08b-guided-setup.png' | relative_url }})
*The guided setup: connect, describe the sensors, verify.*

A question becomes answerable only when both halves exist: the sensor in the graph and its
readings in a registered database. See [Data sources]({{ '/docs/data-sources/' | relative_url }}).

## Ontology

Everything about the knowledge graph, from top to bottom.

**Coverage line.** How many declared sensors are actually answerable.

**Building identity.** Building id (read-only), name, ontology namespace and prefix, saved to
`input/building.yaml`. The `bldg:` prefix is only a label; the namespace is what makes triples
belong to this building, and it must match the `@prefix bldg:` in every Turtle file. Set it before
loading triples. Applies after a restart.

**Semantic search index.** Status of the GraphDB similarity index used to find sensors by
meaning. It rebuilds by itself after sensors are added or Turtle is uploaded; **Rebuild now** is
for bulk loads done outside the console.

**Building capabilities.** Amenities answered in plain English (prayer room, lift, café,
showers). The type list in **+ Add capability** comes from the
[OCBV schema]({{ '/docs/ocbv-schema/' | relative_url }}) (its subclasses of `ontosage:Amenity` and
`ontosage:KnowledgeTopic`). Below Type, ID and Label the dialog draws the fields the schema
gives that type, read from each datatype property's `rdfs:domain`: every type gets lay terms,
category, opening hours and a note; an amenity adds a location and floor; a knowledge topic adds
an answer, a link, contact details and who to report to; a procedure adds steps and a
maintenance issue a default priority. Switching type keeps what you have typed.

**Add capability** saves the entry as triples in `input/<id>_capabilities.ttl` (a backup of the
previous file goes to `input/.trash/`), loads it into the graph, and clears the caches that could
hold an older answer, so the next question can use it. The file is rewritten as a whole when you
add or delete an entry, so comments you wrote in it by hand are not kept; edit it by hand instead
if you need them.

![The Add capability dialog]({{ '/assets/images/screenshots/admin-capabilities.png' | relative_url }})
*The Add capability dialog with the fields the schema gives an amenity.*

**Named graphs.** Every `input/*.ttl` is loaded into its own named graph at startup. Dropping a
file graph (`urn:ontosage:ttl:<file>`) moves its file to `input/.trash/`, so the drop survives a
restart.

![Named graphs]({{ '/assets/images/screenshots/admin-ontology-graphs.png' | relative_url }})
*Named graphs with their triple counts.*

**Upload TTL.** Paste Turtle, **Validate** (parse only, no write), then **Upload**. A graph named
`urn:ontosage:ttl:<file>` is also written to `input/<file>` and survives a restart; other graph
names live in GraphDB only.

![Validating Turtle before upload]({{ '/assets/images/screenshots/admin-ttl-validate.png' | relative_url }})
*Validation reports the triple count and prefixes, or the parse error.*

![Turtle uploaded into a named graph]({{ '/assets/images/screenshots/admin-ttl-uploaded.png' | relative_url }})
*After upload, the new graph appears in the list.*

**SPARQL browser.** Read-only `SELECT` and `ASK` against the live graph.

![SPARQL browser]({{ '/assets/images/screenshots/admin-sparql.png' | relative_url }})
*A query and its results.*

**Documents.** Upload a policy, manual or contact sheet as `.md`, `.txt` or `.pdf`. The file is
saved to `input/documents/` and the document index is rebuilt; the status line follows that job
and reports how many passages were indexed. A PDF is read through its text layer, so a scanned PDF
with no text is stored but reported as not indexed (there is no OCR). Each listed file is marked
**indexed** or **not indexed**. Indexed documents answer questions such as "what is the wifi
policy?". Deleting a file removes it from the index.

**Floor plans.** Upload a PDF or DWG for a floor number, with an optional label (the active
building id by default). It is stored as `<label> floor <N>.<ext>` and ingested into the floor-plan
registry. A DWG gives room polygons, areas and adjacency; a PDF gives the drawing.

![Documents and floor-plan upload]({{ '/assets/images/screenshots/admin-knowledge-files.png' | relative_url }})
*Document upload on the left, floor-plan upload on the right.*

Writing and editing Turtle by hand is covered in
[Write TTL for your building]({{ '/docs/write-ttl/' | relative_url }}) and
[Edit TTL in a running system]({{ '/docs/edit-ttl/' | relative_url }}).

## Users & Access

- **User accounts**: create an account (user name, a password of 12 or more characters with a
  show/hide switch, a role), change a role from the dropdown, set a new password, or delete. A
  password reset ends that user's sessions.
- **Role → data-source access**: tick the data sources each role may use when answering. A role
  with nothing ticked and **All** off is unrestricted (access control here is opt-in), and
  `admin` always has full access. Saved to `input/role_datasource_access.yaml` and applied to the
  next question.

See [Security & RBAC]({{ '/docs/security-rbac/' | relative_url }}) for what roles permit and how a
role change reaches people who are already signed in.

## Health

Live orchestrator status from `/health`: overall state, response time, each dependency
(PostgreSQL, MySQL, GraphDB, Redis, Qdrant, rag-service, code-executor) and the circuit breakers
that protect the language model and MySQL. **Auto-refresh (5s)** is optional.

![Admin console Health tab]({{ '/admin-portal-screenshots/11-health.png' | relative_url }})
*Dependencies and circuit breakers.*

## Audit

The most recent 200 mutating admin actions: time, user and role, method, path and status. Every
`POST`, `PUT`, `DELETE` or `PATCH` to `/api/v1/admin/*` or `/api/v1/datasources` is recorded,
including failed and unauthenticated attempts.

## Guide

A short in-console primer: the two halves a data source needs (triples in the graph, rows in a
database), a tab summary, a four-step demonstration of switching a capability on, connecting an
external database, switching the model, and roles.

![Admin console Guide tab]({{ '/admin-portal-screenshots/13-guide.png' | relative_url }})
*The in-console guide.*

## See also

- [Onboard a building]({{ '/docs/onboarding-building/' | relative_url }}): the console in a full onboarding.
- [OCBV vocabulary]({{ '/docs/ocbv-schema/' | relative_url }}): the schema behind the capability form.
- [Configuration]({{ '/docs/configuration/' | relative_url }}): the keys behind the Settings tab.
- [Security & RBAC]({{ '/docs/security-rbac/' | relative_url }}): the roles behind Users & Access.
