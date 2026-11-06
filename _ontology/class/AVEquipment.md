---
title: "ontosage:AVEquipment"
layout: post
permalink: /ontology/class/AVEquipment/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › AVEquipment

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#AVEquipment` |
| Label | AV / teaching equipment |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Projector, display, lecture-capture, microphone or hybrid-conferencing rig serving a space. 94 of the supervisors' questions depend on knowing whether the teaching kit in a room works BEFORE the class starts.

## Class hierarchy

Superclasses:

- [`brick:Equipment`](https://ontology.brickschema.org/1.4/#brick:Equipment) › **`ontosage:AVEquipment`**

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

ontosage:AVEquipment a owl:Class ;
    rdfs:label "AV / teaching equipment"@en ;
    rdfs:comment "Projector, display, lecture-capture, microphone or hybrid-conferencing rig serving a space. 94 of the supervisors' questions depend on knowing whether the teaching kit in a room works BEFORE the class starts."@en ;
    rdfs:subClassOf brick:Equipment .
```
{% endraw %}
