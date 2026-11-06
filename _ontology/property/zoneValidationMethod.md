---
title: "ontosage:zoneValidationMethod"
layout: post
permalink: /ontology/property/zoneValidationMethod/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › zoneValidationMethod

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#zoneValidationMethod` |
| Label | zone validation method |
| Kind | datatype property |
| Domain | [`ontosage:ServedZone`]({{ '/ontology/class/ServedZone/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

How the serving relation was established: mechanical\_schedule | commissioning\_survey | tracer\_test | as\_built\_drawing. Recorded because 'validated' means little without saying against what — and because a tracer test and a drawing are not equally strong evidence.

## Examples

- "commissioning\_survey"

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:zoneValidationMethod a owl:DatatypeProperty ;
    rdfs:label "zone validation method"@en ;
    rdfs:comment "How the serving relation was established: mechanical_schedule | commissioning_survey | tracer_test | as_built_drawing. Recorded because 'validated' means little without saying against what — and because a tracer test and a drawing are not equally strong evidence."@en ;
    rdfs:domain ontosage:ServedZone ;
    rdfs:range xsd:string ;
    skos:example "\"commissioning_survey\"" .
```
{% endraw %}
