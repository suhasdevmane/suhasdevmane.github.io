---
title: "ontosage:Noise_Level_Sensor"
layout: post
permalink: /ontology/class/Noise_Level_Sensor/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › Noise\_Level\_Sensor

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Noise_Level_Sensor` |
| Label | Noise level sensor |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Alias kept for graphs that label the same measurement 'noise' rather than 'sound level'.

## Class hierarchy

Superclasses:

- [`brick:Sensor`](https://ontology.brickschema.org/1.4/#brick:Sensor) › [`ontosage:Sound_Level_Sensor`]({{ '/ontology/class/Sound_Level_Sensor/' | relative_url }}) › **`ontosage:Noise_Level_Sensor`**

Subclasses: none.

## Properties

No property declares this class (or a superclass) as its domain.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ontosage:Noise_Level_Sensor a owl:Class ;
    rdfs:label "Noise level sensor"@en ;
    rdfs:comment "Alias kept for graphs that label the same measurement 'noise' rather than 'sound level'."@en ;
    rdfs:subClassOf ontosage:Sound_Level_Sensor .
```
{% endraw %}
