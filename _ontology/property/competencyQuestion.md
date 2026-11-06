---
title: "ontosage:competencyQuestion"
layout: post
permalink: /ontology/property/competencyQuestion/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › competencyQuestion

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#competencyQuestion` |
| Label | competency question |
| Kind | annotation property |
| Domain | not declared (any subject) |
| Range | not declared |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A natural-language question the annotated term is designed to help answer. Used to document and evaluate schema coverage, and as a retrieval anchor for LLM query generation.

## Used in the schema

5 schema term(s) carry this property:

- [`hbco:Concept`]({{ '/ontology/class/Concept/' | relative_url }})
- [`ontosage:Amenity`]({{ '/ontology/class/Amenity/' | relative_url }})
- [`ontosage:MaintenanceIssue`]({{ '/ontology/class/MaintenanceIssue/' | relative_url }})
- [`ontosage:QuestionIntent`]({{ '/ontology/class/QuestionIntent/' | relative_url }})
- [`ontosage:StakeholderRole`]({{ '/ontology/class/StakeholderRole/' | relative_url }})

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ontosage:competencyQuestion a owl:AnnotationProperty ;
    rdfs:label "competency question"@en ;
    rdfs:comment "A natural-language question the annotated term is designed to help answer. Used to document and evaluate schema coverage, and as a retrieval anchor for LLM query generation."@en .
```
{% endraw %}
