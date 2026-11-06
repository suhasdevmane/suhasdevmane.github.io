---
title: "ontosage:engineeringSystem"
layout: post
permalink: /ontology/property/engineeringSystem/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › engineeringSystem

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#engineeringSystem` |
| Label | engineering system |
| Kind | datatype property |
| Domain | [`ontosage:AssetEngineeringProfile`]({{ '/ontology/class/AssetEngineeringProfile/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The system this asset belongs to: chilled water, ventilation, LV distribution, fire, transport, metering. The grouping an estates or M&E question uses before it names any individual item.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`asset_engineering`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#asset_engineering) | `engineering_system` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:engineeringSystem a owl:DatatypeProperty ;
    rdfs:label "engineering system"@en ;
    rdfs:comment "The system this asset belongs to: chilled water, ventilation, LV distribution, fire, transport, metering. The grouping an estates or M&E question uses before it names any individual item."@en ;
    rdfs:domain ontosage:AssetEngineeringProfile ;
    rdfs:range xsd:string .
```
{% endraw %}
