---
title: "ontosage:accountableRole"
layout: post
permalink: /ontology/property/accountableRole/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › accountableRole

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#accountableRole` |
| Label | accountable role |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Who answers for the subject now. A role, so 'who is accountable' is answerable without exposing who holds what.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`approval_evidence`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#approval_evidence) | `accountable_role` | `xsd:string` |
| [`coordination_function`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#coordination_function) | `accountable_role` | `xsd:string` |
| [`department`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#department) | `accountable_role` | `xsd:string` |
| [`stock_item`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#stock_item) | `accountable_role` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:accountableRole a owl:DatatypeProperty ;
    rdfs:label "accountable role"@en ;
    rdfs:comment "Who answers for the subject now. A role, so 'who is accountable' is answerable without exposing who holds what."@en ;
    rdfs:range xsd:string .
```
{% endraw %}
