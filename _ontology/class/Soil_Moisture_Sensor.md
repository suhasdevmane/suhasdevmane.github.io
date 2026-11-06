---
title: "ontosage:Soil_Moisture_Sensor"
layout: post
permalink: /ontology/class/Soil_Moisture_Sensor/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › Soil\_Moisture\_Sensor

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Soil_Moisture_Sensor` |
| Label | Soil moisture sensor |
| Defined in | [`ontology/measurand_kinds.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/measurand_kinds.ttl), [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Measures volumetric water content of a growing medium, reported as a percentage. Declared by OntoSage because the pinned Brick version defines no soil or substrate moisture class; distinct from Relative\_Humidity\_Sensor, which measures air.

## Examples

- "does the green roof need watering?"

## Class hierarchy

Superclasses:

- [`brick:Sensor`](https://ontology.brickschema.org/1.4/#brick:Sensor) › **`ontosage:Soil_Moisture_Sensor`**

Subclasses: none.

## Properties

No property declares this class (or a superclass) as its domain.

## Measured quantity

`ontosage:measuresQuantityKind` [`ontosage:SoilMoisture`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#SoilMoisture)

## Turtle

{% raw %}
```turtle
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:Soil_Moisture_Sensor a owl:Class ;
    rdfs:label "Soil moisture sensor"@en ;
    ontosage:measuresQuantityKind ontosage:SoilMoisture ;
    rdfs:comment "Measures volumetric water content of a growing medium, reported as a percentage. Declared by OntoSage because the pinned Brick version defines no soil or substrate moisture class; distinct from Relative_Humidity_Sensor, which measures air."@en ;
    rdfs:subClassOf brick:Sensor ;
    skos:example "\"does the green roof need watering?\"" .
```
{% endraw %}
