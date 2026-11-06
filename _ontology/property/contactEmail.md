---
title: "ontosage:contactEmail"
layout: post
permalink: /ontology/property/contactEmail/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › contactEmail

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#contactEmail` |
| Label | contact email |
| Kind | datatype property |
| Domain | [`ontosage:KnowledgeTopic`]({{ '/ontology/class/KnowledgeTopic/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The email to contact about this topic.

## Examples

- "estates@example.ac.uk"

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`department`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#department) | `contact_email` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:contactEmail a owl:DatatypeProperty ;
    rdfs:label "contact email"@en ;
    rdfs:comment "The email to contact about this topic."@en ;
    rdfs:domain ontosage:KnowledgeTopic ;
    rdfs:range xsd:string ;
    skos:example "\"estates@example.ac.uk\"" .
```
{% endraw %}
