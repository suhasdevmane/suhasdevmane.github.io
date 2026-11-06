---
title: "ontosage:varianceCause"
layout: post
permalink: /ontology/property/varianceCause/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › varianceCause

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#varianceCause` |
| Label | variance cause |
| Kind | datatype property |
| Domain | [`ontosage:CostLine`]({{ '/ontology/class/CostLine/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Price, quantity, timing or scope. Recorded, because the movement alone cannot say which and the remedies differ.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`cost_line`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#cost_line) | `variance_cause` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:varianceCause a owl:DatatypeProperty ;
    rdfs:label "variance cause"@en ;
    rdfs:comment "Price, quantity, timing or scope. Recorded, because the movement alone cannot say which and the remedies differ."@en ;
    rdfs:domain ontosage:CostLine ;
    rdfs:range xsd:string .
```
{% endraw %}
