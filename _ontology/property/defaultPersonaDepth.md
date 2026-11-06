---
title: "ontosage:defaultPersonaDepth"
layout: post
permalink: /ontology/property/defaultPersonaDepth/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › defaultPersonaDepth

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#defaultPersonaDepth` |
| Label | default persona depth |
| Kind | datatype property |
| Domain | [`ontosage:StakeholderRole`]({{ '/ontology/class/StakeholderRole/' | relative_url }}) |
| Range | `xsd:integer` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Default technical depth (0=lay .. 4=expert) for answers to this role; mirrors hbco:personaDepth so environment explanations match the audience.

## Examples

- `ontosage:Role_Occupant ontosage:defaultPersonaDepth 0 .`

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
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:defaultPersonaDepth a owl:DatatypeProperty ;
    rdfs:label "default persona depth"@en ;
    rdfs:comment "Default technical depth (0=lay .. 4=expert) for answers to this role; mirrors hbco:personaDepth so environment explanations match the audience."@en ;
    rdfs:domain ontosage:StakeholderRole ;
    rdfs:range xsd:integer ;
    skos:example "ontosage:Role_Occupant ontosage:defaultPersonaDepth 0 ." .
```
{% endraw %}
