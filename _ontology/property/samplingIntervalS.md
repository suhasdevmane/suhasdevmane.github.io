---
title: "ontosage:samplingIntervalS"
layout: post
permalink: /ontology/property/samplingIntervalS/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › samplingIntervalS

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#samplingIntervalS` |
| Label | sampling interval (s) |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:integer` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

How often the device physically measures. First of the three clocks; distinct from how often it transmits and from what is archived.

## Turtle

Development notes were removed from one or more text values below; the source file holds the full text.

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:samplingIntervalS a owl:DatatypeProperty ;
    rdfs:label "sampling interval (s)"@en ;
    rdfs:comment "How often the device physically measures. First of the three clocks; distinct from how often it transmits and from what is archived."@en ;
    rdfs:range xsd:integer .
```
{% endraw %}
