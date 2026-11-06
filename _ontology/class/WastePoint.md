---
title: "ontosage:WastePoint"
layout: post
permalink: /ontology/class/WastePoint/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › WastePoint

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#WastePoint` |
| Label | Waste or recycling point |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A bin, cluster of bins or collection point where waste is deposited. An Amenity subclass so the existing capability chain locates it -- 'where are the recycling bins' needs authoring, not engineering.

## Lay terms

Plain-language phrases declared on this term with `ontosage:layTerms`. A question that contains one of them can be matched to this term. (11)

`litter bin`, `litter bins`, `recycling point`, `recycling points`, `recycling station`, `recycling stations`, `trash can`, `trash cans`, `where are the bins`, `where are the recycling bins`, `where can i recycle`

## Class hierarchy

Superclasses:

- [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}) › [`ontosage:Amenity`]({{ '/ontology/class/Amenity/' | relative_url }}) › **`ontosage:WastePoint`**

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:streamCapacityLitres`]({{ '/ontology/property/streamCapacityLitres/' | relative_url }}) | datatype | `xsd:decimal` | this class |
| [`ontosage:wasteStream`]({{ '/ontology/property/wasteStream/' | relative_url }}) | datatype | `xsd:string` | this class |
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

ontosage:WastePoint a owl:Class ;
    rdfs:label "Waste or recycling point"@en ;
    ontosage:layTerms "litter bin",
        "litter bins",
        "recycling point",
        "recycling points",
        "recycling station",
        "recycling stations",
        "trash can",
        "trash cans",
        "where are the bins",
        "where are the recycling bins",
        "where can i recycle" ;
    rdfs:comment "A bin, cluster of bins or collection point where waste is deposited. An Amenity subclass so the existing capability chain locates it -- 'where are the recycling bins' needs authoring, not engineering."@en ;
    rdfs:subClassOf ontosage:Amenity .
```
{% endraw %}
