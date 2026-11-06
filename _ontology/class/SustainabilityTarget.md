---
title: "ontosage:SustainabilityTarget"
layout: post
permalink: /ontology/class/SustainabilityTarget/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › SustainabilityTarget

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#SustainabilityTarget` |
| Label | Sustainability target |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A published institutional commitment against which progress is reported: a diversion rate, a carbon reduction, a consumption ceiling. Authored and cited, NEVER inferred - a target derived from the data it is meant to judge would make every trend look like success or failure by construction.

## Examples

- "are we on track for our recycling target?" -&gt; compare measured diversion against THIS, and say who set it.

## Lay terms

Plain-language phrases declared on this term with `ontosage:layTerms`. A question that contains one of them can be matched to this term. (17)

`are we on track`, `carbon emissions`, `carbon footprint`, `carbon neutral`, `carbon reduction`, `carbon target`, `emissions`, `emissions target`, `energy reduction`, `environmental target`, `net zero`, `reduction target`, `scope 1`, `scope 2`, `sustainability commitment`, `sustainability target`, `sustainability targets`

## Class hierarchy

Superclasses:

- [`ontosage:Record`]({{ '/ontology/class/Record/' | relative_url }}) › **`ontosage:SustainabilityTarget`**

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:targetAuthority`]({{ '/ontology/property/targetAuthority/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:targetBaselinePeriod`]({{ '/ontology/property/targetBaselinePeriod/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:targetDate`]({{ '/ontology/property/targetDate/' | relative_url }}) | datatype | `xsd:date` | this class |
| [`ontosage:targetMetric`]({{ '/ontology/property/targetMetric/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:targetUnit`]({{ '/ontology/property/targetUnit/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:targetValue`]({{ '/ontology/property/targetValue/' | relative_url }}) | datatype | `xsd:decimal` | this class |

## Record document mapping

Record documents of type `sustainability_target` are lifted into instances of this class ([mapping]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#sustainability_target)).

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:SustainabilityTarget a owl:Class ;
    rdfs:label "Sustainability target"@en ;
    ontosage:layTerms "are we on track",
        "carbon emissions",
        "carbon footprint",
        "carbon neutral",
        "carbon reduction",
        "carbon target",
        "emissions",
        "emissions target",
        "energy reduction",
        "environmental target",
        "net zero",
        "reduction target",
        "scope 1",
        "scope 2",
        "sustainability commitment",
        "sustainability target",
        "sustainability targets" ;
    rdfs:comment "A published institutional commitment against which progress is reported: a diversion rate, a carbon reduction, a consumption ceiling. Authored and cited, NEVER inferred - a target derived from the data it is meant to judge would make every trend look like success or failure by construction."@en ;
    rdfs:subClassOf ontosage:Record ;
    skos:example "\"are we on track for our recycling target?\" -> compare measured diversion against THIS, and say who set it." .
```
{% endraw %}
