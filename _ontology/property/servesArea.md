---
title: "ontosage:servesArea"
layout: post
permalink: /ontology/property/servesArea/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › servesArea

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#servesArea` |
| Label | serves area |
| Kind | datatype property |
| Domain | [`ontosage:AssetEngineeringProfile`]({{ '/ontology/class/AssetEngineeringProfile/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The part of the building this asset serves, which is distinct from where it SITS. An AHU in a ground-floor plant room serving Level 3 is the ordinary case, and conflating the two sends an engineer to the wrong floor.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`asset_engineering`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#asset_engineering) | `serves_area` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:servesArea a owl:DatatypeProperty ;
    rdfs:label "serves area"@en ;
    rdfs:comment "The part of the building this asset serves, which is distinct from where it SITS. An AHU in a ground-floor plant room serving Level 3 is the ordinary case, and conflating the two sends an engineer to the wrong floor."@en ;
    rdfs:domain ontosage:AssetEngineeringProfile ;
    rdfs:range xsd:string .
```
{% endraw %}
