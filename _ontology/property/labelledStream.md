---
title: "ontosage:labelledStream"
layout: post
permalink: /ontology/property/labelledStream/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › labelledStream

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#labelledStream` |
| Label | labelled waste stream |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

What is printed on the bin. Separate from the recorded stream so the two can be compared rather than assumed equal.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`waste_collection`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#waste_collection) | `stream_label` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:labelledStream a owl:DatatypeProperty ;
    rdfs:label "labelled waste stream"@en ;
    rdfs:comment "What is printed on the bin. Separate from the recorded stream so the two can be compared rather than assumed equal."@en ;
    rdfs:range xsd:string .
```
{% endraw %}
