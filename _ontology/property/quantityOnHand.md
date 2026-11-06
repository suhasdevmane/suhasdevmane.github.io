---
title: "ontosage:quantityOnHand"
layout: post
permalink: /ontology/property/quantityOnHand/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › quantityOnHand

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#quantityOnHand` |
| Label | quantity on hand |
| Kind | datatype property |
| Domain | [`ontosage:StockItem`]({{ '/ontology/class/StockItem/' | relative_url }}) |
| Range | `xsd:integer` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

What was counted on the shelf on lastCounted. Loan equipment that is out on loan is not on hand.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`stock_item`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#stock_item) | `on_hand` | `xsd:integer` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:quantityOnHand a owl:DatatypeProperty ;
    rdfs:label "quantity on hand"@en ;
    rdfs:comment "What was counted on the shelf on lastCounted. Loan equipment that is out on loan is not on hand."@en ;
    rdfs:domain ontosage:StockItem ;
    rdfs:range xsd:integer .
```
{% endraw %}
