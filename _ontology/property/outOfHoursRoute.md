---
title: "ontosage:outOfHoursRoute"
layout: post
permalink: /ontology/property/outOfHoursRoute/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › outOfHoursRoute

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#outOfHoursRoute` |
| Label | out of hours route |
| Kind | datatype property |
| Domain | [`ontosage:Department`]({{ '/ontology/class/Department/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Who answers outside coverage hours. Separate from requestChannel because they routinely differ, and an occupant told the daytime queue at 22:00 is told the wrong thing.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`department`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#department) | `out_of_hours` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:outOfHoursRoute a owl:DatatypeProperty ;
    rdfs:label "out of hours route"@en ;
    rdfs:comment "Who answers outside coverage hours. Separate from requestChannel because they routinely differ, and an occupant told the daytime queue at 22:00 is told the wrong thing."@en ;
    rdfs:domain ontosage:Department ;
    rdfs:range xsd:string .
```
{% endraw %}
