---
title: "ontosage:isStatutory"
layout: post
permalink: /ontology/property/isStatutory/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › isStatutory

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#isStatutory` |
| Label | is statutory |
| Kind | datatype property |
| Domain | [`ontosage:ServiceSchedule`]({{ '/ontology/class/ServiceSchedule/' | relative_url }}) |
| Range | `xsd:boolean` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Whether missing this task is a legal failure rather than an inconvenience: a missed weekly fire alarm test is reportable, a lift without a current examination may not run, a missed carpet clean is neither. Recorded by the owner of the schedule, never judged. It is the OPPOSITE of ontosage:isOptional, which an earlier mapping wrongly used for it.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`service_schedule`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#service_schedule) | `statutory` | `xsd:boolean` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:isStatutory a owl:DatatypeProperty ;
    rdfs:label "is statutory"@en ;
    rdfs:comment "Whether missing this task is a legal failure rather than an inconvenience: a missed weekly fire alarm test is reportable, a lift without a current examination may not run, a missed carpet clean is neither. Recorded by the owner of the schedule, never judged. It is the OPPOSITE of ontosage:isOptional, which an earlier mapping wrongly used for it."@en ;
    rdfs:domain ontosage:ServiceSchedule ;
    rdfs:range xsd:boolean .
```
{% endraw %}
