---
title: "ontosage:groundedIn"
layout: post
permalink: /ontology/property/groundedIn/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › groundedIn

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#groundedIn` |
| Label | grounded in |
| Kind | object property |
| Domain | not declared (any subject) |
| Range | [`ontosage:SourceType`]({{ '/ontology/class/SourceType/' | relative_url }}) |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Records a source type that produced (part of) an answer. An answer with no ontosage:groundedIn is not grounded and must not assert figures — the honest 'no data' path applies instead.

## Examples

- an answer about last week's CO₂ trend ontosage:groundedIn ontosage:Src\_TimeSeriesDB , ontosage:Src\_Analytics .

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:groundedIn a owl:ObjectProperty ;
    rdfs:label "grounded in"@en ;
    rdfs:comment "Records a source type that produced (part of) an answer. An answer with no ontosage:groundedIn is not grounded and must not assert figures — the honest 'no data' path applies instead."@en ;
    rdfs:range ontosage:SourceType ;
    skos:example "an answer about last week's CO₂ trend ontosage:groundedIn ontosage:Src_TimeSeriesDB , ontosage:Src_Analytics ." .
```
{% endraw %}
