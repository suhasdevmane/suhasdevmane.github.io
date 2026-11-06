---
title: "ontosage:conditionGrade"
layout: post
permalink: /ontology/property/conditionGrade/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › conditionGrade

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#conditionGrade` |
| Label | condition grade |
| Kind | datatype property |
| Domain | [`ontosage:ConditionSurvey`]({{ '/ontology/class/ConditionSurvey/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The grade recorded by the surveyor (A good, B satisfactory, C poor, D end of life), kept verbatim and never re-derived.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`condition_survey`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#condition_survey) | `grade` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:conditionGrade a owl:DatatypeProperty ;
    rdfs:label "condition grade"@en ;
    rdfs:comment "The grade recorded by the surveyor (A good, B satisfactory, C poor, D end of life), kept verbatim and never re-derived."@en ;
    rdfs:domain ontosage:ConditionSurvey ;
    rdfs:range xsd:string .
```
{% endraw %}
