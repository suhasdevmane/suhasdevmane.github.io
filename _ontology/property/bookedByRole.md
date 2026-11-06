---
title: "ontosage:bookedByRole"
layout: post
permalink: /ontology/property/bookedByRole/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › bookedByRole

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#bookedByRole` |
| Label | booked by role |
| Kind | datatype property |
| Domain | [`ontosage:Booking`]({{ '/ontology/class/Booking/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The organising ROLE or team. Never a named individual: an availability question does not need one.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`booking`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#booking) | `booked_by_role` | `xsd:string` |

## Turtle

Development notes were removed from one or more text values below; the source file holds the full text.

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:bookedByRole a owl:DatatypeProperty ;
    rdfs:label "booked by role"@en ;
    rdfs:comment "The organising ROLE or team. Never a named individual: an availability question does not need one."@en ;
    rdfs:domain ontosage:Booking ;
    rdfs:range xsd:string .
```
{% endraw %}
