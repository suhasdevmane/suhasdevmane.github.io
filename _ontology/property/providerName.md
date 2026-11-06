---
title: "ontosage:providerName"
layout: post
permalink: /ontology/property/providerName/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › providerName

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#providerName` |
| Label | provider |
| Kind | datatype property |
| Domain | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The supplier, maintainer or issuing body.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`competency`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#competency) | `authority` | `xsd:string` |
| [`condition_survey`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#condition_survey) | `surveyor` | `xsd:string` |
| [`contract`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#contract) | `provider` | `xsd:string` |
| [`cost_line`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#cost_line) | `supplier` | `xsd:string` |
| [`handover`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#handover) | `issued_by` | `xsd:string` |
| [`permit_to_work`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#permit_to_work) | `contractor` | `xsd:string` |
| [`service_schedule`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#service_schedule) | `provider` | `xsd:string` |
| [`stock_item`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#stock_item) | `supplier` | `xsd:string` |
| [`tariff`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#tariff) | `supplier` | `xsd:string` |
| [`warranty`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#warranty) | `provider` | `xsd:string` |
| [`waste_return`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#waste_return) | `contractor` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:providerName a owl:DatatypeProperty ;
    rdfs:label "provider"@en ;
    rdfs:comment "The supplier, maintainer or issuing body."@en ;
    rdfs:domain ontosage:IntervalRecord ;
    rdfs:range xsd:string .
```
{% endraw %}
