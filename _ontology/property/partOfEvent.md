---
title: "ontosage:partOfEvent"
layout: post
permalink: /ontology/property/partOfEvent/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › partOfEvent

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#partOfEvent` |
| Label | part of event |
| Kind | datatype property |
| Domain | [`ontosage:EventActivity`]({{ '/ontology/class/EventActivity/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The PublicEvent this activity belongs to, by record id, so the two registers join.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`event_activity`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#event_activity) | `event` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:partOfEvent a owl:DatatypeProperty ;
    rdfs:label "part of event"@en ;
    rdfs:comment "The PublicEvent this activity belongs to, by record id, so the two registers join."@en ;
    rdfs:domain ontosage:EventActivity ;
    rdfs:range xsd:string .
```
{% endraw %}
