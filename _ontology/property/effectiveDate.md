---
title: "ontosage:effectiveDate"
layout: post
permalink: /ontology/property/effectiveDate/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › effectiveDate

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#effectiveDate` |
| Label | effective date |
| Kind | datatype property |
| Domain | [`ontosage:KnowledgeTopic`]({{ '/ontology/class/KnowledgeTopic/' | relative_url }}) |
| Range | `xsd:date` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Date this policy came into force. Lets an answer say WHICH version it is quoting, and lets a superseded policy be spotted rather than silently answered from.

## Examples

- "2026-01-01"^^xsd:date

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`timetabled_session`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#timetabled_session) | `session_date` | `xsd:date` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:effectiveDate a owl:DatatypeProperty ;
    rdfs:label "effective date"@en ;
    rdfs:comment "Date this policy came into force. Lets an answer say WHICH version it is quoting, and lets a superseded policy be spotted rather than silently answered from."@en ;
    rdfs:domain ontosage:KnowledgeTopic ;
    rdfs:range xsd:date ;
    skos:example "\"2026-01-01\"^^xsd:date" .
```
{% endraw %}
