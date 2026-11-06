---
title: "ontosage:workspaceKind"
layout: post
permalink: /ontology/property/workspaceKind/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › workspaceKind

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#workspaceKind` |
| Label | workspace kind |
| Kind | datatype property |
| Domain | [`ontosage:WorkspaceProfile`]({{ '/ontology/class/WorkspaceProfile/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

quiet study, open study, group study, bookable room, teaching room, computer lab, common room or breakout.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`workspace_profile`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#workspace_profile) | `kind` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:workspaceKind a owl:DatatypeProperty ;
    rdfs:label "workspace kind"@en ;
    rdfs:comment "quiet study, open study, group study, bookable room, teaching room, computer lab, common room or breakout."@en ;
    rdfs:domain ontosage:WorkspaceProfile ;
    rdfs:range xsd:string .
```
{% endraw %}
