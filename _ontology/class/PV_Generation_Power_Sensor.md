---
title: "ontosage:PV_Generation_Power_Sensor"
layout: post
permalink: /ontology/class/PV_Generation_Power_Sensor/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › PV\_Generation\_Power\_Sensor

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#PV_Generation_Power_Sensor` |
| Label | PV generation power sensor |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Measures the electrical power a photovoltaic array or inverter is generating, normally in kW. Declared by OntoSage because the pinned Brick version has PV equipment (PV\_Panel, PV\_Array, Photovoltaic\_Inverter) but no generation-power point class, so a question about solar output could only resolve to every power sensor in the building -- and was answered with the floor energy meters.

## Examples

- "how much power are the solar panels generating right now?"

## Class hierarchy

Superclasses:

- [`brick:Active_Power_Sensor`](https://ontology.brickschema.org/1.4/#brick:Active_Power_Sensor) › **`ontosage:PV_Generation_Power_Sensor`**

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
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:PV_Generation_Power_Sensor a owl:Class ;
    rdfs:label "PV generation power sensor"@en ;
    rdfs:comment "Measures the electrical power a photovoltaic array or inverter is generating, normally in kW. Declared by OntoSage because the pinned Brick version has PV equipment (PV_Panel, PV_Array, Photovoltaic_Inverter) but no generation-power point class, so a question about solar output could only resolve to every power sensor in the building -- and was answered with the floor energy meters."@en ;
    rdfs:subClassOf brick:Active_Power_Sensor ;
    skos:example "\"how much power are the solar panels generating right now?\"" .
```
{% endraw %}
