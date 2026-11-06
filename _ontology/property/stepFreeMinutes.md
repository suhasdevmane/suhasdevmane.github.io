---
title: "ontosage:stepFreeMinutes"
layout: post
permalink: /ontology/property/stepFreeMinutes/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › stepFreeMinutes

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#stepFreeMinutes` |
| Label | step-free minutes |
| Kind | datatype property |
| Domain | [`ontosage:CirculationTime`]({{ '/ontology/class/CirculationTime/' | relative_url }}) |
| Range | `xsd:decimal` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The same journey using the lift, INCLUDING typical wait. Longer than the walking time on most floor pairs, which is the point: a step-free route is not the walking route with a lift substituted, and planning a transition on the walking figure sends a wheelchair user late.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`circulation_time`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#circulation_time) | `step_free_minutes` | `xsd:decimal` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:stepFreeMinutes a owl:DatatypeProperty ;
    rdfs:label "step-free minutes"@en ;
    rdfs:comment "The same journey using the lift, INCLUDING typical wait. Longer than the walking time on most floor pairs, which is the point: a step-free route is not the walking route with a lift substituted, and planning a transition on the walking figure sends a wheelchair user late."@en ;
    rdfs:domain ontosage:CirculationTime ;
    rdfs:range xsd:decimal .
```
{% endraw %}
