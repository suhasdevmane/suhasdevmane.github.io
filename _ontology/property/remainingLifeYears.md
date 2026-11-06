---
title: "ontosage:remainingLifeYears"
layout: post
permalink: /ontology/property/remainingLifeYears/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › remainingLifeYears

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#remainingLifeYears` |
| Label | remaining life (years) |
| Kind | datatype property |
| Domain | [`ontosage:ConditionSurvey`]({{ '/ontology/class/ConditionSurvey/' | relative_url }}) |
| Range | `xsd:decimal` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Expected remaining life at the survey date, in years. An ESTIMATE by the surveyor, so an answer using it is calculated, never observed. ZERO OR LESS means the asset is at or beyond its expected life: a question about assets beyond expected life must use &lt;= 0, not = 0, or an asset already past its life is left out of its own answer.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`condition_survey`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#condition_survey) | `remaining_life_years` | `xsd:decimal` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:remainingLifeYears a owl:DatatypeProperty ;
    rdfs:label "remaining life (years)"@en ;
    rdfs:comment "Expected remaining life at the survey date, in years. An ESTIMATE by the surveyor, so an answer using it is calculated, never observed. ZERO OR LESS means the asset is at or beyond its expected life: a question about assets beyond expected life must use <= 0, not = 0, or an asset already past its life is left out of its own answer."@en ;
    rdfs:domain ontosage:ConditionSurvey ;
    rdfs:range xsd:decimal .
```
{% endraw %}
