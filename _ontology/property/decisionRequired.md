---
title: "ontosage:decisionRequired"
layout: post
permalink: /ontology/property/decisionRequired/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › decisionRequired

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#decisionRequired` |
| Label | decision required |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:boolean` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Whether an authorised decision is owed before the next operational period. A column rather than prose, because it is the single thing a coordinator most needs listed.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`coordination_function`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#coordination_function) | `decision_needed` | `xsd:boolean` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:decisionRequired a owl:DatatypeProperty ;
    rdfs:label "decision required"@en ;
    rdfs:comment "Whether an authorised decision is owed before the next operational period. A column rather than prose, because it is the single thing a coordinator most needs listed."@en ;
    rdfs:range xsd:boolean .
```
{% endraw %}
