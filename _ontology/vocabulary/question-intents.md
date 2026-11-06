---
title: "Question intents"
layout: post
permalink: /ontology/vocabulary/question-intents/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Vocabularies]({{ '/docs/ontology-browser/' | relative_url }}#vocabularies) › Question intents

The kinds of question a stakeholder asks, each with cue phrases and the source types that usually answer it. Members are instances of [`ontosage:QuestionIntent`]({{ '/ontology/class/QuestionIntent/' | relative_url }}). The schema declares 10.

| Member | Label |
|---|---|
| [`ontosage:Intent_Anomaly`](#Intent_Anomaly) | Anomaly / status |
| [`ontosage:Intent_Comfort`](#Intent_Comfort) | Comfort / environment |
| [`ontosage:Intent_Compare`](#Intent_Compare) | Compare |
| [`ontosage:Intent_Discover`](#Intent_Discover) | Discover / metadata |
| [`ontosage:Intent_Forecast`](#Intent_Forecast) | Forecast / predict |
| [`ontosage:Intent_Locate`](#Intent_Locate) | Locate / wayfinding |
| [`ontosage:Intent_ProcedureAsk`](#Intent_ProcedureAsk) | Procedure / how-to |
| [`ontosage:Intent_Quantify`](#Intent_Quantify) | Quantify / current value |
| [`ontosage:Intent_Report`](#Intent_Report) | Report / statement |
| [`ontosage:Intent_Trend`](#Intent_Trend) | Trend / history |

## Anomaly / status {#Intent_Anomaly}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Intent_Anomaly` |
| [`ontosage:answeredBy`]({{ '/ontology/property/answeredBy/' | relative_url }}) | [`ontosage:Src_Analytics`]({{ '/ontology/vocabulary/source-types/' | relative_url }}#Src_Analytics), [`ontosage:Src_TimeSeriesDB`]({{ '/ontology/vocabulary/source-types/' | relative_url }}#Src_TimeSeriesDB) |
| [`ontosage:intentPattern`]({{ '/ontology/property/intentPattern/' | relative_url }}) | anomaly, abnormal, unusual, is anything wrong, alarms, out of range, faults |

Ask whether something is abnormal or OK — 'is anything wrong?', 'any alarms?'.

## Comfort / environment {#Intent_Comfort}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Intent_Comfort` |
| [`ontosage:answeredBy`]({{ '/ontology/property/answeredBy/' | relative_url }}) | [`ontosage:Src_Analytics`]({{ '/ontology/vocabulary/source-types/' | relative_url }}#Src_Analytics), [`ontosage:Src_TimeSeriesDB`]({{ '/ontology/vocabulary/source-types/' | relative_url }}#Src_TimeSeriesDB) |
| [`ontosage:intentPattern`]({{ '/ontology/property/intentPattern/' | relative_url }}) | too warm, too cold, stuffy, noisy, dark, is it comfortable, air quality |

Ask about how the space feels using lay language — resolved via Module B concepts ('is it stuffy / too warm / noisy?').

## Compare {#Intent_Compare}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Intent_Compare` |
| [`ontosage:answeredBy`]({{ '/ontology/property/answeredBy/' | relative_url }}) | [`ontosage:Src_Analytics`]({{ '/ontology/vocabulary/source-types/' | relative_url }}#Src_Analytics), [`ontosage:Src_TimeSeriesDB`]({{ '/ontology/vocabulary/source-types/' | relative_url }}#Src_TimeSeriesDB) |
| [`ontosage:intentPattern`]({{ '/ontology/property/intentPattern/' | relative_url }}) | compare, versus, vs, difference between, which is higher, warmer than |

Compare two or more things — floors, zones, periods.

## Discover / metadata {#Intent_Discover}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Intent_Discover` |
| [`ontosage:answeredBy`]({{ '/ontology/property/answeredBy/' | relative_url }}) | [`ontosage:Src_GraphDB`]({{ '/ontology/vocabulary/source-types/' | relative_url }}#Src_GraphDB) |
| [`ontosage:intentPattern`]({{ '/ontology/property/intentPattern/' | relative_url }}) | what sensors, list, show me all, what equipment, what can you tell me about |

Explore what the building has — 'what sensors are on floor 3?', 'list the equipment'.

## Forecast / predict {#Intent_Forecast}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Intent_Forecast` |
| [`ontosage:answeredBy`]({{ '/ontology/property/answeredBy/' | relative_url }}) | [`ontosage:Src_Analytics`]({{ '/ontology/vocabulary/source-types/' | relative_url }}#Src_Analytics) |
| [`ontosage:intentPattern`]({{ '/ontology/property/intentPattern/' | relative_url }}) | forecast, predict, will it, expected, tomorrow, next week, projection |

Ask for a projection of a value — 'what will the temperature be tomorrow?'.

## Locate / wayfinding {#Intent_Locate}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Intent_Locate` |
| [`ontosage:answeredBy`]({{ '/ontology/property/answeredBy/' | relative_url }}) | [`ontosage:Src_FloorPlan`]({{ '/ontology/vocabulary/source-types/' | relative_url }}#Src_FloorPlan), [`ontosage:Src_GraphDB`]({{ '/ontology/vocabulary/source-types/' | relative_url }}#Src_GraphDB) |
| [`ontosage:intentPattern`]({{ '/ontology/property/intentPattern/' | relative_url }}) | where is, where can i find, how do i get to, nearest, location of |

Find where something is (amenity, room, sensor, equipment).

## Procedure / how-to {#Intent_ProcedureAsk}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Intent_ProcedureAsk` |
| [`ontosage:answeredBy`]({{ '/ontology/property/answeredBy/' | relative_url }}) | [`ontosage:Src_CapabilityKB`]({{ '/ontology/vocabulary/source-types/' | relative_url }}#Src_CapabilityKB), [`ontosage:Src_GraphDB`]({{ '/ontology/vocabulary/source-types/' | relative_url }}#Src_GraphDB) |
| [`ontosage:intentPattern`]({{ '/ontology/property/intentPattern/' | relative_url }}) | how do i, how to, what is the process for, steps to, procedure for |

Ask how to do something — answered from a Module A ontosage:Procedure.

## Quantify / current value {#Intent_Quantify}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Intent_Quantify` |
| [`ontosage:answeredBy`]({{ '/ontology/property/answeredBy/' | relative_url }}) | [`ontosage:Src_GraphDB`]({{ '/ontology/vocabulary/source-types/' | relative_url }}#Src_GraphDB), [`ontosage:Src_TimeSeriesDB`]({{ '/ontology/vocabulary/source-types/' | relative_url }}#Src_TimeSeriesDB) |
| [`ontosage:intentPattern`]({{ '/ontology/property/intentPattern/' | relative_url }}) | how many, count, number of, what is the, current, right now, level of |

Ask for a count or a current reading — 'how many', 'what is the level right now'.

## Report / statement {#Intent_Report}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Intent_Report` |
| [`ontosage:answeredBy`]({{ '/ontology/property/answeredBy/' | relative_url }}) | [`ontosage:Src_ReportIntake`]({{ '/ontology/vocabulary/source-types/' | relative_url }}#Src_ReportIntake) |
| [`ontosage:intentPattern`]({{ '/ontology/property/intentPattern/' | relative_url }}) | is leaking, is broken, doesn't work, i want to report, there is a problem with |

STATE a problem rather than ask a question — 'the toilet is leaking', 'the lift is broken'. Files a Module E report; distinct from asking whether something is broken.

## Trend / history {#Intent_Trend}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Intent_Trend` |
| [`ontosage:answeredBy`]({{ '/ontology/property/answeredBy/' | relative_url }}) | [`ontosage:Src_Analytics`]({{ '/ontology/vocabulary/source-types/' | relative_url }}#Src_Analytics), [`ontosage:Src_TimeSeriesDB`]({{ '/ontology/vocabulary/source-types/' | relative_url }}#Src_TimeSeriesDB) |
| [`ontosage:intentPattern`]({{ '/ontology/property/intentPattern/' | relative_url }}) | trend, over time, history, average, last week, yesterday, past month, plot |

Ask how a value has changed over a period — 'trend', 'over the last week', 'average yesterday'.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ontosage:Intent_Anomaly a ontosage:QuestionIntent ;
    rdfs:label "Anomaly / status"@en ;
    ontosage:answeredBy ontosage:Src_Analytics,
        ontosage:Src_TimeSeriesDB ;
    ontosage:intentPattern "anomaly, abnormal, unusual, is anything wrong, alarms, out of range, faults" ;
    rdfs:comment "Ask whether something is abnormal or OK — 'is anything wrong?', 'any alarms?'."@en .

ontosage:Intent_Comfort a ontosage:QuestionIntent ;
    rdfs:label "Comfort / environment"@en ;
    ontosage:answeredBy ontosage:Src_Analytics,
        ontosage:Src_TimeSeriesDB ;
    ontosage:intentPattern "too warm, too cold, stuffy, noisy, dark, is it comfortable, air quality" ;
    rdfs:comment "Ask about how the space feels using lay language — resolved via Module B concepts ('is it stuffy / too warm / noisy?')."@en .

ontosage:Intent_Compare a ontosage:QuestionIntent ;
    rdfs:label "Compare"@en ;
    ontosage:answeredBy ontosage:Src_Analytics,
        ontosage:Src_TimeSeriesDB ;
    ontosage:intentPattern "compare, versus, vs, difference between, which is higher, warmer than" ;
    rdfs:comment "Compare two or more things — floors, zones, periods."@en .

ontosage:Intent_Discover a ontosage:QuestionIntent ;
    rdfs:label "Discover / metadata"@en ;
    ontosage:answeredBy ontosage:Src_GraphDB ;
    ontosage:intentPattern "what sensors, list, show me all, what equipment, what can you tell me about" ;
    rdfs:comment "Explore what the building has — 'what sensors are on floor 3?', 'list the equipment'."@en .

ontosage:Intent_Forecast a ontosage:QuestionIntent ;
    rdfs:label "Forecast / predict"@en ;
    ontosage:answeredBy ontosage:Src_Analytics ;
    ontosage:intentPattern "forecast, predict, will it, expected, tomorrow, next week, projection" ;
    rdfs:comment "Ask for a projection of a value — 'what will the temperature be tomorrow?'."@en .

ontosage:Intent_Locate a ontosage:QuestionIntent ;
    rdfs:label "Locate / wayfinding"@en ;
    ontosage:answeredBy ontosage:Src_FloorPlan,
        ontosage:Src_GraphDB ;
    ontosage:intentPattern "where is, where can i find, how do i get to, nearest, location of" ;
    rdfs:comment "Find where something is (amenity, room, sensor, equipment)."@en .

ontosage:Intent_ProcedureAsk a ontosage:QuestionIntent ;
    rdfs:label "Procedure / how-to"@en ;
    ontosage:answeredBy ontosage:Src_CapabilityKB,
        ontosage:Src_GraphDB ;
    ontosage:intentPattern "how do i, how to, what is the process for, steps to, procedure for" ;
    rdfs:comment "Ask how to do something — answered from a Module A ontosage:Procedure."@en .

ontosage:Intent_Quantify a ontosage:QuestionIntent ;
    rdfs:label "Quantify / current value"@en ;
    ontosage:answeredBy ontosage:Src_GraphDB,
        ontosage:Src_TimeSeriesDB ;
    ontosage:intentPattern "how many, count, number of, what is the, current, right now, level of" ;
    rdfs:comment "Ask for a count or a current reading — 'how many', 'what is the level right now'."@en .

ontosage:Intent_Report a ontosage:QuestionIntent ;
    rdfs:label "Report / statement"@en ;
    ontosage:answeredBy ontosage:Src_ReportIntake ;
    ontosage:intentPattern "is leaking, is broken, doesn't work, i want to report, there is a problem with" ;
    rdfs:comment "STATE a problem rather than ask a question — 'the toilet is leaking', 'the lift is broken'. Files a Module E report; distinct from asking whether something is broken."@en .

ontosage:Intent_Trend a ontosage:QuestionIntent ;
    rdfs:label "Trend / history"@en ;
    ontosage:answeredBy ontosage:Src_Analytics,
        ontosage:Src_TimeSeriesDB ;
    ontosage:intentPattern "trend, over time, history, average, last week, yesterday, past month, plot" ;
    rdfs:comment "Ask how a value has changed over a period — 'trend', 'over the last week', 'average yesterday'."@en .
```
{% endraw %}
