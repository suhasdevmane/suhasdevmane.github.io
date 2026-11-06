---
title: "ontosage:calibrationDueOn"
layout: post
permalink: /ontology/property/calibrationDueOn/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › calibrationDueOn

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#calibrationDueOn` |
| Label | calibration due date |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:date` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

When calibration next falls due. Lets a gate distinguish EXPIRED from never-calibrated — a different remedy, and a different level of trust in the interim readings.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:calibrationDueOn a owl:DatatypeProperty ;
    rdfs:label "calibration due date"@en ;
    rdfs:comment "When calibration next falls due. Lets a gate distinguish EXPIRED from never-calibrated — a different remedy, and a different level of trust in the interim readings."@en ;
    rdfs:range xsd:date .
```
{% endraw %}
