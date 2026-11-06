---
title: "ontosage:derivedFromDocument"
layout: post
permalink: /ontology/property/derivedFromDocument/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › derivedFromDocument

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#derivedFromDocument` |
| Label | derived from document |
| Kind | datatype property |
| Domain | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Set on every fact LIFTED from a record document. A document is a statement ABOUT a system of record, not the record itself, so these rank below authored TTL in precedence — without the marker a stale Markdown table could silently outrank a live register.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:derivedFromDocument a owl:DatatypeProperty ;
    rdfs:label "derived from document"@en ;
    rdfs:comment "Set on every fact LIFTED from a record document. A document is a statement ABOUT a system of record, not the record itself, so these rank below authored TTL in precedence — without the marker a stale Markdown table could silently outrank a live register."@en ;
    rdfs:domain ontosage:IntervalRecord ;
    rdfs:range xsd:string .
```
{% endraw %}
