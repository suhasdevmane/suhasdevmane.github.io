---
title: "ontosage:capacityLitres"
layout: post
permalink: /ontology/property/capacityLitres/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › capacityLitres

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#capacityLitres` |
| Label | capacity in litres |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:integer` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The schema gives no definition for this term.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`waste_collection`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#waste_collection) | `capacity_litres` | `xsd:integer` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:capacityLitres a owl:DatatypeProperty ;
    rdfs:label "capacity in litres"@en ;
    rdfs:range xsd:integer .
```
{% endraw %}
