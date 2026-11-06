---
title: "ontosage:Measurand"
layout: post
permalink: /ontology/class/Measurand/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › Measurand

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Measurand` |
| Label | Measurand |
| Defined in | [`ontology/measurand_kinds.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/measurand_kinds.ttl) |

## Definition

A quantity a sensor can measure, at the granularity that distinguishes one gas from another. QUDT stops at VolumeFraction, which cannot tell CO from NO2 - so these are declared here rather than borrowed.

## Class hierarchy

Superclasses: none (a root class).

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:physicalMax`]({{ '/ontology/property/physicalMax/' | relative_url }}) | datatype | not declared | this class |
| [`ontosage:physicalMin`]({{ '/ontology/property/physicalMin/' | relative_url }}) | datatype | not declared | this class |
| [`ontosage:physicalUnit`]({{ '/ontology/property/physicalUnit/' | relative_url }}) | datatype | not declared | this class |
| [`ontosage:typicalDecimals`]({{ '/ontology/property/typicalDecimals/' | relative_url }}) | datatype | not declared | this class |
| [`ontosage:typicalMax`]({{ '/ontology/property/typicalMax/' | relative_url }}) | datatype | not declared | this class |
| [`ontosage:typicalMin`]({{ '/ontology/property/typicalMin/' | relative_url }}) | datatype | not declared | this class |

## Members

The schema declares 30 measurands: see [Measurands]({{ '/ontology/vocabulary/measurands/' | relative_url }}).

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ontosage:Measurand a owl:Class ;
    rdfs:label "Measurand"@en ;
    rdfs:comment "A quantity a sensor can measure, at the granularity that distinguishes one gas from another. QUDT stops at VolumeFraction, which cannot tell CO from NO2 - so these are declared here rather than borrowed."@en .
```
{% endraw %}
