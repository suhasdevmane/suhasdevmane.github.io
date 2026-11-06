---
title: "ontosage:seatedRests"
layout: post
permalink: /ontology/property/seatedRests/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › seatedRests

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#seatedRests` |
| Label | seated rests |
| Kind | datatype property |
| Domain | [`ontosage:AccessibleRoute`]({{ '/ontology/class/AccessibleRoute/' | relative_url }}) |
| Range | `xsd:integer` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

How many places to sit along the route. Asked directly by visitors who need regular rests.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`accessible_route`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#accessible_route) | `seated_rests` | `xsd:integer` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:seatedRests a owl:DatatypeProperty ;
    rdfs:label "seated rests"@en ;
    rdfs:comment "How many places to sit along the route. Asked directly by visitors who need regular rests."@en ;
    rdfs:domain ontosage:AccessibleRoute ;
    rdfs:range xsd:integer .
```
{% endraw %}
