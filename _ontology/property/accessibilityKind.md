---
title: "ontosage:accessibilityKind"
layout: post
permalink: /ontology/property/accessibilityKind/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › accessibilityKind

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#accessibilityKind` |
| Label | accessibility feature kind |
| Kind | datatype property |
| Domain | [`ontosage:AccessibilityFeature`]({{ '/ontology/class/AccessibilityFeature/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

hearing\_loop | tactile\_paving | changing\_places | accessible\_wc | power\_assisted\_door | accessible\_parking | step\_free\_entrance | adjustable\_desk.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:accessibilityKind a owl:DatatypeProperty ;
    rdfs:label "accessibility feature kind"@en ;
    rdfs:comment "hearing_loop | tactile_paving | changing_places | accessible_wc | power_assisted_door | accessible_parking | step_free_entrance | adjustable_desk."@en ;
    rdfs:domain ontosage:AccessibilityFeature ;
    rdfs:range xsd:string .
```
{% endraw %}
