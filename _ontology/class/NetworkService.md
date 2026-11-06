---
title: "ontosage:NetworkService"
layout: post
permalink: /ontology/class/NetworkService/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › NetworkService

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#NetworkService` |
| Label | Network / IT service |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

An aggregate connectivity or IT service serving spaces — wired, wireless, or a named platform. Deliberately an aggregate: per-device or per-user network monitoring would be surveillance the privacy rules forbid.

## Class hierarchy

Superclasses:

- [`brick:System`](https://ontology.brickschema.org/1.4/#brick:System) › **`ontosage:NetworkService`**

Subclasses: none.

## Properties

No property declares this class (or a superclass) as its domain.

## Turtle

Development notes were removed from one or more text values below; the source file holds the full text.

{% raw %}
```turtle
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ontosage:NetworkService a owl:Class ;
    rdfs:label "Network / IT service"@en ;
    rdfs:comment "An aggregate connectivity or IT service serving spaces — wired, wireless, or a named platform. Deliberately an aggregate: per-device or per-user network monitoring would be surveillance the privacy rules forbid."@en ;
    rdfs:subClassOf brick:System .
```
{% endraw %}
