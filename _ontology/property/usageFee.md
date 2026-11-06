---
title: "ontosage:usageFee"
layout: post
permalink: /ontology/property/usageFee/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › usageFee

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#usageFee` |
| Label | usage fee |
| Kind | datatype property |
| Domain | [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

What it costs to use an amenity, in the building's own words: 'free', 'GBP 2.50 per day'. ABSENT MEANS NOT RECORDED, which is a different fact from free -- an answer must never turn an empty field into 'it is free'.

## Examples

- "free for card holders; visitors GBP 3 per day"

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:usageFee a owl:DatatypeProperty ;
    rdfs:label "usage fee"@en ;
    rdfs:comment "What it costs to use an amenity, in the building's own words: 'free', 'GBP 2.50 per day'. ABSENT MEANS NOT RECORDED, which is a different fact from free -- an answer must never turn an empty field into 'it is free'."@en ;
    rdfs:domain ontosage:Capability ;
    rdfs:range xsd:string ;
    skos:example "\"free for card holders; visitors GBP 3 per day\"" .
```
{% endraw %}
