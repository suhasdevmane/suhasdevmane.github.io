---
title: "ontosage:isStepFree"
layout: post
permalink: /ontology/property/isStepFree/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › isStepFree

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#isStepFree` |
| Label | is step free |
| Kind | datatype property |
| Domain | [`ontosage:AccessibleRoute`]({{ '/ontology/class/AccessibleRoute/' | relative_url }}) |
| Range | `xsd:boolean` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

False is recorded, not omitted: a route missing from the register is unknown, while a route marked false is known to be unsuitable, and an answer must be able to tell those apart.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`accessible_route`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#accessible_route) | `step_free` | `xsd:boolean` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:isStepFree a owl:DatatypeProperty ;
    rdfs:label "is step free"@en ;
    rdfs:comment "False is recorded, not omitted: a route missing from the register is unknown, while a route marked false is known to be unsuitable, and an answer must be able to tell those apart."@en ;
    rdfs:domain ontosage:AccessibleRoute ;
    rdfs:range xsd:boolean .
```
{% endraw %}
