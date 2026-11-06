---
title: "ontosage:effectiveFrom"
layout: post
permalink: /ontology/property/effectiveFrom/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › effectiveFrom

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#effectiveFrom` |
| Label | effective from |
| Kind | datatype property |
| Domain | [`ontosage:ConfigurationPeriod`]({{ '/ontology/class/ConfigurationPeriod/' | relative_url }}) |
| Range | `xsd:dateTime` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Start of the period. Inclusive.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`access_permission`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#access_permission) | `valid_from` | `xsd:date` |
| [`booking`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#booking) | `start` | `xsd:dateTime` |
| [`competency`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#competency) | `effective_from` | `xsd:date` |
| [`condition_survey`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#condition_survey) | `surveyed` | `xsd:date` |
| [`contract`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#contract) | `start` | `xsd:date` |
| [`handover`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#handover) | `issued` | `xsd:date` |
| [`incident_record`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#incident_record) | `occurred_on` | `xsd:date` |
| [`permit_to_work`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#permit_to_work) | `date` | `xsd:date` |
| [`public_event`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#public_event) | `date` | `xsd:date` |
| [`risk_assessment`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#risk_assessment) | `assessed` | `xsd:date` |
| [`tariff`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#tariff) | `start` | `xsd:date` |
| [`warranty`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#warranty) | `start` | `xsd:date` |
| [`waste_return`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#waste_return) | `period_start` | `xsd:date` |
| [`work_order`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#work_order) | `raised_on` | `xsd:date` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:effectiveFrom a owl:DatatypeProperty ;
    rdfs:label "effective from"@en ;
    rdfs:comment "Start of the period. Inclusive."@en ;
    rdfs:domain ontosage:ConfigurationPeriod ;
    rdfs:range xsd:dateTime .
```
{% endraw %}
