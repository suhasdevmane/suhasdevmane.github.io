---
title: "ontosage:ciCoverage80"
layout: post
permalink: /ontology/property/ciCoverage80/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › ciCoverage80

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#ciCoverage80` |
| Label | 80% CI coverage (measured) |
| Kind | datatype property |
| Domain | [`ontosage:ForecastSkill`]({{ '/ontology/class/ForecastSkill/' | relative_url }}) |
| Range | `xsd:double` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Fraction of holdout actuals inside the 80% interval — calibration, not hope.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:ciCoverage80 a owl:DatatypeProperty ;
    rdfs:label "80% CI coverage (measured)"@en ;
    rdfs:comment "Fraction of holdout actuals inside the 80% interval — calibration, not hope."@en ;
    rdfs:domain ontosage:ForecastSkill ;
    rdfs:range xsd:double .
```
{% endraw %}
