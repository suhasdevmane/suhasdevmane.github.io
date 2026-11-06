---
title: "Stakeholder roles"
layout: post
permalink: /ontology/vocabulary/stakeholder-roles/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Vocabularies]({{ '/docs/ontology-browser/' | relative_url }}#vocabularies) › Stakeholder roles

Conversational personas. A role frames how an answer is phrased; it does not grant or restrict access (that is RBAC, a separate mechanism). Members are instances of [`ontosage:StakeholderRole`]({{ '/ontology/class/StakeholderRole/' | relative_url }}). The schema declares 9.

| Member | Label |
|---|---|
| [`ontosage:Role_Admin`](#Role_Admin) | Administrator |
| [`ontosage:Role_Executive`](#Role_Executive) | Executive |
| [`ontosage:Role_FacilityManager`](#Role_FacilityManager) | Facility manager |
| [`ontosage:Role_Occupant`](#Role_Occupant) | Occupant |
| [`ontosage:Role_Researcher`](#Role_Researcher) | Researcher |
| [`ontosage:Role_SafetyOfficer`](#Role_SafetyOfficer) | Safety officer |
| [`ontosage:Role_Student`](#Role_Student) | Student |
| [`ontosage:Role_SustainabilityOfficer`](#Role_SustainabilityOfficer) | Sustainability officer |
| [`ontosage:Role_Visitor`](#Role_Visitor) | Visitor |

## Administrator {#Role_Admin}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Role_Admin` |
| [`ontosage:asksAbout`]({{ '/ontology/property/asksAbout/' | relative_url }}) | [`ontosage:cat_INFORMATION`]({{ '/ontology/vocabulary/capability-categories/' | relative_url }}#cat_INFORMATION), [`ontosage:cat_MAINTENANCE`]({{ '/ontology/vocabulary/capability-categories/' | relative_url }}#cat_MAINTENANCE) |
| [`ontosage:defaultPersonaDepth`]({{ '/ontology/property/defaultPersonaDepth/' | relative_url }}) | 4 |

Configures OntoSage and authors the ontology. Uses the admin console and the browsers; the only role that adds/edits triples.

## Executive {#Role_Executive}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Role_Executive` |
| [`ontosage:asksAbout`]({{ '/ontology/property/asksAbout/' | relative_url }}) | [`ontosage:cat_INFORMATION`]({{ '/ontology/vocabulary/capability-categories/' | relative_url }}#cat_INFORMATION), [`ontosage:cat_SUSTAINABILITY`]({{ '/ontology/vocabulary/capability-categories/' | relative_url }}#cat_SUSTAINABILITY) |
| [`ontosage:defaultPersonaDepth`]({{ '/ontology/property/defaultPersonaDepth/' | relative_url }}) | 2 |

A decision-maker wanting summarised, high-level answers (KPIs, headline figures) rather than raw readings.

## Facility manager {#Role_FacilityManager}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Role_FacilityManager` |
| [`ontosage:asksAbout`]({{ '/ontology/property/asksAbout/' | relative_url }}) | [`ontosage:cat_MAINTENANCE`]({{ '/ontology/vocabulary/capability-categories/' | relative_url }}#cat_MAINTENANCE), [`ontosage:cat_SAFETY`]({{ '/ontology/vocabulary/capability-categories/' | relative_url }}#cat_SAFETY), [`ontosage:cat_SUSTAINABILITY`]({{ '/ontology/vocabulary/capability-categories/' | relative_url }}#cat_SUSTAINABILITY) |
| [`ontosage:defaultPersonaDepth`]({{ '/ontology/property/defaultPersonaDepth/' | relative_url }}) | 3 |

Operates the building. Asks about sensor readings, trends, anomalies, maintenance, and equipment — wants figures and evidence, not just plain answers.

## Occupant {#Role_Occupant}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Role_Occupant` |
| [`ontosage:asksAbout`]({{ '/ontology/property/asksAbout/' | relative_url }}) | [`ontosage:cat_AMENITIES`]({{ '/ontology/vocabulary/capability-categories/' | relative_url }}#cat_AMENITIES), [`ontosage:cat_INFORMATION`]({{ '/ontology/vocabulary/capability-categories/' | relative_url }}#cat_INFORMATION), [`ontosage:cat_PROCEDURE`]({{ '/ontology/vocabulary/capability-categories/' | relative_url }}#cat_PROCEDURE) |
| [`ontosage:defaultPersonaDepth`]({{ '/ontology/property/defaultPersonaDepth/' | relative_url }}) | 0 |

A day-to-day building user (staff, student, resident). Asks about comfort, amenities, wayfinding, and how-to procedures in plain language.

## Researcher {#Role_Researcher}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Role_Researcher` |
| [`ontosage:asksAbout`]({{ '/ontology/property/asksAbout/' | relative_url }}) | [`ontosage:cat_INFORMATION`]({{ '/ontology/vocabulary/capability-categories/' | relative_url }}#cat_INFORMATION), [`ontosage:cat_SUSTAINABILITY`]({{ '/ontology/vocabulary/capability-categories/' | relative_url }}#cat_SUSTAINABILITY) |
| [`ontosage:defaultPersonaDepth`]({{ '/ontology/property/defaultPersonaDepth/' | relative_url }}) | 4 |

A researcher/analyst querying the building's data and ontology. Comfortable with Brick classes, SPARQL, and raw figures.

## Safety officer {#Role_SafetyOfficer}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Role_SafetyOfficer` |
| [`ontosage:asksAbout`]({{ '/ontology/property/asksAbout/' | relative_url }}) | [`ontosage:cat_MAINTENANCE`]({{ '/ontology/vocabulary/capability-categories/' | relative_url }}#cat_MAINTENANCE), [`ontosage:cat_SAFETY`]({{ '/ontology/vocabulary/capability-categories/' | relative_url }}#cat_SAFETY) |
| [`ontosage:defaultPersonaDepth`]({{ '/ontology/property/defaultPersonaDepth/' | relative_url }}) | 3 |

Responsible for health, safety, and compliance. Asks about air quality, occupancy limits, alarms, and incident reporting.

## Student {#Role_Student}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Role_Student` |
| [`ontosage:asksAbout`]({{ '/ontology/property/asksAbout/' | relative_url }}) | [`ontosage:cat_AMENITIES`]({{ '/ontology/vocabulary/capability-categories/' | relative_url }}#cat_AMENITIES), [`ontosage:cat_INFORMATION`]({{ '/ontology/vocabulary/capability-categories/' | relative_url }}#cat_INFORMATION), [`ontosage:cat_PROCEDURE`]({{ '/ontology/vocabulary/capability-categories/' | relative_url }}#cat_PROCEDURE) |
| [`ontosage:defaultPersonaDepth`]({{ '/ontology/property/defaultPersonaDepth/' | relative_url }}) | 0 |

A learner using the building; asks about study spaces, amenities, timetables, and how-to procedures.

## Sustainability officer {#Role_SustainabilityOfficer}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Role_SustainabilityOfficer` |
| [`ontosage:asksAbout`]({{ '/ontology/property/asksAbout/' | relative_url }}) | [`ontosage:cat_SUSTAINABILITY`]({{ '/ontology/vocabulary/capability-categories/' | relative_url }}#cat_SUSTAINABILITY) |
| [`ontosage:defaultPersonaDepth`]({{ '/ontology/property/defaultPersonaDepth/' | relative_url }}) | 3 |

Focuses on energy, carbon, and efficiency. Asks about consumption, trends, and comparisons.

## Visitor {#Role_Visitor}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Role_Visitor` |
| [`ontosage:asksAbout`]({{ '/ontology/property/asksAbout/' | relative_url }}) | [`ontosage:cat_ACCESSIBILITY`]({{ '/ontology/vocabulary/capability-categories/' | relative_url }}#cat_ACCESSIBILITY), [`ontosage:cat_AMENITIES`]({{ '/ontology/vocabulary/capability-categories/' | relative_url }}#cat_AMENITIES), [`ontosage:cat_INFORMATION`]({{ '/ontology/vocabulary/capability-categories/' | relative_url }}#cat_INFORMATION) |
| [`ontosage:defaultPersonaDepth`]({{ '/ontology/property/defaultPersonaDepth/' | relative_url }}) | 0 |

A guest with no prior knowledge of the building. Asks wayfinding, amenity, and access questions.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:Role_Admin a ontosage:StakeholderRole ;
    rdfs:label "Administrator"@en ;
    ontosage:asksAbout ontosage:cat_INFORMATION,
        ontosage:cat_MAINTENANCE ;
    ontosage:defaultPersonaDepth 4 ;
    rdfs:comment "Configures OntoSage and authors the ontology. Uses the admin console and the browsers; the only role that adds/edits triples."@en .

ontosage:Role_Executive a ontosage:StakeholderRole ;
    rdfs:label "Executive"@en ;
    ontosage:asksAbout ontosage:cat_INFORMATION,
        ontosage:cat_SUSTAINABILITY ;
    ontosage:defaultPersonaDepth 2 ;
    rdfs:comment "A decision-maker wanting summarised, high-level answers (KPIs, headline figures) rather than raw readings."@en .

ontosage:Role_FacilityManager a ontosage:StakeholderRole ;
    rdfs:label "Facility manager"@en ;
    ontosage:asksAbout ontosage:cat_MAINTENANCE,
        ontosage:cat_SAFETY,
        ontosage:cat_SUSTAINABILITY ;
    ontosage:defaultPersonaDepth 3 ;
    rdfs:comment "Operates the building. Asks about sensor readings, trends, anomalies, maintenance, and equipment — wants figures and evidence, not just plain answers."@en .

ontosage:Role_Occupant a ontosage:StakeholderRole ;
    rdfs:label "Occupant"@en ;
    ontosage:asksAbout ontosage:cat_AMENITIES,
        ontosage:cat_INFORMATION,
        ontosage:cat_PROCEDURE ;
    ontosage:defaultPersonaDepth 0 ;
    rdfs:comment "A day-to-day building user (staff, student, resident). Asks about comfort, amenities, wayfinding, and how-to procedures in plain language."@en .

ontosage:Role_Researcher a ontosage:StakeholderRole ;
    rdfs:label "Researcher"@en ;
    ontosage:asksAbout ontosage:cat_INFORMATION,
        ontosage:cat_SUSTAINABILITY ;
    ontosage:defaultPersonaDepth 4 ;
    rdfs:comment "A researcher/analyst querying the building's data and ontology. Comfortable with Brick classes, SPARQL, and raw figures."@en .

ontosage:Role_SafetyOfficer a ontosage:StakeholderRole ;
    rdfs:label "Safety officer"@en ;
    ontosage:asksAbout ontosage:cat_MAINTENANCE,
        ontosage:cat_SAFETY ;
    ontosage:defaultPersonaDepth 3 ;
    rdfs:comment "Responsible for health, safety, and compliance. Asks about air quality, occupancy limits, alarms, and incident reporting."@en .

ontosage:Role_Student a ontosage:StakeholderRole ;
    rdfs:label "Student"@en ;
    ontosage:asksAbout ontosage:cat_AMENITIES,
        ontosage:cat_INFORMATION,
        ontosage:cat_PROCEDURE ;
    ontosage:defaultPersonaDepth 0 ;
    rdfs:comment "A learner using the building; asks about study spaces, amenities, timetables, and how-to procedures."@en .

ontosage:Role_SustainabilityOfficer a ontosage:StakeholderRole ;
    rdfs:label "Sustainability officer"@en ;
    ontosage:asksAbout ontosage:cat_SUSTAINABILITY ;
    ontosage:defaultPersonaDepth 3 ;
    rdfs:comment "Focuses on energy, carbon, and efficiency. Asks about consumption, trends, and comparisons."@en .

ontosage:Role_Visitor a ontosage:StakeholderRole ;
    rdfs:label "Visitor"@en ;
    ontosage:asksAbout ontosage:cat_ACCESSIBILITY,
        ontosage:cat_AMENITIES,
        ontosage:cat_INFORMATION ;
    ontosage:defaultPersonaDepth 0 ;
    rdfs:comment "A guest with no prior knowledge of the building. Asks wayfinding, amenity, and access questions."@en .
```
{% endraw %}
