---
title: "ontosage:configLocation"
layout: post
permalink: /ontology/property/configLocation/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › configLocation

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#configLocation` |
| Label | configuration location |
| Kind | object property |
| Domain | [`ontosage:ConfigurationPeriod`]({{ '/ontology/class/ConfigurationPeriod/' | relative_url }}) |
| Range | [`brick:Location`](https://ontology.brickschema.org/1.4/#brick:Location) |
| Inverse | none declared |
| Sub-property of | [`ontosage:periodLocation`]({{ '/ontology/property/periodLocation/' | relative_url }}) |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Where the point was during this configuration period. The name building data and the evidence history query use; a sub-property of ontosage:periodLocation.

## Turtle

{% raw %}
```turtle
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ontosage:configLocation a owl:ObjectProperty ;
    rdfs:label "configuration location"@en ;
    rdfs:comment "Where the point was during this configuration period. The name building data and the evidence history query use; a sub-property of ontosage:periodLocation."@en ;
    rdfs:domain ontosage:ConfigurationPeriod ;
    rdfs:range brick:Location ;
    rdfs:subPropertyOf ontosage:periodLocation .
```
{% endraw %}
