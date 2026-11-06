---
title: "ontosage:tagInMaintenance"
layout: post
permalink: /ontology/property/tagInMaintenance/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › tagInMaintenance

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#tagInMaintenance` |
| Label | tag in maintenance system |
| Kind | datatype property |
| Domain | [`ontosage:AssetEngineeringProfile`]({{ '/ontology/class/AssetEngineeringProfile/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Held as three SEPARATE tag fields, not one identifier, for the same reason the waste register separates label from signage: 'are asset names consistent across drawings, BMS and maintenance records?' is only answerable if the disagreement can be represented.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`asset_engineering`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#asset_engineering) | `tag_maintenance` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:tagInMaintenance a owl:DatatypeProperty ;
    rdfs:label "tag in maintenance system"@en ;
    rdfs:comment "Held as three SEPARATE tag fields, not one identifier, for the same reason the waste register separates label from signage: 'are asset names consistent across drawings, BMS and maintenance records?' is only answerable if the disagreement can be represented."@en ;
    rdfs:domain ontosage:AssetEngineeringProfile ;
    rdfs:range xsd:string .
```
{% endraw %}
