---
title: "ontosage:potentialSeverity"
layout: post
permalink: /ontology/property/potentialSeverity/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › potentialSeverity

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#potentialSeverity` |
| Label | potential severity |
| Kind | datatype property |
| Domain | [`ontosage:IncidentRecord`]({{ '/ontology/class/IncidentRecord/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

What could reasonably have happened. The field that stops a near miss being filed and forgotten.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`incident_record`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#incident_record) | `potential_severity` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:potentialSeverity a owl:DatatypeProperty ;
    rdfs:label "potential severity"@en ;
    rdfs:comment "What could reasonably have happened. The field that stops a near miss being filed and forgotten."@en ;
    rdfs:domain ontosage:IncidentRecord ;
    rdfs:range xsd:string .
```
{% endraw %}
