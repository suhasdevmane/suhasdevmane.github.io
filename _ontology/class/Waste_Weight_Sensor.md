---
title: "ontosage:Waste_Weight_Sensor"
layout: post
permalink: /ontology/class/Waste_Weight_Sensor/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › Waste\_Weight\_Sensor

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Waste_Weight_Sensor` |
| Label | Waste weight sensor |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Reports the mass of waste in a receptacle or collected from a stream.

## Class hierarchy

Superclasses:

- [`brick:Sensor`](https://ontology.brickschema.org/1.4/#brick:Sensor) › **`ontosage:Waste_Weight_Sensor`**

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

ontosage:Waste_Weight_Sensor a owl:Class ;
    rdfs:label "Waste weight sensor"@en ;
    rdfs:comment "Reports the mass of waste in a receptacle or collected from a stream."@en ;
    rdfs:subClassOf brick:Sensor .
```
{% endraw %}
