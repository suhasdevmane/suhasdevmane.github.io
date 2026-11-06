---
title: "ontosage:Database"
layout: post
permalink: /ontology/class/Database/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › Database

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Database` |
| Label | Database |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A registered time-series backend holding sensor readings; the object of ref:storedAt, resolved to a connection through database\_registry.yaml.

## Examples

- "bldg:database2" — the MySQL instance behind this building's narrow tables

## Class hierarchy

Superclasses: none (a root class).

Subclasses: none.

## Properties

No property declares this class (or a superclass) as its domain.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:Database a owl:Class ;
    rdfs:label "Database"@en ;
    rdfs:comment "A registered time-series backend holding sensor readings; the object of ref:storedAt, resolved to a connection through database_registry.yaml."@en ;
    skos:example "\"bldg:database2\" — the MySQL instance behind this building's narrow tables" .
```
{% endraw %}
