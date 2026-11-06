---
title: "ontosage:aboutSpace"
layout: post
permalink: /ontology/property/aboutSpace/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › aboutSpace

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#aboutSpace` |
| Label | about space |
| Kind | object property |
| Domain | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| Range | [`brick:Location`](https://ontology.brickschema.org/1.4/#brick:Location) |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The room/zone the record concerns.

## Turtle

{% raw %}
```turtle
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ontosage:aboutSpace a owl:ObjectProperty ;
    rdfs:label "about space"@en ;
    rdfs:comment "The room/zone the record concerns."@en ;
    rdfs:domain ontosage:IntervalRecord ;
    rdfs:range brick:Location .
```
{% endraw %}
