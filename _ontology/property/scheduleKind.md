---
title: "ontosage:scheduleKind"
layout: post
permalink: /ontology/property/scheduleKind/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › scheduleKind

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#scheduleKind` |
| Label | schedule kind |
| Kind | datatype property |
| Domain | [`ontosage:ServiceSchedule`]({{ '/ontology/class/ServiceSchedule/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

cleaning | waste\_collection | planned\_maintenance | planned\_shutdown | inspection.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`service_schedule`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#service_schedule) | `category` | `xsd:string` |
| [`work_order`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#work_order) | `category` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:scheduleKind a owl:DatatypeProperty ;
    rdfs:label "schedule kind"@en ;
    rdfs:comment "cleaning | waste_collection | planned_maintenance | planned_shutdown | inspection."@en ;
    rdfs:domain ontosage:ServiceSchedule ;
    rdfs:range xsd:string .
```
{% endraw %}
