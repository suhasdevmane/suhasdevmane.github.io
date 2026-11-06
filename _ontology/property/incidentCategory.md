---
title: "ontosage:incidentCategory"
layout: post
permalink: /ontology/property/incidentCategory/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › incidentCategory

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#incidentCategory` |
| Label | incident category |
| Kind | datatype property |
| Domain | [`ontosage:IncidentRecord`]({{ '/ontology/class/IncidentRecord/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

injury, near miss, property damage, security, environmental or service failure.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`incident_record`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#incident_record) | `category` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:incidentCategory a owl:DatatypeProperty ;
    rdfs:label "incident category"@en ;
    rdfs:comment "injury, near miss, property damage, security, environmental or service failure."@en ;
    rdfs:domain ontosage:IncidentRecord ;
    rdfs:range xsd:string .
```
{% endraw %}
