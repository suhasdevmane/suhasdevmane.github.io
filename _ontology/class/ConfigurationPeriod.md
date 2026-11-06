---
title: "ontosage:ConfigurationPeriod"
layout: post
permalink: /ontology/class/ConfigurationPeriod/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › ConfigurationPeriod

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#ConfigurationPeriod` |
| Label | Configuration period |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

An interval during which a point's location, calibration and configuration were stable. Readings are interpreted against the period covering their timestamp, so a window spanning a boundary can be flagged rather than silently averaged across a discontinuity.

## Class hierarchy

Superclasses: none (a root class).

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:configLocation`]({{ '/ontology/property/configLocation/' | relative_url }}) | object | [`brick:Location`](https://ontology.brickschema.org/1.4/#brick:Location) | this class |
| [`ontosage:configurationChange`]({{ '/ontology/property/configurationChange/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:configurationOf`]({{ '/ontology/property/configurationOf/' | relative_url }}) | object | [`brick:Point`](https://ontology.brickschema.org/1.4/#brick:Point) | this class |
| [`ontosage:effectiveFrom`]({{ '/ontology/property/effectiveFrom/' | relative_url }}) | datatype | `xsd:dateTime` | this class |
| [`ontosage:effectiveTo`]({{ '/ontology/property/effectiveTo/' | relative_url }}) | datatype | `xsd:dateTime` | this class |
| [`ontosage:periodLocation`]({{ '/ontology/property/periodLocation/' | relative_url }}) | object | [`brick:Location`](https://ontology.brickschema.org/1.4/#brick:Location) | this class |

## Used as the range of

| Property | Kind | Domain |
|---|---|---|
| [`ontosage:hasConfigurationPeriod`]({{ '/ontology/property/hasConfigurationPeriod/' | relative_url }}) | object | [`brick:Point`](https://ontology.brickschema.org/1.4/#brick:Point) |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ontosage:ConfigurationPeriod a owl:Class ;
    rdfs:label "Configuration period"@en ;
    rdfs:comment "An interval during which a point's location, calibration and configuration were stable. Readings are interpreted against the period covering their timestamp, so a window spanning a boundary can be flagged rather than silently averaged across a discontinuity."@en .
```
{% endraw %}
