---
title: "ontosage:WorkOrder"
layout: post
permalink: /ontology/class/WorkOrder/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › WorkOrder

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#WorkOrder` |
| Label | Work order |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A maintenance task with an open-&gt;assigned-&gt;done lifecycle.

## Examples

- "how many overdue tickets?" -&gt; count WorkOrder where status=open and start older than SLA.

## Lay terms

Plain-language phrases declared on this term with `ontosage:layTerms`. A question that contains one of them can be matched to this term. (42)

`assigned task`, `assigned tasks`, `been serviced`, `blocked drain`, `drain blockage`, `drain clearance`, `drain jetting`, `get serviced`, `gets serviced`, `jetting`, `job`, `jobs`, `last maintained`, `last serviced`, `last time that`, `maintenance carried out`, `maintenance done`, `maintenance history`, `maintenance job`, `maintenance log`, `maintenance tasks are overdue`, `maintenance tasks overdue`, `maintenance was carried out`, `maintenance was done`, `maintenance work`, `overdue maintenance tasks`, `reactive job`, `rectification`, `remedial`, `remedial scope`, `remedial work`, `repairs carried out`, `repairs done`, `task at risk`, `tasks at risk`, `ticket`, `tickets`, `work carried out`, `work completed`, `work done`, `work order`, `work orders`

## Class hierarchy

Superclasses:

- [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) › **`ontosage:WorkOrder`**

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:jobHours`]({{ '/ontology/property/jobHours/' | relative_url }}) | datatype | `xsd:decimal` | this class |
| [`ontosage:aboutPoint`]({{ '/ontology/property/aboutPoint/' | relative_url }}) | object | [`brick:Point`](https://ontology.brickschema.org/1.4/#brick:Point) | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:aboutSpace`]({{ '/ontology/property/aboutSpace/' | relative_url }}) | object | [`brick:Location`](https://ontology.brickschema.org/1.4/#brick:Location) | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:completedDate`]({{ '/ontology/property/completedDate/' | relative_url }}) | datatype | `xsd:dateTime` | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:coveredScope`]({{ '/ontology/property/coveredScope/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:coversAsset`]({{ '/ontology/property/coversAsset/' | relative_url }}) | object | [`brick:Equipment`](https://ontology.brickschema.org/1.4/#brick:Equipment) | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:derivedFromDocument`]({{ '/ontology/property/derivedFromDocument/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:liftedByMapping`]({{ '/ontology/property/liftedByMapping/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:owningAuthority`]({{ '/ontology/property/owningAuthority/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:providerName`]({{ '/ontology/property/providerName/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:recordOwner`]({{ '/ontology/property/recordOwner/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:recordVersion`]({{ '/ontology/property/recordVersion/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:responsibleRole`]({{ '/ontology/property/responsibleRole/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:retrievedAt`]({{ '/ontology/property/retrievedAt/' | relative_url }}) | datatype | `xsd:dateTime` | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:supersedes`]({{ '/ontology/property/supersedes/' | relative_url }}) | object | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |

## Record document mapping

Record documents of type `work_order` are lifted into instances of this class ([mapping]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#work_order)).

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:WorkOrder a owl:Class ;
    rdfs:label "Work order"@en ;
    ontosage:layTerms "assigned task",
        "assigned tasks",
        "been serviced",
        "blocked drain",
        "drain blockage",
        "drain clearance",
        "drain jetting",
        "get serviced",
        "gets serviced",
        "jetting",
        "job",
        "jobs",
        "last maintained",
        "last serviced",
        "last time that",
        "maintenance carried out",
        "maintenance done",
        "maintenance history",
        "maintenance job",
        "maintenance log",
        "maintenance tasks are overdue",
        "maintenance tasks overdue",
        "maintenance was carried out",
        "maintenance was done",
        "maintenance work",
        "overdue maintenance tasks",
        "reactive job",
        "rectification",
        "remedial",
        "remedial scope",
        "remedial work",
        "repairs carried out",
        "repairs done",
        "task at risk",
        "tasks at risk",
        "ticket",
        "tickets",
        "work carried out",
        "work completed",
        "work done",
        "work order",
        "work orders" ;
    rdfs:comment "A maintenance task with an open->assigned->done lifecycle."@en ;
    rdfs:subClassOf ontosage:IntervalRecord ;
    skos:example "\"how many overdue tickets?\" -> count WorkOrder where status=open and start older than SLA." .
```
{% endraw %}
