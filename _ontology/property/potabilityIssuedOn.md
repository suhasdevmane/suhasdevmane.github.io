---
title: "ontosage:potabilityIssuedOn"
layout: post
permalink: /ontology/property/potabilityIssuedOn/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › potabilityIssuedOn

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#potabilityIssuedOn` |
| Label | issued on |
| Kind | datatype property |
| Domain | [`ontosage:PotabilityStatement`]({{ '/ontology/class/PotabilityStatement/' | relative_url }}) |
| Range | `xsd:date` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

When the statement was published. A potability statement from four years ago describes a plumbing system that may since have been altered.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:potabilityIssuedOn a owl:DatatypeProperty ;
    rdfs:label "issued on"@en ;
    rdfs:comment "When the statement was published. A potability statement from four years ago describes a plumbing system that may since have been altered."@en ;
    rdfs:domain ontosage:PotabilityStatement ;
    rdfs:range xsd:date .
```
{% endraw %}
