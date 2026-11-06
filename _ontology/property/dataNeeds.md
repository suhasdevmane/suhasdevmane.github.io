---
title: "ontosage:dataNeeds"
layout: post
permalink: /ontology/property/dataNeeds/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › dataNeeds

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#dataNeeds` |
| Label | data needs |
| Kind | datatype property |
| Domain | [`ontosage:StakeholderGroup`]({{ '/ontology/class/StakeholderGroup/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The kinds of building data this group asks for, in their own words.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`stakeholder_group`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#stakeholder_group) | `data_needs` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:dataNeeds a owl:DatatypeProperty ;
    rdfs:label "data needs"@en ;
    rdfs:comment "The kinds of building data this group asks for, in their own words."@en ;
    rdfs:domain ontosage:StakeholderGroup ;
    rdfs:range xsd:string .
```
{% endraw %}
