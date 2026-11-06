---
title: "ontosage:observedValue"
layout: post
permalink: /ontology/property/observedValue/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › observedValue

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#observedValue` |
| Label | observed value |
| Kind | datatype property |
| Domain | [`ontosage:AnomalyEvent`]({{ '/ontology/class/AnomalyEvent/' | relative_url }}) |
| Range | `xsd:double` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The reading that deviated, in the unit of the point it is about (ontosage:aboutPoint). Compared against ontosage:baselineValue; neither is meaningful without the other.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:observedValue a owl:DatatypeProperty ;
    rdfs:label "observed value"@en ;
    rdfs:comment "The reading that deviated, in the unit of the point it is about (ontosage:aboutPoint). Compared against ontosage:baselineValue; neither is meaningful without the other."@en ;
    rdfs:domain ontosage:AnomalyEvent ;
    rdfs:range xsd:double .
```
{% endraw %}
