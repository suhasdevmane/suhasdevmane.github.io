---
title: "ontosage:usedFor"
layout: post
permalink: /ontology/property/usedFor/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › usedFor

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#usedFor` |
| Label | used for |
| Kind | datatype property |
| Domain | [`ontosage:StockItem`]({{ '/ontology/class/StockItem/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The asset, system or task the stock supports, by the name the asset register or service schedule uses.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`stock_item`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#stock_item) | `used_for` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:usedFor a owl:DatatypeProperty ;
    rdfs:label "used for"@en ;
    rdfs:comment "The asset, system or task the stock supports, by the name the asset register or service schedule uses."@en ;
    rdfs:domain ontosage:StockItem ;
    rdfs:range xsd:string .
```
{% endraw %}
