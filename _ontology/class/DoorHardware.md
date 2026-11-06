---
title: "ontosage:DoorHardware"
layout: post
permalink: /ontology/class/DoorHardware/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › DoorHardware

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#DoorHardware` |
| Label | Door and shutter hardware |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

One controlled opening — door, shutter, barrier or turnstile — and how it behaves when power or the fire alarm changes state: its fail state on power loss, any hold-open device, how it is released, and which system commands it. recordStatus is the owner's recorded state; failStateOnPowerLoss is recorded per opening because a fire shutter and an escape door on one circuit fail in opposite directions by design.

## Examples

- which openings fail open on power loss? -&gt; DoorHardware where failStateOnPowerLoss is fail open.

## Lay terms

Plain-language phrases declared on this term with `ontosage:layTerms`. A question that contains one of them can be matched to this term. (23)

`barrier`, `door controller`, `door controllers`, `door hardware`, `door interface`, `door interfaces`, `door lock`, `door locks`, `door release`, `escape door`, `fail locked`, `fail open`, `fail safe`, `fail secure`, `fire shutter`, `hold open`, `maglock`, `power failure`, `power loss`, `roller shutter`, `shutter`, `shutters`, `turnstile`

## Class hierarchy

Superclasses:

- [`ontosage:Record`]({{ '/ontology/class/Record/' | relative_url }}) › **`ontosage:DoorHardware`**

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:commandedBySystem`]({{ '/ontology/property/commandedBySystem/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:failStateOnPowerLoss`]({{ '/ontology/property/failStateOnPowerLoss/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:holdOpenDevice`]({{ '/ontology/property/holdOpenDevice/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:openingKind`]({{ '/ontology/property/openingKind/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:releaseMechanism`]({{ '/ontology/property/releaseMechanism/' | relative_url }}) | datatype | `xsd:string` | this class |

## Record document mapping

Record documents of type `door_hardware` are lifted into instances of this class ([mapping]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#door_hardware)).

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:DoorHardware a owl:Class ;
    rdfs:label "Door and shutter hardware"@en ;
    ontosage:layTerms "barrier",
        "door controller",
        "door controllers",
        "door hardware",
        "door interface",
        "door interfaces",
        "door lock",
        "door locks",
        "door release",
        "escape door",
        "fail locked",
        "fail open",
        "fail safe",
        "fail secure",
        "fire shutter",
        "hold open",
        "maglock",
        "power failure",
        "power loss",
        "roller shutter",
        "shutter",
        "shutters",
        "turnstile" ;
    rdfs:comment "One controlled opening — door, shutter, barrier or turnstile — and how it behaves when power or the fire alarm changes state: its fail state on power loss, any hold-open device, how it is released, and which system commands it. recordStatus is the owner's recorded state; failStateOnPowerLoss is recorded per opening because a fire shutter and an escape door on one circuit fail in opposite directions by design."@en ;
    rdfs:subClassOf ontosage:Record ;
    skos:example "which openings fail open on power loss? -> DoorHardware where failStateOnPowerLoss is fail open." .
```
{% endraw %}
