---
title: "ontosage:Emergency_Generator"
layout: post
permalink: /ontology/class/Emergency_Generator/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › Emergency\_Generator

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Emergency_Generator` |
| Label | Emergency generator |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Standby generation plant serving life-safety and critical loads during a supply failure. Brick 1.4 defines Emergency\_Generator\_Alarm and \_Status points but no equipment class to hang them on.

## Class hierarchy

Superclasses:

- [`brick:Equipment`](https://ontology.brickschema.org/1.4/#brick:Equipment) › **`ontosage:Emergency_Generator`**

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

ontosage:Emergency_Generator a owl:Class ;
    rdfs:label "Emergency generator"@en ;
    rdfs:comment "Standby generation plant serving life-safety and critical loads during a supply failure. Brick 1.4 defines Emergency_Generator_Alarm and _Status points but no equipment class to hang them on."@en ;
    rdfs:subClassOf brick:Equipment .
```
{% endraw %}
