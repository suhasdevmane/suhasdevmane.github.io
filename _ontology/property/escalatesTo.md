---
title: "ontosage:escalatesTo"
layout: post
permalink: /ontology/property/escalatesTo/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › escalatesTo

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#escalatesTo` |
| Label | escalates to |
| Kind | datatype property |
| Domain | [`ontosage:Department`]({{ '/ontology/class/Department/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The function a request escalates to when the response target is missed or the issue exceeds this department's scope.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`department`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#department) | `escalates_to` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:escalatesTo a owl:DatatypeProperty ;
    rdfs:label "escalates to"@en ;
    rdfs:comment "The function a request escalates to when the response target is missed or the issue exceeds this department's scope."@en ;
    rdfs:domain ontosage:Department ;
    rdfs:range xsd:string .
```
{% endraw %}
