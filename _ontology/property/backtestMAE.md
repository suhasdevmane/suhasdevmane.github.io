---
title: "ontosage:backtestMAE"
layout: post
permalink: /ontology/property/backtestMAE/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › backtestMAE

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#backtestMAE` |
| Label | backtest MAE |
| Kind | datatype property |
| Domain | [`ontosage:ForecastSkill`]({{ '/ontology/class/ForecastSkill/' | relative_url }}) |
| Range | `xsd:double` |
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

ontosage:backtestMAE a owl:DatatypeProperty ;
    rdfs:label "backtest MAE"@en ;
    rdfs:domain ontosage:ForecastSkill ;
    rdfs:range xsd:double .
```
{% endraw %}
