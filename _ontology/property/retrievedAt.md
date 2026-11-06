---
title: "ontosage:retrievedAt"
layout: post
permalink: /ontology/property/retrievedAt/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › retrievedAt

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#retrievedAt` |
| Label | retrieved at |
| Kind | datatype property |
| Domain | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| Range | `xsd:dateTime` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

When the service obtained the record. The THIRD time, kept separate from effectiveFrom (when it applies) and statusObservedAt (when it was observed). Retrieval time never substitutes for either — a record fetched now may have taken effect last year or take effect next Monday.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:retrievedAt a owl:DatatypeProperty ;
    rdfs:label "retrieved at"@en ;
    rdfs:comment "When the service obtained the record. The THIRD time, kept separate from effectiveFrom (when it applies) and statusObservedAt (when it was observed). Retrieval time never substitutes for either — a record fetched now may have taken effect last year or take effect next Monday."@en ;
    rdfs:domain ontosage:IntervalRecord ;
    rdfs:range xsd:dateTime .
```
{% endraw %}
