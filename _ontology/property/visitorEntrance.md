---
title: "ontosage:visitorEntrance"
layout: post
permalink: /ontology/property/visitorEntrance/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › visitorEntrance

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#visitorEntrance` |
| Label | visitor entrance |
| Kind | datatype property |
| Domain | [`ontosage:PublicEvent`]({{ '/ontology/class/PublicEvent/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The entrance a visitor should use, which is not always the one nearest the venue.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`accessible_route`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#accessible_route) | `entrance` | `xsd:string` |
| [`public_event`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#public_event) | `entrance` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:visitorEntrance a owl:DatatypeProperty ;
    rdfs:label "visitor entrance"@en ;
    rdfs:comment "The entrance a visitor should use, which is not always the one nearest the venue."@en ;
    rdfs:domain ontosage:PublicEvent ;
    rdfs:range xsd:string .
```
{% endraw %}
