---
title: "ontosage:commandedBySystem"
layout: post
permalink: /ontology/property/commandedBySystem/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › commandedBySystem

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#commandedBySystem` |
| Label | commanded by system |
| Kind | datatype property |
| Domain | [`ontosage:DoorHardware`]({{ '/ontology/class/DoorHardware/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Which system commands the opening: fire alarm, access control, building management or none.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`door_hardware`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#door_hardware) | `commanded_by` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:commandedBySystem a owl:DatatypeProperty ;
    rdfs:label "commanded by system"@en ;
    rdfs:comment "Which system commands the opening: fire alarm, access control, building management or none."@en ;
    rdfs:domain ontosage:DoorHardware ;
    rdfs:range xsd:string .
```
{% endraw %}
