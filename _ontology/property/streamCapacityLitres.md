---
title: "ontosage:streamCapacityLitres"
layout: post
permalink: /ontology/property/streamCapacityLitres/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › streamCapacityLitres

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#streamCapacityLitres` |
| Label | stream capacity (L) |
| Kind | datatype property |
| Domain | [`ontosage:WastePoint`]({{ '/ontology/class/WastePoint/' | relative_url }}) |
| Range | `xsd:decimal` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Nominal capacity of this point for this stream. Needed to turn a fill-level percentage into anything actionable: 80% of a 25 L office bin and 80% of a 1100 L euro-bin are different problems.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:streamCapacityLitres a owl:DatatypeProperty ;
    rdfs:label "stream capacity (L)"@en ;
    rdfs:comment "Nominal capacity of this point for this stream. Needed to turn a fill-level percentage into anything actionable: 80% of a 25 L office bin and 80% of a 1100 L euro-bin are different problems."@en ;
    rdfs:domain ontosage:WastePoint ;
    rdfs:range xsd:decimal .
```
{% endraw %}
