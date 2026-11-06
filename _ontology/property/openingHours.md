---
title: "ontosage:openingHours"
layout: post
permalink: /ontology/property/openingHours/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › openingHours

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#openingHours` |
| Label | opening hours |
| Kind | datatype property |
| Domain | [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Free-text opening hours for an amenity or service.

## Examples

- "Mon-Fri 09:00-16:30; closed weekends"

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`department`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#department) | `coverage_hours` | `xsd:string` |
| [`workspace_profile`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#workspace_profile) | `hours` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:openingHours a owl:DatatypeProperty ;
    rdfs:label "opening hours"@en ;
    rdfs:comment "Free-text opening hours for an amenity or service."@en ;
    rdfs:domain ontosage:Capability ;
    rdfs:range xsd:string ;
    skos:example "\"Mon-Fri 09:00-16:30; closed weekends\"" .
```
{% endraw %}
