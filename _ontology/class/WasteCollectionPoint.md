---
title: "ontosage:WasteCollectionPoint"
layout: post
permalink: /ontology/class/WasteCollectionPoint/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › WasteCollectionPoint

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#WasteCollectionPoint` |
| Label | Waste collection point |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

One bin or container: its station, what the SYSTEM records it as, what the bin is LABELLED, what its aperture physically accepts, its fill against an approved threshold, and when it is next collected. The three stream columns are separate deliberately -- a point recorded as general waste, labelled mixed recycling and fitted with a narrow slot is one people will use wrongly, and collapsing them into a single stream field makes that disagreement unrepresentable when the disagreement IS the answer. Fill threshold is per point, because a 240-litre bin in a busy atrium and a 60-litre one in a quiet corridor do not cross 'full' at the same percentage.

## Examples

- which points will cross their threshold before the next collection? -&gt; WasteCollectionPoint where fillPercent &gt;= approvedFillThreshold, read with nextDue.

## Lay terms

Plain-language phrases declared on this term with `ontosage:layTerms`. A question that contains one of them can be matched to this term. (26)

`bin`, `bin collection`, `bin collections`, `bins`, `collection frequency`, `collection point`, `collection round`, `collection rounds`, `emptied`, `fill level`, `food waste`, `full bin`, `general waste`, `missed collection`, `missed collections`, `recycling`, `recycling stream`, `recycling streams`, `refuse`, `skip`, `waste`, `waste collection`, `waste collections`, `waste station`, `waste stream`, `waste streams`

## Class hierarchy

Superclasses:

- [`ontosage:Record`]({{ '/ontology/class/Record/' | relative_url }}) › **`ontosage:WasteCollectionPoint`**

Subclasses: none.

## Properties

No property declares this class (or a superclass) as its domain.

## Record document mapping

Record documents of type `waste_collection` are lifted into instances of this class ([mapping]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#waste_collection)).

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:WasteCollectionPoint a owl:Class ;
    rdfs:label "Waste collection point"@en ;
    ontosage:layTerms "bin",
        "bin collection",
        "bin collections",
        "bins",
        "collection frequency",
        "collection point",
        "collection round",
        "collection rounds",
        "emptied",
        "fill level",
        "food waste",
        "full bin",
        "general waste",
        "missed collection",
        "missed collections",
        "recycling",
        "recycling stream",
        "recycling streams",
        "refuse",
        "skip",
        "waste",
        "waste collection",
        "waste collections",
        "waste station",
        "waste stream",
        "waste streams" ;
    rdfs:comment "One bin or container: its station, what the SYSTEM records it as, what the bin is LABELLED, what its aperture physically accepts, its fill against an approved threshold, and when it is next collected. The three stream columns are separate deliberately -- a point recorded as general waste, labelled mixed recycling and fitted with a narrow slot is one people will use wrongly, and collapsing them into a single stream field makes that disagreement unrepresentable when the disagreement IS the answer. Fill threshold is per point, because a 240-litre bin in a busy atrium and a 60-litre one in a quiet corridor do not cross 'full' at the same percentage."@en ;
    rdfs:subClassOf ontosage:Record ;
    skos:example "which points will cross their threshold before the next collection? -> WasteCollectionPoint where fillPercent >= approvedFillThreshold, read with nextDue." .
```
{% endraw %}
