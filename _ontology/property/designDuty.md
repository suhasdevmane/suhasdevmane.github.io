---
title: "ontosage:designDuty"
layout: post
permalink: /ontology/property/designDuty/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › designDuty

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#designDuty` |
| Label | design duty |
| Kind | datatype property |
| Domain | [`ontosage:AssetEngineeringProfile`]({{ '/ontology/class/AssetEngineeringProfile/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

What the asset was specified to do, with its unit. The claim on the drawing.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`asset_engineering`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#asset_engineering) | `design_duty` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:designDuty a owl:DatatypeProperty ;
    rdfs:label "design duty"@en ;
    rdfs:comment "What the asset was specified to do, with its unit. The claim on the drawing."@en ;
    rdfs:domain ontosage:AssetEngineeringProfile ;
    rdfs:range xsd:string .
```
{% endraw %}
