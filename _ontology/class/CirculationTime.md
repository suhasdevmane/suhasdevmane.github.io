---
title: "ontosage:CirculationTime"
layout: post
permalink: /ontology/class/CirculationTime/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › CirculationTime

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#CirculationTime` |
| Label | Circulation time |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

How long it takes to get from one part of the building to another, by the walking route and by the step-free route separately. Floor-to-floor rather than room-to-room, because a room-pair matrix grows as the square of the room count and the floor change is what dominates the time.

## Examples

- which transition needs the larger travel allowance? -&gt; CirculationTime between the two floors, walking and step-free.

## Lay terms

Plain-language phrases declared on this term with `ontosage:layTerms`. A question that contains one of them can be matched to this term. (35)

`another floor`, `back to back`, `back-to-back`, `between floors`, `by the stairs`, `changeover`, `changeover time`, `floor pairs`, `floor to floor`, `get from one room to another`, `how long does it take`, `how long to get`, `journey time`, `lift wait`, `lift waits`, `route between floors`, `route length`, `route lengths`, `routes between floors`, `slower than the stairs`, `stairs`, `take to get between`, `take to get from`, `take to get to`, `time between rooms`, `to a different floor`, `to another floor`, `to the other floor`, `transition time`, `travel time`, `travel times`, `vertical route`, `vertical routes`, `vertical travel`, `walking time`

## Class hierarchy

Superclasses:

- [`ontosage:Record`]({{ '/ontology/class/Record/' | relative_url }}) › **`ontosage:CirculationTime`**

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:dependsOnLift`]({{ '/ontology/property/dependsOnLift/' | relative_url }}) | datatype | `xsd:boolean` | this class |
| [`ontosage:fromFloor`]({{ '/ontology/property/fromFloor/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:stepFreeMinutes`]({{ '/ontology/property/stepFreeMinutes/' | relative_url }}) | datatype | `xsd:decimal` | this class |
| [`ontosage:toFloor`]({{ '/ontology/property/toFloor/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:walkingMinutes`]({{ '/ontology/property/walkingMinutes/' | relative_url }}) | datatype | `xsd:decimal` | this class |

## Record document mapping

Record documents of type `circulation_time` are lifted into instances of this class ([mapping]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#circulation_time)).

## Turtle

Development notes were removed from one or more text values below; the source file holds the full text.

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:CirculationTime a owl:Class ;
    rdfs:label "Circulation time"@en ;
    ontosage:layTerms "another floor",
        "back to back",
        "back-to-back",
        "between floors",
        "by the stairs",
        "changeover",
        "changeover time",
        "floor pairs",
        "floor to floor",
        "get from one room to another",
        "how long does it take",
        "how long to get",
        "journey time",
        "lift wait",
        "lift waits",
        "route between floors",
        "route length",
        "route lengths",
        "routes between floors",
        "slower than the stairs",
        "stairs",
        "take to get between",
        "take to get from",
        "take to get to",
        "time between rooms",
        "to a different floor",
        "to another floor",
        "to the other floor",
        "transition time",
        "travel time",
        "travel times",
        "vertical route",
        "vertical routes",
        "vertical travel",
        "walking time" ;
    rdfs:comment "How long it takes to get from one part of the building to another, by the walking route and by the step-free route separately. Floor-to-floor rather than room-to-room, because a room-pair matrix grows as the square of the room count and the floor change is what dominates the time."@en ;
    rdfs:subClassOf ontosage:Record ;
    skos:example "which transition needs the larger travel allowance? -> CirculationTime between the two floors, walking and step-free." .
```
{% endraw %}
