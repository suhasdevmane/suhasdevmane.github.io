---
title: "ontosage:servedByPoint"
layout: post
permalink: /ontology/property/servedByPoint/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › servedByPoint

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#servedByPoint` |
| Label | served by point |
| Kind | object property |
| Domain | [`ontosage:ServedZone`]({{ '/ontology/class/ServedZone/' | relative_url }}) |
| Range | [`brick:Point`](https://ontology.brickschema.org/1.4/#brick:Point) |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The point whose readings represent this zone. Usually located in one of the served spaces, but it may sit in a duct or plenum — which is why ontosage:environmentalBoundary exists alongside containment.

## Turtle

{% raw %}
```turtle
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ontosage:servedByPoint a owl:ObjectProperty ;
    rdfs:label "served by point"@en ;
    rdfs:comment "The point whose readings represent this zone. Usually located in one of the served spaces, but it may sit in a duct or plenum — which is why ontosage:environmentalBoundary exists alongside containment."@en ;
    rdfs:domain ontosage:ServedZone ;
    rdfs:range brick:Point .
```
{% endraw %}
