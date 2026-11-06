---
title: "ontosage:zoneValidated"
layout: post
permalink: /ontology/property/zoneValidated/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › zoneValidated

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#zoneValidated` |
| Label | zone validated |
| Kind | datatype property |
| Domain | [`ontosage:ServedZone`]({{ '/ontology/class/ServedZone/' | relative_url }}) |
| Range | `xsd:boolean` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

True only when the serving relation has been checked against the mechanical design or a commissioning survey. ABSENT OR FALSE MEANS THE ZONE DOES NOT COUNT: the spatial-adequacy gate treats an unvalidated zone as proxy evidence, so it can be reported as context but can never carry a room-level claim. Fail-closed on purpose — an unvalidated zone that were trusted is a silent substitution.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:zoneValidated a owl:DatatypeProperty ;
    rdfs:label "zone validated"@en ;
    rdfs:comment "True only when the serving relation has been checked against the mechanical design or a commissioning survey. ABSENT OR FALSE MEANS THE ZONE DOES NOT COUNT: the spatial-adequacy gate treats an unvalidated zone as proxy evidence, so it can be reported as context but can never carry a room-level claim. Fail-closed on purpose — an unvalidated zone that were trusted is a silent substitution."@en ;
    rdfs:domain ontosage:ServedZone ;
    rdfs:range xsd:boolean .
```
{% endraw %}
