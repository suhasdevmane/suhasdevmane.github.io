---
title: "ontosage:routeFromSpace"
layout: post
permalink: /ontology/property/routeFromSpace/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › routeFromSpace

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#routeFromSpace` |
| Label | route from space |
| Kind | object property |
| Domain | not declared (any subject) |
| Range | [`brick:Location`](https://ontology.brickschema.org/1.4/#brick:Location) |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The space a route record starts from, where its ontosage:routeFrom text names exactly one space of the building. A starting point outside the building has no link.

## Turtle

{% raw %}
```turtle
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ontosage:routeFromSpace a owl:ObjectProperty ;
    rdfs:label "route from space"@en ;
    rdfs:comment "The space a route record starts from, where its ontosage:routeFrom text names exactly one space of the building. A starting point outside the building has no link."@en ;
    rdfs:range brick:Location .
```
{% endraw %}
