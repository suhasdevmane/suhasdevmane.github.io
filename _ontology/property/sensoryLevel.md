---
title: "ontosage:sensoryLevel"
layout: post
permalink: /ontology/property/sensoryLevel/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › sensoryLevel

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#sensoryLevel` |
| Label | sensory level |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

How busy and stimulating the route is, so a lower-stimulation arrival can be offered.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`accessible_route`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#accessible_route) | `sensory` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:sensoryLevel a owl:DatatypeProperty ;
    rdfs:label "sensory level"@en ;
    rdfs:comment "How busy and stimulating the route is, so a lower-stimulation arrival can be offered."@en ;
    rdfs:range xsd:string .
```
{% endraw %}
