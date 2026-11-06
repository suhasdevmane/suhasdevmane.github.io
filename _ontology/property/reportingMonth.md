---
title: "ontosage:reportingMonth"
layout: post
permalink: /ontology/property/reportingMonth/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › reportingMonth

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#reportingMonth` |
| Label | reporting month |
| Kind | datatype property |
| Domain | [`ontosage:WasteReturn`]({{ '/ontology/class/WasteReturn/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The calendar month a return covers, as year-month. The join key for 'last month' and 'August'.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`waste_return`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#waste_return) | `month` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:reportingMonth a owl:DatatypeProperty ;
    rdfs:label "reporting month"@en ;
    rdfs:comment "The calendar month a return covers, as year-month. The join key for 'last month' and 'August'."@en ;
    rdfs:domain ontosage:WasteReturn ;
    rdfs:range xsd:string .
```
{% endraw %}
