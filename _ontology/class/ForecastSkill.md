---
title: "ontosage:ForecastSkill"
layout: post
permalink: /ontology/class/ForecastSkill/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › ForecastSkill

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#ForecastSkill` |
| Label | Forecast skill record |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Measured predictive skill for one (modality x horizon) on THIS building, from walk-forward backtesting. Cited in every forecast answer; makes 'how good are your forecasts?' SPARQL-answerable.

## Examples

- "how confident are you?" -&gt; the ForecastSkill for co2 @ 24h: MAE, MAPE, CI coverage.

## Class hierarchy

Superclasses: none (a root class).

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:backtestMAE`]({{ '/ontology/property/backtestMAE/' | relative_url }}) | datatype | `xsd:double` | this class |
| [`ontosage:backtestMAPE`]({{ '/ontology/property/backtestMAPE/' | relative_url }}) | datatype | `xsd:double` | this class |
| [`ontosage:ciCoverage80`]({{ '/ontology/property/ciCoverage80/' | relative_url }}) | datatype | `xsd:double` | this class |
| [`ontosage:horizonHours`]({{ '/ontology/property/horizonHours/' | relative_url }}) | datatype | `xsd:double` | this class |
| [`ontosage:skillMeasuredAt`]({{ '/ontology/property/skillMeasuredAt/' | relative_url }}) | datatype | `xsd:dateTime` | this class |
| [`ontosage:skillOf`]({{ '/ontology/property/skillOf/' | relative_url }}) | datatype | `xsd:string` | this class |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:ForecastSkill a owl:Class ;
    rdfs:label "Forecast skill record"@en ;
    rdfs:comment "Measured predictive skill for one (modality x horizon) on THIS building, from walk-forward backtesting. Cited in every forecast answer; makes 'how good are your forecasts?' SPARQL-answerable."@en ;
    skos:example "\"how confident are you?\" -> the ForecastSkill for co2 @ 24h: MAE, MAPE, CI coverage." .
```
{% endraw %}
