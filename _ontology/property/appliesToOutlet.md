---
title: "ontosage:appliesToOutlet"
layout: post
permalink: /ontology/property/appliesToOutlet/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › appliesToOutlet

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#appliesToOutlet` |
| Label | applies to outlet |
| Kind | object property |
| Domain | [`ontosage:PotabilityStatement`]({{ '/ontology/class/PotabilityStatement/' | relative_url }}) |
| Range | not declared |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The amenity, space or floor this statement covers. Scoped rather than building-wide because potability commonly differs between a mains-fed drinking point and a tank-fed tap in the same building.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ontosage:appliesToOutlet a owl:ObjectProperty ;
    rdfs:label "applies to outlet"@en ;
    rdfs:comment "The amenity, space or floor this statement covers. Scoped rather than building-wide because potability commonly differs between a mains-fed drinking point and a tank-fed tap in the same building."@en ;
    rdfs:domain ontosage:PotabilityStatement .
```
{% endraw %}
