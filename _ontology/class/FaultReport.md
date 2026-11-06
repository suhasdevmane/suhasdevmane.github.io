---
title: "ontosage:FaultReport"
layout: post
permalink: /ontology/class/FaultReport/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › FaultReport

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#FaultReport` |
| Label | Fault report |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A reported equipment/facility fault (leak, broken light, broken lift). Typically ties to a Module A ontosage:MaintenanceIssue and, via ontosage:aboutEquipment, to the brick:Equipment.

## Examples

- "the lift is stuck".

## Class hierarchy

Superclasses:

- [`ontosage:Report`]({{ '/ontology/class/Report/' | relative_url }}) › **`ontosage:FaultReport`**

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

ontosage:FaultReport a owl:Class ;
    rdfs:label "Fault report"@en ;
    rdfs:comment "A reported equipment/facility fault (leak, broken light, broken lift). Typically ties to a Module A ontosage:MaintenanceIssue and, via ontosage:aboutEquipment, to the brick:Equipment."@en ;
    rdfs:subClassOf ontosage:Report ;
    skos:example "\"the lift is stuck\"." .
```
{% endraw %}
