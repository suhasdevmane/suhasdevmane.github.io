---
title: "ontosage:walkingMinutes"
layout: post
permalink: /ontology/property/walkingMinutes/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › walkingMinutes

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#walkingMinutes` |
| Label | walking minutes |
| Kind | datatype property |
| Domain | [`ontosage:CirculationTime`]({{ '/ontology/class/CirculationTime/' | relative_url }}) |
| Range | `xsd:decimal` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Typical time by stairs at an unhurried pace, between the usual teaching spaces on each floor.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`circulation_time`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#circulation_time) | `walking_minutes` | `xsd:decimal` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:walkingMinutes a owl:DatatypeProperty ;
    rdfs:label "walking minutes"@en ;
    rdfs:comment "Typical time by stairs at an unhurried pace, between the usual teaching spaces on each floor."@en ;
    rdfs:domain ontosage:CirculationTime ;
    rdfs:range xsd:decimal .
```
{% endraw %}
