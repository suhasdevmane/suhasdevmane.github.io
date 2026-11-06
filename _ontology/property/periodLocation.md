---
title: "ontosage:periodLocation"
layout: post
permalink: /ontology/property/periodLocation/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › periodLocation

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#periodLocation` |
| Label | location during period |
| Kind | object property |
| Domain | [`ontosage:ConfigurationPeriod`]({{ '/ontology/class/ConfigurationPeriod/' | relative_url }}) |
| Range | [`brick:Location`](https://ontology.brickschema.org/1.4/#brick:Location) |
| Inverse | none declared |
| Sub-property of | none |
| Sub-properties | [`ontosage:configLocation`]({{ '/ontology/property/configLocation/' | relative_url }}) |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Where the point was during this period. This is what an as-of query resolves, so a reading from March stays attributed to the room the sensor was in during March.

## Turtle

{% raw %}
```turtle
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ontosage:periodLocation a owl:ObjectProperty ;
    rdfs:label "location during period"@en ;
    rdfs:comment "Where the point was during this period. This is what an as-of query resolves, so a reading from March stays attributed to the room the sensor was in during March."@en ;
    rdfs:domain ontosage:ConfigurationPeriod ;
    rdfs:range brick:Location .
```
{% endraw %}
