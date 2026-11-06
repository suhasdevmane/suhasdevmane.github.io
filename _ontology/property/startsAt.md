---
title: "ontosage:startsAt"
layout: post
permalink: /ontology/property/startsAt/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › startsAt

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#startsAt` |
| Label | starts at |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The schema gives no definition for this term.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`event_activity`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#event_activity) | `starts` | `xsd:string` |
| [`public_event`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#public_event) | `starts` | `xsd:string` |
| [`timetabled_session`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#timetabled_session) | `starts_at` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:startsAt a owl:DatatypeProperty ;
    rdfs:label "starts at"@en ;
    rdfs:range xsd:string .
```
{% endraw %}
