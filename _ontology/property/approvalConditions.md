---
title: "ontosage:approvalConditions"
layout: post
permalink: /ontology/property/approvalConditions/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › approvalConditions

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#approvalConditions` |
| Label | approval conditions |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

What a conditional approval depends on, in the register's own words. A condition nobody can read is not a condition.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`approval_evidence`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#approval_evidence) | `conditions` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:approvalConditions a owl:DatatypeProperty ;
    rdfs:label "approval conditions"@en ;
    rdfs:comment "What a conditional approval depends on, in the register's own words. A condition nobody can read is not a condition."@en ;
    rdfs:range xsd:string .
```
{% endraw %}
