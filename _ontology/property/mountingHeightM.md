---
title: "ontosage:mountingHeightM"
layout: post
permalink: /ontology/property/mountingHeightM/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › mountingHeightM

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#mountingHeightM` |
| Label | mounting height (m) |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:decimal` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Height above finished floor. HSE guidance places CO2 monitors at head height and away from openings; a sensor at ceiling level measures something different from one at desk level, and an answer that ignores this compares unlike with unlike.

## Examples

- "1.2"^^xsd:decimal

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:mountingHeightM a owl:DatatypeProperty ;
    rdfs:label "mounting height (m)"@en ;
    rdfs:comment "Height above finished floor. HSE guidance places CO2 monitors at head height and away from openings; a sensor at ceiling level measures something different from one at desk level, and an answer that ignores this compares unlike with unlike."@en ;
    rdfs:range xsd:decimal ;
    skos:example "\"1.2\"^^xsd:decimal" .
```
{% endraw %}
