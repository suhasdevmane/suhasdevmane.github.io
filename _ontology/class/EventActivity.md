---
title: "ontosage:EventActivity"
layout: post
permalink: /ontology/class/EventActivity/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › EventActivity

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#EventActivity` |
| Label | Event activity |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

One item inside a PublicEvent's agenda: its position, start, duration, location, whether a companion may attend and whether it is optional. An agenda is not a property of an event -- it is a sequence of things with their own durations and rules, which is why it is rows. companionPolicy is per ACTIVITY because a campus tour and a one-to-one admissions conversation can sit inside the same open day and differ, and a family planning their day needs it at that level or the answer is wrong for half the visit. isOptional exists so 'we only have two hours, what should we prioritise' is answerable by dropping what the events office marked optional rather than by inventing a preference.

## Examples

- how much time for the talk, tour and questions? -&gt; EventActivity where partOfEvent matches; sum expectedMinutes.

## Lay terms

Plain-language phrases declared on this term with `ontosage:layTerms`. A question that contains one of them can be matched to this term. (17)

`agenda`, `breakout session`, `breakout sessions`, `event activities`, `event activity`, `event program`, `event programme`, `event session`, `event sessions`, `how long will`, `how much time`, `itinerary`, `schedule of the day`, `talk`, `tour`, `what should we prioritise`, `workshop`

## Class hierarchy

Superclasses:

- [`ontosage:Record`]({{ '/ontology/class/Record/' | relative_url }}) › **`ontosage:EventActivity`**

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:partOfEvent`]({{ '/ontology/property/partOfEvent/' | relative_url }}) | datatype | `xsd:string` | this class |

## Record document mapping

Record documents of type `event_activity` are lifted into instances of this class ([mapping]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#event_activity)).

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:EventActivity a owl:Class ;
    rdfs:label "Event activity"@en ;
    ontosage:layTerms "agenda",
        "breakout session",
        "breakout sessions",
        "event activities",
        "event activity",
        "event program",
        "event programme",
        "event session",
        "event sessions",
        "how long will",
        "how much time",
        "itinerary",
        "schedule of the day",
        "talk",
        "tour",
        "what should we prioritise",
        "workshop" ;
    rdfs:comment "One item inside a PublicEvent's agenda: its position, start, duration, location, whether a companion may attend and whether it is optional. An agenda is not a property of an event -- it is a sequence of things with their own durations and rules, which is why it is rows. companionPolicy is per ACTIVITY because a campus tour and a one-to-one admissions conversation can sit inside the same open day and differ, and a family planning their day needs it at that level or the answer is wrong for half the visit. isOptional exists so 'we only have two hours, what should we prioritise' is answerable by dropping what the events office marked optional rather than by inventing a preference."@en ;
    rdfs:subClassOf ontosage:Record ;
    skos:example "how much time for the talk, tour and questions? -> EventActivity where partOfEvent matches; sum expectedMinutes." .
```
{% endraw %}
