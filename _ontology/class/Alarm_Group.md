---
title: "ontosage:Alarm_Group"
layout: post
permalink: /ontology/class/Alarm_Group/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › Alarm\_Group

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Alarm_Group` |
| Label | Alarm group |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A named set of alarms handled together. Deliberately a brick:Collection and NOT a brick:Alarm: a group of alarms is not itself an alarm, and typing it as one would let it match queries asking for active alarms.

## Class hierarchy

Superclasses:

- [`brick:Collection`](https://ontology.brickschema.org/1.4/#brick:Collection) › **`ontosage:Alarm_Group`**

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

ontosage:Alarm_Group a owl:Class ;
    rdfs:label "Alarm group"@en ;
    rdfs:comment "A named set of alarms handled together. Deliberately a brick:Collection and NOT a brick:Alarm: a group of alarms is not itself an alarm, and typing it as one would let it match queries asking for active alarms."@en ;
    rdfs:subClassOf brick:Collection .
```
{% endraw %}
