---
title: "ontosage:statusObservedAt"
layout: post
permalink: /ontology/property/statusObservedAt/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › statusObservedAt

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#statusObservedAt` |
| Label | status observed at |
| Kind | datatype property |
| Domain | [`ontosage:AssetStatus`]({{ '/ontology/class/AssetStatus/' | relative_url }}) |
| Range | `xsd:dateTime` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

When the issuing source last confirmed this state. A three-week-old 'operational' is not current status, and the freshness gate judges it exactly as it judges a sensor reading.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:statusObservedAt a owl:DatatypeProperty ;
    rdfs:label "status observed at"@en ;
    rdfs:comment "When the issuing source last confirmed this state. A three-week-old 'operational' is not current status, and the freshness gate judges it exactly as it judges a sensor reading."@en ;
    rdfs:domain ontosage:AssetStatus ;
    rdfs:range xsd:dateTime .
```
{% endraw %}
