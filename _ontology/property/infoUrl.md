---
title: "ontosage:infoUrl"
layout: post
permalink: /ontology/property/infoUrl/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › infoUrl

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#infoUrl` |
| Label | information URL |
| Kind | datatype property |
| Domain | [`ontosage:KnowledgeTopic`]({{ '/ontology/class/KnowledgeTopic/' | relative_url }}) |
| Range | `xsd:anyURI` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A URL where a stakeholder can find more information.

## Examples

- "https://itservicedesk.example.ac.uk"

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:infoUrl a owl:DatatypeProperty ;
    rdfs:label "information URL"@en ;
    rdfs:comment "A URL where a stakeholder can find more information."@en ;
    rdfs:domain ontosage:KnowledgeTopic ;
    rdfs:range xsd:anyURI ;
    skos:example "\"https://itservicedesk.example.ac.uk\"" .
```
{% endraw %}
