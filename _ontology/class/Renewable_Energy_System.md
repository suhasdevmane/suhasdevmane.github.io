---
title: "ontosage:Renewable_Energy_System"
layout: post
permalink: /ontology/class/Renewable_Energy_System/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › Renewable\_Energy\_System

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Renewable_Energy_System` |
| Label | Renewable energy system |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

On-site generation such as photovoltaic or solar-thermal, modelled as a system rather than a single equipment item because it spans arrays, inverters and metering.

## Class hierarchy

Superclasses:

- [`brick:System`](https://ontology.brickschema.org/1.4/#brick:System) › **`ontosage:Renewable_Energy_System`**

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

ontosage:Renewable_Energy_System a owl:Class ;
    rdfs:label "Renewable energy system"@en ;
    rdfs:comment "On-site generation such as photovoltaic or solar-thermal, modelled as a system rather than a single equipment item because it spans arrays, inverters and metering."@en ;
    rdfs:subClassOf brick:System .
```
{% endraw %}
