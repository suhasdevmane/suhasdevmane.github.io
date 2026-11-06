---
title: "ontosage:unoccupiedSetpoint"
layout: post
permalink: /ontology/property/unoccupiedSetpoint/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › unoccupiedSetpoint

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#unoccupiedSetpoint` |
| Label | unoccupied setpoint |
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
| [`operating_regime`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#operating_regime) | `unoccupied_setpoint` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:unoccupiedSetpoint a owl:DatatypeProperty ;
    rdfs:label "unoccupied setpoint"@en ;
    rdfs:domain ontosage:OperatingRegime ;
    rdfs:range xsd:string .
```
{% endraw %}
