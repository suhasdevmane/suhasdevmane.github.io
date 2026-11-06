---
title: "ontosage:commissionedDuty"
layout: post
permalink: /ontology/property/commissionedDuty/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › commissionedDuty

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#commissionedDuty` |
| Label | commissioned duty |
| Kind | datatype property |
| Domain | [`ontosage:AssetEngineeringProfile`]({{ '/ontology/class/AssetEngineeringProfile/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

What commissioning actually witnessed and signed off. Separate from design duty because the two routinely differ, and the difference is the answer.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`asset_engineering`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#asset_engineering) | `commissioned_duty` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:commissionedDuty a owl:DatatypeProperty ;
    rdfs:label "commissioned duty"@en ;
    rdfs:comment "What commissioning actually witnessed and signed off. Separate from design duty because the two routinely differ, and the difference is the answer."@en ;
    rdfs:domain ontosage:AssetEngineeringProfile ;
    rdfs:range xsd:string .
```
{% endraw %}
