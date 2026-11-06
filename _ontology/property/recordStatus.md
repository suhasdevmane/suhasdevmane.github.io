---
title: "ontosage:recordStatus"
layout: post
permalink: /ontology/property/recordStatus/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › recordStatus

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#recordStatus` |
| Label | record status |
| Kind | datatype property |
| Domain | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Lifecycle state: open | assigned | done | cancelled | detected | resolved.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`access_permission`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#access_permission) | `status` | `xsd:string` |
| [`accessible_route`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#accessible_route) | `status` | `xsd:string` |
| [`approval_evidence`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#approval_evidence) | `status` | `xsd:string` |
| [`asset_engineering`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#asset_engineering) | `status` | `xsd:string` |
| [`av_readiness`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#av_readiness) | `state` | `xsd:string` |
| [`booking`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#booking) | `status` | `xsd:string` |
| [`circulation_time`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#circulation_time) | `status` | `xsd:string` |
| [`cleaning_task`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#cleaning_task) | `status` | `xsd:string` |
| [`continuity_provision`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#continuity_provision) | `status` | `xsd:string` |
| [`contract`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#contract) | `status` | `xsd:string` |
| [`coordination_function`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#coordination_function) | `status` | `xsd:string` |
| [`cost_line`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#cost_line) | `status` | `xsd:string` |
| [`department`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#department) | `status` | `xsd:string` |
| [`door_hardware`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#door_hardware) | `status` | `xsd:string` |
| [`evacuation_provision`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#evacuation_provision) | `status` | `xsd:string` |
| [`event_activity`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#event_activity) | `status` | `xsd:string` |
| [`fire_safety_asset`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#fire_safety_asset) | `status` | `xsd:string` |
| [`handover`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#handover) | `status` | `xsd:string` |
| [`hazard_control`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#hazard_control) | `status` | `xsd:string` |
| [`incident_record`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#incident_record) | `status` | `xsd:string` |
| [`operating_regime`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#operating_regime) | `status` | `xsd:string` |
| [`patrol_checkpoint`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#patrol_checkpoint) | `status` | `xsd:string` |
| [`permit_to_work`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#permit_to_work) | `status` | `xsd:string` |
| [`public_event`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#public_event) | `status` | `xsd:string` |
| [`risk_assessment`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#risk_assessment) | `status` | `xsd:string` |
| [`service_schedule`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#service_schedule) | `status` | `xsd:string` |
| [`stakeholder_group`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#stakeholder_group) | `status` | `xsd:string` |
| [`stock_item`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#stock_item) | `status` | `xsd:string` |
| [`sustainability_target`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#sustainability_target) | `status` | `xsd:string` |
| [`timetabled_session`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#timetabled_session) | `status` | `xsd:string` |
| [`warranty`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#warranty) | `status` | `xsd:string` |
| [`waste_collection`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#waste_collection) | `status` | `xsd:string` |
| [`waste_return`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#waste_return) | `status` | `xsd:string` |
| [`work_order`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#work_order) | `status` | `xsd:string` |
| [`workspace_profile`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#workspace_profile) | `status` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:recordStatus a owl:DatatypeProperty ;
    rdfs:label "record status"@en ;
    rdfs:comment "Lifecycle state: open | assigned | done | cancelled | detected | resolved."@en ;
    rdfs:domain ontosage:IntervalRecord ;
    rdfs:range xsd:string .
```
{% endraw %}
