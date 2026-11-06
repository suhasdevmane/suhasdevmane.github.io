---
title: "ontosage:approvedByRole"
layout: post
permalink: /ontology/property/approvedByRole/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › approvedByRole

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#approvedByRole` |
| Label | approved by role |
| Kind | datatype property |
| Domain | [`ontosage:ApprovalRecord`]({{ '/ontology/class/ApprovalRecord/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The role that took the decision. Never a person.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`approval_evidence`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#approval_evidence) | `approved_by_role` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:approvedByRole a owl:DatatypeProperty ;
    rdfs:label "approved by role"@en ;
    rdfs:comment "The role that took the decision. Never a person."@en ;
    rdfs:domain ontosage:ApprovalRecord ;
    rdfs:range xsd:string .
```
{% endraw %}
