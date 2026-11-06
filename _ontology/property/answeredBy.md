---
title: "ontosage:answeredBy"
layout: post
permalink: /ontology/property/answeredBy/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › answeredBy

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#answeredBy` |
| Label | answered by source type |
| Kind | object property |
| Domain | [`ontosage:QuestionIntent`]({{ '/ontology/class/QuestionIntent/' | relative_url }}) |
| Range | [`ontosage:SourceType`]({{ '/ontology/class/SourceType/' | relative_url }}) |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The provenance/source type (Module F) an intent is typically answered from — e.g. a Quantify intent is answered by a SPARQL COUNT over the graph, a Trend intent by the time-series DB plus analytics.

## Examples

- `ontosage:Intent_Trend ontosage:answeredBy ontosage:Src_TimeSeriesDB , ontosage:Src_Analytics .`

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

ontosage:answeredBy a owl:ObjectProperty ;
    rdfs:label "answered by source type"@en ;
    rdfs:comment "The provenance/source type (Module F) an intent is typically answered from — e.g. a Quantify intent is answered by a SPARQL COUNT over the graph, a Trend intent by the time-series DB plus analytics."@en ;
    rdfs:domain ontosage:QuestionIntent ;
    rdfs:range ontosage:SourceType ;
    skos:example "ontosage:Intent_Trend ontosage:answeredBy ontosage:Src_TimeSeriesDB , ontosage:Src_Analytics ." .
```
{% endraw %}
