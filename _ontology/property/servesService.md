---
title: "ontosage:servesService"
layout: post
permalink: /ontology/property/servesService/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › servesService

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#servesService` |
| Label | service |
| Kind | datatype property |
| Domain | [`ontosage:ContinuityProvision`]({{ '/ontology/class/ContinuityProvision/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The service this row is about, in the words the people who run it use.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`continuity_provision`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#continuity_provision) | `service` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:servesService a owl:DatatypeProperty ;
    rdfs:label "service"@en ;
    rdfs:comment "The service this row is about, in the words the people who run it use."@en ;
    rdfs:domain ontosage:ContinuityProvision ;
    rdfs:range xsd:string .
```
{% endraw %}
