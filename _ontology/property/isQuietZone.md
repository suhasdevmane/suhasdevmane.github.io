---
title: "hbco:isQuietZone"
layout: post
permalink: /ontology/property/isQuietZone/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › isQuietZone

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#isQuietZone` |
| Label | is quiet zone |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:boolean` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

True if this floor or space is designated as a quiet study area.

## Examples

- true

## Turtle

{% raw %}
```turtle
@prefix hbco: <http://ontosage.org/hbco#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

hbco:isQuietZone a owl:DatatypeProperty ;
    rdfs:label "is quiet zone"@en ;
    rdfs:comment "True if this floor or space is designated as a quiet study area."@en ;
    rdfs:isDefinedBy <http://ontosage.org/ontology> ;
    rdfs:range xsd:boolean ;
    skos:example "true" .
```
{% endraw %}
