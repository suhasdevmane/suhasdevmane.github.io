---
title: "ontosage:Parking_Occupancy_Sensor"
layout: post
permalink: /ontology/class/Parking_Occupancy_Sensor/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › Parking\_Occupancy\_Sensor

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Parking_Occupancy_Sensor` |
| Label | Parking bay occupancy / availability sensor |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A count of parking bays that are free or occupied. Brick has no class for this: brick:Occupancy\_Count\_Sensor is the nearest, and it also covers entrance footfall counters and room people-counters. On the building this was developed against that one class held 257 sensors of which exactly ONE was parking, so a parking question resolved to a class it shared with 256 other things and no answer could be given — the system knew the bay count and could not reach it. Declaring the specific class is the TTL-first fix: the CLASS becomes the discriminator, so nothing downstream needs a label filter, and subclassing the Brick parent means every existing query that asks for Occupancy\_Count\_Sensor still finds it.

## Examples

- "how many parking spaces are free?"

## Class hierarchy

Superclasses:

- [`brick:Occupancy_Count_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Count_Sensor) › **`ontosage:Parking_Occupancy_Sensor`**

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

ontosage:Parking_Occupancy_Sensor a owl:Class ;
    rdfs:label "Parking bay occupancy / availability sensor"@en ;
    rdfs:comment "A count of parking bays that are free or occupied. Brick has no class for this: brick:Occupancy_Count_Sensor is the nearest, and it also covers entrance footfall counters and room people-counters. On the building this was developed against that one class held 257 sensors of which exactly ONE was parking, so a parking question resolved to a class it shared with 256 other things and no answer could be given — the system knew the bay count and could not reach it. Declaring the specific class is the TTL-first fix: the CLASS becomes the discriminator, so nothing downstream needs a label filter, and subclassing the Brick parent means every existing query that asks for Occupancy_Count_Sensor still finds it."@en ;
    rdfs:subClassOf brick:Occupancy_Count_Sensor ;
    skos:example "\"how many parking spaces are free?\"" .
```
{% endraw %}
