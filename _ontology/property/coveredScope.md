---
title: "ontosage:coveredScope"
layout: post
permalink: /ontology/property/coveredScope/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › coveredScope

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#coveredScope` |
| Label | covered scope |
| Kind | datatype property |
| Domain | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

What a contract or warranty covers, in the words of its owner.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`competency`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#competency) | `requirement` | `xsd:string` |
| [`condition_survey`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#condition_survey) | `asset` | `xsd:string` |
| [`contract`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#contract) | `scope` | `xsd:string` |
| [`handover`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#handover) | `asset` | `xsd:string` |
| [`operating_regime`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#operating_regime) | `scope` | `xsd:string` |
| [`risk_assessment`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#risk_assessment) | `hazard` | `xsd:string` |
| [`service_schedule`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#service_schedule) | `scope` | `xsd:string` |
| [`warranty`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#warranty) | `asset` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:coveredScope a owl:DatatypeProperty ;
    rdfs:label "covered scope"@en ;
    rdfs:comment "What a contract or warranty covers, in the words of its owner."@en ;
    rdfs:domain ontosage:IntervalRecord ;
    rdfs:range xsd:string .
```
{% endraw %}
