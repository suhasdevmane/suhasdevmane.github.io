---
title: "ontosage:testStandard"
layout: post
permalink: /ontology/property/testStandard/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › testStandard

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#testStandard` |
| Label | test standard |
| Kind | datatype property |
| Domain | [`ontosage:FireSafetyAsset`]({{ '/ontology/class/FireSafetyAsset/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The standard or regime the asset is held to, so 'is this compliant?' has a stated benchmark rather than an opinion.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`fire_safety_asset`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#fire_safety_asset) | `standard` | `xsd:string` |
| [`hazard_control`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#hazard_control) | `regime` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:testStandard a owl:DatatypeProperty ;
    rdfs:label "test standard"@en ;
    rdfs:comment "The standard or regime the asset is held to, so 'is this compliant?' has a stated benchmark rather than an opinion."@en ;
    rdfs:domain ontosage:FireSafetyAsset ;
    rdfs:range xsd:string .
```
{% endraw %}
