---
title: "ontosage:cleaningZone"
layout: post
permalink: /ontology/property/cleaningZone/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › cleaningZone

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#cleaningZone` |
| Label | cleaning zone |
| Kind | datatype property |
| Domain | [`ontosage:CleaningTask`]({{ '/ontology/class/CleaningTask/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The named division of the building a shift is responsible for.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`cleaning_task`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#cleaning_task) | `zone` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:cleaningZone a owl:DatatypeProperty ;
    rdfs:label "cleaning zone"@en ;
    rdfs:comment "The named division of the building a shift is responsible for."@en ;
    rdfs:domain ontosage:CleaningTask ;
    rdfs:range xsd:string .
```
{% endraw %}
