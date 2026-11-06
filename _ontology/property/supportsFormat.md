---
title: "ontosage:supportsFormat"
layout: post
permalink: /ontology/property/supportsFormat/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › supportsFormat

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#supportsFormat` |
| Label | supports format |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Which teaching formats this component serves -- lecture, seminar, hybrid, practical.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`av_readiness`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#av_readiness) | `supports_format` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:supportsFormat a owl:DatatypeProperty ;
    rdfs:label "supports format"@en ;
    rdfs:comment "Which teaching formats this component serves -- lecture, seminar, hybrid, practical."@en ;
    rdfs:range xsd:string .
```
{% endraw %}
