---
title: "ontosage:serviceStatus"
layout: post
permalink: /ontology/property/serviceStatus/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › serviceStatus

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#serviceStatus` |
| Label | current service status |
| Kind | object property |
| Domain | not declared (any subject) |
| Range | [`ontosage:AssetStatus`]({{ '/ontology/class/AssetStatus/' | relative_url }}) |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Convenience link from an asset to its newest AssetStatus record. The records remain the source of truth — this is a shortcut for the common 'is it working now' query, not a replacement for the history.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ontosage:serviceStatus a owl:ObjectProperty ;
    rdfs:label "current service status"@en ;
    rdfs:comment "Convenience link from an asset to its newest AssetStatus record. The records remain the source of truth — this is a shortcut for the common 'is it working now' query, not a replacement for the history."@en ;
    rdfs:range ontosage:AssetStatus .
```
{% endraw %}
