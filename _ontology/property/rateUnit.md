---
title: "ontosage:rateUnit"
layout: post
permalink: /ontology/property/rateUnit/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › rateUnit

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#rateUnit` |
| Label | rate unit |
| Kind | datatype property |
| Domain | [`ontosage:Tariff`]({{ '/ontology/class/Tariff/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The unit the unit rate is charged per (kWh, m3). Transcribed from the tariff's own document, never assumed from the utility.

## Examples

- `bldg:tariff/TAR-WATER-2026 ontosage:rateUnit "m3" .`

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:rateUnit a owl:DatatypeProperty ;
    rdfs:label "rate unit"@en ;
    rdfs:comment "The unit the unit rate is charged per (kWh, m3). Transcribed from the tariff's own document, never assumed from the utility."@en ;
    rdfs:domain ontosage:Tariff ;
    rdfs:range xsd:string ;
    skos:example "bldg:tariff/TAR-WATER-2026 ontosage:rateUnit \"m3\" ." .
```
{% endraw %}
