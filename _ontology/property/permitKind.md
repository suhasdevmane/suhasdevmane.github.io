---
title: "ontosage:permitKind"
layout: post
permalink: /ontology/property/permitKind/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › permitKind

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#permitKind` |
| Label | permit kind |
| Kind | datatype property |
| Domain | [`ontosage:Permit`]({{ '/ontology/class/Permit/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Hot works, roof access, confined space, electrical isolation, work at height.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`permit_to_work`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#permit_to_work) | `type` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:permitKind a owl:DatatypeProperty ;
    rdfs:label "permit kind"@en ;
    rdfs:comment "Hot works, roof access, confined space, electrical isolation, work at height."@en ;
    rdfs:domain ontosage:Permit ;
    rdfs:range xsd:string .
```
{% endraw %}
