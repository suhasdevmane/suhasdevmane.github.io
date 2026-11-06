---
title: "ontosage:provisionState"
layout: post
permalink: /ontology/property/provisionState/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › provisionState

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#provisionState` |
| Label | provision state |
| Kind | datatype property |
| Domain | [`ontosage:EvacuationProvision`]({{ '/ontology/class/EvacuationProvision/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The schema gives no definition for this term.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`evacuation_provision`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#evacuation_provision) | `state` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:provisionState a owl:DatatypeProperty ;
    rdfs:label "provision state"@en ;
    rdfs:domain ontosage:EvacuationProvision ;
    rdfs:range xsd:string .
```
{% endraw %}
