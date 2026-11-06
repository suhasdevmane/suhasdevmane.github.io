---
title: "ontosage:buildingOperator"
layout: post
permalink: /ontology/property/buildingOperator/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › buildingOperator

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#buildingOperator` |
| Label | operator |
| Kind | datatype property |
| Domain | [`brick:Building`](https://ontology.brickschema.org/1.4/#brick:Building) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The organisation or team responsible for running the building day to day — usually who an occupant actually needs when something is wrong.

## Examples

- "Estates & Campus Services"

## Turtle

{% raw %}
```turtle
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:buildingOperator a owl:DatatypeProperty ;
    rdfs:label "operator"@en ;
    rdfs:comment "The organisation or team responsible for running the building day to day — usually who an occupant actually needs when something is wrong."@en ;
    rdfs:domain brick:Building ;
    rdfs:range xsd:string ;
    skos:example "\"Estates & Campus Services\"" .
```
{% endraw %}
