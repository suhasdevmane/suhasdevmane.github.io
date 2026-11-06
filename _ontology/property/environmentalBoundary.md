---
title: "ontosage:environmentalBoundary"
layout: post
permalink: /ontology/property/environmentalBoundary/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › environmentalBoundary

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#environmentalBoundary` |
| Label | environmental boundary |
| Kind | object property |
| Domain | not declared (any subject) |
| Range | [`brick:Location`](https://ontology.brickschema.org/1.4/#brick:Location) |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The space whose conditions this point actually measures. Usually the space that contains it — but NOT always, which is the entire reason the property exists: a sensor in a duct, a plenum, or mounted on a corridor wall serving an adjacent room has a containing space that is not the space it describes. The non-substitution rule (Master 8) is enforced against THIS, never against containment.

## Turtle

{% raw %}
```turtle
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ontosage:environmentalBoundary a owl:ObjectProperty ;
    rdfs:label "environmental boundary"@en ;
    rdfs:comment "The space whose conditions this point actually measures. Usually the space that contains it — but NOT always, which is the entire reason the property exists: a sensor in a duct, a plenum, or mounted on a corridor wall serving an adjacent room has a containing space that is not the space it describes. The non-substitution rule (Master 8) is enforced against THIS, never against containment."@en ;
    rdfs:range brick:Location .
```
{% endraw %}
