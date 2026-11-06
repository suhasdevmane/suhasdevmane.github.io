---
title: "ontosage:documentRef"
layout: post
permalink: /ontology/property/documentRef/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › documentRef

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#documentRef` |
| Label | backing document |
| Kind | datatype property |
| Domain | [`ontosage:KnowledgeTopic`]({{ '/ontology/class/KnowledgeTopic/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

File name of the uploaded document that sets out this topic in full, relative to the building's own documents/ folder. This is the ONE assertion that makes document retrieval deterministic. Without it a question is matched to a document by cosine similarity alone, against a floor calibrated on one corpus and one embedding model — so changing either silently changes which document answers which question. With it, the question is matched to the TOPIC by lay term and the answer is drawn from the document the topic NAMES; similarity then only orders chunks WITHIN the right document. No building name appears in code: the building declares its own documents.

## Examples

- "fire\_safety.md"

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:documentRef a owl:DatatypeProperty ;
    rdfs:label "backing document"@en ;
    rdfs:comment "File name of the uploaded document that sets out this topic in full, relative to the building's own documents/ folder. This is the ONE assertion that makes document retrieval deterministic. Without it a question is matched to a document by cosine similarity alone, against a floor calibrated on one corpus and one embedding model — so changing either silently changes which document answers which question. With it, the question is matched to the TOPIC by lay term and the answer is drawn from the document the topic NAMES; similarity then only orders chunks WITHIN the right document. No building name appears in code: the building declares its own documents."@en ;
    rdfs:domain ontosage:KnowledgeTopic ;
    rdfs:range xsd:string ;
    skos:example "\"fire_safety.md\"" .
```
{% endraw %}
