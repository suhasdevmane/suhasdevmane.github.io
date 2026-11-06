---
title: "Record document mappings"
layout: post
permalink: /ontology/vocabulary/record-document-mappings/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Vocabularies]({{ '/docs/ontology-browser/' | relative_url }}#vocabularies) › Record document mappings

A record document is a Markdown file in a building's `documents/` folder with YAML front matter that names a `record_type`. The mapping for that record type, shipped with the ontology in [`ontology/record_documents/`](https://github.com/suhasdevmane/OntoSage/tree/main/ontology/record_documents), says which class each table row becomes and which predicate each column becomes. There are 38 mappings. See [Ontology Relationships]({{ '/docs/ontology-relationships/' | relative_url }}#records-and-record-documents) for how lifting works.

| Record type | Class | IRI template |
|---|---|---|
| [`access_permission`](#access_permission) | [`ontosage:AccessPermission`]({{ '/ontology/class/AccessPermission/' | relative_url }}) | `access/{group}` |
| [`accessible_route`](#accessible_route) | [`ontosage:AccessibleRoute`]({{ '/ontology/class/AccessibleRoute/' | relative_url }}) | `route/{route}` |
| [`approval_evidence`](#approval_evidence) | [`ontosage:ApprovalRecord`]({{ '/ontology/class/ApprovalRecord/' | relative_url }}) | `approval/{approval}` |
| [`asset_engineering`](#asset_engineering) | [`ontosage:AssetEngineeringProfile`]({{ '/ontology/class/AssetEngineeringProfile/' | relative_url }}) | `assetprofile/{code}` |
| [`av_readiness`](#av_readiness) | [`ontosage:AVReadiness`]({{ '/ontology/class/AVReadiness/' | relative_url }}) | `av/{component}` |
| [`booking`](#booking) | [`ontosage:Booking`]({{ '/ontology/class/Booking/' | relative_url }}) | `booking/{reference}` |
| [`circulation_time`](#circulation_time) | [`ontosage:CirculationTime`]({{ '/ontology/class/CirculationTime/' | relative_url }}) | `circulation/{code}` |
| [`cleaning_task`](#cleaning_task) | [`ontosage:CleaningTask`]({{ '/ontology/class/CleaningTask/' | relative_url }}) | `cleaning/{task}` |
| [`competency`](#competency) | [`ontosage:CompetencyRecord`]({{ '/ontology/class/CompetencyRecord/' | relative_url }}) | `competency/{reference}` |
| [`condition_survey`](#condition_survey) | [`ontosage:ConditionSurvey`]({{ '/ontology/class/ConditionSurvey/' | relative_url }}) | `survey/{reference}` |
| [`continuity_provision`](#continuity_provision) | [`ontosage:ContinuityProvision`]({{ '/ontology/class/ContinuityProvision/' | relative_url }}) | `continuity/{provision}` |
| [`contract`](#contract) | [`ontosage:Contract`]({{ '/ontology/class/Contract/' | relative_url }}) | `contract/{reference}` |
| [`coordination_function`](#coordination_function) | [`ontosage:CoordinationFunction`]({{ '/ontology/class/CoordinationFunction/' | relative_url }}) | `coordination/{function}` |
| [`cost_line`](#cost_line) | [`ontosage:CostLine`]({{ '/ontology/class/CostLine/' | relative_url }}) | `cost/{line}` |
| [`department`](#department) | [`ontosage:Department`]({{ '/ontology/class/Department/' | relative_url }}) | `dept/{code}` |
| [`door_hardware`](#door_hardware) | [`ontosage:DoorHardware`]({{ '/ontology/class/DoorHardware/' | relative_url }}) | `opening/{opening}` |
| [`evacuation_provision`](#evacuation_provision) | [`ontosage:EvacuationProvision`]({{ '/ontology/class/EvacuationProvision/' | relative_url }}) | `evac/{code}` |
| [`event_activity`](#event_activity) | [`ontosage:EventActivity`]({{ '/ontology/class/EventActivity/' | relative_url }}) | `activity/{activity}` |
| [`fire_safety_asset`](#fire_safety_asset) | [`ontosage:FireSafetyAsset`]({{ '/ontology/class/FireSafetyAsset/' | relative_url }}) | `fireasset/{code}` |
| [`handover`](#handover) | [`ontosage:HandoverRecord`]({{ '/ontology/class/HandoverRecord/' | relative_url }}) | `handover/{reference}` |
| [`hazard_control`](#hazard_control) | [`ontosage:HazardControl`]({{ '/ontology/class/HazardControl/' | relative_url }}) | `hazard/{code}` |
| [`incident_record`](#incident_record) | [`ontosage:IncidentRecord`]({{ '/ontology/class/IncidentRecord/' | relative_url }}) | `incident/{ref}` |
| [`operating_regime`](#operating_regime) | [`ontosage:OperatingRegime`]({{ '/ontology/class/OperatingRegime/' | relative_url }}) | `regime/{code}` |
| [`patrol_checkpoint`](#patrol_checkpoint) | [`ontosage:PatrolCheckpoint`]({{ '/ontology/class/PatrolCheckpoint/' | relative_url }}) | `patrol/{checkpoint}` |
| [`permit_to_work`](#permit_to_work) | [`ontosage:Permit`]({{ '/ontology/class/Permit/' | relative_url }}) | `permit/{permit}` |
| [`public_event`](#public_event) | [`ontosage:PublicEvent`]({{ '/ontology/class/PublicEvent/' | relative_url }}) | `event/{event}` |
| [`risk_assessment`](#risk_assessment) | [`ontosage:RiskAssessment`]({{ '/ontology/class/RiskAssessment/' | relative_url }}) | `risk/{reference}` |
| [`service_schedule`](#service_schedule) | [`ontosage:ServiceSchedule`]({{ '/ontology/class/ServiceSchedule/' | relative_url }}) | `service/{code}` |
| [`stakeholder_group`](#stakeholder_group) | [`ontosage:StakeholderGroup`]({{ '/ontology/class/StakeholderGroup/' | relative_url }}) | `stakeholder/{code}` |
| [`stock_item`](#stock_item) | [`ontosage:StockItem`]({{ '/ontology/class/StockItem/' | relative_url }}) | `stock/{code}` |
| [`sustainability_target`](#sustainability_target) | [`ontosage:SustainabilityTarget`]({{ '/ontology/class/SustainabilityTarget/' | relative_url }}) | `target/{reference}` |
| [`tariff`](#tariff) | [`ontosage:Tariff`]({{ '/ontology/class/Tariff/' | relative_url }}) | `tariff/{reference}` |
| [`timetabled_session`](#timetabled_session) | [`ontosage:TimetabledSession`]({{ '/ontology/class/TimetabledSession/' | relative_url }}) | `session/{code}` |
| [`warranty`](#warranty) | [`ontosage:Warranty`]({{ '/ontology/class/Warranty/' | relative_url }}) | `warranty/{reference}` |
| [`waste_collection`](#waste_collection) | [`ontosage:WasteCollectionPoint`]({{ '/ontology/class/WasteCollectionPoint/' | relative_url }}) | `waste/{point}` |
| [`waste_return`](#waste_return) | [`ontosage:WasteReturn`]({{ '/ontology/class/WasteReturn/' | relative_url }}) | `waste_return/{code}` |
| [`work_order`](#work_order) | [`ontosage:WorkOrder`]({{ '/ontology/class/WorkOrder/' | relative_url }}) | `workorder/{ref}` |
| [`workspace_profile`](#workspace_profile) | [`ontosage:WorkspaceProfile`]({{ '/ontology/class/WorkspaceProfile/' | relative_url }}) | `workspace/{code}` |

## access\_permission {#access_permission}

Class [`ontosage:AccessPermission`]({{ '/ontology/class/AccessPermission/' | relative_url }}); IRI template `access/{group}`; label column `group`. Mapping file: [`ontology/record_documents/access_permission.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/access_permission.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `group` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `name` | `rdfs:label` | `xsd:string` | yes |  |  |
| `opening` | [`ontosage:controlsOpening`]({{ '/ontology/property/controlsOpening/' | relative_url }}) | `xsd:string` | yes |  |  |
| `role_template` | [`ontosage:grantedToRole`]({{ '/ontology/property/grantedToRole/' | relative_url }}) | `xsd:string` | yes |  |  |
| `inherits_from` | [`ontosage:inheritsFrom`]({{ '/ontology/property/inheritsFrom/' | relative_url }}) | `xsd:string` |  |  |  |
| `time_profile` | [`ontosage:timeProfile`]({{ '/ontology/property/timeProfile/' | relative_url }}) | `xsd:string` | yes |  |  |
| `override` | [`ontosage:overriddenBy`]({{ '/ontology/property/overriddenBy/' | relative_url }}) | `xsd:string` |  |  |  |
| `approval_route` | [`ontosage:approvalRoute`]({{ '/ontology/property/approvalRoute/' | relative_url }}) | `xsd:string` |  |  |  |
| `valid_from` | [`ontosage:effectiveFrom`]({{ '/ontology/property/effectiveFrom/' | relative_url }}) | `xsd:date` |  |  |  |
| `valid_to` | [`ontosage:effectiveTo`]({{ '/ontology/property/effectiveTo/' | relative_url }}) | `xsd:date` |  |  |  |
| `status` | [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | `xsd:string` | yes |  | active: Active, In force, Enabled; suspended: Suspended, Disabled, On hold; exception: Exception, One-off, Temporary grant; withdrawn: Withdrawn, Revoked, Expired |
| `owner` | [`ontosage:recordOwner`]({{ '/ontology/property/recordOwner/' | relative_url }}) | `xsd:string` |  |  |  |
| `note` | `rdfs:comment` | `xsd:string` |  |  |  |

## accessible\_route {#accessible_route}

Class [`ontosage:AccessibleRoute`]({{ '/ontology/class/AccessibleRoute/' | relative_url }}); IRI template `route/{route}`; label column `name`. Mapping file: [`ontology/record_documents/accessible_route.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/accessible_route.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `route` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `name` | `rdfs:label` | `xsd:string` | yes |  |  |
| `from_point` | [`ontosage:routeFrom`]({{ '/ontology/property/routeFrom/' | relative_url }}) | `xsd:string` | yes | `route_from` |  |
| `to_point` | [`ontosage:routeTo`]({{ '/ontology/property/routeTo/' | relative_url }}) | `xsd:string` | yes | `route_to` |  |
| `entrance` | [`ontosage:visitorEntrance`]({{ '/ontology/property/visitorEntrance/' | relative_url }}) | `xsd:string` | yes |  |  |
| `step_free` | [`ontosage:isStepFree`]({{ '/ontology/property/isStepFree/' | relative_url }}) | `xsd:boolean` | yes |  |  |
| `seated_rests` | [`ontosage:seatedRests`]({{ '/ontology/property/seatedRests/' | relative_url }}) | `xsd:integer` |  |  |  |
| `door_type` | [`ontosage:doorOperation`]({{ '/ontology/property/doorOperation/' | relative_url }}) | `xsd:string` | yes |  | automatic: Automatic, Powered, Auto; assisted: Assisted, Push pad, Power assisted; manual: Manual, Manual heavy, Manual light |
| `lift` | [`ontosage:servedByLift`]({{ '/ontology/property/servedByLift/' | relative_url }}) | `xsd:string` |  |  |  |
| `lift_status` | [`ontosage:liftStatus`]({{ '/ontology/property/liftStatus/' | relative_url }}) | `xsd:string` |  |  | in\_service: In service, Available, Operational; out\_of\_service: Out of service, Faulty, Under repair |
| `distance_m` | [`ontosage:routeDistanceMetres`]({{ '/ontology/property/routeDistanceMetres/' | relative_url }}) | `xsd:integer` |  |  |  |
| `allow_minutes` | [`ontosage:allowMinutes`]({{ '/ontology/property/allowMinutes/' | relative_url }}) | `xsd:integer` |  |  |  |
| `sensory` | [`ontosage:sensoryLevel`]({{ '/ontology/property/sensoryLevel/' | relative_url }}) | `xsd:string` |  |  | quiet: Quiet, Low stimulation, Calm; moderate: Moderate, Typical; busy: Busy, High footfall, Noisy |
| `assistance_contact` | [`ontosage:assistanceContact`]({{ '/ontology/property/assistanceContact/' | relative_url }}) | `xsd:string` |  |  |  |
| `surveyed_on` | [`ontosage:surveyedOn`]({{ '/ontology/property/surveyedOn/' | relative_url }}) | `xsd:date` | yes |  |  |
| `surveyed_by` | [`ontosage:surveyedBy`]({{ '/ontology/property/surveyedBy/' | relative_url }}) | `xsd:string` | yes |  |  |
| `status` | [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | `xsd:string` | yes |  | open: Open, Available, In use; restricted: Restricted, Partly available; closed: Closed, Unavailable, Blocked |
| `note` | `rdfs:comment` | `xsd:string` |  |  |  |

## approval\_evidence {#approval_evidence}

Class [`ontosage:ApprovalRecord`]({{ '/ontology/class/ApprovalRecord/' | relative_url }}); IRI template `approval/{approval}`; label column `subject`. Mapping file: [`ontology/record_documents/approval_evidence.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/approval_evidence.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `approval` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `subject` | `rdfs:label` | `xsd:string` | yes |  |  |
| `subject_kind` | [`ontosage:approvalSubjectKind`]({{ '/ontology/property/approvalSubjectKind/' | relative_url }}) | `xsd:string` | yes |  |  |
| `decision` | [`ontosage:approvalDecision`]({{ '/ontology/property/approvalDecision/' | relative_url }}) | `xsd:string` | yes |  | approved: Approved, Granted, Accepted; conditional: Conditional, Approved with conditions, Provisional; refused: Refused, Rejected, Declined; withdrawn: Withdrawn, Revoked, Lapsed; pending: Pending, Awaiting decision, Submitted |
| `approved_by_role` | [`ontosage:approvedByRole`]({{ '/ontology/property/approvedByRole/' | relative_url }}) | `xsd:string` | yes |  |  |
| `authority` | [`ontosage:owningAuthority`]({{ '/ontology/property/owningAuthority/' | relative_url }}) | `xsd:string` | yes |  |  |
| `approved_on` | [`ontosage:approvedOn`]({{ '/ontology/property/approvedOn/' | relative_url }}) | `xsd:date` |  |  |  |
| `valid_until` | [`ontosage:effectiveTo`]({{ '/ontology/property/effectiveTo/' | relative_url }}) | `xsd:date` |  |  |  |
| `reference` | [`ontosage:approvalReference`]({{ '/ontology/property/approvalReference/' | relative_url }}) | `xsd:string` |  |  |  |
| `evidence_type` | [`ontosage:evidenceKind`]({{ '/ontology/property/evidenceKind/' | relative_url }}) | `xsd:string` |  |  |  |
| `evidence_ref` | [`ontosage:evidenceReference`]({{ '/ontology/property/evidenceReference/' | relative_url }}) | `xsd:string` |  |  |  |
| `evidence_date` | [`ontosage:evidenceDate`]({{ '/ontology/property/evidenceDate/' | relative_url }}) | `xsd:date` |  |  |  |
| `accountable_role` | [`ontosage:accountableRole`]({{ '/ontology/property/accountableRole/' | relative_url }}) | `xsd:string` | yes |  |  |
| `review_due` | [`ontosage:reviewDue`]({{ '/ontology/property/reviewDue/' | relative_url }}) | `xsd:date` |  |  |  |
| `conditions` | [`ontosage:approvalConditions`]({{ '/ontology/property/approvalConditions/' | relative_url }}) | `xsd:string` |  |  |  |
| `status` | [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | `xsd:string` | yes |  | current: Current, In force, Live; due\_review: Due review, Review due, Expiring; expired: Expired, Out of date, Lapsed; no\_evidence: No evidence, Unevidenced, Evidence missing |

## asset\_engineering {#asset_engineering}

Class [`ontosage:AssetEngineeringProfile`]({{ '/ontology/class/AssetEngineeringProfile/' | relative_url }}); IRI template `assetprofile/{code}`; label column `name`. Mapping file: [`ontology/record_documents/asset_engineering.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/asset_engineering.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `code` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `name` | `rdfs:label` | `xsd:string` | yes |  |  |
| `location` | [`ontosage:locationText`]({{ '/ontology/property/locationText/' | relative_url }}) | `xsd:string` | yes | `located_in` |  |
| `floor` | [`ontosage:onFloor`]({{ '/ontology/property/onFloor/' | relative_url }}) | `xsd:string` |  | `on_floor` |  |
| `design_duty` | [`ontosage:designDuty`]({{ '/ontology/property/designDuty/' | relative_url }}) | `xsd:string` | yes |  |  |
| `commissioned_duty` | [`ontosage:commissionedDuty`]({{ '/ontology/property/commissionedDuty/' | relative_url }}) | `xsd:string` |  |  |  |
| `observed_duty` | [`ontosage:observedDuty`]({{ '/ontology/property/observedDuty/' | relative_url }}) | `xsd:string` |  |  |  |
| `duty_evidence` | [`ontosage:dutyEvidence`]({{ '/ontology/property/dutyEvidence/' | relative_url }}) | `xsd:string` |  |  |  |
| `isolation_point` | [`ontosage:isolationPoint`]({{ '/ontology/property/isolationPoint/' | relative_url }}) | `xsd:string` | yes |  |  |
| `isolation_proven_on` | [`ontosage:isolationProvenOn`]({{ '/ontology/property/isolationProvenOn/' | relative_url }}) | `xsd:date` |  |  |  |
| `downstream` | [`ontosage:downstreamDependencies`]({{ '/ontology/property/downstreamDependencies/' | relative_url }}) | `xsd:string` | yes |  |  |
| `tag_drawings` | [`ontosage:tagOnDrawings`]({{ '/ontology/property/tagOnDrawings/' | relative_url }}) | `xsd:string` |  |  |  |
| `tag_bms` | [`ontosage:tagInBMS`]({{ '/ontology/property/tagInBMS/' | relative_url }}) | `xsd:string` |  |  |  |
| `tag_maintenance` | [`ontosage:tagInMaintenance`]({{ '/ontology/property/tagInMaintenance/' | relative_url }}) | `xsd:string` |  |  |  |
| `parent_asset` | [`ontosage:parentAsset`]({{ '/ontology/property/parentAsset/' | relative_url }}) | `xsd:string` |  |  |  |
| `engineering_system` | [`ontosage:engineeringSystem`]({{ '/ontology/property/engineeringSystem/' | relative_url }}) | `xsd:string` | yes |  |  |
| `serves_area` | [`ontosage:servesArea`]({{ '/ontology/property/servesArea/' | relative_url }}) | `xsd:string` | yes | `serves` |  |
| `location_verified_on` | [`ontosage:locationVerifiedOn`]({{ '/ontology/property/locationVerifiedOn/' | relative_url }}) | `xsd:date` |  |  |  |
| `criticality` | [`ontosage:criticality`]({{ '/ontology/property/criticality/' | relative_url }}) | `xsd:string` | yes |  |  |
| `replaceability` | [`ontosage:replaceability`]({{ '/ontology/property/replaceability/' | relative_url }}) | `xsd:string` | yes |  |  |
| `value_band` | [`ontosage:valueBand`]({{ '/ontology/property/valueBand/' | relative_url }}) | `xsd:string` |  |  |  |
| `last_visited` | [`ontosage:lastVisited`]({{ '/ontology/property/lastVisited/' | relative_url }}) | `xsd:date` |  |  |  |
| `inspection_interval_days` | [`ontosage:inspectionIntervalDays`]({{ '/ontology/property/inspectionIntervalDays/' | relative_url }}) | `xsd:integer` | yes |  |  |
| `services_in_void` | [`ontosage:servicesInVoid`]({{ '/ontology/property/servicesInVoid/' | relative_url }}) | `xsd:string` |  |  |  |
| `status` | [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | `xsd:string` | yes |  | active: Active, In service; degraded: Degraded, Running with defect; out\_of\_service: Out of service, Isolated |
| `note` | `rdfs:comment` | `xsd:string` |  |  |  |

## av\_readiness {#av_readiness}

Class [`ontosage:AVReadiness`]({{ '/ontology/class/AVReadiness/' | relative_url }}); IRI template `av/{component}`; label column `name`. Mapping file: [`ontology/record_documents/av_readiness.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/av_readiness.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `component` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `name` | `rdfs:label` | `xsd:string` | yes |  |  |
| `room` | [`ontosage:locationText`]({{ '/ontology/property/locationText/' | relative_url }}) | `xsd:string` | yes | `located_in` |  |
| `kind` | [`ontosage:avComponentKind`]({{ '/ontology/property/avComponentKind/' | relative_url }}) | `xsd:string` | yes |  |  |
| `audio_path` | [`ontosage:inAudioPath`]({{ '/ontology/property/inAudioPath/' | relative_url }}) | `xsd:boolean` | yes |  |  |
| `supports_format` | [`ontosage:supportsFormat`]({{ '/ontology/property/supportsFormat/' | relative_url }}) | `xsd:string` |  |  |  |
| `last_checked` | [`ontosage:lastCompleted`]({{ '/ontology/property/lastCompleted/' | relative_url }}) | `xsd:date` |  |  |  |
| `evidence_ref` | [`ontosage:evidenceReference`]({{ '/ontology/property/evidenceReference/' | relative_url }}) | `xsd:string` |  |  |  |
| `next_due` | [`ontosage:nextDue`]({{ '/ontology/property/nextDue/' | relative_url }}) | `xsd:date` |  |  |  |
| `state` | [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | `xsd:string` | yes |  | ready: Ready, In service, Working; degraded: Degraded, Partial, Reduced; failed: Failed, Out of service, Dead; unevidenced: Unevidenced, Not checked, Evidence missing |
| `owner` | [`ontosage:recordOwner`]({{ '/ontology/property/recordOwner/' | relative_url }}) | `xsd:string` |  |  |  |
| `note` | `rdfs:comment` | `xsd:string` |  |  |  |

## booking {#booking}

Class [`ontosage:Booking`]({{ '/ontology/class/Booking/' | relative_url }}); IRI template `booking/{reference}`; label column `reference`. Mapping file: [`ontology/record_documents/booking.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/booking.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `reference` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `room` | [`ontosage:locationText`]({{ '/ontology/property/locationText/' | relative_url }}) | `xsd:string` | yes | `located_in` |  |
| `start` | [`ontosage:effectiveFrom`]({{ '/ontology/property/effectiveFrom/' | relative_url }}) | `xsd:dateTime` | yes |  |  |
| `end` | [`ontosage:effectiveTo`]({{ '/ontology/property/effectiveTo/' | relative_url }}) | `xsd:dateTime` | yes |  |  |
| `booked_by_role` | [`ontosage:bookedByRole`]({{ '/ontology/property/bookedByRole/' | relative_url }}) | `xsd:string` | yes |  |  |
| `expected_attendees` | [`ontosage:expectedAttendees`]({{ '/ontology/property/expectedAttendees/' | relative_url }}) | `xsd:integer` |  |  |  |
| `status` | [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | `xsd:string` | yes |  | confirmed: Confirmed, Booked, Approved; provisional: Provisional, Tentative, Held; cancelled: Cancelled, Withdrawn |

## circulation\_time {#circulation_time}

Class [`ontosage:CirculationTime`]({{ '/ontology/class/CirculationTime/' | relative_url }}); IRI template `circulation/{code}`; label column `route`. Mapping file: [`ontology/record_documents/circulation_time.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/circulation_time.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `code` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `route` | `rdfs:label` | `xsd:string` | yes |  |  |
| `from_floor` | [`ontosage:fromFloor`]({{ '/ontology/property/fromFloor/' | relative_url }}) | `xsd:string` | yes |  |  |
| `to_floor` | [`ontosage:toFloor`]({{ '/ontology/property/toFloor/' | relative_url }}) | `xsd:string` | yes |  |  |
| `walking_minutes` | [`ontosage:walkingMinutes`]({{ '/ontology/property/walkingMinutes/' | relative_url }}) | `xsd:decimal` | yes |  |  |
| `step_free_minutes` | [`ontosage:stepFreeMinutes`]({{ '/ontology/property/stepFreeMinutes/' | relative_url }}) | `xsd:decimal` | yes |  |  |
| `depends_on_lift` | [`ontosage:dependsOnLift`]({{ '/ontology/property/dependsOnLift/' | relative_url }}) | `xsd:boolean` | yes |  |  |
| `vertical_route` | [`ontosage:nearestVerticalRoute`]({{ '/ontology/property/nearestVerticalRoute/' | relative_url }}) | `xsd:string` |  |  |  |
| `status` | [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | `xsd:string` | yes |  | active: Active; degraded: Degraded |
| `note` | `rdfs:comment` | `xsd:string` |  |  |  |

## cleaning\_task {#cleaning_task}

Class [`ontosage:CleaningTask`]({{ '/ontology/class/CleaningTask/' | relative_url }}); IRI template `cleaning/{task}`; label column `task`. Mapping file: [`ontology/record_documents/cleaning_task.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/cleaning_task.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `task` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `zone` | [`ontosage:cleaningZone`]({{ '/ontology/property/cleaningZone/' | relative_url }}) | `xsd:string` | yes |  |  |
| `area` | [`ontosage:locationText`]({{ '/ontology/property/locationText/' | relative_url }}) | `xsd:string` | yes | `located_in` |  |
| `standard` | [`ontosage:cleaningStandard`]({{ '/ontology/property/cleaningStandard/' | relative_url }}) | `xsd:string` | yes |  |  |
| `frequency` | [`ontosage:serviceFrequency`]({{ '/ontology/property/serviceFrequency/' | relative_url }}) | `xsd:string` | yes |  |  |
| `shift` | [`ontosage:shiftName`]({{ '/ontology/property/shiftName/' | relative_url }}) | `xsd:string` | yes |  |  |
| `ready_by` | [`ontosage:readyBy`]({{ '/ontology/property/readyBy/' | relative_url }}) | `xsd:string` |  |  |  |
| `minutes` | [`ontosage:expectedMinutes`]({{ '/ontology/property/expectedMinutes/' | relative_url }}) | `xsd:integer` |  |  |  |
| `last_done` | [`ontosage:lastCompleted`]({{ '/ontology/property/lastCompleted/' | relative_url }}) | `xsd:date` |  |  |  |
| `next_due` | [`ontosage:nextDue`]({{ '/ontology/property/nextDue/' | relative_url }}) | `xsd:date` |  |  |  |
| `status` | [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | `xsd:string` | yes |  | scheduled: Scheduled, Planned, Routine; added: Added, Extra, Additional; handed\_over: Handed over, Handover, Passed on; suspended: Suspended, Closed, Restricted, Reassigned; done: Done, Completed, Signed off |
| `owner` | [`ontosage:recordOwner`]({{ '/ontology/property/recordOwner/' | relative_url }}) | `xsd:string` |  |  |  |
| `note` | `rdfs:comment` | `xsd:string` |  |  |  |

## competency {#competency}

Class [`ontosage:CompetencyRecord`]({{ '/ontology/class/CompetencyRecord/' | relative_url }}); IRI template `competency/{reference}`; label column `reference`. Mapping file: [`ontology/record_documents/competency.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/competency.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `reference` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `area` | [`ontosage:locationText`]({{ '/ontology/property/locationText/' | relative_url }}) | `xsd:string` | yes | `located_in` |  |
| `requirement` | [`ontosage:coveredScope`]({{ '/ontology/property/coveredScope/' | relative_url }}) | `xsd:string` | yes |  |  |
| `applies_to_role` | [`ontosage:appliesToRole`]({{ '/ontology/property/appliesToRole/' | relative_url }}) | `xsd:string` | yes |  |  |
| `valid_for_months` | [`ontosage:note`]({{ '/ontology/property/note/' | relative_url }}) | `xsd:string` |  |  |  |
| `authority` | [`ontosage:providerName`]({{ '/ontology/property/providerName/' | relative_url }}) | `xsd:string` |  |  |  |
| `effective_from` | [`ontosage:effectiveFrom`]({{ '/ontology/property/effectiveFrom/' | relative_url }}) | `xsd:date` | yes |  |  |

## condition\_survey {#condition_survey}

Class [`ontosage:ConditionSurvey`]({{ '/ontology/class/ConditionSurvey/' | relative_url }}); IRI template `survey/{reference}`; label column `reference`. Mapping file: [`ontology/record_documents/condition_survey.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/condition_survey.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `reference` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `asset` | [`ontosage:coveredScope`]({{ '/ontology/property/coveredScope/' | relative_url }}) | `xsd:string` | yes |  |  |
| `surveyed` | [`ontosage:effectiveFrom`]({{ '/ontology/property/effectiveFrom/' | relative_url }}) | `xsd:date` | yes |  |  |
| `grade` | [`ontosage:conditionGrade`]({{ '/ontology/property/conditionGrade/' | relative_url }}) | `xsd:string` | yes |  | A: A, A , Good, As new; B: B, Satisfactory, Fair; C: C, Poor; D: D, End of life, Life expired |
| `remaining_life_years` | [`ontosage:remainingLifeYears`]({{ '/ontology/property/remainingLifeYears/' | relative_url }}) | `xsd:decimal` | yes |  |  |
| `surveyor` | [`ontosage:providerName`]({{ '/ontology/property/providerName/' | relative_url }}) | `xsd:string` |  |  |  |
| `note` | [`ontosage:note`]({{ '/ontology/property/note/' | relative_url }}) | `xsd:string` |  |  |  |

## continuity\_provision {#continuity_provision}

Class [`ontosage:ContinuityProvision`]({{ '/ontology/class/ContinuityProvision/' | relative_url }}); IRI template `continuity/{provision}`; label column `service`. Mapping file: [`ontology/record_documents/continuity_provision.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/continuity_provision.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `provision` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `service` | [`ontosage:servesService`]({{ '/ontology/property/servesService/' | relative_url }}) | `xsd:string` | yes |  |  |
| `depends_on` | [`ontosage:dependsOnSpace`]({{ '/ontology/property/dependsOnSpace/' | relative_url }}) | `xsd:string` | yes |  |  |
| `criticality` | [`ontosage:criticality`]({{ '/ontology/property/criticality/' | relative_url }}) | `xsd:string` |  |  |  |
| `alternative_location` | [`ontosage:alternativeLocation`]({{ '/ontology/property/alternativeLocation/' | relative_url }}) | `xsd:string` | yes |  |  |
| `alternative_path` | [`ontosage:alternativePath`]({{ '/ontology/property/alternativePath/' | relative_url }}) | `xsd:string` |  |  |  |
| `alternative_capacity` | [`ontosage:alternativeCapacity`]({{ '/ontology/property/alternativeCapacity/' | relative_url }}) | `xsd:string` |  |  |  |
| `ride_through_minutes` | [`ontosage:rideThroughMinutes`]({{ '/ontology/property/rideThroughMinutes/' | relative_url }}) | `xsd:integer` |  |  |  |
| `last_proved_on` | [`ontosage:lastProvedOn`]({{ '/ontology/property/lastProvedOn/' | relative_url }}) | `xsd:date` |  |  |  |
| `next_due` | [`ontosage:nextTestDue`]({{ '/ontology/property/nextTestDue/' | relative_url }}) | `xsd:date` |  |  |  |
| `evidence_ref` | [`ontosage:evidenceReference`]({{ '/ontology/property/evidenceReference/' | relative_url }}) | `xsd:string` |  |  |  |
| `status` | [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | `xsd:string` | yes |  | verified: Verified, Proved, Tested; unverified: Unverified, Untested, Planned, Claimed; none: None, No alternative, None identified; overdue: Overdue, Proof overdue |
| `owner` | [`ontosage:recordOwner`]({{ '/ontology/property/recordOwner/' | relative_url }}) | `xsd:string` |  |  |  |
| `note` | `rdfs:comment` | `xsd:string` |  |  |  |

## contract {#contract}

Class [`ontosage:Contract`]({{ '/ontology/class/Contract/' | relative_url }}); IRI template `contract/{reference}`; label column `reference`. Mapping file: [`ontology/record_documents/contract.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/contract.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `reference` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `scope` | [`ontosage:coveredScope`]({{ '/ontology/property/coveredScope/' | relative_url }}) | `xsd:string` | yes |  |  |
| `provider` | [`ontosage:providerName`]({{ '/ontology/property/providerName/' | relative_url }}) | `xsd:string` | yes |  |  |
| `start` | [`ontosage:effectiveFrom`]({{ '/ontology/property/effectiveFrom/' | relative_url }}) | `xsd:date` | yes |  |  |
| `end` | [`ontosage:effectiveTo`]({{ '/ontology/property/effectiveTo/' | relative_url }}) | `xsd:date` | yes |  |  |
| `status` | [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | `xsd:string` | yes |  | active: Active, Live, In force, Current; expired: Expired, Ended, Lapsed; notice: Notice served, Under notice, Terminating |
| `owner_role` | [`ontosage:responsibleRole`]({{ '/ontology/property/responsibleRole/' | relative_url }}) | `xsd:string` |  |  |  |

## coordination\_function {#coordination_function}

Class [`ontosage:CoordinationFunction`]({{ '/ontology/class/CoordinationFunction/' | relative_url }}); IRI template `coordination/{function}`; label column `name`. Mapping file: [`ontology/record_documents/coordination_function.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/coordination_function.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `function` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `name` | `rdfs:label` | `xsd:string` | yes |  |  |
| `accountable_role` | [`ontosage:accountableRole`]({{ '/ontology/property/accountableRole/' | relative_url }}) | `xsd:string` | yes |  |  |
| `operational_period` | [`ontosage:operationalPeriod`]({{ '/ontology/property/operationalPeriod/' | relative_url }}) | `xsd:string` | yes |  |  |
| `primary_system` | [`ontosage:primarySystem`]({{ '/ontology/property/primarySystem/' | relative_url }}) | `xsd:string` | yes |  |  |
| `system_state` | [`ontosage:systemState`]({{ '/ontology/property/systemState/' | relative_url }}) | `xsd:string` | yes |  | ready: Ready, Available, Operational; degraded: Degraded, Partial, Intermittent; unavailable: Unavailable, Down, Out of service |
| `fallback` | [`ontosage:approvedFallback`]({{ '/ontology/property/approvedFallback/' | relative_url }}) | `xsd:string` |  |  |  |
| `activation_criterion` | [`ontosage:activationCriterion`]({{ '/ontology/property/activationCriterion/' | relative_url }}) | `xsd:string` | yes |  |  |
| `criterion_state` | [`ontosage:criterionState`]({{ '/ontology/property/criterionState/' | relative_url }}) | `xsd:string` | yes |  | met: Met, Satisfied, Triggered; not\_met: Not met, Below threshold; conflicting: Conflicting, Sources disagree; unknown: Unknown, Not established, Unverified |
| `evidence_ref` | [`ontosage:evidenceReference`]({{ '/ontology/property/evidenceReference/' | relative_url }}) | `xsd:string` |  |  |  |
| `decision_needed` | [`ontosage:decisionRequired`]({{ '/ontology/property/decisionRequired/' | relative_url }}) | `xsd:boolean` | yes |  |  |
| `status` | [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | `xsd:string` | yes |  | confirmed: Confirmed, Staffed, In place; provisional: Provisional, Pending confirmation; unfilled: Unfilled, No assignment |
| `note` | `rdfs:comment` | `xsd:string` |  |  |  |

## cost\_line {#cost_line}

Class [`ontosage:CostLine`]({{ '/ontology/class/CostLine/' | relative_url }}); IRI template `cost/{line}`; label column `description`. Mapping file: [`ontology/record_documents/cost_line.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/cost_line.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `line` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `description` | `rdfs:label` | `xsd:string` | yes |  |  |
| `cost_centre` | [`ontosage:costCentre`]({{ '/ontology/property/costCentre/' | relative_url }}) | `xsd:string` | yes |  |  |
| `category` | [`ontosage:spendCategory`]({{ '/ontology/property/spendCategory/' | relative_url }}) | `xsd:string` | yes |  | planned: Planned, Programmed, Cyclical; reactive: Reactive, Responsive, Breakdown; statutory: Statutory, Compliance, Mandatory; contract\_fixed: Contract-fixed, Contract fixed, Fixed contract; demand\_led: Demand-led, Demand led, Variable |
| `period` | [`ontosage:financialPeriod`]({{ '/ontology/property/financialPeriod/' | relative_url }}) | `xsd:string` | yes |  |  |
| `budget` | [`ontosage:budgetAmount`]({{ '/ontology/property/budgetAmount/' | relative_url }}) | `xsd:decimal` | yes |  |  |
| `actual` | [`ontosage:actualAmount`]({{ '/ontology/property/actualAmount/' | relative_url }}) | `xsd:decimal` | yes |  |  |
| `committed` | [`ontosage:committedAmount`]({{ '/ontology/property/committedAmount/' | relative_url }}) | `xsd:decimal` |  |  |  |
| `accrued` | [`ontosage:accruedAmount`]({{ '/ontology/property/accruedAmount/' | relative_url }}) | `xsd:decimal` |  |  |  |
| `variance_cause` | [`ontosage:varianceCause`]({{ '/ontology/property/varianceCause/' | relative_url }}) | `xsd:string` |  |  |  |
| `supplier` | [`ontosage:providerName`]({{ '/ontology/property/providerName/' | relative_url }}) | `xsd:string` |  |  |  |
| `coding_check` | [`ontosage:codingCheckRequired`]({{ '/ontology/property/codingCheckRequired/' | relative_url }}) | `xsd:boolean` |  |  |  |
| `status` | [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | `xsd:string` | yes |  | open: Open, In year, Active; closed: Closed, Settled; query: Query, Under review, Disputed |
| `owner` | [`ontosage:recordOwner`]({{ '/ontology/property/recordOwner/' | relative_url }}) | `xsd:string` |  |  |  |

## department {#department}

Class [`ontosage:Department`]({{ '/ontology/class/Department/' | relative_url }}); IRI template `dept/{code}`; label column `name`. Mapping file: [`ontology/record_documents/department.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/department.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `code` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `name` | `rdfs:label` | `xsd:string` | yes |  |  |
| `function` | [`ontosage:departmentFunction`]({{ '/ontology/property/departmentFunction/' | relative_url }}) | `xsd:string` | yes |  |  |
| `scope` | [`ontosage:serviceScope`]({{ '/ontology/property/serviceScope/' | relative_url }}) | `xsd:string` | yes |  |  |
| `based_at` | [`ontosage:locationText`]({{ '/ontology/property/locationText/' | relative_url }}) | `xsd:string` |  | `located_in` |  |
| `coverage_hours` | [`ontosage:openingHours`]({{ '/ontology/property/openingHours/' | relative_url }}) | `xsd:string` | yes |  |  |
| `request_channel` | [`ontosage:requestChannel`]({{ '/ontology/property/requestChannel/' | relative_url }}) | `xsd:string` | yes |  |  |
| `out_of_hours` | [`ontosage:outOfHoursRoute`]({{ '/ontology/property/outOfHoursRoute/' | relative_url }}) | `xsd:string` |  |  |  |
| `responds_within_hours` | [`ontosage:respondsWithinHours`]({{ '/ontology/property/respondsWithinHours/' | relative_url }}) | `xsd:decimal` | yes |  |  |
| `escalates_to` | [`ontosage:escalatesTo`]({{ '/ontology/property/escalatesTo/' | relative_url }}) | `xsd:string` | yes |  |  |
| `accountable_role` | [`ontosage:accountableRole`]({{ '/ontology/property/accountableRole/' | relative_url }}) | `xsd:string` | yes |  |  |
| `contact_email` | [`ontosage:contactEmail`]({{ '/ontology/property/contactEmail/' | relative_url }}) | `xsd:string` |  |  |  |
| `contact_phone` | [`ontosage:contactPhone`]({{ '/ontology/property/contactPhone/' | relative_url }}) | `xsd:string` |  |  |  |
| `status` | [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | `xsd:string` | yes |  | active: Active, In service; reduced: Reduced, Reduced cover, Partial; suspended: Suspended, Withdrawn |
| `note` | `rdfs:comment` | `xsd:string` |  |  |  |

## door\_hardware {#door_hardware}

Class [`ontosage:DoorHardware`]({{ '/ontology/class/DoorHardware/' | relative_url }}); IRI template `opening/{opening}`; label column `name`. Mapping file: [`ontology/record_documents/door_hardware.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/door_hardware.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `opening` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `name` | `rdfs:label` | `xsd:string` | yes |  |  |
| `kind` | [`ontosage:openingKind`]({{ '/ontology/property/openingKind/' | relative_url }}) | `xsd:string` | yes |  |  |
| `location` | [`ontosage:locationText`]({{ '/ontology/property/locationText/' | relative_url }}) | `xsd:string` | yes | `located_in` |  |
| `floor` | [`ontosage:onFloor`]({{ '/ontology/property/onFloor/' | relative_url }}) | `xsd:string` |  | `on_floor` |  |
| `power_loss_state` | [`ontosage:failStateOnPowerLoss`]({{ '/ontology/property/failStateOnPowerLoss/' | relative_url }}) | `xsd:string` | yes |  |  |
| `hold_open` | [`ontosage:holdOpenDevice`]({{ '/ontology/property/holdOpenDevice/' | relative_url }}) | `xsd:string` |  |  |  |
| `release` | [`ontosage:releaseMechanism`]({{ '/ontology/property/releaseMechanism/' | relative_url }}) | `xsd:string` |  |  |  |
| `commanded_by` | [`ontosage:commandedBySystem`]({{ '/ontology/property/commandedBySystem/' | relative_url }}) | `xsd:string` |  |  |  |
| `last_tested` | [`ontosage:lastTestedOn`]({{ '/ontology/property/lastTestedOn/' | relative_url }}) | `xsd:date` |  |  |  |
| `next_due` | [`ontosage:nextTestDue`]({{ '/ontology/property/nextTestDue/' | relative_url }}) | `xsd:date` |  |  |  |
| `evidence_ref` | [`ontosage:evidenceReference`]({{ '/ontology/property/evidenceReference/' | relative_url }}) | `xsd:string` |  |  |  |
| `status` | [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | `xsd:string` | yes |  | active: Active, In service, Operational; defective: Defective, Faulty, Out of service; overdue: Overdue, Test overdue |
| `owner` | [`ontosage:recordOwner`]({{ '/ontology/property/recordOwner/' | relative_url }}) | `xsd:string` |  |  |  |
| `note` | `rdfs:comment` | `xsd:string` |  |  |  |

## evacuation\_provision {#evacuation_provision}

Class [`ontosage:EvacuationProvision`]({{ '/ontology/class/EvacuationProvision/' | relative_url }}); IRI template `evac/{code}`; label column `name`. Mapping file: [`ontology/record_documents/evacuation_provision.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/evacuation_provision.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `code` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `name` | `rdfs:label` | `xsd:string` | yes |  |  |
| `kind` | [`ontosage:provisionKind`]({{ '/ontology/property/provisionKind/' | relative_url }}) | `xsd:string` | yes |  |  |
| `location` | [`ontosage:locationText`]({{ '/ontology/property/locationText/' | relative_url }}) | `xsd:string` | yes | `located_in` |  |
| `floor` | [`ontosage:onFloor`]({{ '/ontology/property/onFloor/' | relative_url }}) | `xsd:string` |  | `on_floor` |  |
| `state` | [`ontosage:provisionState`]({{ '/ontology/property/provisionState/' | relative_url }}) | `xsd:string` | yes |  |  |
| `last_checked` | [`ontosage:lastTestedOn`]({{ '/ontology/property/lastTestedOn/' | relative_url }}) | `xsd:date` |  |  |  |
| `review_due` | [`ontosage:reviewDue`]({{ '/ontology/property/reviewDue/' | relative_url }}) | `xsd:date` | yes |  |  |
| `owner` | [`ontosage:recordOwner`]({{ '/ontology/property/recordOwner/' | relative_url }}) | `xsd:string` | yes |  |  |
| `status` | [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | `xsd:string` | yes |  | active: Active, Available; defective: Defective; overdue: Overdue |
| `note` | `rdfs:comment` | `xsd:string` |  |  |  |

## event\_activity {#event_activity}

Class [`ontosage:EventActivity`]({{ '/ontology/class/EventActivity/' | relative_url }}); IRI template `activity/{activity}`; label column `title`. Mapping file: [`ontology/record_documents/event_activity.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/event_activity.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `activity` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `event` | [`ontosage:partOfEvent`]({{ '/ontology/property/partOfEvent/' | relative_url }}) | `xsd:string` | yes |  |  |
| `title` | `rdfs:label` | `xsd:string` | yes |  |  |
| `sequence` | [`ontosage:circuitSequence`]({{ '/ontology/property/circuitSequence/' | relative_url }}) | `xsd:integer` | yes |  |  |
| `starts` | [`ontosage:startsAt`]({{ '/ontology/property/startsAt/' | relative_url }}) | `xsd:string` | yes |  |  |
| `minutes` | [`ontosage:expectedMinutes`]({{ '/ontology/property/expectedMinutes/' | relative_url }}) | `xsd:integer` | yes |  |  |
| `location` | [`ontosage:locationText`]({{ '/ontology/property/locationText/' | relative_url }}) | `xsd:string` | yes | `located_in` |  |
| `companion` | [`ontosage:companionPolicy`]({{ '/ontology/property/companionPolicy/' | relative_url }}) | `xsd:string` |  |  |  |
| `optional` | [`ontosage:isOptional`]({{ '/ontology/property/isOptional/' | relative_url }}) | `xsd:boolean` | yes |  |  |
| `access_note` | [`ontosage:accessibilityNote`]({{ '/ontology/property/accessibilityNote/' | relative_url }}) | `xsd:string` |  |  |  |
| `status` | [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | `xsd:string` | yes |  | scheduled: Scheduled, Confirmed, On; full: Full, Booked out; cancelled: Cancelled, Withdrawn |
| `owner` | [`ontosage:recordOwner`]({{ '/ontology/property/recordOwner/' | relative_url }}) | `xsd:string` |  |  |  |

## fire\_safety\_asset {#fire_safety_asset}

Class [`ontosage:FireSafetyAsset`]({{ '/ontology/class/FireSafetyAsset/' | relative_url }}); IRI template `fireasset/{code}`; label column `name`. Mapping file: [`ontology/record_documents/fire_safety_asset.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/fire_safety_asset.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `code` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `name` | `rdfs:label` | `xsd:string` | yes |  |  |
| `kind` | [`ontosage:fireAssetKind`]({{ '/ontology/property/fireAssetKind/' | relative_url }}) | `xsd:string` | yes |  |  |
| `location` | [`ontosage:locationText`]({{ '/ontology/property/locationText/' | relative_url }}) | `xsd:string` | yes | `located_in` |  |
| `floor` | [`ontosage:onFloor`]({{ '/ontology/property/onFloor/' | relative_url }}) | `xsd:string` |  | `on_floor` |  |
| `standard` | [`ontosage:testStandard`]({{ '/ontology/property/testStandard/' | relative_url }}) | `xsd:string` | yes |  |  |
| `last_tested_on` | [`ontosage:lastTestedOn`]({{ '/ontology/property/lastTestedOn/' | relative_url }}) | `xsd:date` |  |  |  |
| `next_test_due` | [`ontosage:nextTestDue`]({{ '/ontology/property/nextTestDue/' | relative_url }}) | `xsd:date` | yes |  |  |
| `evidence_ref` | [`ontosage:evidenceReference`]({{ '/ontology/property/evidenceReference/' | relative_url }}) | `xsd:string` |  |  |  |
| `open_defect` | [`ontosage:openDefect`]({{ '/ontology/property/openDefect/' | relative_url }}) | `xsd:string` |  |  |  |
| `owner` | [`ontosage:recordOwner`]({{ '/ontology/property/recordOwner/' | relative_url }}) | `xsd:string` | yes |  |  |
| `status` | [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | `xsd:string` | yes |  | active: Active, Serviceable; defective: Defective, Defect open; unevidenced: Unevidenced, Not proved; overdue: Overdue |
| `note` | `rdfs:comment` | `xsd:string` |  |  |  |

## handover {#handover}

Class [`ontosage:HandoverRecord`]({{ '/ontology/class/HandoverRecord/' | relative_url }}); IRI template `handover/{reference}`; label column `reference`. Mapping file: [`ontology/record_documents/handover.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/handover.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `reference` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `asset` | [`ontosage:coveredScope`]({{ '/ontology/property/coveredScope/' | relative_url }}) | `xsd:string` | yes |  |  |
| `document_kind` | [`ontosage:note`]({{ '/ontology/property/note/' | relative_url }}) | `xsd:string` | yes |  |  |
| `issued` | [`ontosage:effectiveFrom`]({{ '/ontology/property/effectiveFrom/' | relative_url }}) | `xsd:date` | yes |  |  |
| `issued_by` | [`ontosage:providerName`]({{ '/ontology/property/providerName/' | relative_url }}) | `xsd:string` |  |  |  |
| `status` | [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | `xsd:string` | yes |  | held: Held, On file, Received, Complete; outstanding: Outstanding, Missing, Not received, Awaited |

## hazard\_control {#hazard_control}

Class [`ontosage:HazardControl`]({{ '/ontology/class/HazardControl/' | relative_url }}); IRI template `hazard/{code}`; label column `hazard`. Mapping file: [`ontology/record_documents/hazard_control.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/hazard_control.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `code` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `hazard` | `rdfs:label` | `xsd:string` | yes |  |  |
| `kind` | [`ontosage:hazardKind`]({{ '/ontology/property/hazardKind/' | relative_url }}) | `xsd:string` | yes |  |  |
| `location` | [`ontosage:locationText`]({{ '/ontology/property/locationText/' | relative_url }}) | `xsd:string` | yes | `located_in` |  |
| `control` | [`ontosage:controlMeasure`]({{ '/ontology/property/controlMeasure/' | relative_url }}) | `xsd:string` | yes |  |  |
| `condition` | [`ontosage:hazardCondition`]({{ '/ontology/property/hazardCondition/' | relative_url }}) | `xsd:string` |  |  |  |
| `regime` | [`ontosage:testStandard`]({{ '/ontology/property/testStandard/' | relative_url }}) | `xsd:string` | yes |  |  |
| `last_tested_on` | [`ontosage:lastTestedOn`]({{ '/ontology/property/lastTestedOn/' | relative_url }}) | `xsd:date` |  |  |  |
| `next_test_due` | [`ontosage:nextTestDue`]({{ '/ontology/property/nextTestDue/' | relative_url }}) | `xsd:date` | yes |  |  |
| `evidence_ref` | [`ontosage:evidenceReference`]({{ '/ontology/property/evidenceReference/' | relative_url }}) | `xsd:string` |  |  |  |
| `owner` | [`ontosage:recordOwner`]({{ '/ontology/property/recordOwner/' | relative_url }}) | `xsd:string` | yes |  |  |
| `status` | [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | `xsd:string` | yes |  | active: Active, Controlled; overdue: Overdue; defective: Defective, Control impaired |
| `note` | `rdfs:comment` | `xsd:string` |  |  |  |

## incident\_record {#incident_record}

Class [`ontosage:IncidentRecord`]({{ '/ontology/class/IncidentRecord/' | relative_url }}); IRI template `incident/{ref}`; label column `summary`. Mapping file: [`ontology/record_documents/incident_record.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/incident_record.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `ref` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `summary` | `rdfs:label` | `xsd:string` | yes |  |  |
| `occurred_on` | [`ontosage:effectiveFrom`]({{ '/ontology/property/effectiveFrom/' | relative_url }}) | `xsd:date` | yes |  |  |
| `location` | [`ontosage:locationText`]({{ '/ontology/property/locationText/' | relative_url }}) | `xsd:string` | yes | `located_in` |  |
| `category` | [`ontosage:incidentCategory`]({{ '/ontology/property/incidentCategory/' | relative_url }}) | `xsd:string` | yes |  |  |
| `severity` | [`ontosage:incidentSeverity`]({{ '/ontology/property/incidentSeverity/' | relative_url }}) | `xsd:string` | yes |  |  |
| `potential_severity` | [`ontosage:potentialSeverity`]({{ '/ontology/property/potentialSeverity/' | relative_url }}) | `xsd:string` | yes |  |  |
| `immediate_action` | [`ontosage:immediateAction`]({{ '/ontology/property/immediateAction/' | relative_url }}) | `xsd:string` | yes |  |  |
| `investigation_finding` | [`ontosage:investigationFinding`]({{ '/ontology/property/investigationFinding/' | relative_url }}) | `xsd:string` |  |  |  |
| `reportable` | [`ontosage:externallyReportable`]({{ '/ontology/property/externallyReportable/' | relative_url }}) | `xsd:boolean` | yes |  |  |
| `actions_outstanding` | [`ontosage:actionsOutstanding`]({{ '/ontology/property/actionsOutstanding/' | relative_url }}) | `xsd:string` |  |  |  |
| `reported_by_role` | [`ontosage:reportTo`]({{ '/ontology/property/reportTo/' | relative_url }}) | `xsd:string` |  |  |  |
| `owner` | [`ontosage:recordOwner`]({{ '/ontology/property/recordOwner/' | relative_url }}) | `xsd:string` | yes |  |  |
| `closed_on` | [`ontosage:completedDate`]({{ '/ontology/property/completedDate/' | relative_url }}) | `xsd:date` |  |  |  |
| `status` | [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | `xsd:string` | yes |  | open: Open, Under investigation; closed: Closed; monitoring: Monitoring, Action tracked |
| `note` | `rdfs:comment` | `xsd:string` |  |  |  |

## operating\_regime {#operating_regime}

Class [`ontosage:OperatingRegime`]({{ '/ontology/class/OperatingRegime/' | relative_url }}); IRI template `regime/{code}`; label column `system`. Mapping file: [`ontology/record_documents/operating_regime.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/operating_regime.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `code` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `system` | `rdfs:label` | `xsd:string` | yes |  |  |
| `scope` | [`ontosage:coveredScope`]({{ '/ontology/property/coveredScope/' | relative_url }}) | `xsd:string` | yes |  |  |
| `occupied_setpoint` | [`ontosage:occupiedSetpoint`]({{ '/ontology/property/occupiedSetpoint/' | relative_url }}) | `xsd:string` | yes |  |  |
| `unoccupied_setpoint` | [`ontosage:unoccupiedSetpoint`]({{ '/ontology/property/unoccupiedSetpoint/' | relative_url }}) | `xsd:string` |  |  |  |
| `operating_window` | [`ontosage:operatingWindow`]({{ '/ontology/property/operatingWindow/' | relative_url }}) | `xsd:string` | yes |  |  |
| `seasonal_changeover` | [`ontosage:seasonalChangeover`]({{ '/ontology/property/seasonalChangeover/' | relative_url }}) | `xsd:string` |  |  |  |
| `approved_exception` | [`ontosage:approvedException`]({{ '/ontology/property/approvedException/' | relative_url }}) | `xsd:string` |  |  |  |
| `owner` | [`ontosage:recordOwner`]({{ '/ontology/property/recordOwner/' | relative_url }}) | `xsd:string` | yes |  |  |
| `status` | [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | `xsd:string` | yes |  | active: Active, In force; overridden: Overridden; under\_review: Under review |
| `note` | `rdfs:comment` | `xsd:string` |  |  |  |

## patrol\_checkpoint {#patrol_checkpoint}

Class [`ontosage:PatrolCheckpoint`]({{ '/ontology/class/PatrolCheckpoint/' | relative_url }}); IRI template `patrol/{checkpoint}`; label column `name`. Mapping file: [`ontology/record_documents/patrol_checkpoint.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/patrol_checkpoint.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `checkpoint` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `name` | `rdfs:label` | `xsd:string` | yes |  |  |
| `circuit` | [`ontosage:patrolCircuit`]({{ '/ontology/property/patrolCircuit/' | relative_url }}) | `xsd:string` | yes |  |  |
| `sequence` | [`ontosage:circuitSequence`]({{ '/ontology/property/circuitSequence/' | relative_url }}) | `xsd:integer` |  |  |  |
| `location` | [`ontosage:locationText`]({{ '/ontology/property/locationText/' | relative_url }}) | `xsd:string` | yes | `located_in` |  |
| `shift` | [`ontosage:shiftName`]({{ '/ontology/property/shiftName/' | relative_url }}) | `xsd:string` | yes |  |  |
| `frequency` | [`ontosage:serviceFrequency`]({{ '/ontology/property/serviceFrequency/' | relative_url }}) | `xsd:string` | yes |  |  |
| `last_verified` | [`ontosage:lastCompleted`]({{ '/ontology/property/lastCompleted/' | relative_url }}) | `xsd:dateTime` |  |  |  |
| `due` | [`ontosage:nextDue`]({{ '/ontology/property/nextDue/' | relative_url }}) | `xsd:dateTime` |  |  |  |
| `walk_minutes` | [`ontosage:expectedMinutes`]({{ '/ontology/property/expectedMinutes/' | relative_url }}) | `xsd:integer` |  |  |  |
| `qualification` | [`ontosage:requiredQualification`]({{ '/ontology/property/requiredQualification/' | relative_url }}) | `xsd:string` |  |  |  |
| `status` | [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | `xsd:string` | yes |  | current: Current, Verified, Complete; due: Due, Scheduled; overdue: Overdue, Missed, Late; unverifiable: Unverifiable, Blocked, No access, Tag faulty |
| `exception` | [`ontosage:openException`]({{ '/ontology/property/openException/' | relative_url }}) | `xsd:string` |  |  |  |
| `owner` | [`ontosage:recordOwner`]({{ '/ontology/property/recordOwner/' | relative_url }}) | `xsd:string` |  |  |  |

## permit\_to\_work {#permit_to_work}

Class [`ontosage:Permit`]({{ '/ontology/class/Permit/' | relative_url }}); IRI template `permit/{permit}`; label column `permit`. Mapping file: [`ontology/record_documents/permit_to_work.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/permit_to_work.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `permit` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `type` | [`ontosage:permitKind`]({{ '/ontology/property/permitKind/' | relative_url }}) | `xsd:string` | yes |  |  |
| `date` | [`ontosage:effectiveFrom`]({{ '/ontology/property/effectiveFrom/' | relative_url }}) | `xsd:date` | yes |  |  |
| `expires` | [`ontosage:effectiveTo`]({{ '/ontology/property/effectiveTo/' | relative_url }}) | `xsd:date` |  |  |  |
| `area` | [`ontosage:locationText`]({{ '/ontology/property/locationText/' | relative_url }}) | `xsd:string` |  | `located_in` |  |
| `status` | [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | `xsd:string` | yes |  | open: Open, Issued, Active, In progress; closed: Closed, Completed, Signed off; suspended: Suspended, On hold |
| `contractor` | [`ontosage:providerName`]({{ '/ontology/property/providerName/' | relative_url }}) | `xsd:string` |  |  |  |

## public\_event {#public_event}

Class [`ontosage:PublicEvent`]({{ '/ontology/class/PublicEvent/' | relative_url }}); IRI template `event/{event}`; label column `title`. Mapping file: [`ontology/record_documents/public_event.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/public_event.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `event` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `title` | `rdfs:label` | `xsd:string` | yes |  |  |
| `venue` | [`ontosage:locationText`]({{ '/ontology/property/locationText/' | relative_url }}) | `xsd:string` | yes | `located_in` |  |
| `date` | [`ontosage:effectiveFrom`]({{ '/ontology/property/effectiveFrom/' | relative_url }}) | `xsd:date` | yes |  |  |
| `starts` | [`ontosage:startsAt`]({{ '/ontology/property/startsAt/' | relative_url }}) | `xsd:string` | yes |  |  |
| `ends` | [`ontosage:endsAt`]({{ '/ontology/property/endsAt/' | relative_url }}) | `xsd:string` |  |  |  |
| `doors_open` | [`ontosage:doorsOpenAt`]({{ '/ontology/property/doorsOpenAt/' | relative_url }}) | `xsd:string` |  |  |  |
| `check_in_from` | [`ontosage:checkInFrom`]({{ '/ontology/property/checkInFrom/' | relative_url }}) | `xsd:string` |  |  |  |
| `entrance` | [`ontosage:visitorEntrance`]({{ '/ontology/property/visitorEntrance/' | relative_url }}) | `xsd:string` | yes |  |  |
| `registration` | [`ontosage:registrationPolicy`]({{ '/ontology/property/registrationPolicy/' | relative_url }}) | `xsd:string` | yes |  | required: Required, Ticketed, Pre-registration required; walk\_up: Walk-up, Open, No registration; closed: Closed, Full, Waitlist |
| `companion` | [`ontosage:companionPolicy`]({{ '/ontology/property/companionPolicy/' | relative_url }}) | `xsd:string` |  |  |  |
| `access_note` | [`ontosage:accessibilityNote`]({{ '/ontology/property/accessibilityNote/' | relative_url }}) | `xsd:string` |  |  |  |
| `previous_venue` | [`ontosage:previousLocationText`]({{ '/ontology/property/previousLocationText/' | relative_url }}) | `xsd:string` |  |  |  |
| `status` | [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | `xsd:string` | yes |  | scheduled: Scheduled, Confirmed, On; moved: Moved, Relocated, Rescheduled; cancelled: Cancelled, Withdrawn |
| `owner` | [`ontosage:recordOwner`]({{ '/ontology/property/recordOwner/' | relative_url }}) | `xsd:string` |  |  |  |

## risk\_assessment {#risk_assessment}

Class [`ontosage:RiskAssessment`]({{ '/ontology/class/RiskAssessment/' | relative_url }}); IRI template `risk/{reference}`; label column `reference`. Mapping file: [`ontology/record_documents/risk_assessment.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/risk_assessment.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `reference` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `hazard` | [`ontosage:coveredScope`]({{ '/ontology/property/coveredScope/' | relative_url }}) | `xsd:string` | yes |  |  |
| `area` | [`ontosage:locationText`]({{ '/ontology/property/locationText/' | relative_url }}) | `xsd:string` |  | `located_in` |  |
| `assessed` | [`ontosage:effectiveFrom`]({{ '/ontology/property/effectiveFrom/' | relative_url }}) | `xsd:date` | yes |  |  |
| `review_due` | [`ontosage:dueDate`]({{ '/ontology/property/dueDate/' | relative_url }}) | `xsd:date` | yes |  |  |
| `assessor_role` | [`ontosage:responsibleRole`]({{ '/ontology/property/responsibleRole/' | relative_url }}) | `xsd:string` |  |  |  |
| `status` | [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | `xsd:string` | yes |  | current: Current, In date, Valid; due: Due, Due for review, Review due; overdue: Overdue, Past review, Expired |

## service\_schedule {#service_schedule}

Class [`ontosage:ServiceSchedule`]({{ '/ontology/class/ServiceSchedule/' | relative_url }}); IRI template `service/{code}`; label column `task`. Mapping file: [`ontology/record_documents/service_schedule.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/service_schedule.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `code` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `task` | `rdfs:label` | `xsd:string` | yes |  |  |
| `category` | [`ontosage:scheduleKind`]({{ '/ontology/property/scheduleKind/' | relative_url }}) | `xsd:string` | yes |  |  |
| `scope` | [`ontosage:coveredScope`]({{ '/ontology/property/coveredScope/' | relative_url }}) | `xsd:string` | yes |  |  |
| `frequency` | [`ontosage:serviceFrequency`]({{ '/ontology/property/serviceFrequency/' | relative_url }}) | `xsd:string` | yes |  |  |
| `last_completed` | [`ontosage:lastCompleted`]({{ '/ontology/property/lastCompleted/' | relative_url }}) | `xsd:date` | yes |  |  |
| `next_due` | [`ontosage:nextDue`]({{ '/ontology/property/nextDue/' | relative_url }}) | `xsd:date` | yes |  |  |
| `statutory` | [`ontosage:isStatutory`]({{ '/ontology/property/isStatutory/' | relative_url }}) | `xsd:boolean` |  |  |  |
| `owner` | [`ontosage:recordOwner`]({{ '/ontology/property/recordOwner/' | relative_url }}) | `xsd:string` | yes |  |  |
| `provider` | [`ontosage:providerName`]({{ '/ontology/property/providerName/' | relative_url }}) | `xsd:string` |  |  |  |
| `status` | [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | `xsd:string` | yes |  | active: Active, On schedule; due: Due, Due soon; overdue: Overdue |
| `note` | `rdfs:comment` | `xsd:string` |  |  |  |

## stakeholder\_group {#stakeholder_group}

Class [`ontosage:StakeholderGroup`]({{ '/ontology/class/StakeholderGroup/' | relative_url }}); IRI template `stakeholder/{code}`; label column `name`. Mapping file: [`ontology/record_documents/stakeholder_group.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/stakeholder_group.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `code` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `name` | `rdfs:label` | `xsd:string` | yes |  |  |
| `category` | [`ontosage:stakeholderCategory`]({{ '/ontology/property/stakeholderCategory/' | relative_url }}) | `xsd:string` | yes |  | occupant: Occupant; operations: Operations; specialist: Specialist; external: External; governance: Governance; visitor: Visitor |
| `primary_need` | [`ontosage:primaryNeed`]({{ '/ontology/property/primaryNeed/' | relative_url }}) | `xsd:string` | yes |  |  |
| `served_by` | [`ontosage:servedByDepartment`]({{ '/ontology/property/servedByDepartment/' | relative_url }}) | `xsd:string` | yes |  |  |
| `accountable_for` | [`ontosage:accountableFor`]({{ '/ontology/property/accountableFor/' | relative_url }}) | `xsd:string` |  |  |  |
| `access_tier` | [`ontosage:accessTier`]({{ '/ontology/property/accessTier/' | relative_url }}) | `xsd:string` | yes |  |  |
| `presence` | [`ontosage:presencePattern`]({{ '/ontology/property/presencePattern/' | relative_url }}) | `xsd:string` | yes |  |  |
| `data_needs` | [`ontosage:dataNeeds`]({{ '/ontology/property/dataNeeds/' | relative_url }}) | `xsd:string` | yes |  |  |
| `status` | [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | `xsd:string` | yes |  | active: Active; occasional: Occasional, Seasonal; inactive: Inactive, Withdrawn |
| `note` | `rdfs:comment` | `xsd:string` |  |  |  |

## stock\_item {#stock_item}

Class [`ontosage:StockItem`]({{ '/ontology/class/StockItem/' | relative_url }}); IRI template `stock/{code}`; label column `item`. Mapping file: [`ontology/record_documents/stock_item.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/stock_item.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `code` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `item` | `rdfs:label` | `xsd:string` | yes |  |  |
| `kind` | [`ontosage:stockKind`]({{ '/ontology/property/stockKind/' | relative_url }}) | `xsd:string` | yes |  | consumable: Consumable; spare: Spare; loan: Loan; surplus: Surplus |
| `category` | [`ontosage:stockCategory`]({{ '/ontology/property/stockCategory/' | relative_url }}) | `xsd:string` |  |  |  |
| `store` | [`ontosage:locationText`]({{ '/ontology/property/locationText/' | relative_url }}) | `xsd:string` | yes | `located_in` |  |
| `on_hand` | [`ontosage:quantityOnHand`]({{ '/ontology/property/quantityOnHand/' | relative_url }}) | `xsd:integer` | yes |  |  |
| `minimum` | [`ontosage:minimumLevel`]({{ '/ontology/property/minimumLevel/' | relative_url }}) | `xsd:integer` | yes |  |  |
| `unit` | [`ontosage:stockUnit`]({{ '/ontology/property/stockUnit/' | relative_url }}) | `xsd:string` |  |  |  |
| `used_for` | [`ontosage:usedFor`]({{ '/ontology/property/usedFor/' | relative_url }}) | `xsd:string` |  |  |  |
| `supplier` | [`ontosage:providerName`]({{ '/ontology/property/providerName/' | relative_url }}) | `xsd:string` |  |  |  |
| `lead_time_days` | [`ontosage:leadTimeDays`]({{ '/ontology/property/leadTimeDays/' | relative_url }}) | `xsd:integer` |  |  |  |
| `last_counted` | [`ontosage:lastCounted`]({{ '/ontology/property/lastCounted/' | relative_url }}) | `xsd:date` | yes |  |  |
| `next_due` | [`ontosage:nextDue`]({{ '/ontology/property/nextDue/' | relative_url }}) | `xsd:date` |  |  |  |
| `status` | [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | `xsd:string` | yes |  | in\_stock: In stock; low: Low; on\_order: On order; out\_of\_stock: Out of stock; available\_for\_reuse: Available for reuse; withdrawn: Withdrawn |
| `accountable_role` | [`ontosage:accountableRole`]({{ '/ontology/property/accountableRole/' | relative_url }}) | `xsd:string` |  |  |  |
| `note` | `rdfs:comment` | `xsd:string` |  |  |  |

## sustainability\_target {#sustainability_target}

Class [`ontosage:SustainabilityTarget`]({{ '/ontology/class/SustainabilityTarget/' | relative_url }}); IRI template `target/{reference}`; label column `reference`. Mapping file: [`ontology/record_documents/sustainability_target.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/sustainability_target.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `reference` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `metric` | [`ontosage:targetMetric`]({{ '/ontology/property/targetMetric/' | relative_url }}) | `xsd:string` | yes |  |  |
| `target_value` | [`ontosage:targetValue`]({{ '/ontology/property/targetValue/' | relative_url }}) | `xsd:decimal` | yes |  |  |
| `unit` | [`ontosage:targetUnit`]({{ '/ontology/property/targetUnit/' | relative_url }}) | `xsd:string` | yes |  |  |
| `baseline_value` | [`ontosage:baselineValue`]({{ '/ontology/property/baselineValue/' | relative_url }}) | `xsd:decimal` | yes |  |  |
| `baseline_period` | [`ontosage:targetBaselinePeriod`]({{ '/ontology/property/targetBaselinePeriod/' | relative_url }}) | `xsd:string` | yes |  |  |
| `target_date` | [`ontosage:targetDate`]({{ '/ontology/property/targetDate/' | relative_url }}) | `xsd:date` | yes |  |  |
| `authority` | [`ontosage:targetAuthority`]({{ '/ontology/property/targetAuthority/' | relative_url }}) | `xsd:string` | yes |  |  |
| `status` | [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | `xsd:string` | yes |  | on\_track: On track, On-track, Ahead; at\_risk: At risk, At-risk, Behind; met: Met, Achieved, Complete |

## tariff {#tariff}

Class [`ontosage:Tariff`]({{ '/ontology/class/Tariff/' | relative_url }}); IRI template `tariff/{reference}`; label column `reference`. Mapping file: [`ontology/record_documents/tariff.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/tariff.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `reference` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `utility` | [`ontosage:utilityKind`]({{ '/ontology/property/utilityKind/' | relative_url }}) | `xsd:string` | yes |  |  |
| `unit_rate` | [`ontosage:unitRate`]({{ '/ontology/property/unitRate/' | relative_url }}) | `xsd:decimal` | yes |  |  |
| `standing_charge` | [`ontosage:standingCharge`]({{ '/ontology/property/standingCharge/' | relative_url }}) | `xsd:decimal` |  |  |  |
| `currency` | [`ontosage:currencyCode`]({{ '/ontology/property/currencyCode/' | relative_url }}) | `xsd:string` | yes |  |  |
| `start` | [`ontosage:effectiveFrom`]({{ '/ontology/property/effectiveFrom/' | relative_url }}) | `xsd:date` | yes |  |  |
| `end` | [`ontosage:effectiveTo`]({{ '/ontology/property/effectiveTo/' | relative_url }}) | `xsd:date` |  |  |  |
| `supplier` | [`ontosage:providerName`]({{ '/ontology/property/providerName/' | relative_url }}) | `xsd:string` | yes |  |  |

## timetabled\_session {#timetabled_session}

Class [`ontosage:TimetabledSession`]({{ '/ontology/class/TimetabledSession/' | relative_url }}); IRI template `session/{code}`; label column `module`. Mapping file: [`ontology/record_documents/timetabled_session.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/timetabled_session.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `code` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `module` | `rdfs:label` | `xsd:string` | yes |  |  |
| `room` | [`ontosage:locationText`]({{ '/ontology/property/locationText/' | relative_url }}) | `xsd:string` | yes | `located_in` |  |
| `floor` | [`ontosage:onFloor`]({{ '/ontology/property/onFloor/' | relative_url }}) | `xsd:string` |  | `on_floor` |  |
| `session_date` | [`ontosage:effectiveDate`]({{ '/ontology/property/effectiveDate/' | relative_url }}) | `xsd:date` | yes |  |  |
| `weekday` | [`ontosage:timeProfile`]({{ '/ontology/property/timeProfile/' | relative_url }}) | `xsd:string` | yes |  |  |
| `starts_at` | [`ontosage:startsAt`]({{ '/ontology/property/startsAt/' | relative_url }}) | `xsd:string` | yes |  |  |
| `ends_at` | [`ontosage:endsAt`]({{ '/ontology/property/endsAt/' | relative_url }}) | `xsd:string` | yes |  |  |
| `duration_minutes` | [`ontosage:expectedMinutes`]({{ '/ontology/property/expectedMinutes/' | relative_url }}) | `xsd:integer` | yes |  |  |
| `session_kind` | [`ontosage:sessionKind`]({{ '/ontology/property/sessionKind/' | relative_url }}) | `xsd:string` | yes |  |  |
| `status` | [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | `xsd:string` | yes |  | scheduled: Scheduled; completed: Completed; cancelled: Cancelled |

## warranty {#warranty}

Class [`ontosage:Warranty`]({{ '/ontology/class/Warranty/' | relative_url }}); IRI template `warranty/{reference}`; label column `reference`. Mapping file: [`ontology/record_documents/warranty.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/warranty.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `reference` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `asset` | [`ontosage:coveredScope`]({{ '/ontology/property/coveredScope/' | relative_url }}) | `xsd:string` | yes |  |  |
| `provider` | [`ontosage:providerName`]({{ '/ontology/property/providerName/' | relative_url }}) | `xsd:string` | yes |  |  |
| `start` | [`ontosage:effectiveFrom`]({{ '/ontology/property/effectiveFrom/' | relative_url }}) | `xsd:date` | yes |  |  |
| `end` | [`ontosage:effectiveTo`]({{ '/ontology/property/effectiveTo/' | relative_url }}) | `xsd:date` | yes |  |  |
| `status` | [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | `xsd:string` | yes |  | active: Active, In warranty, Current, Valid; expired: Expired, Out of warranty, Lapsed; void: Void, Voided, Invalidated |

## waste\_collection {#waste_collection}

Class [`ontosage:WasteCollectionPoint`]({{ '/ontology/class/WasteCollectionPoint/' | relative_url }}); IRI template `waste/{point}`; label column `name`. Mapping file: [`ontology/record_documents/waste_collection.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/waste_collection.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `point` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `name` | `rdfs:label` | `xsd:string` | yes |  |  |
| `station` | [`ontosage:wasteStation`]({{ '/ontology/property/wasteStation/' | relative_url }}) | `xsd:string` | yes |  |  |
| `location` | [`ontosage:locationText`]({{ '/ontology/property/locationText/' | relative_url }}) | `xsd:string` | yes | `located_in` |  |
| `stream_record` | [`ontosage:wasteStream`]({{ '/ontology/property/wasteStream/' | relative_url }}) | `xsd:string` | yes |  |  |
| `stream_label` | [`ontosage:labelledStream`]({{ '/ontology/property/labelledStream/' | relative_url }}) | `xsd:string` | yes |  |  |
| `aperture` | [`ontosage:apertureKind`]({{ '/ontology/property/apertureKind/' | relative_url }}) | `xsd:string` |  |  |  |
| `capacity_litres` | [`ontosage:capacityLitres`]({{ '/ontology/property/capacityLitres/' | relative_url }}) | `xsd:integer` |  |  |  |
| `fill_percent` | [`ontosage:fillPercent`]({{ '/ontology/property/fillPercent/' | relative_url }}) | `xsd:integer` |  |  |  |
| `fill_threshold` | [`ontosage:approvedFillThreshold`]({{ '/ontology/property/approvedFillThreshold/' | relative_url }}) | `xsd:integer` |  |  |  |
| `next_collection` | [`ontosage:nextDue`]({{ '/ontology/property/nextDue/' | relative_url }}) | `xsd:date` | yes |  |  |
| `service_period` | [`ontosage:serviceFrequency`]({{ '/ontology/property/serviceFrequency/' | relative_url }}) | `xsd:string` | yes |  |  |
| `temporary` | [`ontosage:isTemporary`]({{ '/ontology/property/isTemporary/' | relative_url }}) | `xsd:boolean` | yes |  |  |
| `status` | [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | `xsd:string` | yes |  | active: Active, In service; overdue: Overdue, Missed collection; withdrawn: Withdrawn, Removed, Out of service |
| `owner` | [`ontosage:recordOwner`]({{ '/ontology/property/recordOwner/' | relative_url }}) | `xsd:string` |  |  |  |
| `note` | `rdfs:comment` | `xsd:string` |  |  |  |

## waste\_return {#waste_return}

Class [`ontosage:WasteReturn`]({{ '/ontology/class/WasteReturn/' | relative_url }}); IRI template `waste_return/{code}`; label column `name`. Mapping file: [`ontology/record_documents/waste_return.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/waste_return.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `code` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `name` | `rdfs:label` | `xsd:string` | yes |  |  |
| `month` | [`ontosage:reportingMonth`]({{ '/ontology/property/reportingMonth/' | relative_url }}) | `xsd:string` | yes |  |  |
| `period_start` | [`ontosage:effectiveFrom`]({{ '/ontology/property/effectiveFrom/' | relative_url }}) | `xsd:date` | yes |  |  |
| `period_end` | [`ontosage:effectiveTo`]({{ '/ontology/property/effectiveTo/' | relative_url }}) | `xsd:date` | yes |  |  |
| `stream` | [`ontosage:wasteStream`]({{ '/ontology/property/wasteStream/' | relative_url }}) | `xsd:string` | yes |  |  |
| `tonnes` | [`ontosage:wasteTonnes`]({{ '/ontology/property/wasteTonnes/' | relative_url }}) | `xsd:decimal` |  |  |  |
| `diverted_pct` | [`ontosage:divertedPercent`]({{ '/ontology/property/divertedPercent/' | relative_url }}) | `xsd:decimal` |  |  |  |
| `treatment` | [`ontosage:treatmentRoute`]({{ '/ontology/property/treatmentRoute/' | relative_url }}) | `xsd:string` |  |  |  |
| `weighing` | [`ontosage:weighingMethod`]({{ '/ontology/property/weighingMethod/' | relative_url }}) | `xsd:string` |  |  |  |
| `contractor` | [`ontosage:providerName`]({{ '/ontology/property/providerName/' | relative_url }}) | `xsd:string` |  |  |  |
| `status` | [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | `xsd:string` | yes |  | confirmed: Confirmed, Final, Issued; pending: Pending, Not yet issued; query: Query, Disputed, Under review; provisional: Provisional, Estimated |
| `note` | `rdfs:comment` | `xsd:string` |  |  |  |

## work\_order {#work_order}

Class [`ontosage:WorkOrder`]({{ '/ontology/class/WorkOrder/' | relative_url }}); IRI template `workorder/{ref}`; label column `task`. Mapping file: [`ontology/record_documents/work_order.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/work_order.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `ref` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `task` | `rdfs:label` | `xsd:string` | yes |  |  |
| `asset_code` | [`ontosage:primarySystem`]({{ '/ontology/property/primarySystem/' | relative_url }}) | `xsd:string` | yes |  |  |
| `asset_name` | [`ontosage:locationText`]({{ '/ontology/property/locationText/' | relative_url }}) | `xsd:string` | yes | `located_in` |  |
| `raised_on` | [`ontosage:effectiveFrom`]({{ '/ontology/property/effectiveFrom/' | relative_url }}) | `xsd:date` | yes |  |  |
| `category` | [`ontosage:scheduleKind`]({{ '/ontology/property/scheduleKind/' | relative_url }}) | `xsd:string` | yes |  |  |
| `trade` | [`ontosage:responsibleRole`]({{ '/ontology/property/responsibleRole/' | relative_url }}) | `xsd:string` | yes |  |  |
| `hours` | [`ontosage:jobHours`]({{ '/ontology/property/jobHours/' | relative_url }}) | `xsd:decimal` |  |  |  |
| `priority` | [`ontosage:priority`]({{ '/ontology/property/priority/' | relative_url }}) | `xsd:string` | yes |  |  |
| `completed_on` | [`ontosage:completedDate`]({{ '/ontology/property/completedDate/' | relative_url }}) | `xsd:date` |  |  |  |
| `status` | [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | `xsd:string` | yes |  | open: Open, Pending; in\_progress: In progress; completed: Completed |
| `note` | `rdfs:comment` | `xsd:string` |  |  |  |

## workspace\_profile {#workspace_profile}

Class [`ontosage:WorkspaceProfile`]({{ '/ontology/class/WorkspaceProfile/' | relative_url }}); IRI template `workspace/{code}`; label column `name`. Mapping file: [`ontology/record_documents/workspace_profile.yaml`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/record_documents/workspace_profile.yaml).

| Column | Predicate | Datatype | Required | Links to | Values |
|---|---|---|---|---|---|
| `code` | [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | `xsd:string` | yes |  |  |
| `name` | `rdfs:label` | `xsd:string` | yes |  |  |
| `room` | [`ontosage:locationText`]({{ '/ontology/property/locationText/' | relative_url }}) | `xsd:string` | yes | `located_in` |  |
| `floor` | [`ontosage:onFloor`]({{ '/ontology/property/onFloor/' | relative_url }}) | `xsd:string` | yes | `on_floor` |  |
| `kind` | [`ontosage:workspaceKind`]({{ '/ontology/property/workspaceKind/' | relative_url }}) | `xsd:string` | yes |  |  |
| `seats` | [`ontosage:seatCount`]({{ '/ontology/property/seatCount/' | relative_url }}) | `xsd:integer` | yes |  |  |
| `bookable` | [`ontosage:isBookable`]({{ '/ontology/property/isBookable/' | relative_url }}) | `xsd:boolean` | yes |  |  |
| `power` | [`ontosage:powerAccess`]({{ '/ontology/property/powerAccess/' | relative_url }}) | `xsd:string` | yes |  |  |
| `network` | [`ontosage:networkRating`]({{ '/ontology/property/networkRating/' | relative_url }}) | `xsd:string` | yes |  |  |
| `daylight` | [`ontosage:daylightAspect`]({{ '/ontology/property/daylightAspect/' | relative_url }}) | `xsd:string` |  |  |  |
| `noise` | [`ontosage:noiseProfile`]({{ '/ontology/property/noiseProfile/' | relative_url }}) | `xsd:string` | yes |  |  |
| `calls_ok` | [`ontosage:suitableForCalls`]({{ '/ontology/property/suitableForCalls/' | relative_url }}) | `xsd:boolean` | yes |  |  |
| `group_ok` | [`ontosage:groupFriendly`]({{ '/ontology/property/groupFriendly/' | relative_url }}) | `xsd:boolean` | yes |  |  |
| `access` | [`ontosage:accessClassification`]({{ '/ontology/property/accessClassification/' | relative_url }}) | `xsd:string` | yes |  |  |
| `hours` | [`ontosage:openingHours`]({{ '/ontology/property/openingHours/' | relative_url }}) | `xsd:string` | yes |  |  |
| `busiest` | [`ontosage:busiestPeriod`]({{ '/ontology/property/busiestPeriod/' | relative_url }}) | `xsd:string` | yes |  |  |
| `quietest` | [`ontosage:quietestPeriod`]({{ '/ontology/property/quietestPeriod/' | relative_url }}) | `xsd:string` | yes |  |  |
| `setup_minutes` | [`ontosage:setupMinutes`]({{ '/ontology/property/setupMinutes/' | relative_url }}) | `xsd:decimal` |  |  |  |
| `recovery_minutes` | [`ontosage:recoveryMinutes`]({{ '/ontology/property/recoveryMinutes/' | relative_url }}) | `xsd:decimal` |  |  |  |
| `vertical_route` | [`ontosage:nearestVerticalRoute`]({{ '/ontology/property/nearestVerticalRoute/' | relative_url }}) | `xsd:string` | yes |  |  |
| `status` | [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | `xsd:string` | yes |  | active: Active, Available; restricted: Restricted; unavailable: Unavailable, Out of use |
| `note` | `rdfs:comment` | `xsd:string` |  |  |  |

