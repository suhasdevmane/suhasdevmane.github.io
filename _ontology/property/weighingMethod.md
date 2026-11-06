---
title: "ontosage:weighingMethod"
layout: post
permalink: /ontology/property/weighingMethod/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › weighingMethod

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#weighingMethod` |
| Label | weighing method |
| Kind | datatype property |
| Domain | [`ontosage:WasteReturn`]({{ '/ontology/class/WasteReturn/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

How the weight was obtained: bin-lift scale, weighbridge ticket, delivery note, or estimated from container volume. An estimate is reported as one.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`waste_return`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#waste_return) | `weighing` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:weighingMethod a owl:DatatypeProperty ;
    rdfs:label "weighing method"@en ;
    rdfs:comment "How the weight was obtained: bin-lift scale, weighbridge ticket, delivery note, or estimated from container volume. An estimate is reported as one."@en ;
    rdfs:domain ontosage:WasteReturn ;
    rdfs:range xsd:string .
```
{% endraw %}
