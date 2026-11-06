---
title: "ontosage:hasConfigurationPeriod"
layout: post
permalink: /ontology/property/hasConfigurationPeriod/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › hasConfigurationPeriod

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#hasConfigurationPeriod` |
| Label | has configuration period |
| Kind | object property |
| Domain | [`brick:Point`](https://ontology.brickschema.org/1.4/#brick:Point) |
| Range | [`ontosage:ConfigurationPeriod`]({{ '/ontology/class/ConfigurationPeriod/' | relative_url }}) |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The schema gives no definition for this term.

## Turtle

{% raw %}
```turtle
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ontosage:hasConfigurationPeriod a owl:ObjectProperty ;
    rdfs:label "has configuration period"@en ;
    rdfs:domain brick:Point ;
    rdfs:range ontosage:ConfigurationPeriod .
```
{% endraw %}
