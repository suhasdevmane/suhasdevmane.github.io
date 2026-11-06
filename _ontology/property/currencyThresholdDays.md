---
title: "ontosage:currencyThresholdDays"
layout: post
permalink: /ontology/property/currencyThresholdDays/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › currencyThresholdDays

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#currencyThresholdDays` |
| Label | currency threshold (days) |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:integer` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

How long a record of this class stays current, set by its owner. Staleness is decision-specific: a CO2 reading is stale in minutes, an asbestos survey in years. One global freshness rule must either call a valid survey stale or let an hours-old reading pass as current.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:currencyThresholdDays a owl:DatatypeProperty ;
    rdfs:label "currency threshold (days)"@en ;
    rdfs:comment "How long a record of this class stays current, set by its owner. Staleness is decision-specific: a CO2 reading is stale in minutes, an asbestos survey in years. One global freshness rule must either call a valid survey stale or let an hours-old reading pass as current."@en ;
    rdfs:range xsd:integer .
```
{% endraw %}
