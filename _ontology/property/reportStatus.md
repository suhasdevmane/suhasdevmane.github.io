---
title: "ontosage:reportStatus"
layout: post
permalink: /ontology/property/reportStatus/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › reportStatus

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#reportStatus` |
| Label | report status |
| Kind | datatype property |
| Domain | [`ontosage:Report`]({{ '/ontology/class/Report/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Triage state of a report. Values: NEW, ACKNOWLEDGED, IN\_PROGRESS, RESOLVED, CLOSED.

## Examples

- "NEW"

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:reportStatus a owl:DatatypeProperty ;
    rdfs:label "report status"@en ;
    rdfs:comment "Triage state of a report. Values: NEW, ACKNOWLEDGED, IN_PROGRESS, RESOLVED, CLOSED."@en ;
    rdfs:domain ontosage:Report ;
    rdfs:range xsd:string ;
    skos:example "\"NEW\"" .
```
{% endraw %}
