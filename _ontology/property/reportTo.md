---
title: "ontosage:reportTo"
layout: post
permalink: /ontology/property/reportTo/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › reportTo

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#reportTo` |
| Label | report to |
| Kind | datatype property |
| Domain | [`ontosage:KnowledgeTopic`]({{ '/ontology/class/KnowledgeTopic/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Where or to whom a maintenance issue / procedure should be reported.

## Examples

- "Estates FM helpdesk (estates@example.ac.uk / 029 2087 6026); out-of-hours 029 2087 5555"

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`incident_record`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#incident_record) | `reported_by_role` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:reportTo a owl:DatatypeProperty ;
    rdfs:label "report to"@en ;
    rdfs:comment "Where or to whom a maintenance issue / procedure should be reported."@en ;
    rdfs:domain ontosage:KnowledgeTopic ;
    rdfs:range xsd:string ;
    skos:example "\"Estates FM helpdesk (estates@example.ac.uk / 029 2087 6026); out-of-hours 029 2087 5555\"" .
```
{% endraw %}
