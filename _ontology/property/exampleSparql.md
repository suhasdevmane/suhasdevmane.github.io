---
title: "ontosage:exampleSparql"
layout: post
permalink: /ontology/property/exampleSparql/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › exampleSparql

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#exampleSparql` |
| Label | example SPARQL |
| Kind | annotation property |
| Domain | not declared (any subject) |
| Range | not declared |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A worked SPARQL query answering a competency question for the annotated term, over a combined Brick + OCBV graph (prefixes bldg:, brick:, ontosage:, hbco:).

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

ontosage:exampleSparql a owl:AnnotationProperty ;
    rdfs:label "example SPARQL"@en ;
    rdfs:comment "A worked SPARQL query answering a competency question for the annotated term, over a combined Brick + OCBV graph (prefixes bldg:, brick:, ontosage:, hbco:)."@en .
```
{% endraw %}
