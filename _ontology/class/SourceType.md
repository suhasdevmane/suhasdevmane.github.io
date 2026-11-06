---
title: "ontosage:SourceType"
layout: post
permalink: /ontology/class/SourceType/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › SourceType

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#SourceType` |
| Label | Answer source type |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A category of grounding source for an answer (graph, time-series DB, floor plan, analytics, …).

## Description

A kind of system an OntoSage answer can be grounded in. An answer records which source type(s) produced it, so it is auditable and never a plausible-but-unsourced guess.

## Examples

- A trend answer is grounded in Src\_TimeSeriesDB + Src\_Analytics.

## Class hierarchy

Superclasses: none (a root class).

Subclasses: none.

## Properties

No property declares this class (or a superclass) as its domain.

## Used as the range of

| Property | Kind | Domain |
|---|---|---|
| [`ontosage:answeredBy`]({{ '/ontology/property/answeredBy/' | relative_url }}) | object | [`ontosage:QuestionIntent`]({{ '/ontology/class/QuestionIntent/' | relative_url }}) |
| [`ontosage:groundedIn`]({{ '/ontology/property/groundedIn/' | relative_url }}) | object | any |

## Members

The schema declares 8 members of this class: see [Answer source types]({{ '/ontology/vocabulary/source-types/' | relative_url }}).

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:SourceType a owl:Class ;
    rdfs:label "Answer source type"@en ;
    rdfs:comment "A kind of system an OntoSage answer can be grounded in. An answer records which source type(s) produced it, so it is auditable and never a plausible-but-unsourced guess."@en ;
    skos:definition "A category of grounding source for an answer (graph, time-series DB, floor plan, analytics, …)."@en ;
    skos:example "A trend answer is grounded in Src_TimeSeriesDB + Src_Analytics." .
```
{% endraw %}
