---
title: "ontosage:policyOwner"
layout: post
permalink: /ontology/property/policyOwner/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › policyOwner

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#policyOwner` |
| Label | policy owner |
| Kind | datatype property |
| Domain | [`ontosage:KnowledgeTopic`]({{ '/ontology/class/KnowledgeTopic/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The team accountable for this policy, so an answer can say who to take it up with rather than leaving the user to guess.

## Examples

- "IT Services"

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:policyOwner a owl:DatatypeProperty ;
    rdfs:label "policy owner"@en ;
    rdfs:comment "The team accountable for this policy, so an answer can say who to take it up with rather than leaving the user to guess."@en ;
    rdfs:domain ontosage:KnowledgeTopic ;
    rdfs:range xsd:string ;
    skos:example "\"IT Services\"" .
```
{% endraw %}
