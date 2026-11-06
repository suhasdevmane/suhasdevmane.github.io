---
title: "ontosage:alternativeCapacity"
layout: post
permalink: /ontology/property/alternativeCapacity/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › alternativeCapacity

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#alternativeCapacity` |
| Label | alternative capacity |
| Kind | datatype property |
| Domain | [`ontosage:ContinuityProvision`]({{ '/ontology/class/ContinuityProvision/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

What the alternative can actually carry, against what the service needs. A half-capacity fallback is a different answer from a full one.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`continuity_provision`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#continuity_provision) | `alternative_capacity` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:alternativeCapacity a owl:DatatypeProperty ;
    rdfs:label "alternative capacity"@en ;
    rdfs:comment "What the alternative can actually carry, against what the service needs. A half-capacity fallback is a different answer from a full one."@en ;
    rdfs:domain ontosage:ContinuityProvision ;
    rdfs:range xsd:string .
```
{% endraw %}
