---
title: "ontosage:responsibleRole"
layout: post
permalink: /ontology/property/responsibleRole/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › responsibleRole

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#responsibleRole` |
| Label | responsible role |
| Kind | datatype property |
| Domain | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A ROLE name, never a person identifier (privacy by design).

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`contract`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#contract) | `owner_role` | `xsd:string` |
| [`risk_assessment`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#risk_assessment) | `assessor_role` | `xsd:string` |
| [`work_order`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#work_order) | `trade` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:responsibleRole a owl:DatatypeProperty ;
    rdfs:label "responsible role"@en ;
    rdfs:comment "A ROLE name, never a person identifier (privacy by design)."@en ;
    rdfs:domain ontosage:IntervalRecord ;
    rdfs:range xsd:string .
```
{% endraw %}
