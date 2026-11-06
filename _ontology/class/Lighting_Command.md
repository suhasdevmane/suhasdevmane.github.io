---
title: "ontosage:Lighting_Command"
layout: post
permalink: /ontology/class/Lighting_Command/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › Lighting\_Command

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Lighting_Command` |
| Label | Lighting command |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A writable point controlling luminaire state or level.

## Class hierarchy

Superclasses:

- [`brick:Command`](https://ontology.brickschema.org/1.4/#brick:Command) › **`ontosage:Lighting_Command`**

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

ontosage:Lighting_Command a owl:Class ;
    rdfs:label "Lighting command"@en ;
    rdfs:comment "A writable point controlling luminaire state or level."@en ;
    rdfs:subClassOf brick:Command .
```
{% endraw %}
