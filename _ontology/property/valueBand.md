---
title: "ontosage:valueBand"
layout: post
permalink: /ontology/property/valueBand/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › valueBand

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#valueBand` |
| Label | value band |
| Kind | datatype property |
| Domain | [`ontosage:AssetEngineeringProfile`]({{ '/ontology/class/AssetEngineeringProfile/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Replacement value band. A band rather than a figure, because a precise figure implies a valuation nobody has done.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`asset_engineering`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#asset_engineering) | `value_band` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:valueBand a owl:DatatypeProperty ;
    rdfs:label "value band"@en ;
    rdfs:comment "Replacement value band. A band rather than a figure, because a precise figure implies a valuation nobody has done."@en ;
    rdfs:domain ontosage:AssetEngineeringProfile ;
    rdfs:range xsd:string .
```
{% endraw %}
