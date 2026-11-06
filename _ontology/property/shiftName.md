---
title: "ontosage:shiftName"
layout: post
permalink: /ontology/property/shiftName/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › shiftName

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#shiftName` |
| Label | shift |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The working period that owns a task.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`cleaning_task`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#cleaning_task) | `shift` | `xsd:string` |
| [`patrol_checkpoint`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#patrol_checkpoint) | `shift` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:shiftName a owl:DatatypeProperty ;
    rdfs:label "shift"@en ;
    rdfs:comment "The working period that owns a task."@en ;
    rdfs:range xsd:string .
```
{% endraw %}
