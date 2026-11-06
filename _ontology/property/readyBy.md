---
title: "ontosage:readyBy"
layout: post
permalink: /ontology/property/readyBy/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › readyBy

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#readyBy` |
| Label | ready by |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The time an area must be released for use. A service commitment, so a task still open past it is an exception to report rather than a task running late.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`cleaning_task`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#cleaning_task) | `ready_by` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:readyBy a owl:DatatypeProperty ;
    rdfs:label "ready by"@en ;
    rdfs:comment "The time an area must be released for use. A service commitment, so a task still open past it is an exception to report rather than a task running late."@en ;
    rdfs:range xsd:string .
```
{% endraw %}
