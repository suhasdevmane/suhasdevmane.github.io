# rdf-toolkit, pinned, for building the ontology explorer (explorer/ on the site).
#
# The fork is the one ontology.brickschema.org builds with: it adds search and tree
# expansion to ektrah/rdf-toolkit (MIT). Pinned to a commit so a rebuild is repeatable.
#
#   docker build -t ontosage-rdf-toolkit _tools/explorer
#
# gen_ontology_explorer.py runs it; see that script for the full build.

FROM node:22-bookworm-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends git ca-certificates \
    && rm -rf /var/lib/apt/lists/*

ARG RDF_TOOLKIT_REPO=https://github.com/KrishnanN27/rdf-toolkit.git
ARG RDF_TOOLKIT_COMMIT=4a9cce8a27e25f05c07b24aa78d5cdca7f282de1

RUN git clone "$RDF_TOOLKIT_REPO" /opt/rdf-toolkit \
    && cd /opt/rdf-toolkit \
    && git checkout --quiet "$RDF_TOOLKIT_COMMIT" \
    && npm ci --no-audit --no-fund \
    && npm run build

ENTRYPOINT ["node", "/opt/rdf-toolkit/packages/cli/dist/main.js"]
