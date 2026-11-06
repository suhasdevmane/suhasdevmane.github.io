---
title: "ontosage:answerText"
layout: post
permalink: /ontology/property/answerText/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › answerText

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#answerText` |
| Label | canonical answer |
| Kind | datatype property |
| Domain | [`ontosage:KnowledgeTopic`]({{ '/ontology/class/KnowledgeTopic/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The one-line canonical answer for a KnowledgeTopic — what OntoSage says when a stakeholder asks about it.

## Examples

- "Complaints go to the Building Manager via the Facilities helpdesk."

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:answerText a owl:DatatypeProperty ;
    rdfs:label "canonical answer"@en ;
    rdfs:comment "The one-line canonical answer for a KnowledgeTopic — what OntoSage says when a stakeholder asks about it."@en ;
    rdfs:domain ontosage:KnowledgeTopic ;
    rdfs:range xsd:string ;
    skos:example "\"Complaints go to the Building Manager via the Facilities helpdesk.\"" .
```
{% endraw %}
