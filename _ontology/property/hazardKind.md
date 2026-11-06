---
title: "ontosage:hazardKind"
layout: post
permalink: /ontology/property/hazardKind/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › hazardKind

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#hazardKind` |
| Label | hazard kind |
| Kind | datatype property |
| Domain | [`ontosage:HazardControl`]({{ '/ontology/class/HazardControl/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

COSHH substance, local exhaust ventilation, asbestos-containing material, water system or biological.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`hazard_control`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#hazard_control) | `kind` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:hazardKind a owl:DatatypeProperty ;
    rdfs:label "hazard kind"@en ;
    rdfs:comment "COSHH substance, local exhaust ventilation, asbestos-containing material, water system or biological."@en ;
    rdfs:domain ontosage:HazardControl ;
    rdfs:range xsd:string .
```
{% endraw %}
