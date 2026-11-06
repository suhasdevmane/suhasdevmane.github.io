---
title: "ontosage:cubicleCount"
layout: post
permalink: /ontology/property/cubicleCount/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › cubicleCount

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#cubicleCount` |
| Label | cubicle count |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:integer` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

How many cubicles the washroom block holds. A block of five cubicles is one facility with five, not five facilities -- counting it either way without saying which is how a floor's provision gets misreported.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:cubicleCount a owl:DatatypeProperty ;
    rdfs:label "cubicle count"@en ;
    rdfs:comment "How many cubicles the washroom block holds. A block of five cubicles is one facility with five, not five facilities -- counting it either way without saying which is how a floor's provision gets misreported."@en ;
    rdfs:range xsd:integer .
```
{% endraw %}
