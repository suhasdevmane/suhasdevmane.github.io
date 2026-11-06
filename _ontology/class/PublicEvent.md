---
title: "ontosage:PublicEvent"
layout: post
permalink: /ontology/class/PublicEvent/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › PublicEvent

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#PublicEvent` |
| Label | Public event |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A published, visitor-facing arrangement over a space: admission times, entrance, registration policy and change history. DISTINCT FROM ontosage:Booking, which is a room held for a period — a booking can move without the published event changing, and that disagreement is precisely what a visitor asking 'has the venue changed since my invitation' needs reported.

## Examples

- which entrance should visitors use tomorrow evening? -&gt; PublicEvent on that date, read visitorEntrance and doorsOpenAt.

## Lay terms

Plain-language phrases declared on this term with `ontosage:layTerms`. A question that contains one of them can be matched to this term. (29)

`attending`, `check in`, `check-in`, `companion`, `doors open`, `event has moved`, `event moved`, `event room changed`, `event room has changed`, `event venue`, `events are due`, `events due`, `events today`, `has the venue changed`, `open day`, `open days`, `public lecture`, `public lectures`, `public talk`, `public talks`, `registration`, `seminar`, `showcase`, `support person`, `ticket`, `today's events`, `upcoming events`, `what time should i arrive`, `which entrance`

## Class hierarchy

Superclasses:

- [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) › **`ontosage:PublicEvent`**

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:checkInFrom`]({{ '/ontology/property/checkInFrom/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:companionPolicy`]({{ '/ontology/property/companionPolicy/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:doorsOpenAt`]({{ '/ontology/property/doorsOpenAt/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:registrationPolicy`]({{ '/ontology/property/registrationPolicy/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:visitorEntrance`]({{ '/ontology/property/visitorEntrance/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:aboutPoint`]({{ '/ontology/property/aboutPoint/' | relative_url }}) | object | [`brick:Point`](https://ontology.brickschema.org/1.4/#brick:Point) | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:aboutSpace`]({{ '/ontology/property/aboutSpace/' | relative_url }}) | object | [`brick:Location`](https://ontology.brickschema.org/1.4/#brick:Location) | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:completedDate`]({{ '/ontology/property/completedDate/' | relative_url }}) | datatype | `xsd:dateTime` | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:coveredScope`]({{ '/ontology/property/coveredScope/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:coversAsset`]({{ '/ontology/property/coversAsset/' | relative_url }}) | object | [`brick:Equipment`](https://ontology.brickschema.org/1.4/#brick:Equipment) | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:derivedFromDocument`]({{ '/ontology/property/derivedFromDocument/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:liftedByMapping`]({{ '/ontology/property/liftedByMapping/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:owningAuthority`]({{ '/ontology/property/owningAuthority/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:providerName`]({{ '/ontology/property/providerName/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:recordOwner`]({{ '/ontology/property/recordOwner/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:recordVersion`]({{ '/ontology/property/recordVersion/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:responsibleRole`]({{ '/ontology/property/responsibleRole/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:retrievedAt`]({{ '/ontology/property/retrievedAt/' | relative_url }}) | datatype | `xsd:dateTime` | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:supersedes`]({{ '/ontology/property/supersedes/' | relative_url }}) | object | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |

## Record document mapping

Record documents of type `public_event` are lifted into instances of this class ([mapping]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#public_event)).

## Turtle

Development notes were removed from one or more text values below; the source file holds the full text.

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:PublicEvent a owl:Class ;
    rdfs:label "Public event"@en ;
    ontosage:layTerms "attending",
        "check in",
        "check-in",
        "companion",
        "doors open",
        "event has moved",
        "event moved",
        "event room changed",
        "event room has changed",
        "event venue",
        "events are due",
        "events due",
        "events today",
        "has the venue changed",
        "open day",
        "open days",
        "public lecture",
        "public lectures",
        "public talk",
        "public talks",
        "registration",
        "seminar",
        "showcase",
        "support person",
        "ticket",
        "today's events",
        "upcoming events",
        "what time should i arrive",
        "which entrance" ;
    rdfs:comment "A published, visitor-facing arrangement over a space: admission times, entrance, registration policy and change history. DISTINCT FROM ontosage:Booking, which is a room held for a period — a booking can move without the published event changing, and that disagreement is precisely what a visitor asking 'has the venue changed since my invitation' needs reported."@en ;
    rdfs:subClassOf ontosage:IntervalRecord ;
    skos:example "which entrance should visitors use tomorrow evening? -> PublicEvent on that date, read visitorEntrance and doorsOpenAt." .
```
{% endraw %}
