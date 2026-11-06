---
title: "ontosage:archivalIntervalS"
layout: post
permalink: /ontology/property/archivalIntervalS/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › archivalIntervalS

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#archivalIntervalS` |
| Label | archival interval (s) |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:integer` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The permanent canonical resolution. Third of the three clocks, and the one a completeness gate needs: expected sample count over a window is derived from THIS, never assumed.

## Examples

- "60"^^xsd:integer

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:archivalIntervalS a owl:DatatypeProperty ;
    rdfs:label "archival interval (s)"@en ;
    rdfs:comment "The permanent canonical resolution. Third of the three clocks, and the one a completeness gate needs: expected sample count over a window is derived from THIS, never assumed."@en ;
    rdfs:range xsd:integer ;
    skos:example "\"60\"^^xsd:integer" .
```
{% endraw %}
