---
title: "ontosage:AVReadiness"
layout: post
permalink: /ontology/class/AVReadiness/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › AVReadiness

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#AVReadiness` |
| Label | Teaching AV readiness |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

One audiovisual component in a teaching room, with its state, the formats it serves, when it was last checked and the evidence reference for that check. THE AUDIO PATH IS A CHAIN: a room with a working projector, a working display and a dead microphone cannot run a lecture that needs amplification, so inAudioPath marks the links and a room's readiness for a format follows from the chain rather than from one asserted flag. No component may be recorded READY without evidence -- 'checked' without a record is a claim, and withholding a room from service on somebody's recollection is what the team is trying to avoid. The rule is conditional rather than a required column, because a component that has NEVER been tested has no check date and no reference, and that is the most important row in the register rather than one to exclude: `unevidenced` exists so it can be stated.

## Examples

- which rooms have complete current AV evidence for a lecture? -&gt; AVReadiness grouped by locationText where supportsFormat names the format; a room fails if any inAudioPath component is not ready.

## Lay terms

Plain-language phrases declared on this term with `ontosage:layTerms`. A question that contains one of them can be matched to this term. (18)

`amplifier`, `audio path`, `audio visual`, `audiovisual`, `av`, `av check`, `av evidence`, `av readiness`, `camera`, `confirmed readiness`, `display`, `hearing loop`, `is the room ready`, `microphone`, `projector`, `readiness for the next`, `room ready for teaching`, `teaching room ready`

## Class hierarchy

Superclasses:

- [`ontosage:Record`]({{ '/ontology/class/Record/' | relative_url }}) › **`ontosage:AVReadiness`**

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:avComponentKind`]({{ '/ontology/property/avComponentKind/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:inAudioPath`]({{ '/ontology/property/inAudioPath/' | relative_url }}) | datatype | `xsd:boolean` | this class |

## Record document mapping

Record documents of type `av_readiness` are lifted into instances of this class ([mapping]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#av_readiness)).

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:AVReadiness a owl:Class ;
    rdfs:label "Teaching AV readiness"@en ;
    ontosage:layTerms "amplifier",
        "audio path",
        "audio visual",
        "audiovisual",
        "av",
        "av check",
        "av evidence",
        "av readiness",
        "camera",
        "confirmed readiness",
        "display",
        "hearing loop",
        "is the room ready",
        "microphone",
        "projector",
        "readiness for the next",
        "room ready for teaching",
        "teaching room ready" ;
    rdfs:comment "One audiovisual component in a teaching room, with its state, the formats it serves, when it was last checked and the evidence reference for that check. THE AUDIO PATH IS A CHAIN: a room with a working projector, a working display and a dead microphone cannot run a lecture that needs amplification, so inAudioPath marks the links and a room's readiness for a format follows from the chain rather than from one asserted flag. No component may be recorded READY without evidence -- 'checked' without a record is a claim, and withholding a room from service on somebody's recollection is what the team is trying to avoid. The rule is conditional rather than a required column, because a component that has NEVER been tested has no check date and no reference, and that is the most important row in the register rather than one to exclude: `unevidenced` exists so it can be stated."@en ;
    rdfs:subClassOf ontosage:Record ;
    skos:example "which rooms have complete current AV evidence for a lecture? -> AVReadiness grouped by locationText where supportsFormat names the format; a room fails if any inAudioPath component is not ready." .
```
{% endraw %}
