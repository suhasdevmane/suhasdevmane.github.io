---
title: "ontosage:leadTimeDays"
layout: post
permalink: /ontology/property/leadTimeDays/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › leadTimeDays

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#leadTimeDays` |
| Label | lead time (days) |
| Kind | datatype property |
| Domain | [`ontosage:StockItem`]({{ '/ontology/class/StockItem/' | relative_url }}) |
| Range | `xsd:integer` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

How long a reorder normally takes to arrive. Left blank where nothing has been agreed rather than guessed.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`stock_item`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#stock_item) | `lead_time_days` | `xsd:integer` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:leadTimeDays a owl:DatatypeProperty ;
    rdfs:label "lead time (days)"@en ;
    rdfs:comment "How long a reorder normally takes to arrive. Left blank where nothing has been agreed rather than guessed."@en ;
    rdfs:domain ontosage:StockItem ;
    rdfs:range xsd:integer .
```
{% endraw %}
