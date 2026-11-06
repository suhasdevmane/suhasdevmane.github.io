---
title: "ontosage:registrationPolicy"
layout: post
permalink: /ontology/property/registrationPolicy/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › registrationPolicy

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#registrationPolicy` |
| Label | registration policy |
| Kind | datatype property |
| Domain | [`ontosage:PublicEvent`]({{ '/ontology/class/PublicEvent/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The schema gives no definition for this term.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`public_event`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#public_event) | `registration` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:registrationPolicy a owl:DatatypeProperty ;
    rdfs:label "registration policy"@en ;
    rdfs:domain ontosage:PublicEvent ;
    rdfs:range xsd:string .
```
{% endraw %}
