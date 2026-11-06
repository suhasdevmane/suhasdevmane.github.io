---
title: "ontosage:acknowledgedAt"
layout: post
permalink: /ontology/property/acknowledgedAt/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › acknowledgedAt

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#acknowledgedAt` |
| Label | acknowledged at |
| Kind | datatype property |
| Domain | [`ontosage:AlarmEvent`]({{ '/ontology/class/AlarmEvent/' | relative_url }}) |
| Range | `xsd:dateTime` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

When an operator acknowledged the alarm. ABSENT means it has never been acknowledged — not that the time is unknown — and an unacknowledged active alarm is the case an answer must surface first. Raised is effectiveFrom, cleared is effectiveTo.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:acknowledgedAt a owl:DatatypeProperty ;
    rdfs:label "acknowledged at"@en ;
    rdfs:comment "When an operator acknowledged the alarm. ABSENT means it has never been acknowledged — not that the time is unknown — and an unacknowledged active alarm is the case an answer must surface first. Raised is effectiveFrom, cleared is effectiveTo."@en ;
    rdfs:domain ontosage:AlarmEvent ;
    rdfs:range xsd:dateTime .
```
{% endraw %}
