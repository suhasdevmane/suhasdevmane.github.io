---
title: "Answer source types"
layout: post
permalink: /ontology/vocabulary/source-types/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Vocabularies]({{ '/docs/ontology-browser/' | relative_url }}#vocabularies) › Answer source types

The kinds of system an answer can be grounded in. Members are instances of [`ontosage:SourceType`]({{ '/ontology/class/SourceType/' | relative_url }}). The schema declares 8.

| Member | Label |
|---|---|
| [`ontosage:Src_Analytics`](#Src_Analytics) | Analytics / forecast engine |
| [`ontosage:Src_CapabilityKB`](#Src_CapabilityKB) | Capability / document KB (deprecated) |
| [`ontosage:Src_Document`](#Src_Document) | Uploaded document |
| [`ontosage:Src_FloorPlan`](#Src_FloorPlan) | Floor plan (PDF/DWG) |
| [`ontosage:Src_GraphDB`](#Src_GraphDB) | Knowledge graph (SPARQL/GraphDB) |
| [`ontosage:Src_Ontology`](#Src_Ontology) | Building ontology (triples) |
| [`ontosage:Src_ReportIntake`](#Src_ReportIntake) | Report intake |
| [`ontosage:Src_TimeSeriesDB`](#Src_TimeSeriesDB) | Time-series database |

## Analytics / forecast engine {#Src_Analytics}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Src_Analytics` |

Computed results — aggregates, anomalies, forecasts — over sensor data.

## Capability / document KB (deprecated) {#Src_CapabilityKB}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Src_CapabilityKB` |
| Status | deprecated |

DEPRECATED — superseded by ontosage:Src\_Ontology and ontosage:Src\_Document, which distinguish an asserted fact from retrieved prose. Kept so historical provenance records still resolve.

## Uploaded document {#Src_Document}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Src_Document` |

Prose retrieved from an uploaded manual or policy document. When the topic names its document via ontosage:documentRef the retrieval is scoped to that document; otherwise it was chosen by similarity alone and is weaker evidence.

## Floor plan (PDF/DWG) {#Src_FloorPlan}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Src_FloorPlan` |

Spatial geometry answers from floor-plan manifests (areas, adjacency, block locations).

## Knowledge graph (SPARQL/GraphDB) {#Src_GraphDB}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Src_GraphDB` |

Structural/metadata facts answered by SPARQL over the Brick + OCBV graph.

## Building ontology (triples) {#Src_Ontology}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Src_Ontology` |

Amenity / knowledge-topic / policy facts asserted as triples in the building's own TTL (Module A). Authored and auditable — the answer is what the building states.

## Report intake {#Src_ReportIntake}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Src_ReportIntake` |

The report-filing path (Module E) — used when the utterance states a problem.

## Time-series database {#Src_TimeSeriesDB}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Src_TimeSeriesDB` |

Live sensor readings fetched by UUID from the registered time-series store.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:Src_Analytics a ontosage:SourceType ;
    rdfs:label "Analytics / forecast engine"@en ;
    rdfs:comment "Computed results — aggregates, anomalies, forecasts — over sensor data."@en .

ontosage:Src_CapabilityKB a ontosage:SourceType ;
    rdfs:label "Capability / document KB (deprecated)"@en ;
    rdfs:comment "DEPRECATED — superseded by ontosage:Src_Ontology and ontosage:Src_Document, which distinguish an asserted fact from retrieved prose. Kept so historical provenance records still resolve."@en ;
    owl:deprecated true .

ontosage:Src_Document a ontosage:SourceType ;
    rdfs:label "Uploaded document"@en ;
    rdfs:comment "Prose retrieved from an uploaded manual or policy document. When the topic names its document via ontosage:documentRef the retrieval is scoped to that document; otherwise it was chosen by similarity alone and is weaker evidence."@en .

ontosage:Src_FloorPlan a ontosage:SourceType ;
    rdfs:label "Floor plan (PDF/DWG)"@en ;
    rdfs:comment "Spatial geometry answers from floor-plan manifests (areas, adjacency, block locations)."@en .

ontosage:Src_GraphDB a ontosage:SourceType ;
    rdfs:label "Knowledge graph (SPARQL/GraphDB)"@en ;
    rdfs:comment "Structural/metadata facts answered by SPARQL over the Brick + OCBV graph."@en .

ontosage:Src_Ontology a ontosage:SourceType ;
    rdfs:label "Building ontology (triples)"@en ;
    rdfs:comment "Amenity / knowledge-topic / policy facts asserted as triples in the building's own TTL (Module A). Authored and auditable — the answer is what the building states."@en .

ontosage:Src_ReportIntake a ontosage:SourceType ;
    rdfs:label "Report intake"@en ;
    rdfs:comment "The report-filing path (Module E) — used when the utterance states a problem."@en .

ontosage:Src_TimeSeriesDB a ontosage:SourceType ;
    rdfs:label "Time-series database"@en ;
    rdfs:comment "Live sensor readings fetched by UUID from the registered time-series store."@en .
```
{% endraw %}
