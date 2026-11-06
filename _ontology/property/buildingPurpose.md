---
title: "ontosage:buildingPurpose"
layout: post
permalink: /ontology/property/buildingPurpose/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › buildingPurpose

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#buildingPurpose` |
| Label | purpose |
| Kind | datatype property |
| Domain | [`brick:Building`](https://ontology.brickschema.org/1.4/#brick:Building) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

One or two sentences on what the building is FOR, in plain language. brick:buildingPrimaryFunction gives a controlled classification ('Education'); this gives the sentence a person actually wanted.

## Examples

- "Teaching and research building for computer science and mathematics, with lecture theatres, labs and academic offices."

## Turtle

{% raw %}
```turtle
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:buildingPurpose a owl:DatatypeProperty ;
    rdfs:label "purpose"@en ;
    rdfs:comment "One or two sentences on what the building is FOR, in plain language. brick:buildingPrimaryFunction gives a controlled classification ('Education'); this gives the sentence a person actually wanted."@en ;
    rdfs:domain brick:Building ;
    rdfs:range xsd:string ;
    skos:example "\"Teaching and research building for computer science and mathematics, with lecture theatres, labs and academic offices.\"" .
```
{% endraw %}
