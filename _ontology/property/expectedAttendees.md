---
title: "ontosage:expectedAttendees"
layout: post
permalink: /ontology/property/expectedAttendees/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › expectedAttendees

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#expectedAttendees` |
| Label | expected attendees |
| Kind | datatype property |
| Domain | [`ontosage:Booking`]({{ '/ontology/class/Booking/' | relative_url }}) |
| Range | `xsd:integer` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The group size the booking was made for, used for capacity and turnaround checks.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`booking`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#booking) | `expected_attendees` | `xsd:integer` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:expectedAttendees a owl:DatatypeProperty ;
    rdfs:label "expected attendees"@en ;
    rdfs:comment "The group size the booking was made for, used for capacity and turnaround checks."@en ;
    rdfs:domain ontosage:Booking ;
    rdfs:range xsd:integer .
```
{% endraw %}
