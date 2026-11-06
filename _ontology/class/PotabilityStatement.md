---
title: "ontosage:PotabilityStatement"
layout: post
permalink: /ontology/class/PotabilityStatement/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › PotabilityStatement

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#PotabilityStatement` |
| Label | Potability statement |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A published statement about whether water from a given outlet or area is fit to drink, with the responsible owner and the date it was issued. A KnowledgeTopic subclass so the existing capability resolver answers it with no new code.

## Class hierarchy

Superclasses:

- [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}) › [`ontosage:KnowledgeTopic`]({{ '/ontology/class/KnowledgeTopic/' | relative_url }}) › **`ontosage:PotabilityStatement`**

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:appliesToOutlet`]({{ '/ontology/property/appliesToOutlet/' | relative_url }}) | object | not declared | this class |
| [`ontosage:potabilityAuthority`]({{ '/ontology/property/potabilityAuthority/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:potabilityIssuedOn`]({{ '/ontology/property/potabilityIssuedOn/' | relative_url }}) | datatype | `xsd:date` | this class |
| [`ontosage:potabilityValue`]({{ '/ontology/property/potabilityValue/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:answerText`]({{ '/ontology/property/answerText/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:KnowledgeTopic`]({{ '/ontology/class/KnowledgeTopic/' | relative_url }}) |
| [`ontosage:contactEmail`]({{ '/ontology/property/contactEmail/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:KnowledgeTopic`]({{ '/ontology/class/KnowledgeTopic/' | relative_url }}) |
| [`ontosage:contactPhone`]({{ '/ontology/property/contactPhone/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:KnowledgeTopic`]({{ '/ontology/class/KnowledgeTopic/' | relative_url }}) |
| [`ontosage:documentRef`]({{ '/ontology/property/documentRef/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:KnowledgeTopic`]({{ '/ontology/class/KnowledgeTopic/' | relative_url }}) |
| [`ontosage:effectiveDate`]({{ '/ontology/property/effectiveDate/' | relative_url }}) | datatype | `xsd:date` | [`ontosage:KnowledgeTopic`]({{ '/ontology/class/KnowledgeTopic/' | relative_url }}) |
| [`ontosage:infoUrl`]({{ '/ontology/property/infoUrl/' | relative_url }}) | datatype | `xsd:anyURI` | [`ontosage:KnowledgeTopic`]({{ '/ontology/class/KnowledgeTopic/' | relative_url }}) |
| [`ontosage:policyOwner`]({{ '/ontology/property/policyOwner/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:KnowledgeTopic`]({{ '/ontology/class/KnowledgeTopic/' | relative_url }}) |
| [`ontosage:reportTo`]({{ '/ontology/property/reportTo/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:KnowledgeTopic`]({{ '/ontology/class/KnowledgeTopic/' | relative_url }}) |
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

ontosage:PotabilityStatement a owl:Class ;
    rdfs:label "Potability statement"@en ;
    rdfs:comment "A published statement about whether water from a given outlet or area is fit to drink, with the responsible owner and the date it was issued. A KnowledgeTopic subclass so the existing capability resolver answers it with no new code."@en ;
    rdfs:subClassOf ontosage:KnowledgeTopic .
```
{% endraw %}
