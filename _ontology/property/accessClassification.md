---
title: "ontosage:accessClassification"
layout: post
permalink: /ontology/property/accessClassification/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › accessClassification

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#accessClassification` |
| Label | access tier |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Which of the six access tiers may see this point: public | occupant | operational | safety\_security | research | strategic. The conversational layer must enforce the same permissions as the underlying systems and must never become a route around them.

## Examples

- "operational"

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`workspace_profile`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#workspace_profile) | `access` | `xsd:string` |

## Turtle

Development notes were removed from one or more text values below; the source file holds the full text.

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:accessClassification a owl:DatatypeProperty ;
    rdfs:label "access tier"@en ;
    rdfs:comment "Which of the six access tiers may see this point: public | occupant | operational | safety_security | research | strategic. The conversational layer must enforce the same permissions as the underlying systems and must never become a route around them."@en ;
    rdfs:range xsd:string ;
    skos:example "\"operational\"" .
```
{% endraw %}
