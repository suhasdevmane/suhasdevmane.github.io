---
title: "ontosage:companionPolicy"
layout: post
permalink: /ontology/property/companionPolicy/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › companionPolicy

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#companionPolicy` |
| Label | companion policy |
| Kind | datatype property |
| Domain | [`ontosage:PublicEvent`]({{ '/ontology/class/PublicEvent/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Whether a companion or support person may attend, and whether they register separately.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`event_activity`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#event_activity) | `companion` | `xsd:string` |
| [`public_event`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#public_event) | `companion` | `xsd:string` |

## Turtle

Development notes were removed from one or more text values below; the source file holds the full text.

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:companionPolicy a owl:DatatypeProperty ;
    rdfs:label "companion policy"@en ;
    rdfs:comment "Whether a companion or support person may attend, and whether they register separately."@en ;
    rdfs:domain ontosage:PublicEvent ;
    rdfs:range xsd:string .
```
{% endraw %}
