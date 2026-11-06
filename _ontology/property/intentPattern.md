---
title: "ontosage:intentPattern"
layout: post
permalink: /ontology/property/intentPattern/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › intentPattern

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#intentPattern` |
| Label | intent phrasings |
| Kind | datatype property |
| Domain | [`ontosage:QuestionIntent`]({{ '/ontology/class/QuestionIntent/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Comma-separated example phrasings / trigger cues for an intent — the lay grammar OntoSage matches to classify a question into this intent.

## Examples

- "how many, count, number of, total"

## Used in the schema

10 schema term(s) carry this property:

- [`ontosage:Intent_Anomaly`]({{ '/ontology/vocabulary/question-intents/' | relative_url }}#Intent_Anomaly)
- [`ontosage:Intent_Comfort`]({{ '/ontology/vocabulary/question-intents/' | relative_url }}#Intent_Comfort)
- [`ontosage:Intent_Compare`]({{ '/ontology/vocabulary/question-intents/' | relative_url }}#Intent_Compare)
- [`ontosage:Intent_Discover`]({{ '/ontology/vocabulary/question-intents/' | relative_url }}#Intent_Discover)
- [`ontosage:Intent_Forecast`]({{ '/ontology/vocabulary/question-intents/' | relative_url }}#Intent_Forecast)
- [`ontosage:Intent_Locate`]({{ '/ontology/vocabulary/question-intents/' | relative_url }}#Intent_Locate)
- [`ontosage:Intent_ProcedureAsk`]({{ '/ontology/vocabulary/question-intents/' | relative_url }}#Intent_ProcedureAsk)
- [`ontosage:Intent_Quantify`]({{ '/ontology/vocabulary/question-intents/' | relative_url }}#Intent_Quantify)
- [`ontosage:Intent_Report`]({{ '/ontology/vocabulary/question-intents/' | relative_url }}#Intent_Report)
- [`ontosage:Intent_Trend`]({{ '/ontology/vocabulary/question-intents/' | relative_url }}#Intent_Trend)

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:intentPattern a owl:DatatypeProperty ;
    rdfs:label "intent phrasings"@en ;
    rdfs:comment "Comma-separated example phrasings / trigger cues for an intent — the lay grammar OntoSage matches to classify a question into this intent."@en ;
    rdfs:domain ontosage:QuestionIntent ;
    rdfs:range xsd:string ;
    skos:example "\"how many, count, number of, total\"" .
```
{% endraw %}
