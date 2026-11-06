---
title: "ontosage:onFloorEntity"
layout: post
permalink: /ontology/property/onFloorEntity/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › onFloorEntity

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#onFloorEntity` |
| Label | on floor (entity) |
| Kind | object property |
| Domain | not declared (any subject) |
| Range | [`brick:Location`](https://ontology.brickschema.org/1.4/#brick:Location) |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The floor a record's floor text names, resolved by the floor's declared level number or, failing that, the number in the floor's own name or its exact label. Points only at a brick:Floor. Also written when a location text names a whole floor and nothing else, so a query for the space a record is in never returns a floor.

## Examples

- ?record ontosage:onFloorEntity ?floor . ?space brick:isPartOf ?floor .

## Turtle

{% raw %}
```turtle
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:onFloorEntity a owl:ObjectProperty ;
    rdfs:label "on floor (entity)"@en ;
    rdfs:comment "The floor a record's floor text names, resolved by the floor's declared level number or, failing that, the number in the floor's own name or its exact label. Points only at a brick:Floor. Also written when a location text names a whole floor and nothing else, so a query for the space a record is in never returns a floor."@en ;
    rdfs:range brick:Location ;
    skos:example "?record ontosage:onFloorEntity ?floor . ?space brick:isPartOf ?floor ." .
```
{% endraw %}
