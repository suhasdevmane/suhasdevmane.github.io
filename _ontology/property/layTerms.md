---
title: "ontosage:layTerms"
layout: post
permalink: /ontology/property/layTerms/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › layTerms

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#layTerms` |
| Label | lay-term keywords |
| Kind | datatype property |
| Domain | [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Comma-separated plain-language phrasings a stakeholder might use, INCLUDING full questions. OntoSage matches a question to this capability on these phrases (multi-word phrases and distinctive single words). The single most important field for retrieval quality.

## Examples

- "prayer room, quiet room, where can i pray, faith room"

## Alignments

| Mapping | Term |
|---|---|
| `skos:related` | [`hbco:layTerm`]({{ '/ontology/property/layTerm/' | relative_url }}) |

## Used in the schema

63 schema term(s) carry this property:

- [`ontosage:AccessEvent`]({{ '/ontology/class/AccessEvent/' | relative_url }})
- [`ontosage:AccessibilityFeature`]({{ '/ontology/class/AccessibilityFeature/' | relative_url }})
- [`ontosage:AccessibleRoute`]({{ '/ontology/class/AccessibleRoute/' | relative_url }})
- [`ontosage:AccessPermission`]({{ '/ontology/class/AccessPermission/' | relative_url }})
- [`ontosage:AlarmEvent`]({{ '/ontology/class/AlarmEvent/' | relative_url }})
- [`ontosage:AnomalyEvent`]({{ '/ontology/class/AnomalyEvent/' | relative_url }})
- [`ontosage:ApprovalRecord`]({{ '/ontology/class/ApprovalRecord/' | relative_url }})
- [`ontosage:AssemblyPoint`]({{ '/ontology/class/AssemblyPoint/' | relative_url }})
- [`ontosage:AssetEngineeringProfile`]({{ '/ontology/class/AssetEngineeringProfile/' | relative_url }})
- [`ontosage:AssetStatus`]({{ '/ontology/class/AssetStatus/' | relative_url }})
- [`ontosage:AVReadiness`]({{ '/ontology/class/AVReadiness/' | relative_url }})
- [`ontosage:BikeStorage`]({{ '/ontology/class/BikeStorage/' | relative_url }})
- [`ontosage:Booking`]({{ '/ontology/class/Booking/' | relative_url }})
- [`ontosage:Cafe`]({{ '/ontology/class/Cafe/' | relative_url }})
- [`ontosage:CirculationTime`]({{ '/ontology/class/CirculationTime/' | relative_url }})
- [`ontosage:CleaningTask`]({{ '/ontology/class/CleaningTask/' | relative_url }})
- [`ontosage:ClosurePeriod`]({{ '/ontology/class/ClosurePeriod/' | relative_url }})
- [`ontosage:CompetencyRecord`]({{ '/ontology/class/CompetencyRecord/' | relative_url }})
- [`ontosage:ComplianceCheck`]({{ '/ontology/class/ComplianceCheck/' | relative_url }})
- [`ontosage:ConditionSurvey`]({{ '/ontology/class/ConditionSurvey/' | relative_url }})
- [`ontosage:ContinuityProvision`]({{ '/ontology/class/ContinuityProvision/' | relative_url }})
- [`ontosage:Contract`]({{ '/ontology/class/Contract/' | relative_url }})
- [`ontosage:CoordinationFunction`]({{ '/ontology/class/CoordinationFunction/' | relative_url }})
- [`ontosage:CostLine`]({{ '/ontology/class/CostLine/' | relative_url }})
- [`ontosage:Department`]({{ '/ontology/class/Department/' | relative_url }})
- [`ontosage:DisclosureRule`]({{ '/ontology/class/DisclosureRule/' | relative_url }})
- [`ontosage:DoorHardware`]({{ '/ontology/class/DoorHardware/' | relative_url }})
- [`ontosage:DrinkingWater`]({{ '/ontology/class/DrinkingWater/' | relative_url }})
- [`ontosage:EvacuationProvision`]({{ '/ontology/class/EvacuationProvision/' | relative_url }})
- [`ontosage:EventActivity`]({{ '/ontology/class/EventActivity/' | relative_url }})
- [`ontosage:FireSafetyAsset`]({{ '/ontology/class/FireSafetyAsset/' | relative_url }})
- [`ontosage:FirstAidPoint`]({{ '/ontology/class/FirstAidPoint/' | relative_url }})
- [`ontosage:HandoverRecord`]({{ '/ontology/class/HandoverRecord/' | relative_url }})
- [`ontosage:HazardControl`]({{ '/ontology/class/HazardControl/' | relative_url }})
- [`ontosage:IncidentRecord`]({{ '/ontology/class/IncidentRecord/' | relative_url }})
- [`ontosage:Kitchenette`]({{ '/ontology/class/Kitchenette/' | relative_url }})
- [`ontosage:Lift`]({{ '/ontology/class/Lift/' | relative_url }})
- [`ontosage:Locker`]({{ '/ontology/class/Locker/' | relative_url }})
- [`ontosage:NursingRoom`]({{ '/ontology/class/NursingRoom/' | relative_url }})
- [`ontosage:OperatingRegime`]({{ '/ontology/class/OperatingRegime/' | relative_url }})
- [`ontosage:ParkingArea`]({{ '/ontology/class/ParkingArea/' | relative_url }})
- [`ontosage:PatrolCheckpoint`]({{ '/ontology/class/PatrolCheckpoint/' | relative_url }})
- [`ontosage:Permit`]({{ '/ontology/class/Permit/' | relative_url }})
- [`ontosage:PrayerRoom`]({{ '/ontology/class/PrayerRoom/' | relative_url }})
- [`ontosage:PrinterPoint`]({{ '/ontology/class/PrinterPoint/' | relative_url }})
- [`ontosage:PublicEvent`]({{ '/ontology/class/PublicEvent/' | relative_url }})
- [`ontosage:RiskAssessment`]({{ '/ontology/class/RiskAssessment/' | relative_url }})
- [`ontosage:ServiceSchedule`]({{ '/ontology/class/ServiceSchedule/' | relative_url }})
- [`ontosage:ShowerFacility`]({{ '/ontology/class/ShowerFacility/' | relative_url }})
- [`ontosage:StakeholderGroup`]({{ '/ontology/class/StakeholderGroup/' | relative_url }})
- [`ontosage:StockItem`]({{ '/ontology/class/StockItem/' | relative_url }})
- [`ontosage:StudyArea`]({{ '/ontology/class/StudyArea/' | relative_url }})
- [`ontosage:SustainabilityTarget`]({{ '/ontology/class/SustainabilityTarget/' | relative_url }})
- [`ontosage:Tariff`]({{ '/ontology/class/Tariff/' | relative_url }})
- [`ontosage:TimetabledSession`]({{ '/ontology/class/TimetabledSession/' | relative_url }})
- [`ontosage:ToiletFacility`]({{ '/ontology/class/ToiletFacility/' | relative_url }})
- [`ontosage:VendingMachine`]({{ '/ontology/class/VendingMachine/' | relative_url }})
- [`ontosage:Warranty`]({{ '/ontology/class/Warranty/' | relative_url }})
- [`ontosage:WasteCollectionPoint`]({{ '/ontology/class/WasteCollectionPoint/' | relative_url }})
- [`ontosage:WastePoint`]({{ '/ontology/class/WastePoint/' | relative_url }})
- [`ontosage:WasteReturn`]({{ '/ontology/class/WasteReturn/' | relative_url }})
- [`ontosage:WorkOrder`]({{ '/ontology/class/WorkOrder/' | relative_url }})
- [`ontosage:WorkspaceProfile`]({{ '/ontology/class/WorkspaceProfile/' | relative_url }})

## Turtle

{% raw %}
```turtle
@prefix hbco: <http://ontosage.org/hbco#> .
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:layTerms a owl:DatatypeProperty ;
    rdfs:label "lay-term keywords"@en ;
    rdfs:comment "Comma-separated plain-language phrasings a stakeholder might use, INCLUDING full questions. OntoSage matches a question to this capability on these phrases (multi-word phrases and distinctive single words). The single most important field for retrieval quality."@en ;
    rdfs:domain ontosage:Capability ;
    rdfs:range xsd:string ;
    skos:example "\"prayer room, quiet room, where can i pray, faith room\"" ;
    skos:related hbco:layTerm .
```
{% endraw %}
