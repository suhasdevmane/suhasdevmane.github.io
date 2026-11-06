---
title: "ontosage:servesFloor"
layout: post
permalink: /ontology/property/servesFloor/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › servesFloor

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#servesFloor` |
| Label | serves floor |
| Kind | object property |
| Domain | [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}) |
| Range | [`brick:Floor`](https://ontology.brickschema.org/1.4/#brick:Floor) |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A brick:Floor a capability serves (e.g. the floors a lift reaches).

## Examples

- `bldg:Lift_Main ontosage:servesFloor bldg:Floor_3 .`

## Alignments

| Mapping | Term |
|---|---|
| `skos:relatedMatch` | [`bot:hasStorey`](https://w3id.org/bot#hasStorey) |

## Turtle

{% raw %}
```turtle
@prefix bot: <https://w3id.org/bot#> .
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:servesFloor a owl:ObjectProperty ;
    rdfs:label "serves floor"@en ;
    rdfs:comment "A brick:Floor a capability serves (e.g. the floors a lift reaches)."@en ;
    rdfs:domain ontosage:Capability ;
    rdfs:range brick:Floor ;
    skos:example "bldg:Lift_Main ontosage:servesFloor bldg:Floor_3 ." ;
    skos:relatedMatch bot:hasStorey .
```
{% endraw %}
