---
title: "ontosage:busiestPeriod"
layout: post
permalink: /ontology/property/busiestPeriod/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › busiestPeriod

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#busiestPeriod` |
| Label | busiest period |
| Kind | datatype property |
| Domain | [`ontosage:WorkspaceProfile`]({{ '/ontology/class/WorkspaceProfile/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

When this space is typically hardest to get a seat in. A TYPICAL PATTERN, not a live occupancy reading — 'when should I arrive?' is a question about the pattern, and answering it from the current count would be wrong tomorrow.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`workspace_profile`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#workspace_profile) | `busiest` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:busiestPeriod a owl:DatatypeProperty ;
    rdfs:label "busiest period"@en ;
    rdfs:comment "When this space is typically hardest to get a seat in. A TYPICAL PATTERN, not a live occupancy reading — 'when should I arrive?' is a question about the pattern, and answering it from the current count would be wrong tomorrow."@en ;
    rdfs:domain ontosage:WorkspaceProfile ;
    rdfs:range xsd:string .
```
{% endraw %}
