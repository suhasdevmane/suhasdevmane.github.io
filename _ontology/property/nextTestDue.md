---
title: "ontosage:nextTestDue"
layout: post
permalink: /ontology/property/nextTestDue/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › nextTestDue

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#nextTestDue` |
| Label | next test due |
| Kind | datatype property |
| Domain | [`ontosage:FireSafetyAsset`]({{ '/ontology/class/FireSafetyAsset/' | relative_url }}) |
| Range | `xsd:date` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The schema gives no definition for this term.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`continuity_provision`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#continuity_provision) | `next_due` | `xsd:date` |
| [`door_hardware`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#door_hardware) | `next_due` | `xsd:date` |
| [`fire_safety_asset`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#fire_safety_asset) | `next_test_due` | `xsd:date` |
| [`hazard_control`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#hazard_control) | `next_test_due` | `xsd:date` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:nextTestDue a owl:DatatypeProperty ;
    rdfs:label "next test due"@en ;
    rdfs:domain ontosage:FireSafetyAsset ;
    rdfs:range xsd:date .
```
{% endraw %}
