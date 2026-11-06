---
title: "ontosage:locatedIn"
layout: post
permalink: /ontology/property/locatedIn/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › locatedIn

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#locatedIn` |
| Label | located in |
| Kind | object property |
| Domain | [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}) |
| Range | [`brick:Location`](https://ontology.brickschema.org/1.4/#brick:Location) |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Ties a capability to the Brick location (floor / room / zone) it sits in, so spatial questions can join OCBV facts to the Brick model. RANGE IS A brick:Location — this is the primary OCBV↔Brick bridge.

## Examples

- `bldg:PrayerRoom_104 ontosage:locatedIn bldg:Room_1.04 .`

## Alignments

| Mapping | Term |
|---|---|
| `skos:relatedMatch` | [`bot:containsElement`](https://w3id.org/bot#containsElement) |
| `skos:relatedMatch` | [`rec:isLocationOf`](https://w3id.org/rec#isLocationOf) |

## Turtle

{% raw %}
```turtle
@prefix bot: <https://w3id.org/bot#> .
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rec: <https://w3id.org/rec#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:locatedIn a owl:ObjectProperty ;
    rdfs:label "located in"@en ;
    rdfs:comment "Ties a capability to the Brick location (floor / room / zone) it sits in, so spatial questions can join OCBV facts to the Brick model. RANGE IS A brick:Location — this is the primary OCBV↔Brick bridge."@en ;
    rdfs:domain ontosage:Capability ;
    rdfs:range brick:Location ;
    skos:example "bldg:PrayerRoom_104 ontosage:locatedIn bldg:Room_1.04 ." ;
    skos:relatedMatch bot:containsElement,
        rec:isLocationOf .
```
{% endraw %}
