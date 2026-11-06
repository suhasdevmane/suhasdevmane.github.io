---
title: "ontosage:calibrationMethod"
layout: post
permalink: /ontology/property/calibrationMethod/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › calibrationMethod

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#calibrationMethod` |
| Label | calibration method |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

How the calibration was performed, and against what reference. Master 10.1 asks for comparison against trusted reference instruments; recording the method is what makes one calibration comparable to another.

## Examples

- "NDIR two-point against a certified 400/1000 ppm reference"

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:calibrationMethod a owl:DatatypeProperty ;
    rdfs:label "calibration method"@en ;
    rdfs:comment "How the calibration was performed, and against what reference. Master 10.1 asks for comparison against trusted reference instruments; recording the method is what makes one calibration comparable to another."@en ;
    rdfs:range xsd:string ;
    skos:example "\"NDIR two-point against a certified 400/1000 ppm reference\"" .
```
{% endraw %}
