---
title: "ontosage:resolutionTier"
layout: post
permalink: /ontology/property/resolutionTier/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › resolutionTier

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#resolutionTier` |
| Label | resolution tier |
| Kind | datatype property |
| Domain | [`ontosage:AccessPolicy`]({{ '/ontology/class/AccessPolicy/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Serialized 'recencyMinutes:maxResolutionSeconds' pairs; finer data for recent windows, coarser for history.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:resolutionTier a owl:DatatypeProperty ;
    rdfs:label "resolution tier"@en ;
    rdfs:comment "Serialized 'recencyMinutes:maxResolutionSeconds' pairs; finer data for recent windows, coarser for history."@en ;
    rdfs:domain ontosage:AccessPolicy ;
    rdfs:range xsd:string .
```
{% endraw %}
