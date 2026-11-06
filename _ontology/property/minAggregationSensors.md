---
title: "ontosage:minAggregationSensors"
layout: post
permalink: /ontology/property/minAggregationSensors/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › minAggregationSensors

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#minAggregationSensors` |
| Label | k-anonymity sensor floor |
| Kind | datatype property |
| Domain | [`ontosage:AccessPolicy`]({{ '/ontology/class/AccessPolicy/' | relative_url }}) |
| Range | `xsd:integer` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The schema gives no definition for this term.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:minAggregationSensors a owl:DatatypeProperty ;
    rdfs:label "k-anonymity sensor floor"@en ;
    rdfs:domain ontosage:AccessPolicy ;
    rdfs:range xsd:integer .
```
{% endraw %}
