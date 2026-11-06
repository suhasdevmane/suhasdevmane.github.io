---
title: "ontosage:AccessibilityFeature"
layout: post
permalink: /ontology/class/AccessibilityFeature/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › AccessibilityFeature

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#AccessibilityFeature` |
| Label | Accessibility feature |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A feature provided for accessibility: hearing loop, tactile paving, Changing Places facility, accessible WC, power-assisted door, accessible parking bay. An Amenity subclass so the existing capability resolver locates it with no new code.

## Lay terms

Plain-language phrases declared on this term with `ontosage:layTerms`. A question that contains one of them can be matched to this term. (25)

`accessible bay`, `accessible bays`, `accessible parking`, `accessible toilet`, `accessible toilets`, `accessible wc`, `adjustable desk`, `blue badge parking`, `changing places`, `disabled bay`, `disabled bays`, `disabled parking`, `disabled toilet`, `disabled toilets`, `handicap parking`, `handicapped bay`, `handicapped bays`, `handicapped parking`, `hearing loops`, `height adjustable desk`, `induction loop`, `induction loops`, `power assisted door`, `power-assisted door`, `tactile paving`

## Class hierarchy

Superclasses:

- [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}) › [`ontosage:Amenity`]({{ '/ontology/class/Amenity/' | relative_url }}) › **`ontosage:AccessibilityFeature`**

Direct subclasses (1; 1 descendants in all):

- [`ontosage:AccessibleToilet`]({{ '/ontology/class/AccessibleToilet/' | relative_url }}) Accessible toilet

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:accessibilityKind`]({{ '/ontology/property/accessibilityKind/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:accessibilityVerified`]({{ '/ontology/property/accessibilityVerified/' | relative_url }}) | datatype | `xsd:boolean` | this class |
| [`ontosage:accessibilityVerifiedOn`]({{ '/ontology/property/accessibilityVerifiedOn/' | relative_url }}) | datatype | `xsd:date` | this class |
| [`ontosage:amenityStatus`]({{ '/ontology/property/amenityStatus/' | relative_url }}) | object | [`ontosage:AssetStatus`]({{ '/ontology/class/AssetStatus/' | relative_url }}) | [`ontosage:Amenity`]({{ '/ontology/class/Amenity/' | relative_url }}) |
| [`ontosage:locationText`]({{ '/ontology/property/locationText/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:Amenity`]({{ '/ontology/class/Amenity/' | relative_url }}) |
| [`ontosage:onFloor`]({{ '/ontology/property/onFloor/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:Amenity`]({{ '/ontology/class/Amenity/' | relative_url }}) |
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

ontosage:AccessibilityFeature a owl:Class ;
    rdfs:label "Accessibility feature"@en ;
    ontosage:layTerms "accessible bay",
        "accessible bays",
        "accessible parking",
        "accessible toilet",
        "accessible toilets",
        "accessible wc",
        "adjustable desk",
        "blue badge parking",
        "changing places",
        "disabled bay",
        "disabled bays",
        "disabled parking",
        "disabled toilet",
        "disabled toilets",
        "handicap parking",
        "handicapped bay",
        "handicapped bays",
        "handicapped parking",
        "hearing loops",
        "height adjustable desk",
        "induction loop",
        "induction loops",
        "power assisted door",
        "power-assisted door",
        "tactile paving" ;
    rdfs:comment "A feature provided for accessibility: hearing loop, tactile paving, Changing Places facility, accessible WC, power-assisted door, accessible parking bay. An Amenity subclass so the existing capability resolver locates it with no new code."@en ;
    rdfs:subClassOf ontosage:Amenity .
```
{% endraw %}
