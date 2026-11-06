---
title: "ontosage:targetDate"
layout: post
permalink: /ontology/property/targetDate/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › targetDate

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#targetDate` |
| Label | target date |
| Kind | datatype property |
| Domain | [`ontosage:SustainabilityTarget`]({{ '/ontology/class/SustainabilityTarget/' | relative_url }}) |
| Range | `xsd:date` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

When the target is to be met. Progress against an undated target cannot be judged, because 'on track' is a statement about a rate, not a level.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`sustainability_target`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#sustainability_target) | `target_date` | `xsd:date` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:targetDate a owl:DatatypeProperty ;
    rdfs:label "target date"@en ;
    rdfs:comment "When the target is to be met. Progress against an undated target cannot be judged, because 'on track' is a statement about a rate, not a level."@en ;
    rdfs:domain ontosage:SustainabilityTarget ;
    rdfs:range xsd:date .
```
{% endraw %}
