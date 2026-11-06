---
title: "ontosage:nearestVerticalRoute"
layout: post
permalink: /ontology/property/nearestVerticalRoute/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › nearestVerticalRoute

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#nearestVerticalRoute` |
| Label | nearest vertical route |
| Kind | datatype property |
| Domain | [`ontosage:WorkspaceProfile`]({{ '/ontology/class/WorkspaceProfile/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The lift or stair core serving this space, so travel between levels can be reasoned about rather than guessed.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`circulation_time`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#circulation_time) | `vertical_route` | `xsd:string` |
| [`workspace_profile`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#workspace_profile) | `vertical_route` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:nearestVerticalRoute a owl:DatatypeProperty ;
    rdfs:label "nearest vertical route"@en ;
    rdfs:comment "The lift or stair core serving this space, so travel between levels can be reasoned about rather than guessed."@en ;
    rdfs:domain ontosage:WorkspaceProfile ;
    rdfs:range xsd:string .
```
{% endraw %}
