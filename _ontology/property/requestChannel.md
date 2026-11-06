---
title: "ontosage:requestChannel"
layout: post
permalink: /ontology/property/requestChannel/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › requestChannel

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#requestChannel` |
| Label | request channel |
| Kind | datatype property |
| Domain | [`ontosage:Department`]({{ '/ontology/class/Department/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

How a request reaches this department — helpdesk queue, phone, form or duty line.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`department`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#department) | `request_channel` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:requestChannel a owl:DatatypeProperty ;
    rdfs:label "request channel"@en ;
    rdfs:comment "How a request reaches this department — helpdesk queue, phone, form or duty line."@en ;
    rdfs:domain ontosage:Department ;
    rdfs:range xsd:string .
```
{% endraw %}
