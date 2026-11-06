---
title: "ontosage:approvalReference"
layout: post
permalink: /ontology/property/approvalReference/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › approvalReference

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#approvalReference` |
| Label | approval reference |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The decision's own identifier, so an answer can be traced back to the record that made it.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`approval_evidence`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#approval_evidence) | `reference` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:approvalReference a owl:DatatypeProperty ;
    rdfs:label "approval reference"@en ;
    rdfs:comment "The decision's own identifier, so an answer can be traced back to the record that made it."@en ;
    rdfs:range xsd:string .
```
{% endraw %}
