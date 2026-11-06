---
title: "ontosage:Amenity"
layout: post
permalink: /ontology/class/Amenity/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › Amenity

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Amenity` |
| Label | Amenity |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A physical building facility or service with a human-readable location and features.

## Description

A physical facility or service a stakeholder can locate and use (prayer room, café, lift, showers, …). Distinct from a brick:Point/brick:Equipment: it is described for humans, and MAY be tied to a brick:Location via ontosage:locatedIn.

## Examples

- A multi-faith prayer room on Floor 1; the main passenger lift; the ground-floor café.

## Class hierarchy

Superclasses:

- [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}) › **`ontosage:Amenity`**

Direct subclasses (20; 21 descendants in all):

- [`ontosage:AccessibilityFeature`]({{ '/ontology/class/AccessibilityFeature/' | relative_url }}) Accessibility feature
- [`ontosage:AssemblyPoint`]({{ '/ontology/class/AssemblyPoint/' | relative_url }}) Fire assembly point
- [`ontosage:BikeStorage`]({{ '/ontology/class/BikeStorage/' | relative_url }}) Bicycle storage
- [`ontosage:Cafe`]({{ '/ontology/class/Cafe/' | relative_url }}) Café / catering
- [`ontosage:DrinkingWater`]({{ '/ontology/class/DrinkingWater/' | relative_url }}) Drinking water
- [`ontosage:Facility`]({{ '/ontology/class/Facility/' | relative_url }}) Named facility
- [`ontosage:FirstAidPoint`]({{ '/ontology/class/FirstAidPoint/' | relative_url }}) First aid / defibrillator
- [`ontosage:Kitchenette`]({{ '/ontology/class/Kitchenette/' | relative_url }}) Kitchenette / tea point
- [`ontosage:Lift`]({{ '/ontology/class/Lift/' | relative_url }}) Passenger lift / elevator
- [`ontosage:Locker`]({{ '/ontology/class/Locker/' | relative_url }}) Locker bank
- [`ontosage:NursingRoom`]({{ '/ontology/class/NursingRoom/' | relative_url }}) Nursing / feeding room
- [`ontosage:ParkingArea`]({{ '/ontology/class/ParkingArea/' | relative_url }}) Parking area
- [`ontosage:PrayerRoom`]({{ '/ontology/class/PrayerRoom/' | relative_url }}) Prayer / reflection room
- [`ontosage:PrinterPoint`]({{ '/ontology/class/PrinterPoint/' | relative_url }}) Printer / copy point
- [`ontosage:Service`]({{ '/ontology/class/Service/' | relative_url }}) Building service
- [`ontosage:ShowerFacility`]({{ '/ontology/class/ShowerFacility/' | relative_url }}) Shower facility
- [`ontosage:StudyArea`]({{ '/ontology/class/StudyArea/' | relative_url }}) Study / workspace area
- [`ontosage:ToiletFacility`]({{ '/ontology/class/ToiletFacility/' | relative_url }}) Toilet facility
- [`ontosage:VendingMachine`]({{ '/ontology/class/VendingMachine/' | relative_url }}) Vending machine
- [`ontosage:WastePoint`]({{ '/ontology/class/WastePoint/' | relative_url }}) Waste or recycling point

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:amenityStatus`]({{ '/ontology/property/amenityStatus/' | relative_url }}) | object | [`ontosage:AssetStatus`]({{ '/ontology/class/AssetStatus/' | relative_url }}) | this class |
| [`ontosage:locationText`]({{ '/ontology/property/locationText/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:onFloor`]({{ '/ontology/property/onFloor/' | relative_url }}) | datatype | `xsd:string` | this class |
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

## Competency questions

- What amenities are on floor 1?
- Where is the prayer room / café / nearest lift?

## Example SPARQL

{% raw %}
```sparql
# "where can I pray?" — match lay terms, return the human location.
SELECT ?amenity ?label ?where WHERE {
  ?amenity a ontosage:Amenity ;
           ontosage:layTerms ?lt ;
           rdfs:label ?label .
  OPTIONAL { ?amenity ontosage:locationText ?where }
  FILTER(CONTAINS(LCASE(?lt), "pray"))
} LIMIT 5
```
{% endraw %}

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:Amenity a owl:Class ;
    rdfs:label "Amenity"@en ;
    ontosage:competencyQuestion "What amenities are on floor 1?",
        "Where is the prayer room / café / nearest lift?" ;
    ontosage:exampleSparql """
        # "where can I pray?" — match lay terms, return the human location.
        SELECT ?amenity ?label ?where WHERE {
          ?amenity a ontosage:Amenity ;
                   ontosage:layTerms ?lt ;
                   rdfs:label ?label .
          OPTIONAL { ?amenity ontosage:locationText ?where }
          FILTER(CONTAINS(LCASE(?lt), "pray"))
        } LIMIT 5""" ;
    rdfs:comment "A physical facility or service a stakeholder can locate and use (prayer room, café, lift, showers, …). Distinct from a brick:Point/brick:Equipment: it is described for humans, and MAY be tied to a brick:Location via ontosage:locatedIn."@en ;
    rdfs:subClassOf ontosage:Capability ;
    skos:definition "A physical building facility or service with a human-readable location and features."@en ;
    skos:example "A multi-faith prayer room on Floor 1; the main passenger lift; the ground-floor café." .
```
{% endraw %}
