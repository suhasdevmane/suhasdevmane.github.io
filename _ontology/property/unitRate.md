---
title: "ontosage:unitRate"
layout: post
permalink: /ontology/property/unitRate/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › unitRate

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#unitRate` |
| Label | unit rate |
| Kind | datatype property |
| Domain | [`ontosage:Tariff`]({{ '/ontology/class/Tariff/' | relative_url }}) |
| Range | `xsd:decimal` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Cost per unit (per kWh, per cubic metre). Only ever read from a registered Tariff — never defaulted, never assumed.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`tariff`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#tariff) | `unit_rate` | `xsd:decimal` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:unitRate a owl:DatatypeProperty ;
    rdfs:label "unit rate"@en ;
    rdfs:comment "Cost per unit (per kWh, per cubic metre). Only ever read from a registered Tariff — never defaulted, never assumed."@en ;
    rdfs:domain ontosage:Tariff ;
    rdfs:range xsd:decimal .
```
{% endraw %}
