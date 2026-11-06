---
title: "ontosage:reportSubjectText"
layout: post
permalink: /ontology/property/reportSubjectText/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › reportSubjectText

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#reportSubjectText` |
| Label | report subject |
| Kind | datatype property |
| Domain | [`ontosage:Report`]({{ '/ontology/class/Report/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The stakeholder's own words describing what they are reporting.

## Examples

- "water dripping from the ceiling near the lift"

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:reportSubjectText a owl:DatatypeProperty ;
    rdfs:label "report subject"@en ;
    rdfs:comment "The stakeholder's own words describing what they are reporting."@en ;
    rdfs:domain ontosage:Report ;
    rdfs:range xsd:string ;
    skos:example "\"water dripping from the ceiling near the lift\"" .
```
{% endraw %}
