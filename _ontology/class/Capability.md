---
title: "ontosage:Capability"
layout: post
permalink: /ontology/class/Capability/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › Capability

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Capability` |
| Label | Capability |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Anything a stakeholder can ask a building about via OntoSage.

## Description

Abstract superclass of everything a building stakeholder can ask OntoSage about that Brick does not already model — a physical amenity or a knowledge topic.

## Class hierarchy

Superclasses: none (a root class).

Direct subclasses (2; 28 descendants in all):

- [`ontosage:Amenity`]({{ '/ontology/class/Amenity/' | relative_url }}) Amenity
- [`ontosage:KnowledgeTopic`]({{ '/ontology/class/KnowledgeTopic/' | relative_url }}) Knowledge topic

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:capabilityCategory`]({{ '/ontology/property/capabilityCategory/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:layTerms`]({{ '/ontology/property/layTerms/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:locatedIn`]({{ '/ontology/property/locatedIn/' | relative_url }}) | object | [`brick:Location`](https://ontology.brickschema.org/1.4/#brick:Location) | this class |
| [`ontosage:note`]({{ '/ontology/property/note/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:openingHours`]({{ '/ontology/property/openingHours/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:relatedTopic`]({{ '/ontology/property/relatedTopic/' | relative_url }}) | object | [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}) | this class |
| [`ontosage:servesFloor`]({{ '/ontology/property/servesFloor/' | relative_url }}) | object | [`brick:Floor`](https://ontology.brickschema.org/1.4/#brick:Floor) | this class |
| [`ontosage:usageFee`]({{ '/ontology/property/usageFee/' | relative_url }}) | datatype | `xsd:string` | this class |

## Used as the range of

| Property | Kind | Domain |
|---|---|---|
| [`ontosage:relatedTopic`]({{ '/ontology/property/relatedTopic/' | relative_url }}) | object | [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}) |

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

ontosage:Capability a owl:Class ;
    rdfs:label "Capability"@en ;
    rdfs:comment "Abstract superclass of everything a building stakeholder can ask OntoSage about that Brick does not already model — a physical amenity or a knowledge topic."@en ;
    skos:definition "Anything a stakeholder can ask a building about via OntoSage."@en .
```
{% endraw %}
