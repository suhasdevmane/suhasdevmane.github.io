---
title: "ontosage:routeTo"
layout: post
permalink: /ontology/property/routeTo/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › routeTo

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#routeTo` |
| Label | route to |
| Kind | datatype property |
| Domain | [`ontosage:AccessibleRoute`]({{ '/ontology/class/AccessibleRoute/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The schema gives no definition for this term.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`accessible_route`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#accessible_route) | `to_point` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:routeTo a owl:DatatypeProperty ;
    rdfs:label "route to"@en ;
    rdfs:domain ontosage:AccessibleRoute ;
    rdfs:range xsd:string .
```
{% endraw %}
