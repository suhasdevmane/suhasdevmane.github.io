---
title: "ontosage:servesAreaSpace"
layout: post
permalink: /ontology/property/servesAreaSpace/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › servesAreaSpace

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#servesAreaSpace` |
| Label | serves area space |
| Kind | object property |
| Domain | not declared (any subject) |
| Range | [`brick:Location`](https://ontology.brickschema.org/1.4/#brick:Location) |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The space an asset serves, where its ontosage:servesArea text names exactly one space. A served area described as several spaces or a whole floor has no link: picking one of them would claim a service relation nobody recorded.

## Turtle

{% raw %}
```turtle
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ontosage:servesAreaSpace a owl:ObjectProperty ;
    rdfs:label "serves area space"@en ;
    rdfs:comment "The space an asset serves, where its ontosage:servesArea text names exactly one space. A served area described as several spaces or a whole floor has no link: picking one of them would claim a service relation nobody recorded."@en ;
    rdfs:range brick:Location .
```
{% endraw %}
