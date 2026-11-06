---
title: "ontosage:primaryNeed"
layout: post
permalink: /ontology/property/primaryNeed/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › primaryNeed

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#primaryNeed` |
| Label | primary need |
| Kind | datatype property |
| Domain | [`ontosage:StakeholderGroup`]({{ '/ontology/class/StakeholderGroup/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

What this group mostly comes to the building's data for.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`stakeholder_group`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#stakeholder_group) | `primary_need` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:primaryNeed a owl:DatatypeProperty ;
    rdfs:label "primary need"@en ;
    rdfs:comment "What this group mostly comes to the building's data for."@en ;
    rdfs:domain ontosage:StakeholderGroup ;
    rdfs:range xsd:string .
```
{% endraw %}
