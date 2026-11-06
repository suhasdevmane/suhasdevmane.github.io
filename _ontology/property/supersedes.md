---
title: "ontosage:supersedes"
layout: post
permalink: /ontology/property/supersedes/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › supersedes

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#supersedes` |
| Label | supersedes |
| Kind | object property |
| Domain | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| Range | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

This record replaces an earlier one. Both are retained: conflicting originals are preserved for the accountable owner rather than silently resolved.

## Turtle

Development notes were removed from one or more text values below; the source file holds the full text.

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ontosage:supersedes a owl:ObjectProperty ;
    rdfs:label "supersedes"@en ;
    rdfs:comment "This record replaces an earlier one. Both are retained: conflicting originals are preserved for the accountable owner rather than silently resolved."@en ;
    rdfs:domain ontosage:IntervalRecord ;
    rdfs:range ontosage:IntervalRecord .
```
{% endraw %}
