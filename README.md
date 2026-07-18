# OntoSage — documentation site

Public documentation for **OntoSage**, an agentic conversational layer over one smart building's own
data — *connect a building's data, then ask it anything in plain English.*

**Live site:** https://suhasdevmane.github.io

## What's here

A Jekyll site (gitbook theme). The docs live in `_docs/` and are ordered in the sidebar by date:

| Page | Path |
|---|---|
| Introduction | `/docs/introduction/` |
| Quick start | `/docs/quickstart/` |
| Architecture | `/docs/architecture/` |
| OCBV — Conversational Building Vocabulary | `/docs/ocbv-schema/` |
| Admin console | `/docs/admin-console/` |
| Onboard a building | `/docs/onboarding-building/` |
| Stakeholder guide | `/docs/stakeholder-guide/` |
| Configuration | `/docs/configuration/` |
| Security & RBAC | `/docs/security-rbac/` |
| API reference | `/docs/api-reference/` |
| Full technical reference | `/docs/ontosage/` |

## Product source

OntoSage itself lives at **https://github.com/suhasdevmane/OntoSage** (LangGraph + Brick Schema).
The OCBV vocabulary is released under CC-BY-4.0.

## Build locally

```bash
bundle install
bundle exec jekyll serve   # → http://localhost:4000
```
