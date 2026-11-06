---
title: "ontosage:recoveryMinutes"
layout: post
permalink: /ontology/property/recoveryMinutes/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › recoveryMinutes

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#recoveryMinutes` |
| Label | recovery minutes |
| Kind | datatype property |
| Domain | [`ontosage:WorkspaceProfile`]({{ '/ontology/class/WorkspaceProfile/' | relative_url }}) |
| Range | `xsd:decimal` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

How long after a full session the room's conditions return to their normal range. The field that makes 'did the previous class leave too little recovery time before mine?' a calculation against the timetable rather than a guess.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`workspace_profile`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#workspace_profile) | `recovery_minutes` | `xsd:decimal` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:recoveryMinutes a owl:DatatypeProperty ;
    rdfs:label "recovery minutes"@en ;
    rdfs:comment "How long after a full session the room's conditions return to their normal range. The field that makes 'did the previous class leave too little recovery time before mine?' a calculation against the timetable rather than a guess."@en ;
    rdfs:domain ontosage:WorkspaceProfile ;
    rdfs:range xsd:decimal .
```
{% endraw %}
