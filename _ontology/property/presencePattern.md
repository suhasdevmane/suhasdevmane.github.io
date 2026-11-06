---
title: "ontosage:presencePattern"
layout: post
permalink: /ontology/property/presencePattern/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › presencePattern

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#presencePattern` |
| Label | presence pattern |
| Kind | datatype property |
| Domain | [`ontosage:StakeholderGroup`]({{ '/ontology/class/StakeholderGroup/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

When this group is typically in the building. The field that makes 'who is affected by a Saturday shutdown?' answerable.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`stakeholder_group`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#stakeholder_group) | `presence` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:presencePattern a owl:DatatypeProperty ;
    rdfs:label "presence pattern"@en ;
    rdfs:comment "When this group is typically in the building. The field that makes 'who is affected by a Saturday shutdown?' answerable."@en ;
    rdfs:domain ontosage:StakeholderGroup ;
    rdfs:range xsd:string .
```
{% endraw %}
