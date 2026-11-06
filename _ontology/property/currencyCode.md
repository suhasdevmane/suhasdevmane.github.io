---
title: "ontosage:currencyCode"
layout: post
permalink: /ontology/property/currencyCode/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › currencyCode

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#currencyCode` |
| Label | currency |
| Kind | datatype property |
| Domain | [`ontosage:Tariff`]({{ '/ontology/class/Tariff/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

ISO currency code. Stated in every cost answer — a bare number is ambiguous across buildings.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`tariff`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#tariff) | `currency` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:currencyCode a owl:DatatypeProperty ;
    rdfs:label "currency"@en ;
    rdfs:comment "ISO currency code. Stated in every cost answer — a bare number is ambiguous across buildings."@en ;
    rdfs:domain ontosage:Tariff ;
    rdfs:range xsd:string .
```
{% endraw %}
