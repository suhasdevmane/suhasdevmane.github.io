---
title: "ontosage:openException"
layout: post
permalink: /ontology/property/openException/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › openException

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#openException` |
| Label | open exception |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

What must be called out at handover, in the register's own words.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`patrol_checkpoint`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#patrol_checkpoint) | `exception` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:openException a owl:DatatypeProperty ;
    rdfs:label "open exception"@en ;
    rdfs:comment "What must be called out at handover, in the register's own words."@en ;
    rdfs:range xsd:string .
```
{% endraw %}
