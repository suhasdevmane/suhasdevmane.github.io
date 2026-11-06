---
title: "ontosage:holdOpenDevice"
layout: post
permalink: /ontology/property/holdOpenDevice/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › holdOpenDevice

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#holdOpenDevice` |
| Label | hold-open device |
| Kind | datatype property |
| Domain | [`ontosage:DoorHardware`]({{ '/ontology/class/DoorHardware/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The device holding the opening open in normal use, and what drops it — an acoustic or wired hold-open, a magnet on the fire panel, or none.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`door_hardware`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#door_hardware) | `hold_open` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:holdOpenDevice a owl:DatatypeProperty ;
    rdfs:label "hold-open device"@en ;
    rdfs:comment "The device holding the opening open in normal use, and what drops it — an acoustic or wired hold-open, a magnet on the fire panel, or none."@en ;
    rdfs:domain ontosage:DoorHardware ;
    rdfs:range xsd:string .
```
{% endraw %}
