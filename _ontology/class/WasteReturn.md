---
title: "ontosage:WasteReturn"
layout: post
permalink: /ontology/class/WasteReturn/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › WasteReturn

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#WasteReturn` |
| Label | Waste return |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

One line of the waste contractor's monthly return: the weight collected from the building in one month for one stream, how it was weighed, how it was treated and what share of it was diverted from landfill. TONNES, NOT BINS: the collection point register records containers and their fill percentage, which is not a weight. A MONTH IS NOT A FIGURE UNTIL ITS RETURN IS ISSUED -- the current month is held as pending with no weight, so a question about this month has no issued answer and the honest reply is the latest complete month, dated. HOW A WEIGHT WAS OBTAINED MATTERS: a weight estimated from container volume is an estimate and must be reported as one. The building's diverted share is weighted by tonnage, never the average of the stream percentages. Weights are for the whole building: nothing here is per floor, per room or per day.

## Examples

- how much waste did we produce last month? -&gt; WasteReturn where reportingMonth is the latest month whose status is not pending; sum wasteTonnes across streams.

## Lay terms

Plain-language phrases declared on this term with `ontosage:layTerms`. A question that contains one of them can be matched to this term. (46)

`amount of waste`, `diversion rate`, `diverted from landfill`, `how much did we recycle`, `how much do we recycle`, `how much food waste`, `how much general waste`, `how much recycling`, `how much waste`, `landfill`, `least food waste`, `least general waste`, `monthly waste`, `most food waste`, `most general waste`, `recycling percentage`, `recycling rate`, `recycling rates`, `tonnes diverted`, `tonnes of waste`, `tonnes recycled`, `waste by month`, `waste by stream`, `waste contractor return`, `waste diversion`, `waste diverted`, `waste each month`, `waste figures`, `waste generated`, `waste last month`, `waste over time`, `waste per month`, `waste produced`, `waste return`, `waste returns`, `waste this month`, `waste to landfill`, `waste tonnage`, `waste trend`, `waste weight`, `waste weights`, `weighbridge`, `weight of food waste`, `weight of general waste`, `weight of recycling`, `weight of waste`

## Class hierarchy

Superclasses:

- [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) › **`ontosage:WasteReturn`**

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:divertedPercent`]({{ '/ontology/property/divertedPercent/' | relative_url }}) | datatype | `xsd:decimal` | this class |
| [`ontosage:reportingMonth`]({{ '/ontology/property/reportingMonth/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:treatmentRoute`]({{ '/ontology/property/treatmentRoute/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:wasteTonnes`]({{ '/ontology/property/wasteTonnes/' | relative_url }}) | datatype | `xsd:decimal` | this class |
| [`ontosage:weighingMethod`]({{ '/ontology/property/weighingMethod/' | relative_url }}) | datatype | `xsd:string` | this class |
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

Record documents of type `waste_return` are lifted into instances of this class ([mapping]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#waste_return)).

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:WasteReturn a owl:Class ;
    rdfs:label "Waste return"@en ;
    ontosage:layTerms "amount of waste",
        "diversion rate",
        "diverted from landfill",
        "how much did we recycle",
        "how much do we recycle",
        "how much food waste",
        "how much general waste",
        "how much recycling",
        "how much waste",
        "landfill",
        "least food waste",
        "least general waste",
        "monthly waste",
        "most food waste",
        "most general waste",
        "recycling percentage",
        "recycling rate",
        "recycling rates",
        "tonnes diverted",
        "tonnes of waste",
        "tonnes recycled",
        "waste by month",
        "waste by stream",
        "waste contractor return",
        "waste diversion",
        "waste diverted",
        "waste each month",
        "waste figures",
        "waste generated",
        "waste last month",
        "waste over time",
        "waste per month",
        "waste produced",
        "waste return",
        "waste returns",
        "waste this month",
        "waste to landfill",
        "waste tonnage",
        "waste trend",
        "waste weight",
        "waste weights",
        "weighbridge",
        "weight of food waste",
        "weight of general waste",
        "weight of recycling",
        "weight of waste" ;
    rdfs:comment "One line of the waste contractor's monthly return: the weight collected from the building in one month for one stream, how it was weighed, how it was treated and what share of it was diverted from landfill. TONNES, NOT BINS: the collection point register records containers and their fill percentage, which is not a weight. A MONTH IS NOT A FIGURE UNTIL ITS RETURN IS ISSUED -- the current month is held as pending with no weight, so a question about this month has no issued answer and the honest reply is the latest complete month, dated. HOW A WEIGHT WAS OBTAINED MATTERS: a weight estimated from container volume is an estimate and must be reported as one. The building's diverted share is weighted by tonnage, never the average of the stream percentages. Weights are for the whole building: nothing here is per floor, per room or per day."@en ;
    rdfs:subClassOf ontosage:IntervalRecord ;
    skos:example "how much waste did we produce last month? -> WasteReturn where reportingMonth is the latest month whose status is not pending; sum wasteTonnes across streams." .
```
{% endraw %}
