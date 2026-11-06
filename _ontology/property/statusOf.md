---
title: "ontosage:statusOf"
layout: post
permalink: /ontology/property/statusOf/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › statusOf

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#statusOf` |
| Label | status of |
| Kind | object property |
| Domain | [`ontosage:AssetStatus`]({{ '/ontology/class/AssetStatus/' | relative_url }}) |
| Range | not declared |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The asset, amenity or service this record describes.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ontosage:statusOf a owl:ObjectProperty ;
    rdfs:label "status of"@en ;
    rdfs:comment "The asset, amenity or service this record describes."@en ;
    rdfs:domain ontosage:AssetStatus .
```
{% endraw %}
