---
title: "ontosage:presentedRole"
layout: post
permalink: /ontology/property/presentedRole/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › presentedRole

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#presentedRole` |
| Label | presented role |
| Kind | datatype property |
| Domain | [`ontosage:AccessEvent`]({{ '/ontology/class/AccessEvent/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The ROLE TEMPLATE of the credential presented (caretaking and cleaning, academic staff, contractor) — NEVER an individual, a card number or anything that identifies a person. Per-person access questions are refused by inference-class policy whatever this field holds.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:presentedRole a owl:DatatypeProperty ;
    rdfs:label "presented role"@en ;
    rdfs:comment "The ROLE TEMPLATE of the credential presented (caretaking and cleaning, academic staff, contractor) — NEVER an individual, a card number or anything that identifies a person. Per-person access questions are refused by inference-class policy whatever this field holds."@en ;
    rdfs:domain ontosage:AccessEvent ;
    rdfs:range xsd:string .
```
{% endraw %}
