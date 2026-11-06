---
title: "ontosage:locationText"
layout: post
permalink: /ontology/property/locationText/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › locationText

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#locationText` |
| Label | human-readable location |
| Kind | datatype property |
| Domain | [`ontosage:Amenity`]({{ '/ontology/class/Amenity/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Free-text location for an amenity, as a person would describe it.

## Examples

- "Floor 1, room 1.04" or "Left of the main entrance, ~25 m"

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`asset_engineering`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#asset_engineering) | `location` | `xsd:string` |
| [`av_readiness`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#av_readiness) | `room` | `xsd:string` |
| [`booking`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#booking) | `room` | `xsd:string` |
| [`cleaning_task`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#cleaning_task) | `area` | `xsd:string` |
| [`competency`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#competency) | `area` | `xsd:string` |
| [`department`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#department) | `based_at` | `xsd:string` |
| [`door_hardware`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#door_hardware) | `location` | `xsd:string` |
| [`evacuation_provision`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#evacuation_provision) | `location` | `xsd:string` |
| [`event_activity`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#event_activity) | `location` | `xsd:string` |
| [`fire_safety_asset`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#fire_safety_asset) | `location` | `xsd:string` |
| [`hazard_control`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#hazard_control) | `location` | `xsd:string` |
| [`incident_record`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#incident_record) | `location` | `xsd:string` |
| [`patrol_checkpoint`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#patrol_checkpoint) | `location` | `xsd:string` |
| [`permit_to_work`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#permit_to_work) | `area` | `xsd:string` |
| [`public_event`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#public_event) | `venue` | `xsd:string` |
| [`risk_assessment`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#risk_assessment) | `area` | `xsd:string` |
| [`stock_item`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#stock_item) | `store` | `xsd:string` |
| [`timetabled_session`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#timetabled_session) | `room` | `xsd:string` |
| [`waste_collection`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#waste_collection) | `location` | `xsd:string` |
| [`work_order`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#work_order) | `asset_name` | `xsd:string` |
| [`workspace_profile`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#workspace_profile) | `room` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:locationText a owl:DatatypeProperty ;
    rdfs:label "human-readable location"@en ;
    rdfs:comment "Free-text location for an amenity, as a person would describe it."@en ;
    rdfs:domain ontosage:Amenity ;
    rdfs:range xsd:string ;
    skos:example "\"Floor 1, room 1.04\" or \"Left of the main entrance, ~25 m\"" .
```
{% endraw %}
