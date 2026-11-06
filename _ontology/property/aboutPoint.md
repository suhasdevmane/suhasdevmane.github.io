---
title: "ontosage:aboutPoint"
layout: post
permalink: /ontology/property/aboutPoint/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › aboutPoint

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#aboutPoint` |
| Label | about point |
| Kind | object property |
| Domain | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| Range | [`brick:Point`](https://ontology.brickschema.org/1.4/#brick:Point) |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

AnomalyEvent: the sensor concerned.

## Turtle

{% raw %}
```turtle
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ontosage:aboutPoint a owl:ObjectProperty ;
    rdfs:label "about point"@en ;
    rdfs:comment "AnomalyEvent: the sensor concerned."@en ;
    rdfs:domain ontosage:IntervalRecord ;
    rdfs:range brick:Point .
```
{% endraw %}
