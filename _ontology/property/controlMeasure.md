---
title: "ontosage:controlMeasure"
layout: post
permalink: /ontology/property/controlMeasure/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › controlMeasure

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#controlMeasure` |
| Label | control measure |
| Kind | datatype property |
| Domain | [`ontosage:HazardControl`]({{ '/ontology/class/HazardControl/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

What actually keeps the hazard safe. The thing that must not silently stop working.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`hazard_control`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#hazard_control) | `control` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:controlMeasure a owl:DatatypeProperty ;
    rdfs:label "control measure"@en ;
    rdfs:comment "What actually keeps the hazard safe. The thing that must not silently stop working."@en ;
    rdfs:domain ontosage:HazardControl ;
    rdfs:range xsd:string .
```
{% endraw %}
