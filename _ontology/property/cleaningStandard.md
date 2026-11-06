---
title: "ontosage:cleaningStandard"
layout: post
permalink: /ontology/property/cleaningStandard/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › cleaningStandard

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#cleaningStandard` |
| Label | cleaning standard |
| Kind | datatype property |
| Domain | [`ontosage:CleaningTask`]({{ '/ontology/class/CleaningTask/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The specification applied on a visit — enhanced, standard, presentation or light. Distinct from frequency: a room may be cleaned daily to a light standard.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`cleaning_task`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#cleaning_task) | `standard` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:cleaningStandard a owl:DatatypeProperty ;
    rdfs:label "cleaning standard"@en ;
    rdfs:comment "The specification applied on a visit — enhanced, standard, presentation or light. Distinct from frequency: a room may be cleaned daily to a light standard."@en ;
    rdfs:domain ontosage:CleaningTask ;
    rdfs:range xsd:string .
```
{% endraw %}
