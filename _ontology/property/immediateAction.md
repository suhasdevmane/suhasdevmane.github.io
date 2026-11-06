---
title: "ontosage:immediateAction"
layout: post
permalink: /ontology/property/immediateAction/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › immediateAction

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#immediateAction` |
| Label | immediate action |
| Kind | datatype property |
| Domain | [`ontosage:IncidentRecord`]({{ '/ontology/class/IncidentRecord/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The schema gives no definition for this term.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`incident_record`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#incident_record) | `immediate_action` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:immediateAction a owl:DatatypeProperty ;
    rdfs:label "immediate action"@en ;
    rdfs:domain ontosage:IncidentRecord ;
    rdfs:range xsd:string .
```
{% endraw %}
