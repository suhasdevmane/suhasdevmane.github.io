---
title: "ontosage:targetMetric"
layout: post
permalink: /ontology/property/targetMetric/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › targetMetric

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#targetMetric` |
| Label | target metric |
| Kind | datatype property |
| Domain | [`ontosage:SustainabilityTarget`]({{ '/ontology/class/SustainabilityTarget/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

What is being targeted, in the same terms the measurement uses: diversion\_rate | carbon\_intensity | energy\_intensity | water\_per\_capita | waste\_per\_capita.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`sustainability_target`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#sustainability_target) | `metric` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:targetMetric a owl:DatatypeProperty ;
    rdfs:label "target metric"@en ;
    rdfs:comment "What is being targeted, in the same terms the measurement uses: diversion_rate | carbon_intensity | energy_intensity | water_per_capita | waste_per_capita."@en ;
    rdfs:domain ontosage:SustainabilityTarget ;
    rdfs:range xsd:string .
```
{% endraw %}
