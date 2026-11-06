---
title: "ontosage:wasteTonnes"
layout: post
permalink: /ontology/property/wasteTonnes/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › wasteTonnes

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#wasteTonnes` |
| Label | waste tonnes |
| Kind | datatype property |
| Domain | [`ontosage:WasteReturn`]({{ '/ontology/class/WasteReturn/' | relative_url }}) |
| Range | `xsd:decimal` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The weight collected in the month, in tonnes. Absent while the return is pending: a blank is the finding, not a zero.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`waste_return`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#waste_return) | `tonnes` | `xsd:decimal` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:wasteTonnes a owl:DatatypeProperty ;
    rdfs:label "waste tonnes"@en ;
    rdfs:comment "The weight collected in the month, in tonnes. Absent while the return is pending: a blank is the finding, not a zero."@en ;
    rdfs:domain ontosage:WasteReturn ;
    rdfs:range xsd:decimal .
```
{% endraw %}
