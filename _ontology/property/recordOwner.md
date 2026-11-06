---
title: "ontosage:recordOwner"
layout: post
permalink: /ontology/property/recordOwner/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › recordOwner

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#recordOwner` |
| Label | record owner |
| Kind | datatype property |
| Domain | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The accountable owner of this record — a role or team, not a person. Named in every answer that rests on it, so the reader knows who to defer to.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`access_permission`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#access_permission) | `owner` | `xsd:string` |
| [`av_readiness`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#av_readiness) | `owner` | `xsd:string` |
| [`cleaning_task`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#cleaning_task) | `owner` | `xsd:string` |
| [`continuity_provision`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#continuity_provision) | `owner` | `xsd:string` |
| [`cost_line`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#cost_line) | `owner` | `xsd:string` |
| [`door_hardware`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#door_hardware) | `owner` | `xsd:string` |
| [`evacuation_provision`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#evacuation_provision) | `owner` | `xsd:string` |
| [`event_activity`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#event_activity) | `owner` | `xsd:string` |
| [`fire_safety_asset`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#fire_safety_asset) | `owner` | `xsd:string` |
| [`hazard_control`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#hazard_control) | `owner` | `xsd:string` |
| [`incident_record`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#incident_record) | `owner` | `xsd:string` |
| [`operating_regime`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#operating_regime) | `owner` | `xsd:string` |
| [`patrol_checkpoint`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#patrol_checkpoint) | `owner` | `xsd:string` |
| [`public_event`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#public_event) | `owner` | `xsd:string` |
| [`service_schedule`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#service_schedule) | `owner` | `xsd:string` |
| [`waste_collection`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#waste_collection) | `owner` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:recordOwner a owl:DatatypeProperty ;
    rdfs:label "record owner"@en ;
    rdfs:comment "The accountable owner of this record — a role or team, not a person. Named in every answer that rests on it, so the reader knows who to defer to."@en ;
    rdfs:domain ontosage:IntervalRecord ;
    rdfs:range xsd:string .
```
{% endraw %}
