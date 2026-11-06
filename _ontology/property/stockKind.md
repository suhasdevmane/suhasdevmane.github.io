---
title: "ontosage:stockKind"
layout: post
permalink: /ontology/property/stockKind/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › stockKind

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#stockKind` |
| Label | stock kind |
| Kind | datatype property |
| Domain | [`ontosage:StockItem`]({{ '/ontology/class/StockItem/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Consumable, spare, loan or surplus. Kept as its own field because 'are we running low' means something different for each: a consumable is reordered, a spare is held against an asset, a loan line is about availability, and surplus has no minimum.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`stock_item`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#stock_item) | `kind` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:stockKind a owl:DatatypeProperty ;
    rdfs:label "stock kind"@en ;
    rdfs:comment "Consumable, spare, loan or surplus. Kept as its own field because 'are we running low' means something different for each: a consumable is reordered, a spare is held against an asset, a loan line is about availability, and surplus has no minimum."@en ;
    rdfs:domain ontosage:StockItem ;
    rdfs:range xsd:string .
```
{% endraw %}
