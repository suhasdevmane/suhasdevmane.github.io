---
title: "ontosage:stakeholderCategory"
layout: post
permalink: /ontology/property/stakeholderCategory/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › stakeholderCategory

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#stakeholderCategory` |
| Label | stakeholder category |
| Kind | datatype property |
| Domain | [`ontosage:StakeholderGroup`]({{ '/ontology/class/StakeholderGroup/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Broad family: occupant, operations, specialist, external, governance or visitor. Used to answer 'which groups are affected' without enumerating every row.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`stakeholder_group`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#stakeholder_group) | `category` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:stakeholderCategory a owl:DatatypeProperty ;
    rdfs:label "stakeholder category"@en ;
    rdfs:comment "Broad family: occupant, operations, specialist, external, governance or visitor. Used to answer 'which groups are affected' without enumerating every row."@en ;
    rdfs:domain ontosage:StakeholderGroup ;
    rdfs:range xsd:string .
```
{% endraw %}
