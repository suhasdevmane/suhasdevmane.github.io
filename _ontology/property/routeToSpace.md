---
title: "ontosage:routeToSpace"
layout: post
permalink: /ontology/property/routeToSpace/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › routeToSpace

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#routeToSpace` |
| Label | route to space |
| Kind | object property |
| Domain | not declared (any subject) |
| Range | [`brick:Location`](https://ontology.brickschema.org/1.4/#brick:Location) |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The space a route record ends at, where its ontosage:routeTo text names exactly one space of the building.

## Turtle

{% raw %}
```turtle
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ontosage:routeToSpace a owl:ObjectProperty ;
    rdfs:label "route to space"@en ;
    rdfs:comment "The space a route record ends at, where its ontosage:routeTo text names exactly one space of the building."@en ;
    rdfs:range brick:Location .
```
{% endraw %}
