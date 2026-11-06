---
title: "ontosage:faultState"
layout: post
permalink: /ontology/property/faultState/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › faultState

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#faultState` |
| Label | fault state |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Current fault condition, where the device or BMS reports one.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:faultState a owl:DatatypeProperty ;
    rdfs:label "fault state"@en ;
    rdfs:comment "Current fault condition, where the device or BMS reports one."@en ;
    rdfs:range xsd:string .
```
{% endraw %}
