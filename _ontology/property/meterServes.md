---
title: "ontosage:meterServes"
layout: post
permalink: /ontology/property/meterServes/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › meterServes

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#meterServes` |
| Label | meter serves |
| Kind | object property |
| Domain | not declared (any subject) |
| Range | not declared |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

What a meter's reading covers: the building, a floor or a system. An energy answer states this boundary, so a floor sub-meter is never read as the whole building's consumption.

## Examples

- `bldg:Building_Electrical_Meter ontosage:meterServes bldg:Building .`

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:meterServes a owl:ObjectProperty ;
    rdfs:label "meter serves"@en ;
    rdfs:comment "What a meter's reading covers: the building, a floor or a system. An energy answer states this boundary, so a floor sub-meter is never read as the whole building's consumption."@en ;
    skos:example "bldg:Building_Electrical_Meter ontosage:meterServes bldg:Building ." .
```
{% endraw %}
