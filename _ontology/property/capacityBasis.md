---
title: "ontosage:capacityBasis"
layout: post
permalink: /ontology/property/capacityBasis/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › capacityBasis

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#capacityBasis` |
| Label | capacity basis |
| Kind | datatype property |
| Domain | [`brick:Space`](https://ontology.brickschema.org/1.4/#brick:Space) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

How the space's hbco:roomCapacity was arrived at: certified, surveyed, or ESTIMATED from floor-plan area at a stated density, with the density and its source. A capacity with no basis cannot be told apart from a certified fire capacity, and an estimate quoted as a limit is a safety claim nobody made.

## Turtle

{% raw %}
```turtle
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:capacityBasis a owl:DatatypeProperty ;
    rdfs:label "capacity basis"@en ;
    rdfs:comment "How the space's hbco:roomCapacity was arrived at: certified, surveyed, or ESTIMATED from floor-plan area at a stated density, with the density and its source. A capacity with no basis cannot be told apart from a certified fire capacity, and an estimate quoted as a limit is a safety claim nobody made."@en ;
    rdfs:domain brick:Space ;
    rdfs:range xsd:string .
```
{% endraw %}
