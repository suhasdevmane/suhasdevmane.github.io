---
title: "ontosage:servesSpace"
layout: post
permalink: /ontology/property/servesSpace/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › servesSpace

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#servesSpace` |
| Label | serves space |
| Kind | object property |
| Domain | [`ontosage:ServedZone`]({{ '/ontology/class/ServedZone/' | relative_url }}) |
| Range | [`brick:Location`](https://ontology.brickschema.org/1.4/#brick:Location) |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A space this zone genuinely represents. Asserted from the mechanical design or a commissioning survey — never derived from adjacency, floor membership or distance.

## Turtle

{% raw %}
```turtle
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ontosage:servesSpace a owl:ObjectProperty ;
    rdfs:label "serves space"@en ;
    rdfs:comment "A space this zone genuinely represents. Asserted from the mechanical design or a commissioning survey — never derived from adjacency, floor membership or distance."@en ;
    rdfs:domain ontosage:ServedZone ;
    rdfs:range brick:Location .
```
{% endraw %}
