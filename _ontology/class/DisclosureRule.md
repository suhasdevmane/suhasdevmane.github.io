---
title: "ontosage:DisclosureRule"
layout: post
permalink: /ontology/class/DisclosureRule/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › DisclosureRule

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#DisclosureRule` |
| Label | Data disclosure rule |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A rule saying which fields of a view of the building may be shown as they stand, which must be suppressed or aggregated before sharing, which need a caveat and which must be confirmed by their owner first. Declared so that a question about those rules is recognised as one about a register the building may not hold, and is answered by naming what is and is not recorded — instead of by describing a different view of the building that happens to share the words 'space' and 'fields'.

## Examples

- which fields must be suppressed before this view is shared? -&gt; DisclosureRule where appliesTo matches; none held means the rules are not recorded.

## Lay terms

Plain-language phrases declared on this term with `ontosage:layTerms`. A question that contains one of them can be matched to this term. (13)

`aggregated, caveated`, `caveated or confirmed`, `confirmed by an owner`, `data sharing rule`, `data sharing rules`, `disclosure rule`, `disclosure rules`, `fields must be suppressed`, `fields to suppress`, `must be suppressed`, `suppressed, aggregated`, `suppression rule`, `suppression rules`

## Class hierarchy

Superclasses:

- [`ontosage:Record`]({{ '/ontology/class/Record/' | relative_url }}) › **`ontosage:DisclosureRule`**

Subclasses: none.

## Properties

No property declares this class (or a superclass) as its domain.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:DisclosureRule a owl:Class ;
    rdfs:label "Data disclosure rule"@en ;
    ontosage:layTerms "aggregated, caveated",
        "caveated or confirmed",
        "confirmed by an owner",
        "data sharing rule",
        "data sharing rules",
        "disclosure rule",
        "disclosure rules",
        "fields must be suppressed",
        "fields to suppress",
        "must be suppressed",
        "suppressed, aggregated",
        "suppression rule",
        "suppression rules" ;
    rdfs:comment "A rule saying which fields of a view of the building may be shown as they stand, which must be suppressed or aggregated before sharing, which need a caveat and which must be confirmed by their owner first. Declared so that a question about those rules is recognised as one about a register the building may not hold, and is answered by naming what is and is not recorded — instead of by describing a different view of the building that happens to share the words 'space' and 'fields'."@en ;
    rdfs:subClassOf ontosage:Record ;
    skos:example "which fields must be suppressed before this view is shared? -> DisclosureRule where appliesTo matches; none held means the rules are not recorded." .
```
{% endraw %}
