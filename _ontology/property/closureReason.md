---
title: "ontosage:closureReason"
layout: post
permalink: /ontology/property/closureReason/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › closureReason

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#closureReason` |
| Label | closure reason |
| Kind | datatype property |
| Domain | [`ontosage:ClosurePeriod`]({{ '/ontology/class/ClosurePeriod/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Why the space is closed, in terms a person can act on.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:closureReason a owl:DatatypeProperty ;
    rdfs:label "closure reason"@en ;
    rdfs:comment "Why the space is closed, in terms a person can act on."@en ;
    rdfs:domain ontosage:ClosurePeriod ;
    rdfs:range xsd:string .
```
{% endraw %}
