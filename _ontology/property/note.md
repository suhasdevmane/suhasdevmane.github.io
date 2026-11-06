---
title: "ontosage:note"
layout: post
permalink: /ontology/property/note/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › note

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#note` |
| Label | additional detail |
| Kind | datatype property |
| Domain | [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Any extra free-text detail (features, caveats, opening notes).

## Examples

- "Multi-faith, open to all; wudu facilities adjacent."

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`competency`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#competency) | `valid_for_months` | `xsd:string` |
| [`condition_survey`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#condition_survey) | `note` | `xsd:string` |
| [`handover`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#handover) | `document_kind` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:note a owl:DatatypeProperty ;
    rdfs:label "additional detail"@en ;
    rdfs:comment "Any extra free-text detail (features, caveats, opening notes)."@en ;
    rdfs:domain ontosage:Capability ;
    rdfs:range xsd:string ;
    skos:example "\"Multi-faith, open to all; wudu facilities adjacent.\"" .
```
{% endraw %}
