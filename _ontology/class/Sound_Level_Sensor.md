---
title: "ontosage:Sound_Level_Sensor"
layout: post
permalink: /ontology/class/Sound_Level_Sensor/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › Sound\_Level\_Sensor

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Sound_Level_Sensor` |
| Label | Sound level sensor |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Measures ambient sound pressure level, normally reported in dB(A). Declared by OntoSage because the pinned Brick version defines no acoustic sensor class; the WHO indoor guideline band 30-70 dB(A) anchors its comfort scoring.

## Examples

- "which room is quietest right now?"

## Class hierarchy

Superclasses:

- [`brick:Sensor`](https://ontology.brickschema.org/1.4/#brick:Sensor) › **`ontosage:Sound_Level_Sensor`**

Direct subclasses (1; 1 descendants in all):

- [`ontosage:Noise_Level_Sensor`]({{ '/ontology/class/Noise_Level_Sensor/' | relative_url }}) Noise level sensor

## Properties

No property declares this class (or a superclass) as its domain.

## Turtle

{% raw %}
```turtle
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:Sound_Level_Sensor a owl:Class ;
    rdfs:label "Sound level sensor"@en ;
    rdfs:comment "Measures ambient sound pressure level, normally reported in dB(A). Declared by OntoSage because the pinned Brick version defines no acoustic sensor class; the WHO indoor guideline band 30-70 dB(A) anchors its comfort scoring."@en ;
    rdfs:subClassOf brick:Sensor ;
    skos:example "\"which room is quietest right now?\"" .
```
{% endraw %}
