---
title: "ontosage:incidentSeverity"
layout: post
permalink: /ontology/property/incidentSeverity/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › incidentSeverity

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#incidentSeverity` |
| Label | incident severity |
| Kind | datatype property |
| Domain | [`ontosage:IncidentRecord`]({{ '/ontology/class/IncidentRecord/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Actual severity of what happened. Kept apart from potential severity, because a near miss with low actual and high potential severity is the most important row in any incident register.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`incident_record`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#incident_record) | `severity` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:incidentSeverity a owl:DatatypeProperty ;
    rdfs:label "incident severity"@en ;
    rdfs:comment "Actual severity of what happened. Kept apart from potential severity, because a near miss with low actual and high potential severity is the most important row in any incident register."@en ;
    rdfs:domain ontosage:IncidentRecord ;
    rdfs:range xsd:string .
```
{% endraw %}
