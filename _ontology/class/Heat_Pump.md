---
title: "ontosage:Heat_Pump"
layout: post
permalink: /ontology/class/Heat_Pump/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › Heat\_Pump

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Heat_Pump` |
| Label | Heat pump |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Reversible heat-transfer plant. Brick 1.4 defines only the compound condensing-unit variants (Heat\_Pump\_Condensing\_Unit and its air/ground-source subclasses), none of which fit a whole-unit instance.

## Class hierarchy

Superclasses:

- [`brick:Equipment`](https://ontology.brickschema.org/1.4/#brick:Equipment) › **`ontosage:Heat_Pump`**

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

ontosage:Heat_Pump a owl:Class ;
    rdfs:label "Heat pump"@en ;
    rdfs:comment "Reversible heat-transfer plant. Brick 1.4 defines only the compound condensing-unit variants (Heat_Pump_Condensing_Unit and its air/ground-source subclasses), none of which fit a whole-unit instance."@en ;
    rdfs:subClassOf brick:Equipment .
```
{% endraw %}
