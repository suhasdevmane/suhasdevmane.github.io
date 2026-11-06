---
title: "ontosage:buildingAddress"
layout: post
permalink: /ontology/property/buildingAddress/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › buildingAddress

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#buildingAddress` |
| Label | address |
| Kind | datatype property |
| Domain | [`brick:Building`](https://ontology.brickschema.org/1.4/#brick:Building) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Street address as a person would write it. Brick carries coordinates for geometry; this carries the form a human asks for and can act on.

## Examples

- "Example Building, 1 Campus Road, Exampletown EX1 2AB"

## Turtle

{% raw %}
```turtle
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:buildingAddress a owl:DatatypeProperty ;
    rdfs:label "address"@en ;
    rdfs:comment "Street address as a person would write it. Brick carries coordinates for geometry; this carries the form a human asks for and can act on."@en ;
    rdfs:domain brick:Building ;
    rdfs:range xsd:string ;
    skos:example "\"Example Building, 1 Campus Road, Exampletown EX1 2AB\"" .
```
{% endraw %}
