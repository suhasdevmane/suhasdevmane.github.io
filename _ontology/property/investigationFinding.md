---
title: "ontosage:investigationFinding"
layout: post
permalink: /ontology/property/investigationFinding/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › investigationFinding

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#investigationFinding` |
| Label | investigation finding |
| Kind | datatype property |
| Domain | [`ontosage:IncidentRecord`]({{ '/ontology/class/IncidentRecord/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

What the investigation concluded. Blank where none has been done — and a blank on a high-potential row is itself the finding.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`incident_record`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#incident_record) | `investigation_finding` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:investigationFinding a owl:DatatypeProperty ;
    rdfs:label "investigation finding"@en ;
    rdfs:comment "What the investigation concluded. Blank where none has been done — and a blank on a high-potential row is itself the finding."@en ;
    rdfs:domain ontosage:IncidentRecord ;
    rdfs:range xsd:string .
```
{% endraw %}
