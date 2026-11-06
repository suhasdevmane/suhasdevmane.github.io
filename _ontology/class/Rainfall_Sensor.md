---
title: "ontosage:Rainfall_Sensor"
layout: post
permalink: /ontology/class/Rainfall_Sensor/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › Rainfall\_Sensor

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Rainfall_Sensor` |
| Label | Rainfall sensor |
| Defined in | [`ontology/measurand_kinds.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/measurand_kinds.ttl), [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Measures precipitation depth over an interval, normally in millimetres. Declared by OntoSage because the pinned Brick version defines no precipitation class; relevant to green-roof retention and rainwater harvesting questions.

## Examples

- "how much rain fell on the roof this week?"

## Class hierarchy

Superclasses:

- [`brick:Sensor`](https://ontology.brickschema.org/1.4/#brick:Sensor) › **`ontosage:Rainfall_Sensor`**

Subclasses: none.

## Properties

No property declares this class (or a superclass) as its domain.

## Measured quantity

`ontosage:measuresQuantityKind` [`ontosage:Rainfall`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#Rainfall)

## Turtle

{% raw %}
```turtle
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:Rainfall_Sensor a owl:Class ;
    rdfs:label "Rainfall sensor"@en ;
    ontosage:measuresQuantityKind ontosage:Rainfall ;
    rdfs:comment "Measures precipitation depth over an interval, normally in millimetres. Declared by OntoSage because the pinned Brick version defines no precipitation class; relevant to green-roof retention and rainwater harvesting questions."@en ;
    rdfs:subClassOf brick:Sensor ;
    skos:example "\"how much rain fell on the roof this week?\"" .
```
{% endraw %}
