---
title: "ontosage:accessTier"
layout: post
permalink: /ontology/property/accessTier/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › accessTier

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#accessTier` |
| Label | access tier |
| Kind | datatype property |
| Domain | [`ontosage:StakeholderGroup`]({{ '/ontology/class/StakeholderGroup/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

How far this group's access reaches: public, visitor, occupant, staff, operational or restricted. Advisory context for an answer — the PDP, not this field, decides what is released.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`stakeholder_group`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#stakeholder_group) | `access_tier` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:accessTier a owl:DatatypeProperty ;
    rdfs:label "access tier"@en ;
    rdfs:comment "How far this group's access reaches: public, visitor, occupant, staff, operational or restricted. Advisory context for an answer — the PDP, not this field, decides what is released."@en ;
    rdfs:domain ontosage:StakeholderGroup ;
    rdfs:range xsd:string .
```
{% endraw %}
