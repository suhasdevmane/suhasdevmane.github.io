---
title: "ontosage:approvalRoute"
layout: post
permalink: /ontology/property/approvalRoute/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › approvalRoute

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#approvalRoute` |
| Label | approval route |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Who must approve a grant, so 'does this need a formal exception' is answerable from the register rather than from memory.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`access_permission`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#access_permission) | `approval_route` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:approvalRoute a owl:DatatypeProperty ;
    rdfs:label "approval route"@en ;
    rdfs:comment "Who must approve a grant, so 'does this need a formal exception' is answerable from the register rather than from memory."@en ;
    rdfs:range xsd:string .
```
{% endraw %}
