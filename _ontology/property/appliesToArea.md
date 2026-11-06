---
title: "ontosage:appliesToArea"
layout: post
permalink: /ontology/property/appliesToArea/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › appliesToArea

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#appliesToArea` |
| Label | applies to area |
| Kind | object property |
| Domain | [`ontosage:CompetencyRecord`]({{ '/ontology/class/CompetencyRecord/' | relative_url }}) |
| Range | [`brick:Location`](https://ontology.brickschema.org/1.4/#brick:Location) |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The restricted area or space a competency is required for.

## Turtle

{% raw %}
```turtle
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ontosage:appliesToArea a owl:ObjectProperty ;
    rdfs:label "applies to area"@en ;
    rdfs:comment "The restricted area or space a competency is required for."@en ;
    rdfs:domain ontosage:CompetencyRecord ;
    rdfs:range brick:Location .
```
{% endraw %}
