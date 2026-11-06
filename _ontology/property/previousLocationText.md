---
title: "ontosage:previousLocationText"
layout: post
permalink: /ontology/property/previousLocationText/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › previousLocationText

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#previousLocationText` |
| Label | previous location |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Where a record used to be. ABSENT means the register records no move — not that nothing changed, and an answer must say which.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`public_event`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#public_event) | `previous_venue` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:previousLocationText a owl:DatatypeProperty ;
    rdfs:label "previous location"@en ;
    rdfs:comment "Where a record used to be. ABSENT means the register records no move — not that nothing changed, and an answer must say which."@en ;
    rdfs:range xsd:string .
```
{% endraw %}
