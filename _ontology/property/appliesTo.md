---
title: "ontosage:appliesTo"
layout: post
permalink: /ontology/property/appliesTo/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › appliesTo

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#appliesTo` |
| Label | applies to |
| Kind | object property |
| Domain | not declared (any subject) |
| Range | [`brick:Location`](https://ontology.brickschema.org/1.4/#brick:Location) |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The floor, room or zone a closure period or service schedule covers. No domain is declared: it is used by several record kinds, and a domain would type each of them as one class.

## Turtle

{% raw %}
```turtle
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ontosage:appliesTo a owl:ObjectProperty ;
    rdfs:label "applies to"@en ;
    rdfs:comment "The floor, room or zone a closure period or service schedule covers. No domain is declared: it is used by several record kinds, and a domain would type each of them as one class."@en ;
    rdfs:range brick:Location .
```
{% endraw %}
