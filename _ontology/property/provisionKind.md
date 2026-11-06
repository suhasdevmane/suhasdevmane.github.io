---
title: "ontosage:provisionKind"
layout: post
permalink: /ontology/property/provisionKind/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › provisionKind

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#provisionKind` |
| Label | provision kind |
| Kind | datatype property |
| Domain | [`ontosage:EvacuationProvision`]({{ '/ontology/class/EvacuationProvision/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

refuge point, evacuation chair, communication unit, personal plan or assisted route.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`evacuation_provision`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#evacuation_provision) | `kind` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:provisionKind a owl:DatatypeProperty ;
    rdfs:label "provision kind"@en ;
    rdfs:comment "refuge point, evacuation chair, communication unit, personal plan or assisted route."@en ;
    rdfs:domain ontosage:EvacuationProvision ;
    rdfs:range xsd:string .
```
{% endraw %}
