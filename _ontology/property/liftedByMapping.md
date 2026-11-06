---
title: "ontosage:liftedByMapping"
layout: post
permalink: /ontology/property/liftedByMapping/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › liftedByMapping

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#liftedByMapping` |
| Label | lifted by mapping |
| Kind | datatype property |
| Domain | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The record-document mapping that produced this fact, so a wrong value can be traced to the rule that made it rather than only to the document.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:liftedByMapping a owl:DatatypeProperty ;
    rdfs:label "lifted by mapping"@en ;
    rdfs:comment "The record-document mapping that produced this fact, so a wrong value can be traced to the rule that made it rather than only to the document."@en ;
    rdfs:domain ontosage:IntervalRecord ;
    rdfs:range xsd:string .
```
{% endraw %}
