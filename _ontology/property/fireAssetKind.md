---
title: "ontosage:fireAssetKind"
layout: post
permalink: /ontology/property/fireAssetKind/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › fireAssetKind

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#fireAssetKind` |
| Label | fire asset kind |
| Kind | datatype property |
| Domain | [`ontosage:FireSafetyAsset`]({{ '/ontology/class/FireSafetyAsset/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

detection, alarm, suppression, extinguisher, fire door, compartmentation, escape provision or signage.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`fire_safety_asset`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#fire_safety_asset) | `kind` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:fireAssetKind a owl:DatatypeProperty ;
    rdfs:label "fire asset kind"@en ;
    rdfs:comment "detection, alarm, suppression, extinguisher, fire door, compartmentation, escape provision or signage."@en ;
    rdfs:domain ontosage:FireSafetyAsset ;
    rdfs:range xsd:string .
```
{% endraw %}
