---
title: "ontosage:EvacuationProvision"
layout: post
permalink: /ontology/class/EvacuationProvision/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › EvacuationProvision

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#EvacuationProvision` |
| Label | Evacuation provision |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A named arrangement for getting a person out of the building who cannot simply walk down the stairs: a refuge point, an evacuation chair, a communication unit, or a personal emergency evacuation plan held at role level. Deliberately does NOT record who any plan belongs to — the plan's EXISTENCE, location and review date are operational facts anyone may need; its subject is not.

## Examples

- which refuge points have a working communication unit? -&gt; EvacuationProvision of kind refuge, read provisionState.

## Lay terms

Plain-language phrases declared on this term with `ontosage:layTerms`. A question that contains one of them can be matched to this term. (13)

`assisted escape`, `assisted evacuation`, `communication unit`, `evacuation chair`, `evacuation chairs`, `evacuation provision`, `how do i get out`, `peep`, `peeps`, `personal emergency evacuation plan`, `refuge`, `refuge point`, `refuge points`

## Class hierarchy

Superclasses:

- [`ontosage:Record`]({{ '/ontology/class/Record/' | relative_url }}) › **`ontosage:EvacuationProvision`**

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:provisionKind`]({{ '/ontology/property/provisionKind/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:provisionState`]({{ '/ontology/property/provisionState/' | relative_url }}) | datatype | `xsd:string` | this class |

## Record document mapping

Record documents of type `evacuation_provision` are lifted into instances of this class ([mapping]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#evacuation_provision)).

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:EvacuationProvision a owl:Class ;
    rdfs:label "Evacuation provision"@en ;
    ontosage:layTerms "assisted escape",
        "assisted evacuation",
        "communication unit",
        "evacuation chair",
        "evacuation chairs",
        "evacuation provision",
        "how do i get out",
        "peep",
        "peeps",
        "personal emergency evacuation plan",
        "refuge",
        "refuge point",
        "refuge points" ;
    rdfs:comment "A named arrangement for getting a person out of the building who cannot simply walk down the stairs: a refuge point, an evacuation chair, a communication unit, or a personal emergency evacuation plan held at role level. Deliberately does NOT record who any plan belongs to — the plan's EXISTENCE, location and review date are operational facts anyone may need; its subject is not."@en ;
    rdfs:subClassOf ontosage:Record ;
    skos:example "which refuge points have a working communication unit? -> EvacuationProvision of kind refuge, read provisionState." .
```
{% endraw %}
