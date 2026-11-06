---
title: "ontosage:noiseProfile"
layout: post
permalink: /ontology/property/noiseProfile/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › noiseProfile

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#noiseProfile` |
| Label | noise profile |
| Kind | datatype property |
| Domain | [`ontosage:WorkspaceProfile`]({{ '/ontology/class/WorkspaceProfile/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The acoustic expectation people hold for this space: silent, quiet, conversational or busy. An expectation, not a measurement — it is what makes a group in the wrong room a problem.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`workspace_profile`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#workspace_profile) | `noise` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:noiseProfile a owl:DatatypeProperty ;
    rdfs:label "noise profile"@en ;
    rdfs:comment "The acoustic expectation people hold for this space: silent, quiet, conversational or busy. An expectation, not a measurement — it is what makes a group in the wrong room a problem."@en ;
    rdfs:domain ontosage:WorkspaceProfile ;
    rdfs:range xsd:string .
```
{% endraw %}
