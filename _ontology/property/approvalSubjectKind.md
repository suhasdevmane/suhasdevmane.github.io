---
title: "ontosage:approvalSubjectKind"
layout: post
permalink: /ontology/property/approvalSubjectKind/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › approvalSubjectKind

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#approvalSubjectKind` |
| Label | approval subject kind |
| Kind | datatype property |
| Domain | [`ontosage:ApprovalRecord`]({{ '/ontology/class/ApprovalRecord/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

What sort of thing is approved -- a route, a space use, a procedure, a permission group, a policy, a system, an asset, a cost line.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`approval_evidence`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#approval_evidence) | `subject_kind` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:approvalSubjectKind a owl:DatatypeProperty ;
    rdfs:label "approval subject kind"@en ;
    rdfs:comment "What sort of thing is approved -- a route, a space use, a procedure, a permission group, a policy, a system, an asset, a cost line."@en ;
    rdfs:domain ontosage:ApprovalRecord ;
    rdfs:range xsd:string .
```
{% endraw %}
