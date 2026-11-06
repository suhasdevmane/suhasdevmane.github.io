---
title: "ontosage:calibratedOn"
layout: post
permalink: /ontology/property/calibratedOn/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › calibratedOn

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#calibratedOn` |
| Label | calibration date |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:date` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Date this point was last calibrated. Absence means UNKNOWN — not uncalibrated, and not fine: a standards or compliance verdict may not rest on a point whose calibration state is unknown.

## Examples

- "2026-03-14"^^xsd:date

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:calibratedOn a owl:DatatypeProperty ;
    rdfs:label "calibration date"@en ;
    rdfs:comment "Date this point was last calibrated. Absence means UNKNOWN — not uncalibrated, and not fine: a standards or compliance verdict may not rest on a point whose calibration state is unknown."@en ;
    rdfs:range xsd:date ;
    skos:example "\"2026-03-14\"^^xsd:date" .
```
{% endraw %}
