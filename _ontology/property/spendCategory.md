---
title: "ontosage:spendCategory"
layout: post
permalink: /ontology/property/spendCategory/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › spendCategory

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#spendCategory` |
| Label | spend category |
| Kind | datatype property |
| Domain | [`ontosage:CostLine`]({{ '/ontology/class/CostLine/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Planned, reactive, statutory, contract-fixed or demand-led. Asked directly: what proportion of spend is each.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`cost_line`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#cost_line) | `category` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:spendCategory a owl:DatatypeProperty ;
    rdfs:label "spend category"@en ;
    rdfs:comment "Planned, reactive, statutory, contract-fixed or demand-led. Asked directly: what proportion of spend is each."@en ;
    rdfs:domain ontosage:CostLine ;
    rdfs:range xsd:string .
```
{% endraw %}
