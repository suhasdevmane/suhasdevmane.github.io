---
title: "ontosage:HazardControl"
layout: post
permalink: /ontology/class/HazardControl/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › HazardControl

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#HazardControl` |
| Label | Hazard control |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A recognised hazard present in the building, the control applied to it, the regime that tests the control and when that test is next due. One class serves COSHH substances, local exhaust ventilation, asbestos-containing materials and water hygiene because they share exactly this shape — a hazard that is managed rather than removed, whose safety depends on a test somebody has to keep doing. Modelling them separately would have produced four near-identical registers and four places for the same question to be half-answered.

## Examples

- which hazard controls are overdue for test? -&gt; HazardControl where nextTestDue has passed.

## Lay terms

Plain-language phrases declared on this term with `ontosage:layTerms`. A question that contains one of them can be matched to this term. (16)

`asbestos`, `asbestos containing material`, `control measure`, `control measures`, `coshh`, `fume cupboard`, `fume cupboards`, `hazard`, `hazardous substance`, `hazardous substances`, `hazards`, `legionella`, `lev`, `local exhaust ventilation`, `safe to work`, `water hygiene`

## Class hierarchy

Superclasses:

- [`ontosage:Record`]({{ '/ontology/class/Record/' | relative_url }}) › **`ontosage:HazardControl`**

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:controlMeasure`]({{ '/ontology/property/controlMeasure/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:hazardCondition`]({{ '/ontology/property/hazardCondition/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:hazardKind`]({{ '/ontology/property/hazardKind/' | relative_url }}) | datatype | `xsd:string` | this class |

## Record document mapping

Record documents of type `hazard_control` are lifted into instances of this class ([mapping]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#hazard_control)).

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:HazardControl a owl:Class ;
    rdfs:label "Hazard control"@en ;
    ontosage:layTerms "asbestos",
        "asbestos containing material",
        "control measure",
        "control measures",
        "coshh",
        "fume cupboard",
        "fume cupboards",
        "hazard",
        "hazardous substance",
        "hazardous substances",
        "hazards",
        "legionella",
        "lev",
        "local exhaust ventilation",
        "safe to work",
        "water hygiene" ;
    rdfs:comment "A recognised hazard present in the building, the control applied to it, the regime that tests the control and when that test is next due. One class serves COSHH substances, local exhaust ventilation, asbestos-containing materials and water hygiene because they share exactly this shape — a hazard that is managed rather than removed, whose safety depends on a test somebody has to keep doing. Modelling them separately would have produced four near-identical registers and four places for the same question to be half-answered."@en ;
    rdfs:subClassOf ontosage:Record ;
    skos:example "which hazard controls are overdue for test? -> HazardControl where nextTestDue has passed." .
```
{% endraw %}
