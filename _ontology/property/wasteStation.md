---
title: "ontosage:wasteStation"
layout: post
permalink: /ontology/property/wasteStation/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › wasteStation

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#wasteStation` |
| Label | waste station |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The grouping of bins a user meets together. Conflicts are judged WITHIN a station, because that is where somebody stands and chooses.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`waste_collection`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#waste_collection) | `station` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:wasteStation a owl:DatatypeProperty ;
    rdfs:label "waste station"@en ;
    rdfs:comment "The grouping of bins a user meets together. Conflicts are judged WITHIN a station, because that is where somebody stands and chooses."@en ;
    rdfs:range xsd:string .
```
{% endraw %}
