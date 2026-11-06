---
title: "ontosage:accountableFor"
layout: post
permalink: /ontology/property/accountableFor/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › accountableFor

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#accountableFor` |
| Label | accountable for |
| Kind | datatype property |
| Domain | [`ontosage:StakeholderGroup`]({{ '/ontology/class/StakeholderGroup/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

What this group is answerable for, if anything. Blank for groups the building serves rather than groups that run it.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`stakeholder_group`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#stakeholder_group) | `accountable_for` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:accountableFor a owl:DatatypeProperty ;
    rdfs:label "accountable for"@en ;
    rdfs:comment "What this group is answerable for, if anything. Blank for groups the building serves rather than groups that run it."@en ;
    rdfs:domain ontosage:StakeholderGroup ;
    rdfs:range xsd:string .
```
{% endraw %}
