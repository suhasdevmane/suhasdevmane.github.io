---
title: "ontosage:AccessPolicy"
layout: post
permalink: /ontology/class/AccessPolicy/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › AccessPolicy

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#AccessPolicy` |
| Label | Access policy |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A query-parameter access policy: who may see what, at which aggregation floor, resolution tier and rate. Consumed ONLY by the deterministic Policy Decision Point; cited in the evidence dossier of every answer it shapes.

## Examples

- "what am I allowed to ask?" -&gt; the AccessPolicy set for the session role.

## Class hierarchy

Superclasses: none (a root class).

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:appliesToRole`]({{ '/ontology/property/appliesToRole/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:inferenceClass`]({{ '/ontology/property/inferenceClass/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:minAggregationSensors`]({{ '/ontology/property/minAggregationSensors/' | relative_url }}) | datatype | `xsd:integer` | this class |
| [`ontosage:minAggregationSpaces`]({{ '/ontology/property/minAggregationSpaces/' | relative_url }}) | datatype | `xsd:integer` | this class |
| [`ontosage:rateLimit`]({{ '/ontology/property/rateLimit/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:resolutionTier`]({{ '/ontology/property/resolutionTier/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:scopeSpaces`]({{ '/ontology/property/scopeSpaces/' | relative_url }}) | datatype | `xsd:string` | this class |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:AccessPolicy a owl:Class ;
    rdfs:label "Access policy"@en ;
    rdfs:comment "A query-parameter access policy: who may see what, at which aggregation floor, resolution tier and rate. Consumed ONLY by the deterministic Policy Decision Point; cited in the evidence dossier of every answer it shapes."@en ;
    skos:example "\"what am I allowed to ask?\" -> the AccessPolicy set for the session role." .
```
{% endraw %}
