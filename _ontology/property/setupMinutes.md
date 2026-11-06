---
title: "ontosage:setupMinutes"
layout: post
permalink: /ontology/property/setupMinutes/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › setupMinutes

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#setupMinutes` |
| Label | setup minutes |
| Kind | datatype property |
| Domain | [`ontosage:WorkspaceProfile`]({{ '/ontology/class/WorkspaceProfile/' | relative_url }}) |
| Range | `xsd:decimal` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Time needed in the room before a session can start — logging in, connecting, arranging. Separate from travel because they are paid by different people at different moments, and a transition that fits the travel can still fail on the setup.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`workspace_profile`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#workspace_profile) | `setup_minutes` | `xsd:decimal` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:setupMinutes a owl:DatatypeProperty ;
    rdfs:label "setup minutes"@en ;
    rdfs:comment "Time needed in the room before a session can start — logging in, connecting, arranging. Separate from travel because they are paid by different people at different moments, and a transition that fits the travel can still fail on the setup."@en ;
    rdfs:domain ontosage:WorkspaceProfile ;
    rdfs:range xsd:decimal .
```
{% endraw %}
