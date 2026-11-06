---
title: "ontosage:evidenceDate"
layout: post
permalink: /ontology/property/evidenceDate/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › evidenceDate

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#evidenceDate` |
| Label | evidence date |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:date` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

When the evidence was produced -- distinct from when the approval was made, because evidence ages and approvals do not.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`approval_evidence`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#approval_evidence) | `evidence_date` | `xsd:date` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:evidenceDate a owl:DatatypeProperty ;
    rdfs:label "evidence date"@en ;
    rdfs:comment "When the evidence was produced -- distinct from when the approval was made, because evidence ages and approvals do not."@en ;
    rdfs:range xsd:date .
```
{% endraw %}
