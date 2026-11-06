---
title: "ontosage:Waste_Fill_Sensor"
layout: post
permalink: /ontology/class/Waste_Fill_Sensor/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › Waste\_Fill\_Sensor

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Waste_Fill_Sensor` |
| Label | Waste fill-level sensor |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Reports how full a waste or recycling receptacle is, as a percentage of its capacity.

## Class hierarchy

Superclasses:

- [`brick:Sensor`](https://ontology.brickschema.org/1.4/#brick:Sensor) › **`ontosage:Waste_Fill_Sensor`**

Subclasses: none.

## Properties

No property declares this class (or a superclass) as its domain.

## Turtle

{% raw %}
```turtle
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ontosage:Waste_Fill_Sensor a owl:Class ;
    rdfs:label "Waste fill-level sensor"@en ;
    rdfs:comment "Reports how full a waste or recycling receptacle is, as a percentage of its capacity."@en ;
    rdfs:subClassOf brick:Sensor .
```
{% endraw %}
