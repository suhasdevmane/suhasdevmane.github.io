---
title: "ontosage:ServedZone"
layout: post
permalink: /ontology/class/ServedZone/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › ServedZone

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#ServedZone` |
| Label | Served zone |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A set of spaces whose conditions are genuinely represented by a shared point — typically because one air-handling unit, one thermal zone or one distributed sensor array serves them all. Membership is a claim about the MECHANICAL design, not about geometry, and it must be validated before any answer may rest on it.

## Class hierarchy

Superclasses:

- [`brick:Location`](https://ontology.brickschema.org/1.4/#brick:Location) › **`ontosage:ServedZone`**

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:servedByPoint`]({{ '/ontology/property/servedByPoint/' | relative_url }}) | object | [`brick:Point`](https://ontology.brickschema.org/1.4/#brick:Point) | this class |
| [`ontosage:servesSpace`]({{ '/ontology/property/servesSpace/' | relative_url }}) | object | [`brick:Location`](https://ontology.brickschema.org/1.4/#brick:Location) | this class |
| [`ontosage:zoneValidated`]({{ '/ontology/property/zoneValidated/' | relative_url }}) | datatype | `xsd:boolean` | this class |
| [`ontosage:zoneValidatedOn`]({{ '/ontology/property/zoneValidatedOn/' | relative_url }}) | datatype | `xsd:date` | this class |
| [`ontosage:zoneValidationMethod`]({{ '/ontology/property/zoneValidationMethod/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:zoneId`]({{ '/ontology/property/zoneId/' | relative_url }}) | datatype | `xsd:string` | [`brick:Location`](https://ontology.brickschema.org/1.4/#brick:Location) |

## Turtle

{% raw %}
```turtle
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ontosage:ServedZone a owl:Class ;
    rdfs:label "Served zone"@en ;
    rdfs:comment "A set of spaces whose conditions are genuinely represented by a shared point — typically because one air-handling unit, one thermal zone or one distributed sensor array serves them all. Membership is a claim about the MECHANICAL design, not about geometry, and it must be validated before any answer may rest on it."@en ;
    rdfs:subClassOf brick:Location .
```
{% endraw %}
