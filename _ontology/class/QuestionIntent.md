---
title: "ontosage:QuestionIntent"
layout: post
permalink: /ontology/class/QuestionIntent/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › QuestionIntent

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#QuestionIntent` |
| Label | Question intent |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The shape/kind of a stakeholder question (locate, quantify, trend, compare, …).

## Description

A kind of question a stakeholder can ask, independent of the specific building. Classifying an utterance to an intent selects the answering strategy (fact lookup vs computation vs time-series vs report).

## Examples

- "how many CO₂ sensors are there?" -&gt; ontosage:Intent\_Quantify.

## Class hierarchy

Superclasses: none (a root class).

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:answeredBy`]({{ '/ontology/property/answeredBy/' | relative_url }}) | object | [`ontosage:SourceType`]({{ '/ontology/class/SourceType/' | relative_url }}) | this class |
| [`ontosage:intentPattern`]({{ '/ontology/property/intentPattern/' | relative_url }}) | datatype | `xsd:string` | this class |

## Members

The schema declares 10 members of this class: see [Question intents]({{ '/ontology/vocabulary/question-intents/' | relative_url }}).

## Competency questions

- What kind of question is this, and how should it be answered?

## Example SPARQL

{% raw %}
```sparql
# Given cue words, find the matching intent and its answering source types.
SELECT ?intent ?label (GROUP_CONCAT(?src; separator=", ") AS ?sources) WHERE {
  ?intent a ontosage:QuestionIntent ; rdfs:label ?label ; ontosage:intentPattern ?pat .
  OPTIONAL { ?intent ontosage:answeredBy ?s . ?s rdfs:label ?src }
  FILTER(CONTAINS(LCASE(?pat), "how many"))
} GROUP BY ?intent ?label
```
{% endraw %}

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:QuestionIntent a owl:Class ;
    rdfs:label "Question intent"@en ;
    ontosage:competencyQuestion "What kind of question is this, and how should it be answered?" ;
    ontosage:exampleSparql """
        # Given cue words, find the matching intent and its answering source types.
        SELECT ?intent ?label (GROUP_CONCAT(?src; separator=", ") AS ?sources) WHERE {
          ?intent a ontosage:QuestionIntent ; rdfs:label ?label ; ontosage:intentPattern ?pat .
          OPTIONAL { ?intent ontosage:answeredBy ?s . ?s rdfs:label ?src }
          FILTER(CONTAINS(LCASE(?pat), "how many"))
        } GROUP BY ?intent ?label""" ;
    rdfs:comment "A kind of question a stakeholder can ask, independent of the specific building. Classifying an utterance to an intent selects the answering strategy (fact lookup vs computation vs time-series vs report)."@en ;
    skos:definition "The shape/kind of a stakeholder question (locate, quantify, trend, compare, …)."@en ;
    skos:example "\"how many CO₂ sensors are there?\" -> ontosage:Intent_Quantify." .
```
{% endraw %}
