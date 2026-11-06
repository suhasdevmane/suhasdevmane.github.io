---
title: "ontosage:toFloor"
layout: post
permalink: /ontology/property/toFloor/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › toFloor

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#toFloor` |
| Label | to floor |
| Kind | datatype property |
| Domain | [`ontosage:CirculationTime`]({{ '/ontology/class/CirculationTime/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The schema gives no definition for this term.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`circulation_time`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#circulation_time) | `to_floor` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:toFloor a owl:DatatypeProperty ;
    rdfs:label "to floor"@en ;
    rdfs:domain ontosage:CirculationTime ;
    rdfs:range xsd:string .
```
{% endraw %}
