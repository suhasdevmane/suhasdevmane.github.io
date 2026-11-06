---
title: "ontosage:alternativePath"
layout: post
permalink: /ontology/property/alternativePath/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › alternativePath

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#alternativePath` |
| Label | alternative path |
| Kind | datatype property |
| Domain | [`ontosage:ContinuityProvision`]({{ '/ontology/class/ContinuityProvision/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

How the service reaches the alternative: a diverse fibre route, a second riser, a generator feed, a manual process.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`continuity_provision`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#continuity_provision) | `alternative_path` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:alternativePath a owl:DatatypeProperty ;
    rdfs:label "alternative path"@en ;
    rdfs:comment "How the service reaches the alternative: a diverse fibre route, a second riser, a generator feed, a manual process."@en ;
    rdfs:domain ontosage:ContinuityProvision ;
    rdfs:range xsd:string .
```
{% endraw %}
