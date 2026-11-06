---
title: "ontosage:Feedback"
layout: post
permalink: /ontology/class/Feedback/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › Feedback

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Feedback` |
| Label | Feedback |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

General feedback about the building or OntoSage itself.

## Examples

- "the new signage is really helpful".

## Class hierarchy

Superclasses:

- [`ontosage:Report`]({{ '/ontology/class/Report/' | relative_url }}) › **`ontosage:Feedback`**

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

ontosage:Feedback a owl:Class ;
    rdfs:label "Feedback"@en ;
    rdfs:comment "General feedback about the building or OntoSage itself."@en ;
    rdfs:subClassOf ontosage:Report ;
    skos:example "\"the new signage is really helpful\"." .
```
{% endraw %}
