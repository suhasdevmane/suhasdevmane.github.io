---
title: "ontosage:configurationOf"
layout: post
permalink: /ontology/property/configurationOf/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › configurationOf

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#configurationOf` |
| Label | configuration of |
| Kind | object property |
| Domain | [`ontosage:ConfigurationPeriod`]({{ '/ontology/class/ConfigurationPeriod/' | relative_url }}) |
| Range | [`brick:Point`](https://ontology.brickschema.org/1.4/#brick:Point) |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The point a configuration period describes. The direction building data uses (period to point); ontosage:hasConfigurationPeriod states the same link from the point.

## Turtle

{% raw %}
```turtle
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ontosage:configurationOf a owl:ObjectProperty ;
    rdfs:label "configuration of"@en ;
    rdfs:comment "The point a configuration period describes. The direction building data uses (period to point); ontosage:hasConfigurationPeriod states the same link from the point."@en ;
    rdfs:domain ontosage:ConfigurationPeriod ;
    rdfs:range brick:Point .
```
{% endraw %}
