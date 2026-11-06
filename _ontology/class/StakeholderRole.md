---
title: "ontosage:StakeholderRole"
layout: post
permalink: /ontology/class/StakeholderRole/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › StakeholderRole

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#StakeholderRole` |
| Label | Stakeholder role |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A category of building stakeholder, used only to frame and prioritise answers (not for access control).

## Description

A conversational persona OntoSage serves. Roles bias answer framing (depth, tone) and the capability categories surfaced first — they are NOT RBAC permissions. One natural-language interface serves every role.

## Examples

- An Occupant asking 'is it stuffy?' gets a plain answer; a FacilityManager gets the CO₂ figure + trend.

## Class hierarchy

Superclasses: none (a root class).

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:asksAbout`]({{ '/ontology/property/asksAbout/' | relative_url }}) | object | `skos:Concept` | this class |
| [`ontosage:defaultPersonaDepth`]({{ '/ontology/property/defaultPersonaDepth/' | relative_url }}) | datatype | `xsd:integer` | this class |

## Used as the range of

| Property | Kind | Domain |
|---|---|---|
| [`ontosage:reportedByRole`]({{ '/ontology/property/reportedByRole/' | relative_url }}) | object | [`ontosage:Report`]({{ '/ontology/class/Report/' | relative_url }}) |

## Members

The schema declares 9 members of this class: see [Stakeholder roles]({{ '/ontology/vocabulary/stakeholder-roles/' | relative_url }}).

## Competency questions

- For this role, how deep should the answer be and what do they care about?

## Example SPARQL

{% raw %}
```sparql
SELECT ?role ?depth (GROUP_CONCAT(?cat; separator=", ") AS ?cats) WHERE {
  ?role a ontosage:StakeholderRole ; ontosage:defaultPersonaDepth ?depth .
  OPTIONAL { ?role ontosage:asksAbout ?c . ?c skos:prefLabel ?cat }
} GROUP BY ?role ?depth
```
{% endraw %}

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:StakeholderRole a owl:Class ;
    rdfs:label "Stakeholder role"@en ;
    ontosage:competencyQuestion "For this role, how deep should the answer be and what do they care about?" ;
    ontosage:exampleSparql """
        SELECT ?role ?depth (GROUP_CONCAT(?cat; separator=", ") AS ?cats) WHERE {
          ?role a ontosage:StakeholderRole ; ontosage:defaultPersonaDepth ?depth .
          OPTIONAL { ?role ontosage:asksAbout ?c . ?c skos:prefLabel ?cat }
        } GROUP BY ?role ?depth""" ;
    rdfs:comment "A conversational persona OntoSage serves. Roles bias answer framing (depth, tone) and the capability categories surfaced first — they are NOT RBAC permissions. One natural-language interface serves every role."@en ;
    skos:definition "A category of building stakeholder, used only to frame and prioritise answers (not for access control)."@en ;
    skos:example "An Occupant asking 'is it stuffy?' gets a plain answer; a FacilityManager gets the CO₂ figure + trend." .
```
{% endraw %}
