---
title: "hbco:defaultUnit"
layout: post
permalink: /ontology/property/defaultUnit/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › defaultUnit

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#defaultUnit` |
| Label | default unit |
| Kind | datatype property |
| Domain | [`hbco:Concept`]({{ '/ontology/class/Concept/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

QUDT unit symbol or plain string (e.g. 'degC', 'ppm', 'lux') for the primary measurement of this concept.

## Examples

- "ppm"

## Turtle

{% raw %}
```turtle
@prefix hbco: <http://ontosage.org/hbco#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

hbco:defaultUnit a owl:DatatypeProperty ;
    rdfs:label "default unit"@en ;
    rdfs:comment "QUDT unit symbol or plain string (e.g. 'degC', 'ppm', 'lux') for the primary measurement of this concept."@en ;
    rdfs:domain hbco:Concept ;
    rdfs:isDefinedBy <http://ontosage.org/ontology> ;
    rdfs:range xsd:string ;
    skos:example "\"ppm\"" .
```
{% endraw %}
