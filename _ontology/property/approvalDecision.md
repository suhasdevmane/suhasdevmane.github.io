---
title: "ontosage:approvalDecision"
layout: post
permalink: /ontology/property/approvalDecision/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › approvalDecision

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#approvalDecision` |
| Label | approval decision |
| Kind | datatype property |
| Domain | [`ontosage:ApprovalRecord`]({{ '/ontology/class/ApprovalRecord/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Approved, conditional, refused, withdrawn or pending. Refused is RECORDED rather than omitted, so a refused option is never offered by silence.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`approval_evidence`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#approval_evidence) | `decision` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:approvalDecision a owl:DatatypeProperty ;
    rdfs:label "approval decision"@en ;
    rdfs:comment "Approved, conditional, refused, withdrawn or pending. Refused is RECORDED rather than omitted, so a refused option is never offered by silence."@en ;
    rdfs:domain ontosage:ApprovalRecord ;
    rdfs:range xsd:string .
```
{% endraw %}
