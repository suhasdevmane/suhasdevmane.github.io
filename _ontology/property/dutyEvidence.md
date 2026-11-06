---
title: "ontosage:dutyEvidence"
layout: post
permalink: /ontology/property/dutyEvidence/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › dutyEvidence

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#dutyEvidence` |
| Label | duty evidence |
| Kind | datatype property |
| Domain | [`ontosage:AssetEngineeringProfile`]({{ '/ontology/class/AssetEngineeringProfile/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The document or record that substantiates the commissioned duty. Without it the duty is an assertion.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`asset_engineering`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#asset_engineering) | `duty_evidence` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:dutyEvidence a owl:DatatypeProperty ;
    rdfs:label "duty evidence"@en ;
    rdfs:comment "The document or record that substantiates the commissioned duty. Without it the duty is an assertion."@en ;
    rdfs:domain ontosage:AssetEngineeringProfile ;
    rdfs:range xsd:string .
```
{% endraw %}
