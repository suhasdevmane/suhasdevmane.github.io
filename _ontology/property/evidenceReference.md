---
title: "ontosage:evidenceReference"
layout: post
permalink: /ontology/property/evidenceReference/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › evidenceReference

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#evidenceReference` |
| Label | evidence reference |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The schema gives no definition for this term.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`approval_evidence`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#approval_evidence) | `evidence_ref` | `xsd:string` |
| [`av_readiness`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#av_readiness) | `evidence_ref` | `xsd:string` |
| [`continuity_provision`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#continuity_provision) | `evidence_ref` | `xsd:string` |
| [`coordination_function`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#coordination_function) | `evidence_ref` | `xsd:string` |
| [`door_hardware`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#door_hardware) | `evidence_ref` | `xsd:string` |
| [`fire_safety_asset`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#fire_safety_asset) | `evidence_ref` | `xsd:string` |
| [`hazard_control`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#hazard_control) | `evidence_ref` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:evidenceReference a owl:DatatypeProperty ;
    rdfs:label "evidence reference"@en ;
    rdfs:range xsd:string .
```
{% endraw %}
