---
title: "ontosage:networkRating"
layout: post
permalink: /ontology/property/networkRating/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › networkRating

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#networkRating` |
| Label | network rating |
| Kind | datatype property |
| Domain | [`ontosage:WorkspaceProfile`]({{ '/ontology/class/WorkspaceProfile/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Surveyed wireless quality in this space: strong, adequate or weak. Surveyed, not inferred from the nearest access point, because a wall between them is the usual reason an answer is wrong.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`workspace_profile`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#workspace_profile) | `network` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:networkRating a owl:DatatypeProperty ;
    rdfs:label "network rating"@en ;
    rdfs:comment "Surveyed wireless quality in this space: strong, adequate or weak. Surveyed, not inferred from the nearest access point, because a wall between them is the usual reason an answer is wrong."@en ;
    rdfs:domain ontosage:WorkspaceProfile ;
    rdfs:range xsd:string .
```
{% endraw %}
