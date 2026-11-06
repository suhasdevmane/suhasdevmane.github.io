---
title: "ontosage:serviceFrequency"
layout: post
permalink: /ontology/property/serviceFrequency/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › serviceFrequency

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#serviceFrequency` |
| Label | service frequency |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

How often a recurring task falls due, in the register's own words.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`cleaning_task`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#cleaning_task) | `frequency` | `xsd:string` |
| [`patrol_checkpoint`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#patrol_checkpoint) | `frequency` | `xsd:string` |
| [`service_schedule`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#service_schedule) | `frequency` | `xsd:string` |
| [`waste_collection`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#waste_collection) | `service_period` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:serviceFrequency a owl:DatatypeProperty ;
    rdfs:label "service frequency"@en ;
    rdfs:comment "How often a recurring task falls due, in the register's own words."@en ;
    rdfs:range xsd:string .
```
{% endraw %}
