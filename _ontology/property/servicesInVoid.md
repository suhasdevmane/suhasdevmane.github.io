---
title: "ontosage:servicesInVoid"
layout: post
permalink: /ontology/property/servicesInVoid/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › servicesInVoid

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#servicesInVoid` |
| Label | services in void |
| Kind | datatype property |
| Domain | [`ontosage:AssetEngineeringProfile`]({{ '/ontology/class/AssetEngineeringProfile/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

What runs in the ceiling, riser or floor void at this asset, graded confirmed, probable or unknown. Before intrusive work the grade matters more than the list.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`asset_engineering`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#asset_engineering) | `services_in_void` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:servicesInVoid a owl:DatatypeProperty ;
    rdfs:label "services in void"@en ;
    rdfs:comment "What runs in the ceiling, riser or floor void at this asset, graded confirmed, probable or unknown. Before intrusive work the grade matters more than the list."@en ;
    rdfs:domain ontosage:AssetEngineeringProfile ;
    rdfs:range xsd:string .
```
{% endraw %}
