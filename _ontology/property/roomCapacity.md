---
title: "hbco:roomCapacity"
layout: post
permalink: /ontology/property/roomCapacity/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › roomCapacity

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#roomCapacity` |
| Label | room capacity |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:integer` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Estimated or certified occupant capacity of a room or space (persons).

## Examples

- 40

## Turtle

{% raw %}
```turtle
@prefix hbco: <http://ontosage.org/hbco#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

hbco:roomCapacity a owl:DatatypeProperty ;
    rdfs:label "room capacity"@en ;
    rdfs:comment "Estimated or certified occupant capacity of a room or space (persons)."@en ;
    rdfs:isDefinedBy <http://ontosage.org/ontology> ;
    rdfs:range xsd:integer ;
    skos:example "40" .
```
{% endraw %}
