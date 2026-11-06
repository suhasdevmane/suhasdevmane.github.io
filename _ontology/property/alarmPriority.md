---
title: "ontosage:alarmPriority"
layout: post
permalink: /ontology/property/alarmPriority/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › alarmPriority

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#alarmPriority` |
| Label | alarm priority |
| Kind | datatype property |
| Domain | [`ontosage:AlarmEvent`]({{ '/ontology/class/AlarmEvent/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The priority the source system assigned to this activation. Declared separately from ontosage:priority, whose domain is ontosage:MaintenanceIssue: using that one on an alarm lets an RDFS reasoner type the alarm as a maintenance issue, and so as a KnowledgeTopic.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:alarmPriority a owl:DatatypeProperty ;
    rdfs:label "alarm priority"@en ;
    rdfs:comment "The priority the source system assigned to this activation. Declared separately from ontosage:priority, whose domain is ontosage:MaintenanceIssue: using that one on an alarm lets an RDFS reasoner type the alarm as a maintenance issue, and so as a KnowledgeTopic."@en ;
    rdfs:domain ontosage:AlarmEvent ;
    rdfs:range xsd:string .
```
{% endraw %}
