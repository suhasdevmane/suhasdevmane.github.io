---
title: "ontosage:expectedAttendance"
layout: post
permalink: /ontology/property/expectedAttendance/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › expectedAttendance

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#expectedAttendance` |
| Label | expected attendance |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:integer` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Planned headcount. An institutional expectation, never an occupancy measurement — a planned figure must not be reported as an observed one.

## Turtle

Development notes were removed from one or more text values below; the source file holds the full text.

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:expectedAttendance a owl:DatatypeProperty ;
    rdfs:label "expected attendance"@en ;
    rdfs:comment "Planned headcount. An institutional expectation, never an occupancy measurement — a planned figure must not be reported as an observed one."@en ;
    rdfs:range xsd:integer .
```
{% endraw %}
