---
title: "ontosage:inspectionIntervalDays"
layout: post
permalink: /ontology/property/inspectionIntervalDays/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › inspectionIntervalDays

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#inspectionIntervalDays` |
| Label | inspection interval days |
| Kind | datatype property |
| Domain | [`ontosage:AssetEngineeringProfile`]({{ '/ontology/class/AssetEngineeringProfile/' | relative_url }}) |
| Range | `xsd:integer` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The intended interval between physical visits. With lastVisited this makes the 'longest blind interval' question a calculation.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`asset_engineering`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#asset_engineering) | `inspection_interval_days` | `xsd:integer` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:inspectionIntervalDays a owl:DatatypeProperty ;
    rdfs:label "inspection interval days"@en ;
    rdfs:comment "The intended interval between physical visits. With lastVisited this makes the 'longest blind interval' question a calculation."@en ;
    rdfs:domain ontosage:AssetEngineeringProfile ;
    rdfs:range xsd:integer .
```
{% endraw %}
