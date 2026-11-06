---
title: "ontosage:transmissionIntervalS"
layout: post
permalink: /ontology/property/transmissionIntervalS/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › transmissionIntervalS

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#transmissionIntervalS` |
| Label | transmission interval (s) |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:integer` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

How often the device reports. Second of the three clocks. This is what a freshness gate must judge against: a point transmitting every 15 minutes is not stale at 10.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:transmissionIntervalS a owl:DatatypeProperty ;
    rdfs:label "transmission interval (s)"@en ;
    rdfs:comment "How often the device reports. Second of the three clocks. This is what a freshness gate must judge against: a point transmitting every 15 minutes is not stale at 10."@en ;
    rdfs:range xsd:integer .
```
{% endraw %}
