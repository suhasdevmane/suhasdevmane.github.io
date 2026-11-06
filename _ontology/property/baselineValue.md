---
title: "ontosage:baselineValue"
layout: post
permalink: /ontology/property/baselineValue/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › baselineValue

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#baselineValue` |
| Label | baseline value |
| Kind | datatype property |
| Domain | [`ontosage:AnomalyEvent`]({{ '/ontology/class/AnomalyEvent/' | relative_url }}) |
| Range | `xsd:double` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The expected-band context the deviation is measured against.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`sustainability_target`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#sustainability_target) | `baseline_value` | `xsd:decimal` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:baselineValue a owl:DatatypeProperty ;
    rdfs:label "baseline value"@en ;
    rdfs:comment "The expected-band context the deviation is measured against."@en ;
    rdfs:domain ontosage:AnomalyEvent ;
    rdfs:range xsd:double .
```
{% endraw %}
