---
title: "ontosage:buildingStoreys"
layout: post
permalink: /ontology/property/buildingStoreys/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › buildingStoreys

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#buildingStoreys` |
| Label | number of storeys |
| Kind | datatype property |
| Domain | [`brick:Building`](https://ontology.brickschema.org/1.4/#brick:Building) |
| Range | `xsd:integer` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Declared storey count. Usually the live count of brick:Floor instances is the better answer and is preferred; this exists for buildings whose declared storeys differ from the floors modelled in the graph (a basement or plant deck that carries no sensors).

## Examples

- "5"^^xsd:integer

## Turtle

{% raw %}
```turtle
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:buildingStoreys a owl:DatatypeProperty ;
    rdfs:label "number of storeys"@en ;
    rdfs:comment "Declared storey count. Usually the live count of brick:Floor instances is the better answer and is preferred; this exists for buildings whose declared storeys differ from the floors modelled in the graph (a basement or plant deck that carries no sensors)."@en ;
    rdfs:domain brick:Building ;
    rdfs:range xsd:integer ;
    skos:example "\"5\"^^xsd:integer" .
```
{% endraw %}
