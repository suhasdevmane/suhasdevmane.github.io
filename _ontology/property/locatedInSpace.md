---
title: "ontosage:locatedInSpace"
layout: post
permalink: /ontology/property/locatedInSpace/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › locatedInSpace

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#locatedInSpace` |
| Label | located in space |
| Kind | object property |
| Domain | not declared (any subject) |
| Range | [`brick:Location`](https://ontology.brickschema.org/1.4/#brick:Location) |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The space a record's location text names exactly, resolved when the record was lifted. Joins a register row to the sensors and properties of that space. Written beside ontosage:locationText, never instead of it, and absent wherever the text named no single space.

## Examples

- ?record ontosage:locatedInSpace ?space . ?sensor brick:hasLocation ?space .

## Turtle

{% raw %}
```turtle
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:locatedInSpace a owl:ObjectProperty ;
    rdfs:label "located in space"@en ;
    rdfs:comment "The space a record's location text names exactly, resolved when the record was lifted. Joins a register row to the sensors and properties of that space. Written beside ontosage:locationText, never instead of it, and absent wherever the text named no single space."@en ;
    rdfs:range brick:Location ;
    skos:example "?record ontosage:locatedInSpace ?space . ?sensor brick:hasLocation ?space ." .
```
{% endraw %}
