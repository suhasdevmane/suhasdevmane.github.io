---
title: "Capability categories"
layout: post
permalink: /ontology/vocabulary/capability-categories/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Vocabularies]({{ '/docs/ontology-browser/' | relative_url }}#vocabularies) › Capability categories

SKOS concepts used as `ontosage:capabilityCategory` values and as the categories a stakeholder role `ontosage:asksAbout`. Members are instances of `skos:Concept`. The schema declares 7.

Concept scheme: `ontosage:CategoryScheme` (OCBV capability categories).

| Member | Label |
|---|---|
| [`ontosage:cat_ACCESSIBILITY`](#cat_ACCESSIBILITY) | ACCESSIBILITY |
| [`ontosage:cat_AMENITIES`](#cat_AMENITIES) | AMENITIES |
| [`ontosage:cat_INFORMATION`](#cat_INFORMATION) | INFORMATION |
| [`ontosage:cat_MAINTENANCE`](#cat_MAINTENANCE) | MAINTENANCE |
| [`ontosage:cat_PROCEDURE`](#cat_PROCEDURE) | PROCEDURE |
| [`ontosage:cat_SAFETY`](#cat_SAFETY) | SAFETY |
| [`ontosage:cat_SUSTAINABILITY`](#cat_SUSTAINABILITY) | SUSTAINABILITY |

## ACCESSIBILITY {#cat_ACCESSIBILITY}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#cat_ACCESSIBILITY` |
| `skos:inScheme` | `ontosage:CategoryScheme` |

## AMENITIES {#cat_AMENITIES}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#cat_AMENITIES` |
| `skos:inScheme` | `ontosage:CategoryScheme` |

## INFORMATION {#cat_INFORMATION}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#cat_INFORMATION` |
| `skos:inScheme` | `ontosage:CategoryScheme` |

## MAINTENANCE {#cat_MAINTENANCE}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#cat_MAINTENANCE` |
| `skos:inScheme` | `ontosage:CategoryScheme` |

## PROCEDURE {#cat_PROCEDURE}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#cat_PROCEDURE` |
| `skos:inScheme` | `ontosage:CategoryScheme` |

## SAFETY {#cat_SAFETY}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#cat_SAFETY` |
| `skos:inScheme` | `ontosage:CategoryScheme` |

## SUSTAINABILITY {#cat_SUSTAINABILITY}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#cat_SUSTAINABILITY` |
| `skos:inScheme` | `ontosage:CategoryScheme` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:cat_ACCESSIBILITY a skos:Concept ;
    skos:inScheme ontosage:CategoryScheme ;
    skos:prefLabel "ACCESSIBILITY"@en .

ontosage:cat_AMENITIES a skos:Concept ;
    skos:inScheme ontosage:CategoryScheme ;
    skos:prefLabel "AMENITIES"@en .

ontosage:cat_INFORMATION a skos:Concept ;
    skos:inScheme ontosage:CategoryScheme ;
    skos:prefLabel "INFORMATION"@en .

ontosage:cat_MAINTENANCE a skos:Concept ;
    skos:inScheme ontosage:CategoryScheme ;
    skos:prefLabel "MAINTENANCE"@en .

ontosage:cat_PROCEDURE a skos:Concept ;
    skos:inScheme ontosage:CategoryScheme ;
    skos:prefLabel "PROCEDURE"@en .

ontosage:cat_SAFETY a skos:Concept ;
    skos:inScheme ontosage:CategoryScheme ;
    skos:prefLabel "SAFETY"@en .

ontosage:cat_SUSTAINABILITY a skos:Concept ;
    skos:inScheme ontosage:CategoryScheme ;
    skos:prefLabel "SUSTAINABILITY"@en .

ontosage:CategoryScheme a skos:ConceptScheme ;
    rdfs:label "OCBV capability categories"@en .
```
{% endraw %}
