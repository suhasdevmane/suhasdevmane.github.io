---
title: "ontosage:serviceScope"
layout: post
permalink: /ontology/property/serviceScope/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › serviceScope

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#serviceScope` |
| Label | service scope |
| Kind | datatype property |
| Domain | [`ontosage:Department`]({{ '/ontology/class/Department/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The assets, spaces or activities this department is accountable for. The field a 'who owns this?' question is answered from.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`department`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#department) | `scope` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:serviceScope a owl:DatatypeProperty ;
    rdfs:label "service scope"@en ;
    rdfs:comment "The assets, spaces or activities this department is accountable for. The field a 'who owns this?' question is answered from."@en ;
    rdfs:domain ontosage:Department ;
    rdfs:range xsd:string .
```
{% endraw %}
