---
title: "ontosage:openDefect"
layout: post
permalink: /ontology/property/openDefect/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › openDefect

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#openDefect` |
| Label | open defect |
| Kind | datatype property |
| Domain | [`ontosage:FireSafetyAsset`]({{ '/ontology/class/FireSafetyAsset/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A defect recorded against this asset and not yet closed. Blank means none recorded, which is not the same as none present, and the register says so.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`fire_safety_asset`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#fire_safety_asset) | `open_defect` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:openDefect a owl:DatatypeProperty ;
    rdfs:label "open defect"@en ;
    rdfs:comment "A defect recorded against this asset and not yet closed. Blank means none recorded, which is not the same as none present, and the register says so."@en ;
    rdfs:domain ontosage:FireSafetyAsset ;
    rdfs:range xsd:string .
```
{% endraw %}
