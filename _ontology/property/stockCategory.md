---
title: "ontosage:stockCategory"
layout: post
permalink: /ontology/property/stockCategory/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › stockCategory

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#stockCategory` |
| Label | stock category |
| Kind | datatype property |
| Domain | [`ontosage:StockItem`]({{ '/ontology/class/StockItem/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The trade or service the item supports: cleaning, waste, HVAC, controls, lighting, audio-visual, IT, reception or furniture.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`stock_item`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#stock_item) | `category` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:stockCategory a owl:DatatypeProperty ;
    rdfs:label "stock category"@en ;
    rdfs:comment "The trade or service the item supports: cleaning, waste, HVAC, controls, lighting, audio-visual, IT, reception or furniture."@en ;
    rdfs:domain ontosage:StockItem ;
    rdfs:range xsd:string .
```
{% endraw %}
