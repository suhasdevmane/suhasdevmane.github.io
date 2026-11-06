---
title: "ontosage:committedAmount"
layout: post
permalink: /ontology/property/committedAmount/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › committedAmount

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#committedAmount` |
| Label | committed amount |
| Kind | datatype property |
| Domain | [`ontosage:CostLine`]({{ '/ontology/class/CostLine/' | relative_url }}) |
| Range | `xsd:decimal` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Money a purchase order has claimed but not yet spent. Separate from actual so a free balance cannot be overstated.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`cost_line`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#cost_line) | `committed` | `xsd:decimal` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:committedAmount a owl:DatatypeProperty ;
    rdfs:label "committed amount"@en ;
    rdfs:comment "Money a purchase order has claimed but not yet spent. Separate from actual so a free balance cannot be overstated."@en ;
    rdfs:domain ontosage:CostLine ;
    rdfs:range xsd:decimal .
```
{% endraw %}
