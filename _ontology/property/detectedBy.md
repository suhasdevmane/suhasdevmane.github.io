---
title: "ontosage:detectedBy"
layout: post
permalink: /ontology/property/detectedBy/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › detectedBy

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#detectedBy` |
| Label | detected by |
| Kind | datatype property |
| Domain | [`ontosage:AnomalyEvent`]({{ '/ontology/class/AnomalyEvent/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Detector id, e.g. seasonal\_residual, stuck\_sensor.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:detectedBy a owl:DatatypeProperty ;
    rdfs:label "detected by"@en ;
    rdfs:comment "Detector id, e.g. seasonal_residual, stuck_sensor."@en ;
    rdfs:domain ontosage:AnomalyEvent ;
    rdfs:range xsd:string .
```
{% endraw %}
