---
title: "ontosage:approvedFillThreshold"
layout: post
permalink: /ontology/property/approvedFillThreshold/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › approvedFillThreshold

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#approvedFillThreshold` |
| Label | approved fill threshold |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:integer` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Per point, not a constant: a service decision about when this container needs emptying.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`waste_collection`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#waste_collection) | `fill_threshold` | `xsd:integer` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:approvedFillThreshold a owl:DatatypeProperty ;
    rdfs:label "approved fill threshold"@en ;
    rdfs:comment "Per point, not a constant: a service decision about when this container needs emptying."@en ;
    rdfs:range xsd:integer .
```
{% endraw %}
