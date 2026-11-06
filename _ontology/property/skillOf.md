---
title: "ontosage:skillOf"
layout: post
permalink: /ontology/property/skillOf/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › skillOf

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#skillOf` |
| Label | skill of modality |
| Kind | datatype property |
| Domain | [`ontosage:ForecastSkill`]({{ '/ontology/class/ForecastSkill/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The schema gives no definition for this term.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:skillOf a owl:DatatypeProperty ;
    rdfs:label "skill of modality"@en ;
    rdfs:domain ontosage:ForecastSkill ;
    rdfs:range xsd:string .
```
{% endraw %}
