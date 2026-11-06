---
title: "ontosage:patrolCircuit"
layout: post
permalink: /ontology/property/patrolCircuit/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › patrolCircuit

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#patrolCircuit` |
| Label | patrol circuit |
| Kind | datatype property |
| Domain | [`ontosage:PatrolCheckpoint`]({{ '/ontology/class/PatrolCheckpoint/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The schema gives no definition for this term.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`patrol_checkpoint`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#patrol_checkpoint) | `circuit` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:patrolCircuit a owl:DatatypeProperty ;
    rdfs:label "patrol circuit"@en ;
    rdfs:domain ontosage:PatrolCheckpoint ;
    rdfs:range xsd:string .
```
{% endraw %}
