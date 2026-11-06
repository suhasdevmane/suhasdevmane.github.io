---
title: "ontosage:accessibilityVerifiedOn"
layout: post
permalink: /ontology/property/accessibilityVerifiedOn/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › accessibilityVerifiedOn

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#accessibilityVerifiedOn` |
| Label | accessibility verified on |
| Kind | datatype property |
| Domain | [`ontosage:AccessibilityFeature`]({{ '/ontology/class/AccessibilityFeature/' | relative_url }}) |
| Range | `xsd:date` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

When the feature was last inspected. A hearing loop verified three years ago is a claim about a building that may no longer be true.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:accessibilityVerifiedOn a owl:DatatypeProperty ;
    rdfs:label "accessibility verified on"@en ;
    rdfs:comment "When the feature was last inspected. A hearing loop verified three years ago is a claim about a building that may no longer be true."@en ;
    rdfs:domain ontosage:AccessibilityFeature ;
    rdfs:range xsd:date .
```
{% endraw %}
