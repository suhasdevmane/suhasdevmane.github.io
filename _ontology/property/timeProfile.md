---
title: "ontosage:timeProfile"
layout: post
permalink: /ontology/property/timeProfile/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › timeProfile

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#timeProfile` |
| Label | time profile |
| Kind | datatype property |
| Domain | [`ontosage:AccessPermission`]({{ '/ontology/class/AccessPermission/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The schema gives no definition for this term.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`access_permission`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#access_permission) | `time_profile` | `xsd:string` |
| [`timetabled_session`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#timetabled_session) | `weekday` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:timeProfile a owl:DatatypeProperty ;
    rdfs:label "time profile"@en ;
    rdfs:domain ontosage:AccessPermission ;
    rdfs:range xsd:string .
```
{% endraw %}
