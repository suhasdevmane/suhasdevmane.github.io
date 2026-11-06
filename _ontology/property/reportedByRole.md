---
title: "ontosage:reportedByRole"
layout: post
permalink: /ontology/property/reportedByRole/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › reportedByRole

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#reportedByRole` |
| Label | reported by role |
| Kind | object property |
| Domain | [`ontosage:Report`]({{ '/ontology/class/Report/' | relative_url }}) |
| Range | [`ontosage:StakeholderRole`]({{ '/ontology/class/StakeholderRole/' | relative_url }}) |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The stakeholder role that filed the report (Module C). Advisory context, not identity.

## Examples

- `bldg:Report_042 ontosage:reportedByRole ontosage:Role_Occupant .`

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:reportedByRole a owl:ObjectProperty ;
    rdfs:label "reported by role"@en ;
    rdfs:comment "The stakeholder role that filed the report (Module C). Advisory context, not identity."@en ;
    rdfs:domain ontosage:Report ;
    rdfs:range ontosage:StakeholderRole ;
    skos:example "bldg:Report_042 ontosage:reportedByRole ontosage:Role_Occupant ." .
```
{% endraw %}
