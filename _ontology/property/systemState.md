---
title: "ontosage:systemState"
layout: post
permalink: /ontology/property/systemState/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › systemState

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#systemState` |
| Label | system state |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Ready, degraded or unavailable. Degraded is recorded rather than rounded to either neighbour, because it changes which fallback applies.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`coordination_function`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#coordination_function) | `system_state` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:systemState a owl:DatatypeProperty ;
    rdfs:label "system state"@en ;
    rdfs:comment "Ready, degraded or unavailable. Degraded is recorded rather than rounded to either neighbour, because it changes which fallback applies."@en ;
    rdfs:range xsd:string .
```
{% endraw %}
