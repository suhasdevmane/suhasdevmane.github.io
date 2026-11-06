# OntoSage documentation site

Public documentation for **OntoSage**, a conversational system that answers plain-English
questions about one smart building from its Brick/RDF graph and its sensor databases.

- Live site: <https://suhasdevmane.github.io>
- OntoSage source: <https://github.com/suhasdevmane/OntoSage>

The site is built by GitHub Pages with Jekyll and the
[`sighingnow/jekyll-gitbook`](https://github.com/sighingnow/jekyll-gitbook) theme. Its pages
describe the system as it is in the OntoSage repository; when they disagree, the code is right
and the page needs fixing.

## Layout

| Path | What it is |
|---|---|
| `_config.yml` | Site settings, the `docs` collection (`/docs/<slug>/`), Kramdown with GFM input, and `remote_theme` |
| `index.html` | The landing page. A standalone page (`layout: null`) with its own CSS |
| `_docs/` | The documentation pages, one Markdown file each |
| `_ontology/` | Generated reference pages for each ontology class, property and vocabulary (see below) |
| `_tools/gen_ontology_reference.py` | Generator for `_ontology/` and the generated blocks of the ontology pages |
| `_layouts/`, `_includes/`, `assets/gitbook/`, `assets/css/` | Theme layouts, includes and styles kept in this repository |
| `assets/images/screenshots/` | Screenshots of the chat interface and the admin console |
| `admin-portal-screenshots/` | Earlier admin console screenshots used by the admin console page |
| `_posts/`, `_pages/`, `_others/` | Theme example posts and short about pages, not part of the documentation |
| `.github/` | The hourly sync workflow used by the `OntoSage-docs/OntoSage-docs.github.io` mirror to copy this repository (see `.github/SYNC-README.md`) |
| `CNAME` | Custom domain for GitHub Pages |

### Documentation pages

The sidebar lists `_docs/` pages in order of their `date` front-matter value.

| Page | Permalink |
|---|---|
| Introduction | `/docs/introduction/` |
| Quick start | `/docs/quickstart/` |
| Architecture | `/docs/architecture/` |
| OCBV vocabulary | `/docs/ocbv-schema/` |
| Data sources | `/docs/data-sources/` |
| Admin console | `/docs/admin-console/` |
| Analytics and forecasting | `/docs/analytics-forecasting/` |
| Onboard a building | `/docs/onboarding-building/` |
| Stakeholder guide | `/docs/stakeholder-guide/` |
| Configuration | `/docs/configuration/` |
| Security & RBAC | `/docs/security-rbac/` |
| API reference | `/docs/api-reference/` |
| Full technical reference | `/docs/ontosage/` |
| How OntoSage answers | `/docs/how-it-answers/` |
| Answer lanes | `/docs/answer-lanes/` |
| Checks and honest answers | `/docs/checks-and-honesty/` |
| Conversation | `/docs/conversation/` |
| Write TTL for your building | `/docs/write-ttl/` |
| Edit TTL in a running system | `/docs/edit-ttl/` |
| Ontology browser | `/docs/ontology-browser/` |
| Ontology relationships | `/docs/ontology-relationships/` |
| How OntoSage extends Brick | `/docs/ontology-extensions/` |
| Use your own building | `/docs/your-own-building/` |

### Writing a page

Front matter:

```yaml
---
title: Page title
layout: post
category: docs
permalink: /docs/<slug>/
date: 2026-07-12      # sets the position in the sidebar
mermaid: true         # only when the page contains ```mermaid blocks
---
```

- Link to another page with `[text]({{ '/docs/<slug>/' | relative_url }})`.
- Images: `![alt]({{ '/assets/images/screenshots/<file>.png' | relative_url }})`.
- A code block that contains `{{` or `{%` must be wrapped in `{% raw %}` and `{% endraw %}`,
  or Liquid will try to evaluate it.
- Markdown is Kramdown with GFM input, so tables and fenced code blocks work as on GitHub.

The site is public. Do not publish secrets, passwords, tokens, internal IP addresses, personal
e-mail addresses or account names, including inside screenshots. Check every command, setting
and route against the OntoSage source before publishing it.

## Preview locally

With Docker (no local Ruby needed), from the repository root:

```bash
docker run --rm -v "${PWD}:/srv/jekyll" -p 4000:4000 jekyll/jekyll:4 jekyll serve
```

Then open <http://localhost:4000>. On Windows PowerShell the same command works as written; in
Git Bash use `-v "$(pwd -W):/srv/jekyll"`. If file changes are not picked up on a Windows or
macOS mount, add `--force_polling`.

The image installs the gems in the `Gemfile` before serving. `Gemfile.lock` was produced on
Windows; if Bundler refuses it on Linux, run once inside the container
`bundle lock --add-platform x86_64-linux`, or let it re-resolve by removing the lock file in
your working copy (do not commit that removal).

With Ruby installed instead:

```bash
bundle install
bundle exec jekyll serve      # http://localhost:4000
```

Locally, the layouts and includes in this repository are used; `remote_theme` is applied by
GitHub Pages when the site is published. The two should look the same; if they differ, the
published site is the reference.

## Regenerate the ontology pages

The class, property and vocabulary pages under `_ontology/`, and the blocks between
`<!-- BEGIN GENERATED: ... -->` and `<!-- END GENERATED: ... -->` in
`_docs/ontology-browser.md`, `_docs/ontology-extensions.md` and
`_docs/ontology-relationships.md`, are written by a script that reads an OntoSage checkout:

```bash
python _tools/gen_ontology_reference.py --source ../OntoSage
```

Options: `--building bldg1` chooses the building whose Turtle files are counted for relationship
usage, `--skip-building` leaves that block unchanged, and `--report FILE` lists every text the
publication filter changed. The script needs `rdflib` 7 and `PyYAML`. Only schema-level content
is published; building instance data (rooms, sensors, ids) is never written. Re-running over
unchanged sources changes nothing.

## Licence

OntoSage's licence is in its own repository. The OCBV vocabulary is released under CC-BY-4.0.
