---
title: "ontosage:minimumLevel"
layout: post
permalink: /ontology/property/minimumLevel/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › minimumLevel

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#minimumLevel` |
| Label | minimum level |
| Kind | datatype property |
| Domain | [`ontosage:StockItem`]({{ '/ontology/class/StockItem/' | relative_url }}) |
| Range | `xsd:integer` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The quantity below which the line is reordered. For loan equipment, the number needed to keep every timetabled teaching room covered. Always zero for surplus.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`stock_item`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#stock_item) | `minimum` | `xsd:integer` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:minimumLevel a owl:DatatypeProperty ;
    rdfs:label "minimum level"@en ;
    rdfs:comment "The quantity below which the line is reordered. For loan equipment, the number needed to keep every timetabled teaching room covered. Always zero for surplus."@en ;
    rdfs:domain ontosage:StockItem ;
    rdfs:range xsd:integer .
```
{% endraw %}
