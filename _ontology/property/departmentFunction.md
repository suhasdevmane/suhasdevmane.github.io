---
title: "ontosage:departmentFunction"
layout: post
permalink: /ontology/property/departmentFunction/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › departmentFunction

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#departmentFunction` |
| Label | department function |
| Kind | datatype property |
| Domain | [`ontosage:Department`]({{ '/ontology/class/Department/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

What this department exists to do, in one line.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`department`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#department) | `function` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:departmentFunction a owl:DatatypeProperty ;
    rdfs:label "department function"@en ;
    rdfs:comment "What this department exists to do, in one line."@en ;
    rdfs:domain ontosage:Department ;
    rdfs:range xsd:string .
```
{% endraw %}
