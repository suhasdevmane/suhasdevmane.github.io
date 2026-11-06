---
title: "ontosage:requiredQualification"
layout: post
permalink: /ontology/property/requiredQualification/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › requiredQualification

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#requiredQualification` |
| Label | required qualification |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

What an officer must hold to work this point. Role-level, never a person.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`patrol_checkpoint`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#patrol_checkpoint) | `qualification` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:requiredQualification a owl:DatatypeProperty ;
    rdfs:label "required qualification"@en ;
    rdfs:comment "What an officer must hold to work this point. Role-level, never a person."@en ;
    rdfs:range xsd:string .
```
{% endraw %}
