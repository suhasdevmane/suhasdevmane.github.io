---
title: "ontosage:stockUnit"
layout: post
permalink: /ontology/property/stockUnit/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › stockUnit

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#stockUnit` |
| Label | stock unit |
| Kind | datatype property |
| Domain | [`ontosage:StockItem`]({{ '/ontology/class/StockItem/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

What one counted unit is: cartridges, cases, sets, receivers. A quantity without its unit cannot be compared with a delivery.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`stock_item`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#stock_item) | `unit` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:stockUnit a owl:DatatypeProperty ;
    rdfs:label "stock unit"@en ;
    rdfs:comment "What one counted unit is: cartridges, cases, sets, receivers. A quantity without its unit cannot be compared with a delivery."@en ;
    rdfs:domain ontosage:StockItem ;
    rdfs:range xsd:string .
```
{% endraw %}
