---
title: "ontosage:AnomalyEvent"
layout: post
permalink: /ontology/class/AnomalyEvent/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › AnomalyEvent

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#AnomalyEvent` |
| Label | Anomaly episode |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A persisted detector finding with a stable id: one episode per contiguous deviation (extended while it persists, closed when readings normalise).

## Examples

- "summarise this week's anomalies" -&gt; AnomalyEvent episodes overlapping the week.

## Lay terms

Plain-language phrases declared on this term with `ontosage:layTerms`. A question that contains one of them can be matched to this term. (8)

`abnormal reading`, `anomalies`, `anomaly`, `odd reading`, `out of range`, `outlier`, `unusual reading`, `unusual readings`

## Class hierarchy

Superclasses:

- [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) › **`ontosage:AnomalyEvent`**

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:baselineValue`]({{ '/ontology/property/baselineValue/' | relative_url }}) | datatype | `xsd:double` | this class |
| [`ontosage:detectedBy`]({{ '/ontology/property/detectedBy/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:observedValue`]({{ '/ontology/property/observedValue/' | relative_url }}) | datatype | `xsd:double` | this class |
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

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:AnomalyEvent a owl:Class ;
    rdfs:label "Anomaly episode"@en ;
    ontosage:layTerms "abnormal reading",
        "anomalies",
        "anomaly",
        "odd reading",
        "out of range",
        "outlier",
        "unusual reading",
        "unusual readings" ;
    rdfs:comment "A persisted detector finding with a stable id: one episode per contiguous deviation (extended while it persists, closed when readings normalise)."@en ;
    rdfs:subClassOf ontosage:IntervalRecord ;
    skos:example "\"summarise this week's anomalies\" -> AnomalyEvent episodes overlapping the week." .
```
{% endraw %}
