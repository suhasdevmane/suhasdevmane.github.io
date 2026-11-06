---
title: "ontosage:reportPriority"
layout: post
permalink: /ontology/property/reportPriority/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › reportPriority

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#reportPriority` |
| Label | report priority |
| Kind | datatype property |
| Domain | [`ontosage:Report`]({{ '/ontology/class/Report/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Triage priority. Values: LOW, MEDIUM, HIGH, URGENT (mirrors ontosage:priority on the related maintenance issue).

## Examples

- "URGENT"

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:reportPriority a owl:DatatypeProperty ;
    rdfs:label "report priority"@en ;
    rdfs:comment "Triage priority. Values: LOW, MEDIUM, HIGH, URGENT (mirrors ontosage:priority on the related maintenance issue)."@en ;
    rdfs:domain ontosage:Report ;
    rdfs:range xsd:string ;
    skos:example "\"URGENT\"" .
```
{% endraw %}
