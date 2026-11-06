---
title: "ontosage:ParkingArea"
layout: post
permalink: /ontology/class/ParkingArea/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › ParkingArea

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#ParkingArea` |
| Label | Parking area |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A car park or parking level. Separate from ontosage:BikeStorage (cycles) and from the accessible bays an AccessibilityFeature declares. Holding it as an Amenity lets 'where can I park' be located; how many bays are FREE is a measurement, and belongs to whatever point the building records it at, never to this record.

## Examples

- "where can I park?" -&gt; the parking area; "how many bays are free?" -&gt; the parking occupancy point.

## Lay terms

Plain-language phrases declared on this term with `ontosage:layTerms`. A question that contains one of them can be matched to this term. (12)

`car park`, `car parking`, `car parks`, `free parking`, `park my car`, `parking bay`, `parking bays`, `parking space`, `parking spaces`, `staff parking`, `visitor parking`, `where can i park`

## Class hierarchy

Superclasses:

- [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}) › [`ontosage:Amenity`]({{ '/ontology/class/Amenity/' | relative_url }}) › **`ontosage:ParkingArea`**

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
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
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:ParkingArea a owl:Class ;
    rdfs:label "Parking area"@en ;
    ontosage:layTerms "car park",
        "car parking",
        "car parks",
        "free parking",
        "park my car",
        "parking bay",
        "parking bays",
        "parking space",
        "parking spaces",
        "staff parking",
        "visitor parking",
        "where can i park" ;
    rdfs:comment "A car park or parking level. Separate from ontosage:BikeStorage (cycles) and from the accessible bays an AccessibilityFeature declares. Holding it as an Amenity lets 'where can I park' be located; how many bays are FREE is a measurement, and belongs to whatever point the building records it at, never to this record."@en ;
    rdfs:subClassOf ontosage:Amenity ;
    skos:example "\"where can I park?\" -> the parking area; \"how many bays are free?\" -> the parking occupancy point." .
```
{% endraw %}
