---
title: "ontosage:targetUnit"
layout: post
permalink: /ontology/property/targetUnit/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › targetUnit

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#targetUnit` |
| Label | target unit |
| Kind | datatype property |
| Domain | [`ontosage:SustainabilityTarget`]({{ '/ontology/class/SustainabilityTarget/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Unit of the target value. Required: a diversion target of 65 means nothing without knowing whether that is a percentage or a tonnage.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`sustainability_target`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#sustainability_target) | `unit` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:targetUnit a owl:DatatypeProperty ;
    rdfs:label "target unit"@en ;
    rdfs:comment "Unit of the target value. Required: a diversion target of 65 means nothing without knowing whether that is a percentage or a tonnage."@en ;
    rdfs:domain ontosage:SustainabilityTarget ;
    rdfs:range xsd:string .
```
{% endraw %}
