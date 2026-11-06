---
title: "ontosage:buildingAccessPolicy"
layout: post
permalink: /ontology/property/buildingAccessPolicy/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › buildingAccessPolicy

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#buildingAccessPolicy` |
| Label | access policy |
| Kind | datatype property |
| Domain | [`brick:Building`](https://ontology.brickschema.org/1.4/#brick:Building) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Whether and how outsiders may enter — the honest answer to 'are visitors allowed?' and 'is check-in staffed or automated?', which otherwise get guessed.

## Examples

- "Visitors welcome during staffed reception hours; sign in at the ground-floor desk."

## Turtle

{% raw %}
```turtle
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:buildingAccessPolicy a owl:DatatypeProperty ;
    rdfs:label "access policy"@en ;
    rdfs:comment "Whether and how outsiders may enter — the honest answer to 'are visitors allowed?' and 'is check-in staffed or automated?', which otherwise get guessed."@en ;
    rdfs:domain brick:Building ;
    rdfs:range xsd:string ;
    skos:example "\"Visitors welcome during staffed reception hours; sign in at the ground-floor desk.\"" .
```
{% endraw %}
