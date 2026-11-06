---
title: "ontosage:budgetAmount"
layout: post
permalink: /ontology/property/budgetAmount/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › budgetAmount

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#budgetAmount` |
| Label | budget amount |
| Kind | datatype property |
| Domain | [`ontosage:CostLine`]({{ '/ontology/class/CostLine/' | relative_url }}) |
| Range | `xsd:decimal` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The schema gives no definition for this term.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`cost_line`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#cost_line) | `budget` | `xsd:decimal` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:budgetAmount a owl:DatatypeProperty ;
    rdfs:label "budget amount"@en ;
    rdfs:domain ontosage:CostLine ;
    rdfs:range xsd:decimal .
```
{% endraw %}
