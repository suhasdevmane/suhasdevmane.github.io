---
title: "ontosage:Report"
layout: post
permalink: /ontology/class/Report/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › Report

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Report` |
| Label | Report |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A submitted fault/complaint/safety/feedback/suggestion record.

## Description

A stakeholder-submitted statement about the building requiring action or acknowledgement: a fault, complaint, safety concern, feedback, or suggestion. Created from a Module D Intent\_Report utterance.

## Examples

- "the toilet on floor 2 is leaking" -&gt; an ontosage:FaultReport.

## Class hierarchy

Superclasses: none (a root class).

Direct subclasses (5; 5 descendants in all):

- [`ontosage:Complaint`]({{ '/ontology/class/Complaint/' | relative_url }}) Complaint
- [`ontosage:FaultReport`]({{ '/ontology/class/FaultReport/' | relative_url }}) Fault report
- [`ontosage:Feedback`]({{ '/ontology/class/Feedback/' | relative_url }}) Feedback
- [`ontosage:SafetyReport`]({{ '/ontology/class/SafetyReport/' | relative_url }}) Safety report
- [`ontosage:Suggestion`]({{ '/ontology/class/Suggestion/' | relative_url }}) Suggestion

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:concernsIssue`]({{ '/ontology/property/concernsIssue/' | relative_url }}) | object | [`ontosage:MaintenanceIssue`]({{ '/ontology/class/MaintenanceIssue/' | relative_url }}) | this class |
| [`ontosage:reportedByRole`]({{ '/ontology/property/reportedByRole/' | relative_url }}) | object | [`ontosage:StakeholderRole`]({{ '/ontology/class/StakeholderRole/' | relative_url }}) | this class |
| [`ontosage:reportPriority`]({{ '/ontology/property/reportPriority/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:reportStatus`]({{ '/ontology/property/reportStatus/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:reportSubjectText`]({{ '/ontology/property/reportSubjectText/' | relative_url }}) | datatype | `xsd:string` | this class |

## SHACL shapes

- [`ontosage:ReportShape`]({{ '/ontology/vocabulary/shacl-shapes/' | relative_url }}#ReportShape) targets [`ontosage:Report`]({{ '/ontology/class/Report/' | relative_url }})
  - path [`ontosage:reportSubjectText`]({{ '/ontology/property/reportSubjectText/' | relative_url }}); min `1`; datatype `xsd:string`. Every ontosage:Report must record what is being reported (ontosage:reportSubjectText).

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:Report a owl:Class ;
    rdfs:label "Report"@en ;
    rdfs:comment "A stakeholder-submitted statement about the building requiring action or acknowledgement: a fault, complaint, safety concern, feedback, or suggestion. Created from a Module D Intent_Report utterance."@en ;
    skos:definition "A submitted fault/complaint/safety/feedback/suggestion record."@en ;
    skos:example "\"the toilet on floor 2 is leaking\" -> an ontosage:FaultReport." .
```
{% endraw %}
