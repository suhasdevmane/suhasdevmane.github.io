---
title: "ontosage:recordId"
layout: post
permalink: /ontology/property/recordId/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › recordId

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#recordId` |
| Label | record id |
| Kind | datatype property |
| Domain | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The identifier this record carries in its own system of record (PTW-2026-0412, a contract number, a survey reference). Quoted back in answers so a reader can find the original, and used as the stable IRI slot so re-ingesting a document updates a record rather than duplicating it.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`access_permission`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#access_permission) | `group` | `xsd:string` |
| [`accessible_route`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#accessible_route) | `route` | `xsd:string` |
| [`approval_evidence`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#approval_evidence) | `approval` | `xsd:string` |
| [`asset_engineering`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#asset_engineering) | `code` | `xsd:string` |
| [`av_readiness`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#av_readiness) | `component` | `xsd:string` |
| [`booking`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#booking) | `reference` | `xsd:string` |
| [`circulation_time`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#circulation_time) | `code` | `xsd:string` |
| [`cleaning_task`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#cleaning_task) | `task` | `xsd:string` |
| [`competency`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#competency) | `reference` | `xsd:string` |
| [`condition_survey`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#condition_survey) | `reference` | `xsd:string` |
| [`continuity_provision`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#continuity_provision) | `provision` | `xsd:string` |
| [`contract`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#contract) | `reference` | `xsd:string` |
| [`coordination_function`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#coordination_function) | `function` | `xsd:string` |
| [`cost_line`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#cost_line) | `line` | `xsd:string` |
| [`department`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#department) | `code` | `xsd:string` |
| [`door_hardware`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#door_hardware) | `opening` | `xsd:string` |
| [`evacuation_provision`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#evacuation_provision) | `code` | `xsd:string` |
| [`event_activity`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#event_activity) | `activity` | `xsd:string` |
| [`fire_safety_asset`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#fire_safety_asset) | `code` | `xsd:string` |
| [`handover`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#handover) | `reference` | `xsd:string` |
| [`hazard_control`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#hazard_control) | `code` | `xsd:string` |
| [`incident_record`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#incident_record) | `ref` | `xsd:string` |
| [`operating_regime`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#operating_regime) | `code` | `xsd:string` |
| [`patrol_checkpoint`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#patrol_checkpoint) | `checkpoint` | `xsd:string` |
| [`permit_to_work`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#permit_to_work) | `permit` | `xsd:string` |
| [`public_event`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#public_event) | `event` | `xsd:string` |
| [`risk_assessment`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#risk_assessment) | `reference` | `xsd:string` |
| [`service_schedule`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#service_schedule) | `code` | `xsd:string` |
| [`stakeholder_group`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#stakeholder_group) | `code` | `xsd:string` |
| [`stock_item`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#stock_item) | `code` | `xsd:string` |
| [`sustainability_target`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#sustainability_target) | `reference` | `xsd:string` |
| [`tariff`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#tariff) | `reference` | `xsd:string` |
| [`timetabled_session`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#timetabled_session) | `code` | `xsd:string` |
| [`warranty`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#warranty) | `reference` | `xsd:string` |
| [`waste_collection`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#waste_collection) | `point` | `xsd:string` |
| [`waste_return`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#waste_return) | `code` | `xsd:string` |
| [`work_order`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#work_order) | `ref` | `xsd:string` |
| [`workspace_profile`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#workspace_profile) | `code` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:recordId a owl:DatatypeProperty ;
    rdfs:label "record id"@en ;
    rdfs:comment "The identifier this record carries in its own system of record (PTW-2026-0412, a contract number, a survey reference). Quoted back in answers so a reader can find the original, and used as the stable IRI slot so re-ingesting a document updates a record rather than duplicating it."@en ;
    rdfs:domain ontosage:IntervalRecord ;
    rdfs:range xsd:string .
```
{% endraw %}
