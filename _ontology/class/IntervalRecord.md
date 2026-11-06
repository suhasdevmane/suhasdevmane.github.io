---
title: "ontosage:IntervalRecord"
layout: post
permalink: /ontology/class/IntervalRecord/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › IntervalRecord

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#IntervalRecord` |
| Label | Interval record |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Abstract supertype for anything that happens over a time interval with a lifecycle: bookings, work orders, access events, alarms, compliance checks, anomaly episodes. Never instantiated directly.

## Class hierarchy

Superclasses: none (a root class).

Direct subclasses (23; 23 descendants in all):

- [`ontosage:AccessEvent`]({{ '/ontology/class/AccessEvent/' | relative_url }}) Access event
- [`ontosage:AccessPermission`]({{ '/ontology/class/AccessPermission/' | relative_url }}) Access permission group
- [`ontosage:AlarmEvent`]({{ '/ontology/class/AlarmEvent/' | relative_url }}) Alarm activation
- [`ontosage:AnomalyEvent`]({{ '/ontology/class/AnomalyEvent/' | relative_url }}) Anomaly episode
- [`ontosage:ApprovalRecord`]({{ '/ontology/class/ApprovalRecord/' | relative_url }}) Approval and evidence record
- [`ontosage:AssetStatus`]({{ '/ontology/class/AssetStatus/' | relative_url }}) Asset status record
- [`ontosage:Booking`]({{ '/ontology/class/Booking/' | relative_url }}) Room booking
- [`ontosage:ClosurePeriod`]({{ '/ontology/class/ClosurePeriod/' | relative_url }}) Closure period
- [`ontosage:CompetencyRecord`]({{ '/ontology/class/CompetencyRecord/' | relative_url }}) Competency requirement
- [`ontosage:ComplianceCheck`]({{ '/ontology/class/ComplianceCheck/' | relative_url }}) Compliance check
- [`ontosage:ConditionSurvey`]({{ '/ontology/class/ConditionSurvey/' | relative_url }}) Condition survey
- [`ontosage:Contract`]({{ '/ontology/class/Contract/' | relative_url }}) Contract
- [`ontosage:HandoverRecord`]({{ '/ontology/class/HandoverRecord/' | relative_url }}) Handover record
- [`ontosage:IncidentRecord`]({{ '/ontology/class/IncidentRecord/' | relative_url }}) Incident record
- [`ontosage:Permit`]({{ '/ontology/class/Permit/' | relative_url }}) Permit to work
- [`ontosage:PublicEvent`]({{ '/ontology/class/PublicEvent/' | relative_url }}) Public event
- [`ontosage:RiskAssessment`]({{ '/ontology/class/RiskAssessment/' | relative_url }}) Risk assessment
- [`ontosage:ServiceSchedule`]({{ '/ontology/class/ServiceSchedule/' | relative_url }}) Planned service schedule entry
- [`ontosage:Tariff`]({{ '/ontology/class/Tariff/' | relative_url }}) Energy tariff
- [`ontosage:TimetabledSession`]({{ '/ontology/class/TimetabledSession/' | relative_url }}) Timetabled session
- [`ontosage:Warranty`]({{ '/ontology/class/Warranty/' | relative_url }}) Warranty
- [`ontosage:WasteReturn`]({{ '/ontology/class/WasteReturn/' | relative_url }}) Waste return
- [`ontosage:WorkOrder`]({{ '/ontology/class/WorkOrder/' | relative_url }}) Work order

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:aboutPoint`]({{ '/ontology/property/aboutPoint/' | relative_url }}) | object | [`brick:Point`](https://ontology.brickschema.org/1.4/#brick:Point) | this class |
| [`ontosage:aboutSpace`]({{ '/ontology/property/aboutSpace/' | relative_url }}) | object | [`brick:Location`](https://ontology.brickschema.org/1.4/#brick:Location) | this class |
| [`ontosage:completedDate`]({{ '/ontology/property/completedDate/' | relative_url }}) | datatype | `xsd:dateTime` | this class |
| [`ontosage:coveredScope`]({{ '/ontology/property/coveredScope/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:coversAsset`]({{ '/ontology/property/coversAsset/' | relative_url }}) | object | [`brick:Equipment`](https://ontology.brickschema.org/1.4/#brick:Equipment) | this class |
| [`ontosage:derivedFromDocument`]({{ '/ontology/property/derivedFromDocument/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:liftedByMapping`]({{ '/ontology/property/liftedByMapping/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:owningAuthority`]({{ '/ontology/property/owningAuthority/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:providerName`]({{ '/ontology/property/providerName/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:recordOwner`]({{ '/ontology/property/recordOwner/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:recordVersion`]({{ '/ontology/property/recordVersion/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:responsibleRole`]({{ '/ontology/property/responsibleRole/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:retrievedAt`]({{ '/ontology/property/retrievedAt/' | relative_url }}) | datatype | `xsd:dateTime` | this class |
| [`ontosage:supersedes`]({{ '/ontology/property/supersedes/' | relative_url }}) | object | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) | this class |

## Used as the range of

| Property | Kind | Domain |
|---|---|---|
| [`ontosage:supersedes`]({{ '/ontology/property/supersedes/' | relative_url }}) | object | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ontosage:IntervalRecord a owl:Class ;
    rdfs:label "Interval record"@en ;
    rdfs:comment "Abstract supertype for anything that happens over a time interval with a lifecycle: bookings, work orders, access events, alarms, compliance checks, anomaly episodes. Never instantiated directly."@en .
```
{% endraw %}
