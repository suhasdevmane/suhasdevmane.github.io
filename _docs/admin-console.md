---
title: Admin Console
layout: post
category: docs
permalink: /docs/admin-console/
date: 2026-07-05
---

# Admin console

The admin console at **`http://localhost:3001`** (the `config-panel` service) is where you run and
administer a building without touching code or Turtle. It has **13 tabs**, is RBAC-gated — admin-only
actions need a `system:admin` account — and every action calls the same permission-protected
`/api/v1/admin/*` endpoints the [API]({{ '/docs/api-reference/' | relative_url }}) exposes.

All screenshots below are from a live deployment (the Abacws building), shown in light theme.

> The React app at `:3000/admin` is a development surface and is off by default. `:3001` is the console
> to use.

## Signing in

Read-only views (Overview, Ask, Health, Guide) load without a login. Admin actions — editing `.env`,
connecting databases, uploading TTL, managing users — need a `system:admin` account. Click **Sign in**
and authenticate; the console stores a session token and the sidebar shows *signed in · &lt;user&gt;*.

![OntoSage admin console sign-in modal]({{ '/admin-portal-screenshots/00-login.png' | relative_url }})
*The sign-in modal states plainly that admin actions need a `system:admin` account.*

## Overview — system state at a glance

The landing tab summarises the whole deployment: how many **data sources** are enabled, **services**
healthy, the active **building**, the **LLM provider** and **embedding** model, and the **user/role**
count — plus quick-action buttons to jump into the common flows.

![Admin console Overview tab]({{ '/admin-portal-screenshots/01-overview.png' | relative_url }})
*Overview cards: 7/8 data sources enabled, 7/8 services healthy, Abacws Building active, Local Ollama
(`gpt-oss:20b`) as the LLM, bge-large-en-v1.5 (1024-d) embeddings, 495 users across 6 roles.*

**How to use it:** start here to confirm the system is healthy and pointed at the right building before
you make changes. The quick-action buttons (*Connect data*, *Try a question*, *Manage data sources*,
*AI & Models*, *How to use this console*) deep-link into the relevant tab.

## Data Sources — toggle capabilities on/off, with provenance

Each card is a synthetic data source (occupancy, energy, noise, air quality, light, equipment, water,
complaints…). Toggling one **on** writes its Brick triples *and* database rows so the matching
questions become answerable; **off** means those questions are politely declined. The **provenance
legend** on the right names every source system — because every answer is tagged with the system that
produced it.

![Admin console Data Sources tab with provenance legend]({{ '/admin-portal-screenshots/02-data-sources.png' | relative_url }})
*Per-source toggles, each showing its provenance system, a `simulated` badge, point count, and what it
unlocks. Illuminance/Daylight is toggled off here.*

**How to use it:**
1. Toggle a source **on** to unlock its questions, or **off** to decline them.
2. **Regenerate** writes fresh synthetic data for that source; **Capabilities & questions** lists what
   it unlocks; **Preview** shows sample rows.
3. **Reset (clean slate)** switches everything off for a repeatable demo; **Enable all** turns them all
   on. The `simulated` badge marks data injected to demonstrate a capability a real BMS wouldn't expose.

## Ask (test) — run the real pipeline in-console

Ask a question straight against the live pipeline and see the **answer**, the **provenance** (which
systems produced it), and the **routed intent** — without leaving the console. This is the fastest way
to prove that a data-source toggle or a new sensor actually took effect.

