---
title: "ontosage:accessibilityVerified"
layout: post
permalink: /ontology/property/accessibilityVerified/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › accessibilityVerified

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#accessibilityVerified` |
| Label | accessibility verified |
| Kind | datatype property |
| Domain | [`ontosage:AccessibilityFeature`]({{ '/ontology/class/AccessibilityFeature/' | relative_url }}) |
| Range | `xsd:boolean` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

True only when the feature has been inspected and confirmed working. ABSENT OR FALSE MEANS UNVERIFIED, and an unverified feature may NOT be presented as accessible — the hard filter fails closed for the same reason a served zone does, but the consequence of getting it wrong is a person stranded rather than a wrong number.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:accessibilityVerified a owl:DatatypeProperty ;
    rdfs:label "accessibility verified"@en ;
    rdfs:comment "True only when the feature has been inspected and confirmed working. ABSENT OR FALSE MEANS UNVERIFIED, and an unverified feature may NOT be presented as accessible — the hard filter fails closed for the same reason a served zone does, but the consequence of getting it wrong is a person stranded rather than a wrong number."@en ;
    rdfs:domain ontosage:AccessibilityFeature ;
    rdfs:range xsd:boolean .
```
{% endraw %}
