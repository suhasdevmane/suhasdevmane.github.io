---
title: "ontosage:isOptional"
layout: post
permalink: /ontology/property/isOptional/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › isOptional

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#isOptional` |
| Label | is optional |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:boolean` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Whether the activity can be skipped. Recorded by whoever owns the programme, never judged.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`event_activity`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#event_activity) | `optional` | `xsd:boolean` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:isOptional a owl:DatatypeProperty ;
    rdfs:label "is optional"@en ;
    rdfs:comment "Whether the activity can be skipped. Recorded by whoever owns the programme, never judged."@en ;
    rdfs:range xsd:boolean .
```
{% endraw %}
