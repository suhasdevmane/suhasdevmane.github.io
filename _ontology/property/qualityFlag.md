---
title: "ontosage:qualityFlag"
layout: post
permalink: /ontology/property/qualityFlag/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › qualityFlag

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#qualityFlag` |
| Label | data quality flag |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Operator-asserted quality state of this point: good | suspect | faulty | unknown. Distinct from computed health (which comes from the readings themselves) because an operator may know a sensor is faulty before the data shows it, and may know a plausible-looking series is wrong.

## Examples

- "suspect"

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:qualityFlag a owl:DatatypeProperty ;
    rdfs:label "data quality flag"@en ;
    rdfs:comment "Operator-asserted quality state of this point: good | suspect | faulty | unknown. Distinct from computed health (which comes from the readings themselves) because an operator may know a sensor is faulty before the data shows it, and may know a plausible-looking series is wrong."@en ;
    rdfs:range xsd:string ;
    skos:example "\"suspect\"" .
```
{% endraw %}
