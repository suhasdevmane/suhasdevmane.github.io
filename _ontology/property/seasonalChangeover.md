---
title: "ontosage:seasonalChangeover"
layout: post
permalink: /ontology/property/seasonalChangeover/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › seasonalChangeover

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#seasonalChangeover` |
| Label | seasonal changeover |
| Kind | datatype property |
| Domain | [`ontosage:OperatingRegime`]({{ '/ontology/class/OperatingRegime/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The schema gives no definition for this term.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`operating_regime`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#operating_regime) | `seasonal_changeover` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:seasonalChangeover a owl:DatatypeProperty ;
    rdfs:label "seasonal changeover"@en ;
    rdfs:domain ontosage:OperatingRegime ;
    rdfs:range xsd:string .
```
{% endraw %}
