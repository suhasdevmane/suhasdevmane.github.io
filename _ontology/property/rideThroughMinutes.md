---
title: "ontosage:rideThroughMinutes"
layout: post
permalink: /ontology/property/rideThroughMinutes/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › rideThroughMinutes

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#rideThroughMinutes` |
| Label | ride-through minutes |
| Kind | datatype property |
| Domain | [`ontosage:ContinuityProvision`]({{ '/ontology/class/ContinuityProvision/' | relative_url }}) |
| Range | `xsd:integer` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

How long the service keeps running on its own before the alternative has to carry it — UPS autonomy, buffer tank, batch queue.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`continuity_provision`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#continuity_provision) | `ride_through_minutes` | `xsd:integer` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:rideThroughMinutes a owl:DatatypeProperty ;
    rdfs:label "ride-through minutes"@en ;
    rdfs:comment "How long the service keeps running on its own before the alternative has to carry it — UPS autonomy, buffer tank, batch queue."@en ;
    rdfs:domain ontosage:ContinuityProvision ;
    rdfs:range xsd:integer .
```
{% endraw %}
