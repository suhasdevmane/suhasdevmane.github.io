---
title: "ontosage:statusSource"
layout: post
permalink: /ontology/property/statusSource/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › statusSource

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#statusSource` |
| Label | issuing source |
| Kind | datatype property |
| Domain | [`ontosage:AssetStatus`]({{ '/ontology/class/AssetStatus/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The authoritative system or role that reported this state. Recorded because OntoSage requires source authority on every consequential answer, and because a status with no traceable issuer cannot be relied on for a safety-adjacent decision.

## Examples

- "lift\_controller" | "estates\_helpdesk" | "av\_support"

## Turtle

Development notes were removed from one or more text values below; the source file holds the full text.

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:statusSource a owl:DatatypeProperty ;
    rdfs:label "issuing source"@en ;
    rdfs:comment "The authoritative system or role that reported this state. Recorded because OntoSage requires source authority on every consequential answer, and because a status with no traceable issuer cannot be relied on for a safety-adjacent decision."@en ;
    rdfs:domain ontosage:AssetStatus ;
    rdfs:range xsd:string ;
    skos:example "\"lift_controller\" | \"estates_helpdesk\" | \"av_support\"" .
```
{% endraw %}
