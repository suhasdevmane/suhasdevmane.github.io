---
title: "ontosage:inAudioPath"
layout: post
permalink: /ontology/property/inAudioPath/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › inAudioPath

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#inAudioPath` |
| Label | in audio path |
| Kind | datatype property |
| Domain | [`ontosage:AVReadiness`]({{ '/ontology/class/AVReadiness/' | relative_url }}) |
| Range | `xsd:boolean` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Whether the component is a link in the amplified audio chain. A format needing a microphone fails if any link is down, whatever the display is doing.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`av_readiness`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#av_readiness) | `audio_path` | `xsd:boolean` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:inAudioPath a owl:DatatypeProperty ;
    rdfs:label "in audio path"@en ;
    rdfs:comment "Whether the component is a link in the amplified audio chain. A format needing a microphone fails if any link is down, whatever the display is doing."@en ;
    rdfs:domain ontosage:AVReadiness ;
    rdfs:range xsd:boolean .
```
{% endraw %}
