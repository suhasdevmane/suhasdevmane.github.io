---
title: "ontosage:zoneId"
layout: post
permalink: /ontology/property/zoneId/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › zoneId

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#zoneId` |
| Label | zone id |
| Kind | datatype property |
| Domain | [`brick:Location`](https://ontology.brickschema.org/1.4/#brick:Location) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The canonical zone identifier a space carries in the building's floor-plan manifests (DWG/PDF pipeline). This literal is THE join key between a manifest Space and its ontology individual — label-based joins break on decorated labels ('HVAC Zone 5.28'@en) and non-dotted CAD ids ('3Z001'), so generators emit this instead and the manifest linker matches on it first.

## Examples

- `bldg:Room_5.28 ontosage:zoneId "5.28" .`

## Turtle

{% raw %}
```turtle
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:zoneId a owl:DatatypeProperty ;
    rdfs:label "zone id"@en ;
    rdfs:comment "The canonical zone identifier a space carries in the building's floor-plan manifests (DWG/PDF pipeline). This literal is THE join key between a manifest Space and its ontology individual — label-based joins break on decorated labels ('HVAC Zone 5.28'@en) and non-dotted CAD ids ('3Z001'), so generators emit this instead and the manifest linker matches on it first."@en ;
    rdfs:domain brick:Location ;
    rdfs:range xsd:string ;
    skos:example "bldg:Room_5.28 ontosage:zoneId \"5.28\" ." .
```
{% endraw %}
