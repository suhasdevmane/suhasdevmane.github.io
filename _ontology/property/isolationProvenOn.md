---
title: "ontosage:isolationProvenOn"
layout: post
permalink: /ontology/property/isolationProvenOn/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › isolationProvenOn

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#isolationProvenOn` |
| Label | isolation proven on |
| Kind | datatype property |
| Domain | [`ontosage:AssetEngineeringProfile`]({{ '/ontology/class/AssetEngineeringProfile/' | relative_url }}) |
| Range | `xsd:date` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

When the isolation was last PROVED dead rather than assumed. A documented isolation point that nobody has proved is a claim.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`asset_engineering`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#asset_engineering) | `isolation_proven_on` | `xsd:date` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:isolationProvenOn a owl:DatatypeProperty ;
    rdfs:label "isolation proven on"@en ;
    rdfs:comment "When the isolation was last PROVED dead rather than assumed. A documented isolation point that nobody has proved is a claim."@en ;
    rdfs:domain ontosage:AssetEngineeringProfile ;
    rdfs:range xsd:date .
```
{% endraw %}
