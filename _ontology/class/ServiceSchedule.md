---
title: "ontosage:ServiceSchedule"
layout: post
permalink: /ontology/class/ServiceSchedule/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › ServiceSchedule

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#ServiceSchedule` |
| Label | Planned service schedule entry |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A planned recurring operation on a space: cleaning, waste collection, planned maintenance, planned shutdown. Distinct from a WorkOrder, which is reactive: 'when is this room next cleaned' and 'who is fixing the broken tap' are different questions with different sources.

## Lay terms

Plain-language phrases declared on this term with `ontosage:layTerms`. A question that contains one of them can be matched to this term. (48)

`ahu filters`, `air filters`, `due for service`, `filter change`, `filter changes`, `filter cleaning`, `filter maintenance`, `filter replacement`, `filters changed`, `filters cleaned`, `filters maintained`, `how often are filters`, `how often are the filters`, `how often are they maintained`, `how often are they serviced`, `how often is it maintained`, `how often is it serviced`, `last completed`, `maintenance due`, `maintenance frequency`, `maintenance interval`, `maintenance is overdue`, `maintenance is planned`, `maintenance is scheduled`, `maintenance overdue`, `maintenance planned`, `maintenance schedule`, `maintenance scheduled`, `maintenance task scheduled`, `maintenance tasks scheduled`, `next due`, `overdue for maintenance`, `overdue for service`, `overdue for servicing`, `overdue maintenance`, `planned maintenance`, `planned preventive maintenance`, `ppm`, `scheduled maintenance`, `scheduled service`, `service frequency`, `service interval`, `service schedule`, `service schedules`, `servicing frequency`, `servicing interval`, `servicing schedule`, `when is it next serviced`

## Class hierarchy

Superclasses:

- [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) › **`ontosage:ServiceSchedule`**

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:isStatutory`]({{ '/ontology/property/isStatutory/' | relative_url }}) | datatype | `xsd:boolean` | this class |
| [`ontosage:scheduleKind`]({{ '/ontology/property/scheduleKind/' | relative_url }}) | datatype | `xsd:string` | this class |
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

Record documents of type `service_schedule` are lifted into instances of this class ([mapping]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#service_schedule)).

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ontosage:ServiceSchedule a owl:Class ;
    rdfs:label "Planned service schedule entry"@en ;
    ontosage:layTerms "ahu filters",
        "air filters",
        "due for service",
        "filter change",
        "filter changes",
        "filter cleaning",
        "filter maintenance",
        "filter replacement",
        "filters changed",
        "filters cleaned",
        "filters maintained",
        "how often are filters",
        "how often are the filters",
        "how often are they maintained",
        "how often are they serviced",
        "how often is it maintained",
        "how often is it serviced",
        "last completed",
        "maintenance due",
        "maintenance frequency",
        "maintenance interval",
        "maintenance is overdue",
        "maintenance is planned",
        "maintenance is scheduled",
        "maintenance overdue",
        "maintenance planned",
        "maintenance schedule",
        "maintenance scheduled",
        "maintenance task scheduled",
        "maintenance tasks scheduled",
        "next due",
        "overdue for maintenance",
        "overdue for service",
        "overdue for servicing",
        "overdue maintenance",
        "planned maintenance",
        "planned preventive maintenance",
        "ppm",
        "scheduled maintenance",
        "scheduled service",
        "service frequency",
        "service interval",
        "service schedule",
        "service schedules",
        "servicing frequency",
        "servicing interval",
        "servicing schedule",
        "when is it next serviced" ;
    rdfs:comment "A planned recurring operation on a space: cleaning, waste collection, planned maintenance, planned shutdown. Distinct from a WorkOrder, which is reactive: 'when is this room next cleaned' and 'who is fixing the broken tap' are different questions with different sources."@en ;
    rdfs:subClassOf ontosage:IntervalRecord .
```
{% endraw %}
