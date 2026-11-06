---
title: "ontosage:quietestPeriod"
layout: post
permalink: /ontology/property/quietestPeriod/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › quietestPeriod

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#quietestPeriod` |
| Label | quietest period |
| Kind | datatype property |
| Domain | [`ontosage:WorkspaceProfile`]({{ '/ontology/class/WorkspaceProfile/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

When a seat is typically easiest to find here.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`workspace_profile`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#workspace_profile) | `quietest` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:quietestPeriod a owl:DatatypeProperty ;
    rdfs:label "quietest period"@en ;
    rdfs:comment "When a seat is typically easiest to find here."@en ;
    rdfs:domain ontosage:WorkspaceProfile ;
    rdfs:range xsd:string .
```
{% endraw %}
