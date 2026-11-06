---
title: "ontosage:evidenceKind"
layout: post
permalink: /ontology/property/evidenceKind/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › evidenceKind

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#evidenceKind` |
| Label | evidence kind |
| Kind | datatype property |
| Domain | [`ontosage:ApprovalRecord`]({{ '/ontology/class/ApprovalRecord/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Certificate, survey, test record, inspection, sign-off, committee minute or drawing. ABSENT means no evidence is recorded, which is a finding rather than a blank.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`approval_evidence`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#approval_evidence) | `evidence_type` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:evidenceKind a owl:DatatypeProperty ;
    rdfs:label "evidence kind"@en ;
    rdfs:comment "Certificate, survey, test record, inspection, sign-off, committee minute or drawing. ABSENT means no evidence is recorded, which is a finding rather than a blank."@en ;
    rdfs:domain ontosage:ApprovalRecord ;
    rdfs:range xsd:string .
```
{% endraw %}