![Admin console Ask test tab]({{ '/admin-portal-screenshots/03-ask.png' | relative_url }})
*The Ask tab with suggested probes ("What is the noise level on floor 5?", "How many temperature
sensors are there?").*

**How to use it:** type a question (or click a suggestion) and press **Ask**. After enabling a source
on the Data Sources tab, ask the matching question here — a real answer with the right provenance chip
confirms the toggle worked.

![Ask tab showing a grounded answer with routing]({{ '/admin-portal-screenshots/03b-ask-answer.png' | relative_url }})
*A live answer to "How many rooms are there?" — real figures computed from the ontology and floor plans
(233 rooms, 1,318 sensors, 20,370 m²), each block cited to its source, with the routed intent shown
bottom-right. Honest and grounded, never fabricated.*

## AI & Models — pick the LLM and embedding backend

Choose the **LLM provider** (Local Ollama, Ollama Cloud, or OpenAI) and model, and the **embedding
backend** (local `bge-large-en-v1.5` 1024-d, or OpenAI 1536-d) — independently. Changes are written to
`.env` and apply after an orchestrator recreate (the provider is validated and its clients built at
boot, so there is no live hot-swap).

![Admin console AI & Models tab]({{ '/admin-portal-screenshots/04-ai-models.png' | relative_url }})
*LLM provider radios with the Ollama base URL + model (default `gpt-oss:20b`, admin-selectable) and
Test-connection; below, the embedding backend with a warning that switching dimensions invalidates the
Qdrant index.*

**How to use it:**
1. Pick a provider; for local Ollama, **Fetch installed** lists models actually present, and **Test
   connection** verifies reachability.
2. Choose the embedding backend. ⚠️ Switching it changes vector dimensions (1024 ↔ 1536) and
   **invalidates the existing Qdrant index — you must re-index** afterward (Ontology → Rebuild).
3. **Save to .env**, then recreate the orchestrator to apply.

## Services — open the attached tools

Launch each attached tool's own web UI (GraphDB workbench, Qdrant dashboard, DB browsers, dashboards)
in a new tab. Status is probed live from inside the stack; optional tools that aren't running yet are
enabled in `docker-compose.yml`.

![Admin console Services tab]({{ '/admin-portal-screenshots/05-services.png' | relative_url }})
*The Services tab — "Open launches each service's own web UI in a new tab; status is probed live from
inside the stack."*

## Integrations — live feeds & notification channels

External **live data feeds** (`input/feeds.yaml`) and **notification channels** (`input/channels.yaml`).
The view shows what's active and lets you **test-send** a channel; the feed/channel definitions are
edited in their YAML files (to preserve their inline docs).

![Admin console Integrations tab]({{ '/admin-portal-screenshots/06-integrations.png' | relative_url }})
*Three `rest_poll` weather feeds (temperature, humidity, wind) polling Open-Meteo every 300s into
`bldg:database1`, plus a `log` notification channel with Test-send.*

## Settings (.env) — the backend environment

The complete `.env` surface as an editable table, with **secrets masked**. Filter by key, edit values,
and **Save** (changes apply after a restart). A **backup & restore** panel downloads/restores a
portable config snapshot.

![Admin console Settings .env tab]({{ '/admin-portal-screenshots/07-settings-env.png' | relative_url }})
*The environment editor — every key (providers, DB hosts, feature flags) with masked secrets and a
config backup/restore panel at the top.*

**How to use it:** never hand-edit inside the container — edit here, Save, then recreate the
orchestrator so the new environment is read at boot. Type a new value over a masked secret to overwrite
it. See [Configuration]({{ '/docs/configuration/' | relative_url }}) for the key reference.

## Databases — connect time-series backends

Every registered database connection, with badges for **active/dormant** and **synthetic**. A sensor's
UUID routes to a connection via `ref:storedAt`; credentials live in `.env`. Per connection you can
**Test**, browse **Data**, **Register sensors**, and **Verify** answerability.

![Admin console Databases tab]({{ '/admin-portal-screenshots/08-databases.png' | relative_url }})
*The Databases tab lists many backends (MySQL narrow/wide, Postgres, Timescale, Mongo, Influx,
Cassandra, Redis…), each with Test / Data / Register sensors / Verify.*

**Data** opens a live preview of a connection's time-series rows:

![Database data preview]({{ '/admin-portal-screenshots/08c-db-data.png' | relative_url }})
*A preview of `energy_data` — 132,688 rows across 8 sensors, with recent timestamped values keyed by
sensor UUID.*

The **Guided setup** wizard walks the whole no-code flow — connect a database, describe its sensors as
triples, then verify OntoSage can answer about them:

![Databases guided-setup wizard]({{ '/admin-portal-screenshots/08b-guided-setup.png' | relative_url }})
*Step 1 of the "Connect a data source" wizard: use an existing connection or add a new one → describe
sensors → verify.*

**How to use it:** click **Guided setup** (or **+ Add connection**), enter host + credentials, then
**Register sensors** by describing them (points form, CSV, or Brick TTL). Each sensor's UUID gets a
`ref:storedAt bldg:<key>` triple so its queries route to that DB — applies immediately. See
[Onboard a building]({{ '/docs/onboarding-building/' | relative_url }}).

## Ontology — building identity, index, capabilities, TTL & SPARQL

The richest tab. It consolidates everything about the knowledge graph:

![Admin console Ontology tab]({{ '/admin-portal-screenshots/09-ontology.png' | relative_url }})
*Building identity (namespace/prefix/name), the semantic search index (rebuild/refresh), building
capabilities (+Add capability), named graphs, an Upload-TTL panel, and a read-only SPARQL browser.*

- **Building identity** — set the ontology **namespace**, **prefix**, and **name**. The `bldg:` prefix
  is only a label; the namespace it binds to is what makes triples belong to *this* building, and it
  lives in `input/building.yaml`. Set this **first** for a new building, before loading triples — it
  must match the `@prefix` in your TTLs. Applies after a restart.
- **Semantic search index** — lets OntoSage find sensors by meaning (semantic RAG). It **rebuilds
  automatically** when you add sensors or upload TTL (debounced); exact name/type questions work
  immediately. Use **Rebuild now** only after a bulk load done outside the console.
- **Building capabilities** — amenities and services answered in plain English, added as
  `ontosage:Amenity` triples saved to `input/<bldg>_capabilities.ttl` (with a `.trash/` backup) so they
  persist across restarts — no Turtle, no code.
- **Named graphs** — every `input/*.ttl` loads into a named graph on startup; dropping a file graph
  moves its `input/` file to `.trash/` so the drop survives a restart.
- **Upload TTL** — paste Turtle, **Validate**, then **Upload**. A `urn:ontosage:ttl:<file>` graph also
  persists to `input/<file>` (survives restart).
- **SPARQL browser** — run read-only `SELECT` / `ASK` against the live graph.
- **Documents** — upload a policy / manual / contact sheet (`.md` / `.txt` / `.pdf`) into the document
  KB (Qdrant `documents_<bldg>`), which answers off-ontology questions ("what's the wifi policy?").
  Saved to `input/documents/` and re-indexed automatically — no host-side file drop.
- **Floor plans** — upload a **PDF** or **DWG** per floor for spatial / floor queries and geometry;
  stored as `<label> floor <N>.<ext>` (label defaults to the active building id) and ingested into the
  manifest registry.

![Ontology tab — named graphs, Upload TTL, and SPARQL browser with results]({{ '/admin-portal-screenshots/09c-sparql-results.png' | relative_url }})
*The lower half of the tab: named graphs (with per-graph triple counts and Drop), the Upload-TTL panel,
and the SPARQL browser showing live class counts from the graph.*

### Documents & floor plans — knowledge files (no host-side drop)

The Ontology tab also uploads the two remaining building inputs straight from the browser, so the
**entire** onboarding — identity, TTL, sensors/DB, documents, floor plans — is doable from the console
for any building. Each writes into the **active** building's `input/` and re-indexes automatically.

![Ontology tab — Documents and Floor plans upload]({{ '/admin-portal-screenshots/09d-knowledge-files.png' | relative_url }})
*Left — **Documents**: pick a `.md` / `.txt` / `.pdf` policy or manual and **Upload document**; it lands
in `input/documents/` and is embedded into the document KB (Qdrant `documents_<bldg>`). Right — **Floor
plans**: give a floor number (label defaults to the active building id), pick a **PDF** or **DWG**, and
**Upload floor plan**; it's stored as `<label> floor <N>.<ext>` and ingested into the spatial manifest
registry.*

**How to use it:**
- **Documents** answer off-ontology questions ("what's the wifi policy?", "how do I book a room?") — drop
  the building's policies, manuals, and contact sheets here. Uploaded files appear in the list below the
  button and can be removed; every add/remove re-indexes the KB (no restart).
- **Floor plans** power spatial and floor queries ("show me floor 3", "how many rooms are adjacent to
  3.01?", "what's the total area?"). A DWG carries geometry (room polygons, areas, adjacency); a PDF gives
  the visual. Upload one per floor.
- Both endpoints are **building-agnostic** — they resolve the target from the active `BUILDING_ID`, so the
  same buttons onboard `bldg1`, `bldg2`, or any building with no code change.

### The schema-driven "Add capability" form

**+ Add capability** opens a form generated from the [OCBV schema]({{ '/docs/ocbv-schema/' | relative_url }}):
the **Type** dropdown lists the OCBV subclasses, and the fields shown are the datatype properties whose
`rdfs:domain` applies to the chosen type.

![Add capability modal — schema-driven form]({{ '/admin-portal-screenshots/09b-add-capability.png' | relative_url }})
*"Fields for this type (from the OCBV schema)" — a Facility needs only a label; other types surface
their own fields. Saved as `ontosage:Amenity` triples, answerable immediately.*

**How to use it:** pick a Type, give an ID and Label, fill any type-specific fields, and **Add
capability**. Add a class or property to `ontosage_schema.ttl` and it appears here after a reload — no
code change. (The form falls back to a built-in list if GraphDB is briefly unreachable.)

## Users & Access — accounts, roles, and per-role data access

Create accounts and assign one of the six roles; a user's role determines their permissions **and**
which data sources they may query. A role left unconfigured is unrestricted (opt-in control); `admin`
always has full access.

![Admin console Users & Access tab]({{ '/admin-portal-screenshots/10-users-access.png' | relative_url }})
*The user list with a role dropdown per account (admin, facility_manager, occupant…) and a Delete
control; + Add user at the top.*

**How to use it:** **+ Add user** to create an account (12+ character password, with a show/hide
toggle so you can confirm what you typed), pick a role from the dropdown to change permissions, and
optionally restrict a role to specific data sources. **Password** on any row sets a new password —
stored hashes are one-way, so an existing password can never be displayed, only replaced, and a
reset signs out that user's active sessions.

Everything here applies to the **next request**: creating a user, changing a role, or resetting a
password needs no restart, re-login or cache flush. Roles also shape chat answers when identity
forwarding is enabled — see [Security & RBAC]({{ '/docs/security-rbac/' | relative_url }}).

## Health — live dependency status

Live orchestrator status and feature state: overall health, request latency, and each dependency
(Postgres, MySQL, GraphDB, Redis, Qdrant, rag-service, code-executor) with a status dot, plus the
**circuit breakers** guarding the LLM and MySQL.

![Admin console Health tab]({{ '/admin-portal-screenshots/11-health.png' | relative_url }})
*Overall healthy, 87.3 ms latency, every dependency ok, and both circuit breakers closed (0/5
failures). Auto-refresh every 5s.*

## Audit — who did what

A running log of every **mutating admin action** — timestamp, user, HTTP method, path, and outcome — so
config changes are accountable.

![Admin console Audit tab]({{ '/admin-portal-screenshots/12-audit.png' | relative_url }})
*The admin-action audit table: capability create/delete, building-config PUTs, reindex, sensor CSV
uploads, TTL upload — each with the acting user and a 200 status.*

## Guide — the in-console how-to

An always-available primer inside the console: the two-halves mental model, a tab-by-tab summary, and
step-by-step demo flows (unlock a capability, connect a database, switch the AI model, manage roles).

![Admin console Guide tab]({{ '/admin-portal-screenshots/13-guide.png' | relative_url }})
*The Guide tab — "a data source has two halves", tabs at a glance, and the four-step capability-unlock
demo.*

## See also

- [OCBV vocabulary]({{ '/docs/ocbv-schema/' | relative_url }}) — what drives the capability form.
- [Onboard a building]({{ '/docs/onboarding-building/' | relative_url }}) — the console in a full onboarding.
- [Configuration]({{ '/docs/configuration/' | relative_url }}) — the `.env` keys behind the Settings tab.
- [Security & RBAC]({{ '/docs/security-rbac/' | relative_url }}) — the roles behind Users & Access.
