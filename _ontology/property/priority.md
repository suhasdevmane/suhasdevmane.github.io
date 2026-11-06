---
title: "ontosage:priority"
layout: post
permalink: /ontology/property/priority/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › priority

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#priority` |
| Label | default priority |
| Kind | datatype property |
| Domain | [`ontosage:MaintenanceIssue`]({{ '/ontology/class/MaintenanceIssue/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Suggested default priority for a maintenance issue. Values: LOW, MEDIUM, HIGH, URGENT.

## Examples

- "URGENT" (e.g. a water leak or anyone trapped in a lift)

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`work_order`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#work_order) | `priority` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:priority a owl:DatatypeProperty ;
    rdfs:label "default priority"@en ;
    rdfs:comment "Suggested default priority for a maintenance issue. Values: LOW, MEDIUM, HIGH, URGENT."@en ;
    rdfs:domain ontosage:MaintenanceIssue ;
    rdfs:range xsd:string ;
    skos:example "\"URGENT\"  (e.g. a water leak or anyone trapped in a lift)" .
```
{% endraw %}
