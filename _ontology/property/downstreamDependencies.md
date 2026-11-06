---
title: "ontosage:downstreamDependencies"
layout: post
permalink: /ontology/property/downstreamDependencies/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › downstreamDependencies

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#downstreamDependencies` |
| Label | downstream dependencies |
| Kind | datatype property |
| Domain | [`ontosage:AssetEngineeringProfile`]({{ '/ontology/class/AssetEngineeringProfile/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

What stops working when this is isolated. The field that turns a five-minute isolation into a decision.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`asset_engineering`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#asset_engineering) | `downstream` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:downstreamDependencies a owl:DatatypeProperty ;
    rdfs:label "downstream dependencies"@en ;
    rdfs:comment "What stops working when this is isolated. The field that turns a five-minute isolation into a decision."@en ;
    rdfs:domain ontosage:AssetEngineeringProfile ;
    rdfs:range xsd:string .
```
{% endraw %}
