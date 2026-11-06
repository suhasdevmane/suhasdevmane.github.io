---
title: "ontosage:asksAbout"
layout: post
permalink: /ontology/property/asksAbout/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › asksAbout

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#asksAbout` |
| Label | typically asks about |
| Kind | object property |
| Domain | [`ontosage:StakeholderRole`]({{ '/ontology/class/StakeholderRole/' | relative_url }}) |
| Range | `skos:Concept` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Associates a stakeholder role with a capability category it most commonly asks about, so answers and suggestions can be prioritised for the audience. Advisory only — any role may ask anything.

## Examples

- `ontosage:Role_SustainabilityOfficer ontosage:asksAbout ontosage:cat_SUSTAINABILITY .`

## Used in the schema

9 schema term(s) carry this property:

- [`ontosage:Role_Admin`]({{ '/ontology/vocabulary/stakeholder-roles/' | relative_url }}#Role_Admin)
- [`ontosage:Role_Executive`]({{ '/ontology/vocabulary/stakeholder-roles/' | relative_url }}#Role_Executive)
- [`ontosage:Role_FacilityManager`]({{ '/ontology/vocabulary/stakeholder-roles/' | relative_url }}#Role_FacilityManager)
- [`ontosage:Role_Occupant`]({{ '/ontology/vocabulary/stakeholder-roles/' | relative_url }}#Role_Occupant)
- [`ontosage:Role_Researcher`]({{ '/ontology/vocabulary/stakeholder-roles/' | relative_url }}#Role_Researcher)
- [`ontosage:Role_SafetyOfficer`]({{ '/ontology/vocabulary/stakeholder-roles/' | relative_url }}#Role_SafetyOfficer)
- [`ontosage:Role_Student`]({{ '/ontology/vocabulary/stakeholder-roles/' | relative_url }}#Role_Student)
- [`ontosage:Role_SustainabilityOfficer`]({{ '/ontology/vocabulary/stakeholder-roles/' | relative_url }}#Role_SustainabilityOfficer)
- [`ontosage:Role_Visitor`]({{ '/ontology/vocabulary/stakeholder-roles/' | relative_url }}#Role_Visitor)

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:asksAbout a owl:ObjectProperty ;
    rdfs:label "typically asks about"@en ;
    rdfs:comment "Associates a stakeholder role with a capability category it most commonly asks about, so answers and suggestions can be prioritised for the audience. Advisory only — any role may ask anything."@en ;
    rdfs:domain ontosage:StakeholderRole ;
    rdfs:range skos:Concept ;
    skos:example "ontosage:Role_SustainabilityOfficer ontosage:asksAbout ontosage:cat_SUSTAINABILITY ." .
```
{% endraw %}
