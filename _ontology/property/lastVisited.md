---
title: "ontosage:lastVisited"
layout: post
permalink: /ontology/property/lastVisited/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › lastVisited

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#lastVisited` |
| Label | last visited |
| Kind | datatype property |
| Domain | [`ontosage:AssetEngineeringProfile`]({{ '/ontology/class/AssetEngineeringProfile/' | relative_url }}) |
| Range | `xsd:date` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

When a person last physically attended this asset — not when a sensor last reported it.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`asset_engineering`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#asset_engineering) | `last_visited` | `xsd:date` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:lastVisited a owl:DatatypeProperty ;
    rdfs:label "last visited"@en ;
    rdfs:comment "When a person last physically attended this asset — not when a sensor last reported it."@en ;
    rdfs:domain ontosage:AssetEngineeringProfile ;
    rdfs:range xsd:date .
```
{% endraw %}
