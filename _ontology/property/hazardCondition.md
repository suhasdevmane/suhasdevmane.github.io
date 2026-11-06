---
title: "ontosage:hazardCondition"
layout: post
permalink: /ontology/property/hazardCondition/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › hazardCondition

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#hazardCondition` |
| Label | hazard condition |
| Kind | datatype property |
| Domain | [`ontosage:HazardControl`]({{ '/ontology/class/HazardControl/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Current assessed condition of the hazard itself, distinct from the state of its control — an asbestos material in good condition under a damaged label is a different problem from a damaged material.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`hazard_control`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#hazard_control) | `condition` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:hazardCondition a owl:DatatypeProperty ;
    rdfs:label "hazard condition"@en ;
    rdfs:comment "Current assessed condition of the hazard itself, distinct from the state of its control — an asbestos material in good condition under a damaged label is a different problem from a damaged material."@en ;
    rdfs:domain ontosage:HazardControl ;
    rdfs:range xsd:string .
```
{% endraw %}
