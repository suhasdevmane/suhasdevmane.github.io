---
title: "ontosage:apertureKind"
layout: post
permalink: /ontology/property/apertureKind/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › apertureKind

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#apertureKind` |
| Label | aperture kind |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

What the opening physically accepts. A narrow slot will not take flattened card whatever the label claims.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`waste_collection`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#waste_collection) | `aperture` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:apertureKind a owl:DatatypeProperty ;
    rdfs:label "aperture kind"@en ;
    rdfs:comment "What the opening physically accepts. A narrow slot will not take flattened card whatever the label claims."@en ;
    rdfs:range xsd:string .
```
{% endraw %}
