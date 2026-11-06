---
title: "hbco:personaDepth"
layout: post
permalink: /ontology/property/personaDepth/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › personaDepth

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#personaDepth` |
| Label | persona depth |
| Kind | datatype property |
| Domain | [`hbco:Concept`]({{ '/ontology/class/Concept/' | relative_url }}) |
| Range | `xsd:integer` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Integer 0-4 indicating the level of technical detail appropriate when explaining this concept to a stakeholder (0=lay occupant, 4=expert). Aligns with the stakeholder roles in Module C.

## Examples

- 0 (explain 'stuffy' to an occupant in plain terms, not as a CO₂ ppm figure)

## Turtle

{% raw %}
```turtle
@prefix hbco: <http://ontosage.org/hbco#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

hbco:personaDepth a owl:DatatypeProperty ;
    rdfs:label "persona depth"@en ;
    rdfs:comment "Integer 0-4 indicating the level of technical detail appropriate when explaining this concept to a stakeholder (0=lay occupant, 4=expert). Aligns with the stakeholder roles in Module C."@en ;
    rdfs:domain hbco:Concept ;
    rdfs:isDefinedBy <http://ontosage.org/ontology> ;
    rdfs:range xsd:integer ;
    skos:example "0  (explain 'stuffy' to an occupant in plain terms, not as a CO₂ ppm figure)" .
```
{% endraw %}
