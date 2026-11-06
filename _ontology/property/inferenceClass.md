---
title: "ontosage:inferenceClass"
layout: post
permalink: /ontology/property/inferenceClass/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › inferenceClass

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#inferenceClass` |
| Label | inference class rule |
| Kind | datatype property |
| Domain | [`ontosage:AccessPolicy`]({{ '/ontology/class/AccessPolicy/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Question-shape rules, e.g. individual\_presence:deny — the system explains the building, never tracks individuals.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:inferenceClass a owl:DatatypeProperty ;
    rdfs:label "inference class rule"@en ;
    rdfs:comment "Question-shape rules, e.g. individual_presence:deny — the system explains the building, never tracks individuals."@en ;
    rdfs:domain ontosage:AccessPolicy ;
    rdfs:range xsd:string .
```
{% endraw %}
