---
title: "ontosage:BuildingDescription"
layout: post
permalink: /ontology/class/BuildingDescription/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › BuildingDescription

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#BuildingDescription` |
| Label | Building description |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The set of self-descriptive assertions carried by a brick:Building instance.

## Description

Marker for the descriptive, non-sensor facts a building states about itself. Not a container: the properties below attach directly to the brick:Building instance, so the building remains a single node and Brick's own predicates keep their meaning.

## Examples

- "how old is this building?" answered from brick:yearBuilt on the Building node.

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

ontosage:BuildingDescription a owl:Class ;
    rdfs:label "Building description"@en ;
    rdfs:comment "Marker for the descriptive, non-sensor facts a building states about itself. Not a container: the properties below attach directly to the brick:Building instance, so the building remains a single node and Brick's own predicates keep their meaning."@en ;
    skos:definition "The set of self-descriptive assertions carried by a brick:Building instance."@en ;
    skos:example "\"how old is this building?\" answered from brick:yearBuilt on the Building node." .
```
{% endraw %}
