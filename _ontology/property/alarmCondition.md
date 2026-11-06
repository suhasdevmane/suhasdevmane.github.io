---
title: "ontosage:alarmCondition"
layout: post
permalink: /ontology/property/alarmCondition/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › alarmCondition

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#alarmCondition` |
| Label | alarm condition |
| Kind | datatype property |
| Domain | [`ontosage:AlarmEvent`]({{ '/ontology/class/AlarmEvent/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The condition the alarm reports, in the source system's own words (frost protection trip, high temperature, filter dirty). Read as recorded; never normalised into a severity, which the record carries separately.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:alarmCondition a owl:DatatypeProperty ;
    rdfs:label "alarm condition"@en ;
    rdfs:comment "The condition the alarm reports, in the source system's own words (frost protection trip, high temperature, filter dirty). Read as recorded; never normalised into a severity, which the record carries separately."@en ;
    rdfs:domain ontosage:AlarmEvent ;
    rdfs:range xsd:string .
```
{% endraw %}
