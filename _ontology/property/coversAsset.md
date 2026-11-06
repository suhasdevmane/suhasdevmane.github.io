---
title: "ontosage:coversAsset"
layout: post
permalink: /ontology/property/coversAsset/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › coversAsset

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#coversAsset` |
| Label | covers asset |
| Kind | object property |
| Domain | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| Range | [`brick:Equipment`](https://ontology.brickschema.org/1.4/#brick:Equipment) |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The equipment a warranty, contract, handover record or condition survey concerns.

## Turtle

{% raw %}
```turtle
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ontosage:coversAsset a owl:ObjectProperty ;
    rdfs:label "covers asset"@en ;
    rdfs:comment "The equipment a warranty, contract, handover record or condition survey concerns."@en ;
    rdfs:domain ontosage:IntervalRecord ;
    rdfs:range brick:Equipment .
```
{% endraw %}
