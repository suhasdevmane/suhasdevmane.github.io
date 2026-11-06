---
title: "ontosage:onFloor"
layout: post
permalink: /ontology/property/onFloor/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › onFloor

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#onFloor` |
| Label | floor identifier |
| Kind | datatype property |
| Domain | [`ontosage:Amenity`]({{ '/ontology/class/Amenity/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A floor label for an amenity (free text; use ontosage:locatedIn/servesFloor to link the actual brick:Floor).

## Examples

- "1" or "Ground"

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`asset_engineering`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#asset_engineering) | `floor` | `xsd:string` |
| [`door_hardware`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#door_hardware) | `floor` | `xsd:string` |
| [`evacuation_provision`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#evacuation_provision) | `floor` | `xsd:string` |
| [`fire_safety_asset`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#fire_safety_asset) | `floor` | `xsd:string` |
| [`timetabled_session`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#timetabled_session) | `floor` | `xsd:string` |
| [`workspace_profile`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#workspace_profile) | `floor` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:onFloor a owl:DatatypeProperty ;
    rdfs:label "floor identifier"@en ;
    rdfs:comment "A floor label for an amenity (free text; use ontosage:locatedIn/servesFloor to link the actual brick:Floor)."@en ;
    rdfs:domain ontosage:Amenity ;
    rdfs:range xsd:string ;
    skos:example "\"1\" or \"Ground\"" .
```
{% endraw %}
