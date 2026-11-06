---
title: "ontosage:standingCharge"
layout: post
permalink: /ontology/property/standingCharge/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › standingCharge

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#standingCharge` |
| Label | standing charge |
| Kind | datatype property |
| Domain | [`ontosage:Tariff`]({{ '/ontology/class/Tariff/' | relative_url }}) |
| Range | `xsd:decimal` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Fixed daily charge, independent of consumption.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`tariff`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#tariff) | `standing_charge` | `xsd:decimal` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:standingCharge a owl:DatatypeProperty ;
    rdfs:label "standing charge"@en ;
    rdfs:comment "Fixed daily charge, independent of consumption."@en ;
    rdfs:domain ontosage:Tariff ;
    rdfs:range xsd:decimal .
```
{% endraw %}
