---
title: "ontosage:codingCheckRequired"
layout: post
permalink: /ontology/property/codingCheckRequired/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › codingCheckRequired

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#codingCheckRequired` |
| Label | coding check required |
| Kind | datatype property |
| Domain | [`ontosage:CostLine`]({{ '/ontology/class/CostLine/' | relative_url }}) |
| Range | `xsd:boolean` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Flagged on the row rather than kept as a list, because a list goes stale the moment the row is corrected.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`cost_line`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#cost_line) | `coding_check` | `xsd:boolean` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:codingCheckRequired a owl:DatatypeProperty ;
    rdfs:label "coding check required"@en ;
    rdfs:comment "Flagged on the row rather than kept as a list, because a list goes stale the moment the row is corrected."@en ;
    rdfs:domain ontosage:CostLine ;
    rdfs:range xsd:boolean .
```
{% endraw %}
