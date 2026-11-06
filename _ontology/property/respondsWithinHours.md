---
title: "ontosage:respondsWithinHours"
layout: post
permalink: /ontology/property/respondsWithinHours/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › respondsWithinHours

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#respondsWithinHours` |
| Label | responds within hours |
| Kind | datatype property |
| Domain | [`ontosage:Department`]({{ '/ontology/class/Department/' | relative_url }}) |
| Range | `xsd:decimal` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Agreed target response time in hours for a routine request. Recorded so 'is this overdue?' is a computation rather than an opinion.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`department`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#department) | `responds_within_hours` | `xsd:decimal` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:respondsWithinHours a owl:DatatypeProperty ;
    rdfs:label "responds within hours"@en ;
    rdfs:comment "Agreed target response time in hours for a routine request. Recorded so 'is this overdue?' is a computation rather than an opinion."@en ;
    rdfs:domain ontosage:Department ;
    rdfs:range xsd:decimal .
```
{% endraw %}
