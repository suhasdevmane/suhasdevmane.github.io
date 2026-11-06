---
title: "ontosage:releaseMechanism"
layout: post
permalink: /ontology/property/releaseMechanism/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › releaseMechanism

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#releaseMechanism` |
| Label | release mechanism |
| Kind | datatype property |
| Domain | [`ontosage:DoorHardware`]({{ '/ontology/class/DoorHardware/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

How the opening is released in an emergency: break-glass, push pad, fire-panel signal, or manual key override.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`door_hardware`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#door_hardware) | `release` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:releaseMechanism a owl:DatatypeProperty ;
    rdfs:label "release mechanism"@en ;
    rdfs:comment "How the opening is released in an emergency: break-glass, push pad, fire-panel signal, or manual key override."@en ;
    rdfs:domain ontosage:DoorHardware ;
    rdfs:range xsd:string .
```
{% endraw %}
