---
title: "ontosage:recordVersion"
layout: post
permalink: /ontology/property/recordVersion/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › recordVersion

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#recordVersion` |
| Label | record version |
| Kind | datatype property |
| Domain | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The version or revision this fact was read from. Without it a superseded record and its replacement are indistinguishable in the evidence record, and an answer cannot be reproduced against what it actually used.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:recordVersion a owl:DatatypeProperty ;
    rdfs:label "record version"@en ;
    rdfs:comment "The version or revision this fact was read from. Without it a superseded record and its replacement are indistinguishable in the evidence record, and an answer cannot be reproduced against what it actually used."@en ;
    rdfs:domain ontosage:IntervalRecord ;
    rdfs:range xsd:string .
```
{% endraw %}
