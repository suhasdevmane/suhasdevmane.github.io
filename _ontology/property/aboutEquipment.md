---
title: "ontosage:aboutEquipment"
layout: post
permalink: /ontology/property/aboutEquipment/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › aboutEquipment

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#aboutEquipment` |
| Label | about equipment |
| Kind | object property |
| Domain | [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}) or [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) or [`ontosage:Record`]({{ '/ontology/class/Record/' | relative_url }}) |
| Range | [`brick:Equipment`](https://ontology.brickschema.org/1.4/#brick:Equipment) |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Links a maintenance issue, capability, interval record or standing record to the Brick equipment it concerns, so a fault report or an alarm can be tied to the real asset.

## Examples

- `bldg:Issue_BrokenLift ontosage:aboutEquipment bldg:Lift_1 .`

## Turtle

{% raw %}
```turtle
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:aboutEquipment a owl:ObjectProperty ;
    rdfs:label "about equipment"@en ;
    rdfs:comment "Links a maintenance issue, capability, interval record or standing record to the Brick equipment it concerns, so a fault report or an alarm can be tied to the real asset."@en ;
    rdfs:domain [ a owl:Class ;
            owl:unionOf ( ontosage:Capability ontosage:IntervalRecord ontosage:Record ) ] ;
    rdfs:range brick:Equipment ;
    skos:example "bldg:Issue_BrokenLift ontosage:aboutEquipment bldg:Lift_1 ." .
```
{% endraw %}
