---
title: "ontosage:activationCriterion"
layout: post
permalink: /ontology/property/activationCriterion/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › activationCriterion

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#activationCriterion` |
| Label | activation criterion |
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
| [`coordination_function`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#coordination_function) | `activation_criterion` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:activationCriterion a owl:DatatypeProperty ;
    rdfs:label "activation criterion"@en ;
    rdfs:range xsd:string .
```
{% endraw %}
