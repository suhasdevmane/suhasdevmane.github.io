---
title: "ontosage:rateLimit"
layout: post
permalink: /ontology/property/rateLimit/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › rateLimit

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#rateLimit` |
| Label | rate limit |
| Kind | datatype property |
| Domain | [`ontosage:AccessPolicy`]({{ '/ontology/class/AccessPolicy/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Serialized 'maxQueries:perMinutes'; 0 = unlimited.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:rateLimit a owl:DatatypeProperty ;
    rdfs:label "rate limit"@en ;
    rdfs:comment "Serialized 'maxQueries:perMinutes'; 0 = unlimited."@en ;
    rdfs:domain ontosage:AccessPolicy ;
    rdfs:range xsd:string .
```
{% endraw %}
