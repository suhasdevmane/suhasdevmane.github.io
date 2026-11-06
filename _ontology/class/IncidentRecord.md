---
title: "ontosage:IncidentRecord"
layout: post
permalink: /ontology/class/IncidentRecord/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › IncidentRecord

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#IncidentRecord` |
| Label | Incident record |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Something that went wrong or nearly did: injury, near miss, property damage, security breach or environmental release, with what was done immediately, what the investigation concluded, whether it is externally reportable and what remains outstanding. A near miss is recorded in the SAME register as an injury deliberately — separating them is how an organisation stops seeing that the two have the same cause.

## Examples

- which incident types recur in the same location? -&gt; IncidentRecord grouped by locationText and incidentCategory.

## Lay terms

Plain-language phrases declared on this term with `ontosage:layTerms`. A question that contains one of them can be matched to this term. (18)

`accident`, `accident report`, `accident reports`, `accidents`, `incident history`, `incident log`, `incident report`, `incident reports`, `incidents`, `injuries`, `injury`, `lessons learned`, `near miss`, `near misses`, `recurring incident`, `reportable incident`, `riddor`, `what went wrong`

## Class hierarchy

Superclasses:

- [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) › **`ontosage:IncidentRecord`**

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:actionsOutstanding`]({{ '/ontology/property/actionsOutstanding/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:externallyReportable`]({{ '/ontology/property/externallyReportable/' | relative_url }}) | datatype | `xsd:boolean` | this class |
| [`ontosage:immediateAction`]({{ '/ontology/property/immediateAction/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:incidentCategory`]({{ '/ontology/property/incidentCategory/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:incidentSeverity`]({{ '/ontology/property/incidentSeverity/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:investigationFinding`]({{ '/ontology/property/investigationFinding/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:potentialSeverity`]({{ '/ontology/property/potentialSeverity/' | relative_url }}) | datatype | `xsd:string` | this class |
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

Record documents of type `incident_record` are lifted into instances of this class ([mapping]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#incident_record)).

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:IncidentRecord a owl:Class ;
    rdfs:label "Incident record"@en ;
    ontosage:layTerms "accident",
        "accident report",
        "accident reports",
        "accidents",
        "incident history",
        "incident log",
        "incident report",
        "incident reports",
        "incidents",
        "injuries",
        "injury",
        "lessons learned",
        "near miss",
        "near misses",
        "recurring incident",
        "reportable incident",
        "riddor",
        "what went wrong" ;
    rdfs:comment "Something that went wrong or nearly did: injury, near miss, property damage, security breach or environmental release, with what was done immediately, what the investigation concluded, whether it is externally reportable and what remains outstanding. A near miss is recorded in the SAME register as an injury deliberately — separating them is how an organisation stops seeing that the two have the same cause."@en ;
    rdfs:subClassOf ontosage:IntervalRecord ;
    skos:example "which incident types recur in the same location? -> IncidentRecord grouped by locationText and incidentCategory." .
```
{% endraw %}
