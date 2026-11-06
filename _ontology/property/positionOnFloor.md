---
title: "ontosage:positionOnFloor"
layout: post
permalink: /ontology/property/positionOnFloor/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › positionOnFloor

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#positionOnFloor` |
| Label | position on floor |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Where on the floor it is, in the words the survey used ('north end', 'by the east stair'), for provision recorded by position rather than by room number. Never invent a room number to fill this: a wrong room is worse than an approximate direction.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:positionOnFloor a owl:DatatypeProperty ;
    rdfs:label "position on floor"@en ;
    rdfs:comment "Where on the floor it is, in the words the survey used ('north end', 'by the east stair'), for provision recorded by position rather than by room number. Never invent a room number to fill this: a wrong room is worse than an approximate direction."@en ;
    rdfs:range xsd:string .
```
{% endraw %}
