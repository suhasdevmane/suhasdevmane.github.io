---
title: "ontosage:powerAccess"
layout: post
permalink: /ontology/property/powerAccess/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › powerAccess

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#powerAccess` |
| Label | power access |
| Kind | datatype property |
| Domain | [`ontosage:WorkspaceProfile`]({{ '/ontology/class/WorkspaceProfile/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

How reliably a laptop can be plugged in: at every seat, at some seats, perimeter only, or none.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`workspace_profile`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#workspace_profile) | `power` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:powerAccess a owl:DatatypeProperty ;
    rdfs:label "power access"@en ;
    rdfs:comment "How reliably a laptop can be plugged in: at every seat, at some seats, perimeter only, or none."@en ;
    rdfs:domain ontosage:WorkspaceProfile ;
    rdfs:range xsd:string .
```
{% endraw %}
