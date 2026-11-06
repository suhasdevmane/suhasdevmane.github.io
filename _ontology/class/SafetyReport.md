---
title: "ontosage:SafetyReport"
layout: post
permalink: /ontology/class/SafetyReport/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › SafetyReport

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#SafetyReport` |
| Label | Safety report |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A health/safety concern or hazard (blocked exit, spill, trip hazard) — usually high priority.

## Examples

- "the fire exit on floor 1 is blocked".

## Class hierarchy

Superclasses:

- [`ontosage:Report`]({{ '/ontology/class/Report/' | relative_url }}) › **`ontosage:SafetyReport`**

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:concernsIssue`]({{ '/ontology/property/concernsIssue/' | relative_url }}) | object | [`ontosage:MaintenanceIssue`]({{ '/ontology/class/MaintenanceIssue/' | relative_url }}) | [`ontosage:Report`]({{ '/ontology/class/Report/' | relative_url }}) |
| [`ontosage:reportedByRole`]({{ '/ontology/property/reportedByRole/' | relative_url }}) | object | [`ontosage:StakeholderRole`]({{ '/ontology/class/StakeholderRole/' | relative_url }}) | [`ontosage:Report`]({{ '/ontology/class/Report/' | relative_url }}) |
| [`ontosage:reportPriority`]({{ '/ontology/property/reportPriority/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:Report`]({{ '/ontology/class/Report/' | relative_url }}) |
| [`ontosage:reportStatus`]({{ '/ontology/property/reportStatus/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:Report`]({{ '/ontology/class/Report/' | relative_url }}) |
| [`ontosage:reportSubjectText`]({{ '/ontology/property/reportSubjectText/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:Report`]({{ '/ontology/class/Report/' | relative_url }}) |

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

ontosage:SafetyReport a owl:Class ;
    rdfs:label "Safety report"@en ;
    rdfs:comment "A health/safety concern or hazard (blocked exit, spill, trip hazard) — usually high priority."@en ;
    rdfs:subClassOf ontosage:Report ;
    skos:example "\"the fire exit on floor 1 is blocked\"." .
```
{% endraw %}
