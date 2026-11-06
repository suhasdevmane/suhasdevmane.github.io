---
title: "ontosage:capabilityCategory"
layout: post
permalink: /ontology/property/capabilityCategory/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › capabilityCategory

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#capabilityCategory` |
| Label | capability category |
| Kind | datatype property |
| Domain | [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A coarse category tag for grouping/filtering. Suggested values: AMENITIES, ACCESSIBILITY, INFORMATION, PROCEDURE, MAINTENANCE, SAFETY, SUSTAINABILITY.

## Examples

- "MAINTENANCE"

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:capabilityCategory a owl:DatatypeProperty ;
    rdfs:label "capability category"@en ;
    rdfs:comment "A coarse category tag for grouping/filtering. Suggested values: AMENITIES, ACCESSIBILITY, INFORMATION, PROCEDURE, MAINTENANCE, SAFETY, SUSTAINABILITY."@en ;
    rdfs:domain ontosage:Capability ;
    rdfs:range xsd:string ;
    skos:example "\"MAINTENANCE\"" .
```
{% endraw %}
