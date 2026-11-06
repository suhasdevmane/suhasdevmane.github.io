---
title: "ontosage:wasteStream"
layout: post
permalink: /ontology/property/wasteStream/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › wasteStream

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#wasteStream` |
| Label | recorded waste stream |
| Kind | datatype property |
| Domain | [`ontosage:WastePoint`]({{ '/ontology/class/WastePoint/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

general | mixed\_recycling | paper | glass | food | WEEE | confidential | batteries. A point may declare several. The stream is what makes a contamination ratio meaningful: without knowing which stream a measurement belongs to, two numbers cannot be compared.

What the system says the point is for.

## Examples

- "mixed\_recycling"

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`waste_collection`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#waste_collection) | `stream_record` | `xsd:string` |
| [`waste_return`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#waste_return) | `stream` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:wasteStream a owl:DatatypeProperty ;
    rdfs:label "recorded waste stream"@en,
        "waste stream"@en ;
    rdfs:comment "What the system says the point is for."@en,
        "general | mixed_recycling | paper | glass | food | WEEE | confidential | batteries. A point may declare several. The stream is what makes a contamination ratio meaningful: without knowing which stream a measurement belongs to, two numbers cannot be compared."@en ;
    rdfs:domain ontosage:WastePoint ;
    rdfs:range xsd:string ;
    skos:example "\"mixed_recycling\"" .
```
{% endraw %}
