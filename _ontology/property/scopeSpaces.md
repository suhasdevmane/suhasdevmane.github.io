---
title: "ontosage:scopeSpaces"
layout: post
permalink: /ontology/property/scopeSpaces/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › scopeSpaces

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#scopeSpaces` |
| Label | space scope |
| Kind | datatype property |
| Domain | [`ontosage:AccessPolicy`]({{ '/ontology/class/AccessPolicy/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

own | public | any.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:scopeSpaces a owl:DatatypeProperty ;
    rdfs:label "space scope"@en ;
    rdfs:comment "own | public | any."@en ;
    rdfs:domain ontosage:AccessPolicy ;
    rdfs:range xsd:string .
```
{% endraw %}
