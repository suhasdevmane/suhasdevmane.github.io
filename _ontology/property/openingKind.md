---
title: "ontosage:openingKind"
layout: post
permalink: /ontology/property/openingKind/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › openingKind

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#openingKind` |
| Label | opening kind |
| Kind | datatype property |
| Domain | [`ontosage:DoorHardware`]({{ '/ontology/class/DoorHardware/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

What the opening is: escape door, fire shutter, security door, turnstile, vehicle barrier.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`door_hardware`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#door_hardware) | `kind` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:openingKind a owl:DatatypeProperty ;
    rdfs:label "opening kind"@en ;
    rdfs:comment "What the opening is: escape door, fire shutter, security door, turnstile, vehicle barrier."@en ;
    rdfs:domain ontosage:DoorHardware ;
    rdfs:range xsd:string .
```
{% endraw %}
