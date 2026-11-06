---
title: "ontosage:utilityKind"
layout: post
permalink: /ontology/property/utilityKind/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › utilityKind

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#utilityKind` |
| Label | utility |
| Kind | datatype property |
| Domain | [`ontosage:Tariff`]({{ '/ontology/class/Tariff/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Electricity, gas, water, heat.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`tariff`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#tariff) | `utility` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:utilityKind a owl:DatatypeProperty ;
    rdfs:label "utility"@en ;
    rdfs:comment "Electricity, gas, water, heat."@en ;
    rdfs:domain ontosage:Tariff ;
    rdfs:range xsd:string .
```
{% endraw %}
