---
title: "ontosage:treatmentRoute"
layout: post
permalink: /ontology/property/treatmentRoute/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › treatmentRoute

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#treatmentRoute` |
| Label | treatment route |
| Kind | datatype property |
| Domain | [`ontosage:WasteReturn`]({{ '/ontology/class/WasteReturn/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Where the stream goes: energy from waste, materials recovery, paper mill, anaerobic digestion, WEEE recycler.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`waste_return`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#waste_return) | `treatment` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:treatmentRoute a owl:DatatypeProperty ;
    rdfs:label "treatment route"@en ;
    rdfs:comment "Where the stream goes: energy from waste, materials recovery, paper mill, anaerobic digestion, WEEE recycler."@en ;
    rdfs:domain ontosage:WasteReturn ;
    rdfs:range xsd:string .
```
{% endraw %}
