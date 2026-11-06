---
title: "ontosage:avComponentKind"
layout: post
permalink: /ontology/property/avComponentKind/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › avComponentKind

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#avComponentKind` |
| Label | AV component kind |
| Kind | datatype property |
| Domain | [`ontosage:AVReadiness`]({{ '/ontology/class/AVReadiness/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The schema gives no definition for this term.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`av_readiness`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#av_readiness) | `kind` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:avComponentKind a owl:DatatypeProperty ;
    rdfs:label "AV component kind"@en ;
    rdfs:domain ontosage:AVReadiness ;
    rdfs:range xsd:string .
```
{% endraw %}
