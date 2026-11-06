---
title: "ontosage:Department"
layout: post
permalink: /ontology/class/Department/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › Department

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Department` |
| Label | Department |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

An organisational function that operates, maintains, secures or administers the building, with its scope, coverage hours, agreed response target, request channel and escalation route recorded as data. Names functions and contact routes only — never individuals.

## Examples

- who do I contact about a broken door closer, and how fast should they respond? -&gt; Department whose serviceScope covers doors, read requestChannel and respondsWithinHours.

## Lay terms

Plain-language phrases declared on this term with `ontosage:layTerms`. A question that contains one of them can be matched to this term. (29)

`accountable owner`, `accountable owners`, `contact route`, `contact routes`, `department`, `departments`, `duty officer`, `duty officers`, `escalation route`, `escalation routes`, `helpdesk`, `maintenance crew`, `maintenance crews`, `maintenance department`, `maintenance staff`, `maintenance team`, `maintenance teams`, `out of hours`, `response target`, `response targets`, `responsible department`, `responsible departments`, `service desk`, `service desks`, `which team handles`, `who do i contact`, `who is my contact`, `who is responsible`, `who should i report this to`

## Class hierarchy

Superclasses:

- [`ontosage:Record`]({{ '/ontology/class/Record/' | relative_url }}) › **`ontosage:Department`**

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:departmentFunction`]({{ '/ontology/property/departmentFunction/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:escalatesTo`]({{ '/ontology/property/escalatesTo/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:outOfHoursRoute`]({{ '/ontology/property/outOfHoursRoute/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:requestChannel`]({{ '/ontology/property/requestChannel/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:respondsWithinHours`]({{ '/ontology/property/respondsWithinHours/' | relative_url }}) | datatype | `xsd:decimal` | this class |
| [`ontosage:serviceScope`]({{ '/ontology/property/serviceScope/' | relative_url }}) | datatype | `xsd:string` | this class |

## Record document mapping

Record documents of type `department` are lifted into instances of this class ([mapping]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#department)).

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:Department a owl:Class ;
    rdfs:label "Department"@en ;
    ontosage:layTerms "accountable owner",
        "accountable owners",
        "contact route",
        "contact routes",
        "department",
        "departments",
        "duty officer",
        "duty officers",
        "escalation route",
        "escalation routes",
        "helpdesk",
        "maintenance crew",
        "maintenance crews",
        "maintenance department",
        "maintenance staff",
        "maintenance team",
        "maintenance teams",
        "out of hours",
        "response target",
        "response targets",
        "responsible department",
        "responsible departments",
        "service desk",
        "service desks",
        "which team handles",
        "who do i contact",
        "who is my contact",
        "who is responsible",
        "who should i report this to" ;
    rdfs:comment "An organisational function that operates, maintains, secures or administers the building, with its scope, coverage hours, agreed response target, request channel and escalation route recorded as data. Names functions and contact routes only — never individuals."@en ;
    rdfs:subClassOf ontosage:Record ;
    skos:example "who do I contact about a broken door closer, and how fast should they respond? -> Department whose serviceScope covers doors, read requestChannel and respondsWithinHours." .
```
{% endraw %}
