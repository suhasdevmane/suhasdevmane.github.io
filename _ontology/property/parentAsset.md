---
title: "ontosage:parentAsset"
layout: post
permalink: /ontology/property/parentAsset/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › parentAsset

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#parentAsset` |
| Label | parent asset |
| Kind | datatype property |
| Domain | [`ontosage:AssetEngineeringProfile`]({{ '/ontology/class/AssetEngineeringProfile/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The asset this one is a part of, if any. Blank for a top-level plant item. Asset-management questions are about the CHAIN — is each asset linked to the correct parent, system, served area and dependency — and a register of unconnected items cannot answer one of them.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`asset_engineering`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#asset_engineering) | `parent_asset` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:parentAsset a owl:DatatypeProperty ;
    rdfs:label "parent asset"@en ;
    rdfs:comment "The asset this one is a part of, if any. Blank for a top-level plant item. Asset-management questions are about the CHAIN — is each asset linked to the correct parent, system, served area and dependency — and a register of unconnected items cannot answer one of them."@en ;
    rdfs:domain ontosage:AssetEngineeringProfile ;
    rdfs:range xsd:string .
```
{% endraw %}
