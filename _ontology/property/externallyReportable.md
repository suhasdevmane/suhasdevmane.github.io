---
title: "ontosage:externallyReportable"
layout: post
permalink: /ontology/property/externallyReportable/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › externallyReportable

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#externallyReportable` |
| Label | externally reportable |
| Kind | datatype property |
| Domain | [`ontosage:IncidentRecord`]({{ '/ontology/class/IncidentRecord/' | relative_url }}) |
| Range | `xsd:boolean` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Whether this must be reported to a regulator. A legal obligation, not a severity judgement.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`incident_record`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#incident_record) | `reportable` | `xsd:boolean` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:externallyReportable a owl:DatatypeProperty ;
    rdfs:label "externally reportable"@en ;
    rdfs:comment "Whether this must be reported to a regulator. A legal obligation, not a severity judgement."@en ;
    rdfs:domain ontosage:IncidentRecord ;
    rdfs:range xsd:boolean .
```
{% endraw %}
