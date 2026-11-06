---
title: "ontosage:nextDue"
layout: post
permalink: /ontology/property/nextDue/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › nextDue

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#nextDue` |
| Label | next due |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:date` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The schema gives no definition for this term.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`av_readiness`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#av_readiness) | `next_due` | `xsd:date` |
| [`cleaning_task`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#cleaning_task) | `next_due` | `xsd:date` |
| [`patrol_checkpoint`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#patrol_checkpoint) | `due` | `xsd:dateTime` |
| [`service_schedule`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#service_schedule) | `next_due` | `xsd:date` |
| [`stock_item`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#stock_item) | `next_due` | `xsd:date` |
| [`waste_collection`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#waste_collection) | `next_collection` | `xsd:date` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:nextDue a owl:DatatypeProperty ;
    rdfs:label "next due"@en ;
    rdfs:range xsd:date .
```
{% endraw %}
