---
title: "ontosage:buildingOwner"
layout: post
permalink: /ontology/property/buildingOwner/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › buildingOwner

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#buildingOwner` |
| Label | owner |
| Kind | datatype property |
| Domain | [`brick:Building`](https://ontology.brickschema.org/1.4/#brick:Building) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The organisation that owns the building. Distinct from the operator: an owner may lease the building to whoever runs it day to day, and 'who owns this?' and 'who runs this?' are different questions with different answers.

## Examples

- "Example University"

## Turtle

{% raw %}
```turtle
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:buildingOwner a owl:DatatypeProperty ;
    rdfs:label "owner"@en ;
    rdfs:comment "The organisation that owns the building. Distinct from the operator: an owner may lease the building to whoever runs it day to day, and 'who owns this?' and 'who runs this?' are different questions with different answers."@en ;
    rdfs:domain brick:Building ;
    rdfs:range xsd:string ;
    skos:example "\"Example University\"" .
```
{% endraw %}
