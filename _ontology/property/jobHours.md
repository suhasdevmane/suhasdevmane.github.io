---
title: "ontosage:jobHours"
layout: post
permalink: /ontology/property/jobHours/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › jobHours

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#jobHours` |
| Label | job hours |
| Kind | datatype property |
| Domain | [`ontosage:WorkOrder`]({{ '/ontology/class/WorkOrder/' | relative_url }}) |
| Range | `xsd:decimal` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Hours of work booked to the job: the time taken on a completed order, the allowance on an open one. In HOURS -- ontosage:expectedMinutes is minutes and holds a different unit for a different class.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`work_order`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#work_order) | `hours` | `xsd:decimal` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:jobHours a owl:DatatypeProperty ;
    rdfs:label "job hours"@en ;
    rdfs:comment "Hours of work booked to the job: the time taken on a completed order, the allowance on an open one. In HOURS -- ontosage:expectedMinutes is minutes and holds a different unit for a different class."@en ;
    rdfs:domain ontosage:WorkOrder ;
    rdfs:range xsd:decimal .
```
{% endraw %}
