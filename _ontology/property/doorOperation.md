---
title: "ontosage:doorOperation"
layout: post
permalink: /ontology/property/doorOperation/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › doorOperation

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#doorOperation` |
| Label | door operation |
| Kind | datatype property |
| Domain | [`ontosage:AccessibleRoute`]({{ '/ontology/class/AccessibleRoute/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Automatic, assisted or manual, PER ROUTE — a step-free route can still carry a heavy manual door, which is the difference between usable and not.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`accessible_route`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#accessible_route) | `door_type` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:doorOperation a owl:DatatypeProperty ;
    rdfs:label "door operation"@en ;
    rdfs:comment "Automatic, assisted or manual, PER ROUTE — a step-free route can still carry a heavy manual door, which is the difference between usable and not."@en ;
    rdfs:domain ontosage:AccessibleRoute ;
    rdfs:range xsd:string .
```
{% endraw %}
