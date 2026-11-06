---
title: "ontosage:circuitSequence"
layout: post
permalink: /ontology/property/circuitSequence/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › circuitSequence

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#circuitSequence` |
| Label | circuit sequence |
| Kind | datatype property |
| Domain | [`ontosage:PatrolCheckpoint`]({{ '/ontology/class/PatrolCheckpoint/' | relative_url }}) |
| Range | `xsd:integer` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Position within the circuit, so a route can be reported in the order it is walked.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`event_activity`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#event_activity) | `sequence` | `xsd:integer` |
| [`patrol_checkpoint`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#patrol_checkpoint) | `sequence` | `xsd:integer` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:circuitSequence a owl:DatatypeProperty ;
    rdfs:label "circuit sequence"@en ;
    rdfs:comment "Position within the circuit, so a route can be reported in the order it is walked."@en ;
    rdfs:domain ontosage:PatrolCheckpoint ;
    rdfs:range xsd:integer .
```
{% endraw %}
