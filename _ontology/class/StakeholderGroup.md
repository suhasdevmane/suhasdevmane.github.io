---
title: "ontosage:StakeholderGroup"
layout: post
permalink: /ontology/class/StakeholderGroup/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › StakeholderGroup

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#StakeholderGroup` |
| Label | Stakeholder group |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A category of person the building serves, recorded with what they need from it, which department serves them, what they are accountable for, when they are present and how far their access reaches. DISTINCT FROM ontosage:StakeholderRole, which is a conversational persona that biases answer framing: this is operational data about a group, with an owner and effective dates, and it is a Record for that reason. No individual is modelled — a group is the finest grain this register goes to.

## Examples

- who serves visitors, and what can they see? -&gt; StakeholderGroup for visitors, read servedByDepartment and accessTier.

## Lay terms

Plain-language phrases declared on this term with `ontosage:layTerms`. A question that contains one of them can be matched to this term. (11)

`building users`, `occupant group`, `stakeholder`, `stakeholder group`, `stakeholders`, `user group`, `which groups`, `who does this affect`, `who is affected`, `who needs to know`, `who uses the building`

## Class hierarchy

Superclasses:

- [`ontosage:Record`]({{ '/ontology/class/Record/' | relative_url }}) › **`ontosage:StakeholderGroup`**

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:accessTier`]({{ '/ontology/property/accessTier/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:accountableFor`]({{ '/ontology/property/accountableFor/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:dataNeeds`]({{ '/ontology/property/dataNeeds/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:presencePattern`]({{ '/ontology/property/presencePattern/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:primaryNeed`]({{ '/ontology/property/primaryNeed/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:servedByDepartment`]({{ '/ontology/property/servedByDepartment/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:stakeholderCategory`]({{ '/ontology/property/stakeholderCategory/' | relative_url }}) | datatype | `xsd:string` | this class |

## Record document mapping

Record documents of type `stakeholder_group` are lifted into instances of this class ([mapping]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#stakeholder_group)).

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:StakeholderGroup a owl:Class ;
    rdfs:label "Stakeholder group"@en ;
    ontosage:layTerms "building users",
        "occupant group",
        "stakeholder",
        "stakeholder group",
        "stakeholders",
        "user group",
        "which groups",
        "who does this affect",
        "who is affected",
        "who needs to know",
        "who uses the building" ;
    rdfs:comment "A category of person the building serves, recorded with what they need from it, which department serves them, what they are accountable for, when they are present and how far their access reaches. DISTINCT FROM ontosage:StakeholderRole, which is a conversational persona that biases answer framing: this is operational data about a group, with an owner and effective dates, and it is a Record for that reason. No individual is modelled — a group is the finest grain this register goes to."@en ;
    rdfs:subClassOf ontosage:Record ;
    skos:example "who serves visitors, and what can they see? -> StakeholderGroup for visitors, read servedByDepartment and accessTier." .
```
{% endraw %}
