---
title: "ontosage:doorsOpenAt"
layout: post
permalink: /ontology/property/doorsOpenAt/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › doorsOpenAt

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#doorsOpenAt` |
| Label | doors open at |
| Kind | datatype property |
| Domain | [`ontosage:PublicEvent`]({{ '/ontology/class/PublicEvent/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

When a visitor may enter, which is earlier than the start and is the time they actually need.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`public_event`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#public_event) | `doors_open` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:doorsOpenAt a owl:DatatypeProperty ;
    rdfs:label "doors open at"@en ;
    rdfs:comment "When a visitor may enter, which is earlier than the start and is the time they actually need."@en ;
    rdfs:domain ontosage:PublicEvent ;
    rdfs:range xsd:string .
```
{% endraw %}
