---
title: "ontosage:Record"
layout: post
permalink: /ontology/class/Record/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › Record

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Record` |
| Label | Record |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Abstract supertype for a standing record a building keeps about itself: a register row such as a fire-safety asset, a department, a workspace profile or a sustainability target. It has an owner, a status and a version rather than an interval lifecycle. Never instantiated directly.

## Class hierarchy

Superclasses: none (a root class).

Direct subclasses (22; 22 descendants in all):

- [`ontosage:AccessibleRoute`]({{ '/ontology/class/AccessibleRoute/' | relative_url }}) Accessible route
- [`ontosage:AssetEngineeringProfile`]({{ '/ontology/class/AssetEngineeringProfile/' | relative_url }}) Asset engineering profile
- [`ontosage:AVReadiness`]({{ '/ontology/class/AVReadiness/' | relative_url }}) Teaching AV readiness
- [`ontosage:CirculationTime`]({{ '/ontology/class/CirculationTime/' | relative_url }}) Circulation time
- [`ontosage:CleaningTask`]({{ '/ontology/class/CleaningTask/' | relative_url }}) Cleaning task
- [`ontosage:ContinuityProvision`]({{ '/ontology/class/ContinuityProvision/' | relative_url }}) Service continuity provision
- [`ontosage:CoordinationFunction`]({{ '/ontology/class/CoordinationFunction/' | relative_url }}) Emergency coordination function
- [`ontosage:CostLine`]({{ '/ontology/class/CostLine/' | relative_url }}) Building cost line
- [`ontosage:Department`]({{ '/ontology/class/Department/' | relative_url }}) Department
- [`ontosage:DisclosureRule`]({{ '/ontology/class/DisclosureRule/' | relative_url }}) Data disclosure rule
- [`ontosage:DoorHardware`]({{ '/ontology/class/DoorHardware/' | relative_url }}) Door and shutter hardware
- [`ontosage:EvacuationProvision`]({{ '/ontology/class/EvacuationProvision/' | relative_url }}) Evacuation provision
- [`ontosage:EventActivity`]({{ '/ontology/class/EventActivity/' | relative_url }}) Event activity
- [`ontosage:FireSafetyAsset`]({{ '/ontology/class/FireSafetyAsset/' | relative_url }}) Fire safety asset
- [`ontosage:HazardControl`]({{ '/ontology/class/HazardControl/' | relative_url }}) Hazard control
- [`ontosage:OperatingRegime`]({{ '/ontology/class/OperatingRegime/' | relative_url }}) Operating regime
- [`ontosage:PatrolCheckpoint`]({{ '/ontology/class/PatrolCheckpoint/' | relative_url }}) Patrol checkpoint
- [`ontosage:StakeholderGroup`]({{ '/ontology/class/StakeholderGroup/' | relative_url }}) Stakeholder group
- [`ontosage:StockItem`]({{ '/ontology/class/StockItem/' | relative_url }}) Stock item
- [`ontosage:SustainabilityTarget`]({{ '/ontology/class/SustainabilityTarget/' | relative_url }}) Sustainability target
- [`ontosage:WasteCollectionPoint`]({{ '/ontology/class/WasteCollectionPoint/' | relative_url }}) Waste collection point
- [`ontosage:WorkspaceProfile`]({{ '/ontology/class/WorkspaceProfile/' | relative_url }}) Workspace profile

## Properties

No property declares this class (or a superclass) as its domain.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ontosage:Record a owl:Class ;
    rdfs:label "Record"@en ;
    rdfs:comment "Abstract supertype for a standing record a building keeps about itself: a register row such as a fire-safety asset, a department, a workspace profile or a sustainability target. It has an owner, a status and a version rather than an interval lifecycle. Never instantiated directly."@en .
```
{% endraw %}
