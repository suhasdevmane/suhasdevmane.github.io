---
title: "ontosage:dueDate"
layout: post
permalink: /ontology/property/dueDate/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › dueDate

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#dueDate` |
| Label | due date |
| Kind | datatype property |
| Domain | [`ontosage:ComplianceCheck`]({{ '/ontology/class/ComplianceCheck/' | relative_url }}) |
| Range | `xsd:dateTime` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The schema gives no definition for this term.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`risk_assessment`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#risk_assessment) | `review_due` | `xsd:date` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:dueDate a owl:DatatypeProperty ;
    rdfs:label "due date"@en ;
    rdfs:domain ontosage:ComplianceCheck ;
    rdfs:range xsd:dateTime .
```
{% endraw %}
