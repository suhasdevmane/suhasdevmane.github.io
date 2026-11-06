---
title: "ontosage:WorkspaceProfile"
layout: post
permalink: /ontology/class/WorkspaceProfile/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › WorkspaceProfile

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#WorkspaceProfile` |
| Label | Workspace profile |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

What a space is like to WORK IN, as opposed to what it is called or how big it is. Records power, network quality, daylight, acoustic character, whether it suits a call, whether a group can use it without disturbing others, and the times it is typically busy or quiet.

## Examples

- where can two of us revise without disturbing quiet study? -&gt; WorkspaceProfile where groupFriendly is true and noiseProfile is not silent.

## Lay terms

Plain-language phrases declared on this term with `ontosage:layTerms`. A question that contains one of them can be matched to this term. (62)

`bookable room`, `bookable rooms`, `bookable space`, `bookable spaces`, `breakout space`, `common room`, `desk space`, `eligible alternative`, `for a group of`, `group study`, `group work`, `hot desk`, `how long to recover`, `how many seats`, `place to study`, `place to work`, `quiet room`, `quiet space`, `quiet study`, `quiet working`, `recover after`, `recovery minutes`, `recovery time`, `room big enough`, `room for`, `room for a call`, `room for a meeting`, `room for a viva`, `room for an interview`, `room readiness`, `room that seats`, `room to book`, `room with`, `rooms for`, `seat`, `seating capacity`, `seats for`, `setup minutes`, `setup time`, `somewhere quiet`, `somewhere to concentrate`, `somewhere to study`, `somewhere to take a call`, `somewhere to work`, `space for`, `space suitable`, `spaces for`, `spaces suitable`, `study area`, `study areas`, `study space`, `study spaces`, `suitable for study`, `suitable for work`, `time to recover`, `to recover`, `where can i study`, `where can i work`, `work as a group`, `work quietly`, `workspace`, `workspaces`

## Class hierarchy

Superclasses:

- [`ontosage:Record`]({{ '/ontology/class/Record/' | relative_url }}) › **`ontosage:WorkspaceProfile`**

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:busiestPeriod`]({{ '/ontology/property/busiestPeriod/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:daylightAspect`]({{ '/ontology/property/daylightAspect/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:groupFriendly`]({{ '/ontology/property/groupFriendly/' | relative_url }}) | datatype | `xsd:boolean` | this class |
| [`ontosage:isBookable`]({{ '/ontology/property/isBookable/' | relative_url }}) | datatype | `xsd:boolean` | this class |
| [`ontosage:nearestVerticalRoute`]({{ '/ontology/property/nearestVerticalRoute/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:networkRating`]({{ '/ontology/property/networkRating/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:noiseProfile`]({{ '/ontology/property/noiseProfile/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:powerAccess`]({{ '/ontology/property/powerAccess/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:quietestPeriod`]({{ '/ontology/property/quietestPeriod/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:recoveryMinutes`]({{ '/ontology/property/recoveryMinutes/' | relative_url }}) | datatype | `xsd:decimal` | this class |
| [`ontosage:seatCount`]({{ '/ontology/property/seatCount/' | relative_url }}) | datatype | `xsd:integer` | this class |
| [`ontosage:setupMinutes`]({{ '/ontology/property/setupMinutes/' | relative_url }}) | datatype | `xsd:decimal` | this class |
| [`ontosage:suitableForCalls`]({{ '/ontology/property/suitableForCalls/' | relative_url }}) | datatype | `xsd:boolean` | this class |
| [`ontosage:workspaceKind`]({{ '/ontology/property/workspaceKind/' | relative_url }}) | datatype | `xsd:string` | this class |

## Record document mapping

Record documents of type `workspace_profile` are lifted into instances of this class ([mapping]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#workspace_profile)).

## Turtle

Development notes were removed from one or more text values below; the source file holds the full text.

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:WorkspaceProfile a owl:Class ;
    rdfs:label "Workspace profile"@en ;
    ontosage:layTerms "bookable room",
        "bookable rooms",
        "bookable space",
        "bookable spaces",
        "breakout space",
        "common room",
        "desk space",
        "eligible alternative",
        "for a group of",
        "group study",
        "group work",
        "hot desk",
        "how long to recover",
        "how many seats",
        "place to study",
        "place to work",
        "quiet room",
        "quiet space",
        "quiet study",
        "quiet working",
        "recover after",
        "recovery minutes",
        "recovery time",
        "room big enough",
        "room for",
        "room for a call",
        "room for a meeting",
        "room for a viva",
        "room for an interview",
        "room readiness",
        "room that seats",
        "room to book",
        "room with",
        "rooms for",
        "seat",
        "seating capacity",
        "seats for",
        "setup minutes",
        "setup time",
        "somewhere quiet",
        "somewhere to concentrate",
        "somewhere to study",
        "somewhere to take a call",
        "somewhere to work",
        "space for",
        "space suitable",
        "spaces for",
        "spaces suitable",
        "study area",
        "study areas",
        "study space",
        "study spaces",
        "suitable for study",
        "suitable for work",
        "time to recover",
        "to recover",
        "where can i study",
        "where can i work",
        "work as a group",
        "work quietly",
        "workspace",
        "workspaces" ;
    rdfs:comment "What a space is like to WORK IN, as opposed to what it is called or how big it is. Records power, network quality, daylight, acoustic character, whether it suits a call, whether a group can use it without disturbing others, and the times it is typically busy or quiet."@en ;
    rdfs:subClassOf ontosage:Record ;
    skos:example "where can two of us revise without disturbing quiet study? -> WorkspaceProfile where groupFriendly is true and noiseProfile is not silent." .
```
{% endraw %}
