---
title: "ontosage:steps"
layout: post
permalink: /ontology/property/steps/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › steps

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#steps` |
| Label | how-to steps |
| Kind | datatype property |
| Domain | [`ontosage:Procedure`]({{ '/ontology/class/Procedure/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Ordered steps for a Procedure, separated by semicolons; OntoSage renders them as a numbered list.

## Examples

- "Note the room and floor; Email the helpdesk or call; Use the app for urgent issues"

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:steps a owl:DatatypeProperty ;
    rdfs:label "how-to steps"@en ;
    rdfs:comment "Ordered steps for a Procedure, separated by semicolons; OntoSage renders them as a numbered list."@en ;
    rdfs:domain ontosage:Procedure ;
    rdfs:range xsd:string ;
    skos:example "\"Note the room and floor; Email the helpdesk or call; Use the app for urgent issues\"" .
```
{% endraw %}
