---
title: "hbco:spaceFunction"
layout: post
permalink: /ontology/property/spaceFunction/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › spaceFunction

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#spaceFunction` |
| Label | space function |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Brief descriptor of the primary function of this space (e.g. seminar room, lab, office, corridor, atrium).

## Examples

- "seminar room"

## Turtle

{% raw %}
```turtle
@prefix hbco: <http://ontosage.org/hbco#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

hbco:spaceFunction a owl:DatatypeProperty ;
    rdfs:label "space function"@en ;
    rdfs:comment "Brief descriptor of the primary function of this space (e.g. seminar room, lab, office, corridor, atrium)."@en ;
    rdfs:isDefinedBy <http://ontosage.org/ontology> ;
    rdfs:range xsd:string ;
    skos:example "\"seminar room\"" .
```
{% endraw %}
