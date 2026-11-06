---
title: "ontosage:KnowledgeTopic"
layout: post
permalink: /ontology/class/KnowledgeTopic/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › KnowledgeTopic

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#KnowledgeTopic` |
| Label | Knowledge topic |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

An informational, procedural, or maintenance topic a stakeholder can ask about.

## Description

A non-physical capability: an informational fact, a how-to procedure, or a maintenance-issue reporting route. Answered from its ontosage:answerText plus contacts/steps — this is what lets policy/how-to/report questions be answered from triples instead of frozen prose.

## Class hierarchy

Superclasses:

- [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}) › **`ontosage:KnowledgeTopic`**

Direct subclasses (5; 5 descendants in all):

- [`ontosage:InformationTopic`]({{ '/ontology/class/InformationTopic/' | relative_url }}) Informational topic
- [`ontosage:MaintenanceIssue`]({{ '/ontology/class/MaintenanceIssue/' | relative_url }}) Maintenance / fault issue
- [`ontosage:Policy`]({{ '/ontology/class/Policy/' | relative_url }}) Policy
- [`ontosage:PotabilityStatement`]({{ '/ontology/class/PotabilityStatement/' | relative_url }}) Potability statement
- [`ontosage:Procedure`]({{ '/ontology/class/Procedure/' | relative_url }}) Procedure (how-to)

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:answerText`]({{ '/ontology/property/answerText/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:contactEmail`]({{ '/ontology/property/contactEmail/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:contactPhone`]({{ '/ontology/property/contactPhone/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:documentRef`]({{ '/ontology/property/documentRef/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:effectiveDate`]({{ '/ontology/property/effectiveDate/' | relative_url }}) | datatype | `xsd:date` | this class |
| [`ontosage:infoUrl`]({{ '/ontology/property/infoUrl/' | relative_url }}) | datatype | `xsd:anyURI` | this class |
| [`ontosage:policyOwner`]({{ '/ontology/property/policyOwner/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:reportTo`]({{ '/ontology/property/reportTo/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:capabilityCategory`]({{ '/ontology/property/capabilityCategory/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}) |
| [`ontosage:layTerms`]({{ '/ontology/property/layTerms/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}) |
| [`ontosage:locatedIn`]({{ '/ontology/property/locatedIn/' | relative_url }}) | object | [`brick:Location`](https://ontology.brickschema.org/1.4/#brick:Location) | [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}) |
| [`ontosage:note`]({{ '/ontology/property/note/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}) |
| [`ontosage:openingHours`]({{ '/ontology/property/openingHours/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}) |
| [`ontosage:relatedTopic`]({{ '/ontology/property/relatedTopic/' | relative_url }}) | object | [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}) | [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}) |
| [`ontosage:servesFloor`]({{ '/ontology/property/servesFloor/' | relative_url }}) | object | [`brick:Floor`](https://ontology.brickschema.org/1.4/#brick:Floor) | [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}) |
| [`ontosage:usageFee`]({{ '/ontology/property/usageFee/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}) |

## SHACL shapes

- [`ontosage:CapabilityShape`]({{ '/ontology/vocabulary/shacl-shapes/' | relative_url }}#CapabilityShape) targets [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }})
  - path [`ontosage:layTerms`]({{ '/ontology/property/layTerms/' | relative_url }}); min `1`; datatype `xsd:string`. Every ontosage:Capability should carry at least one ontosage:layTerms value — it is how a stakeholder question is matched to it.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:KnowledgeTopic a owl:Class ;
    rdfs:label "Knowledge topic"@en ;
    rdfs:comment "A non-physical capability: an informational fact, a how-to procedure, or a maintenance-issue reporting route. Answered from its ontosage:answerText plus contacts/steps — this is what lets policy/how-to/report questions be answered from triples instead of frozen prose."@en ;
    rdfs:subClassOf ontosage:Capability ;
    skos:definition "An informational, procedural, or maintenance topic a stakeholder can ask about."@en .
```
{% endraw %}
