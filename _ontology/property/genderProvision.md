---
title: "ontosage:genderProvision"
layout: post
permalink: /ontology/property/genderProvision/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › genderProvision

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#genderProvision` |
| Label | gender provision |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Who the facility is for: male, female, gender-neutral or unisex. Kept separate from accessibility because a reader may need either, and often needs both.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:genderProvision a owl:DatatypeProperty ;
    rdfs:label "gender provision"@en ;
    rdfs:comment "Who the facility is for: male, female, gender-neutral or unisex. Kept separate from accessibility because a reader may need either, and often needs both."@en ;
    rdfs:range xsd:string .
```
{% endraw %}
