---
title: "ontosage:allowMinutes"
layout: post
permalink: /ontology/property/allowMinutes/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › allowMinutes

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#allowMinutes` |
| Label | allow minutes |
| Kind | datatype property |
| Domain | [`ontosage:AccessibleRoute`]({{ '/ontology/class/AccessibleRoute/' | relative_url }}) |
| Range | `xsd:integer` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Time to ALLOW, including doors, lifts, waiting and check-in — not walking time, because 'how long should I allow' is the question actually asked.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`accessible_route`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#accessible_route) | `allow_minutes` | `xsd:integer` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:allowMinutes a owl:DatatypeProperty ;
    rdfs:label "allow minutes"@en ;
    rdfs:comment "Time to ALLOW, including doors, lifts, waiting and check-in — not walking time, because 'how long should I allow' is the question actually asked."@en ;
    rdfs:domain ontosage:AccessibleRoute ;
    rdfs:range xsd:integer .
```
{% endraw %}
