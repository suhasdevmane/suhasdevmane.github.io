---
title: "ontosage:expectedMinutes"
layout: post
permalink: /ontology/property/expectedMinutes/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › expectedMinutes

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#expectedMinutes` |
| Label | expected minutes |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:integer` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Planned duration, so a shift's workload can be summed against the hours available.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`cleaning_task`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#cleaning_task) | `minutes` | `xsd:integer` |
| [`event_activity`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#event_activity) | `minutes` | `xsd:integer` |
| [`patrol_checkpoint`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#patrol_checkpoint) | `walk_minutes` | `xsd:integer` |
| [`timetabled_session`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#timetabled_session) | `duration_minutes` | `xsd:integer` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:expectedMinutes a owl:DatatypeProperty ;
    rdfs:label "expected minutes"@en ;
    rdfs:comment "Planned duration, so a shift's workload can be summed against the hours available."@en ;
    rdfs:range xsd:integer .
```
{% endraw %}
