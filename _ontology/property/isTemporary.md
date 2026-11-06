---
title: "ontosage:isTemporary"
layout: post
permalink: /ontology/property/isTemporary/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › isTemporary

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#isTemporary` |
| Label | is temporary |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:boolean` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Event assets come and go. Without this the register answers the wrong question after every event.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`waste_collection`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#waste_collection) | `temporary` | `xsd:boolean` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:isTemporary a owl:DatatypeProperty ;
    rdfs:label "is temporary"@en ;
    rdfs:comment "Event assets come and go. Without this the register answers the wrong question after every event."@en ;
    rdfs:range xsd:boolean .
```
{% endraw %}
