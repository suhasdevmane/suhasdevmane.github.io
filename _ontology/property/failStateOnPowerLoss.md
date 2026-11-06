---
title: "ontosage:failStateOnPowerLoss"
layout: post
permalink: /ontology/property/failStateOnPowerLoss/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › failStateOnPowerLoss

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#failStateOnPowerLoss` |
| Label | fail state on power loss |
| Kind | datatype property |
| Domain | [`ontosage:DoorHardware`]({{ '/ontology/class/DoorHardware/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

How the opening rests when power is lost: fail open (releases), fail locked (stays secure), fail safe (releases for escape) or fail closed (drops, as a fire shutter does). Recorded, never inferred from the opening kind.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`door_hardware`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#door_hardware) | `power_loss_state` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:failStateOnPowerLoss a owl:DatatypeProperty ;
    rdfs:label "fail state on power loss"@en ;
    rdfs:comment "How the opening rests when power is lost: fail open (releases), fail locked (stays secure), fail safe (releases for escape) or fail closed (drops, as a fire shutter does). Recorded, never inferred from the opening kind."@en ;
    rdfs:domain ontosage:DoorHardware ;
    rdfs:range xsd:string .
```
{% endraw %}
