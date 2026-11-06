---
title: "ontosage:targetBaselinePeriod"
layout: post
permalink: /ontology/property/targetBaselinePeriod/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › targetBaselinePeriod

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#targetBaselinePeriod` |
| Label | baseline period |
| Kind | datatype property |
| Domain | [`ontosage:SustainabilityTarget`]({{ '/ontology/class/SustainabilityTarget/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The period the target is measured against. A 20% reduction is meaningless without it, and choosing a baseline after the fact is the oldest way to make a number say what you want.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`sustainability_target`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#sustainability_target) | `baseline_period` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:targetBaselinePeriod a owl:DatatypeProperty ;
    rdfs:label "baseline period"@en ;
    rdfs:comment "The period the target is measured against. A 20% reduction is meaningless without it, and choosing a baseline after the fact is the oldest way to make a number say what you want."@en ;
    rdfs:domain ontosage:SustainabilityTarget ;
    rdfs:range xsd:string .
```
{% endraw %}
