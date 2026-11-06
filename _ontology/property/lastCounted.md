---
title: "ontosage:lastCounted"
layout: post
permalink: /ontology/property/lastCounted/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › lastCounted

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#lastCounted` |
| Label | last counted |
| Kind | datatype property |
| Domain | [`ontosage:StockItem`]({{ '/ontology/class/StockItem/' | relative_url }}) |
| Range | `xsd:date` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

When somebody counted the shelf. Stock not counted this month is a claim, not a count.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`stock_item`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#stock_item) | `last_counted` | `xsd:date` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:lastCounted a owl:DatatypeProperty ;
    rdfs:label "last counted"@en ;
    rdfs:comment "When somebody counted the shelf. Stock not counted this month is a claim, not a count."@en ;
    rdfs:domain ontosage:StockItem ;
    rdfs:range xsd:date .
```
{% endraw %}
