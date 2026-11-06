---
title: "ontosage:AssetEngineeringProfile"
layout: post
permalink: /ontology/class/AssetEngineeringProfile/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › AssetEngineeringProfile

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#AssetEngineeringProfile` |
| Label | Asset engineering profile |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The engineering truth about a plant item: what it was designed for, what commissioning proved, what it is observed to deliver, where it is isolated, what depends on it downstream, what it is called in every other system, how critical it is, and how long it goes unvisited. The building recorded that an AHU exists and never recorded what it was for.

## Examples

- what duty was this designed for and what is it delivering? -&gt; AssetEngineeringProfile, compare designDuty, commissionedDuty and observedDuty with their evidence.

## Lay terms

Plain-language phrases declared on this term with `ontosage:layTerms`. A question that contains one of them can be matched to this term. (46)

`asset chain`, `asset hierarchy`, `asset reconciliation`, `asset record`, `asset records`, `asset register`, `asset registers`, `asset tag`, `asset tags`, `blind interval`, `commissioned duty`, `commissioned for`, `commissioning`, `commissioning record`, `continuity critical`, `criticality`, `design duty`, `design intent`, `designed and commissioned`, `designed for`, `downstream dependencies`, `engineering system`, `engineering systems`, `irreplaceable`, `isolation`, `isolation point`, `isolation points`, `location verified`, `m and e asset`, `mechanical and electrical asset`, `parent asset`, `plant item`, `plant items`, `rarely visited`, `reconcile`, `reconciled`, `recorded location`, `replacement value`, `riser contents`, `safe isolation`, `served area`, `serves area`, `service dependencies`, `service dependency`, `services in the void`, `tag consistency`

## Class hierarchy

Superclasses:

- [`ontosage:Record`]({{ '/ontology/class/Record/' | relative_url }}) › **`ontosage:AssetEngineeringProfile`**

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:commissionedDuty`]({{ '/ontology/property/commissionedDuty/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:criticality`]({{ '/ontology/property/criticality/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:designDuty`]({{ '/ontology/property/designDuty/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:downstreamDependencies`]({{ '/ontology/property/downstreamDependencies/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:dutyEvidence`]({{ '/ontology/property/dutyEvidence/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:engineeringSystem`]({{ '/ontology/property/engineeringSystem/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:inspectionIntervalDays`]({{ '/ontology/property/inspectionIntervalDays/' | relative_url }}) | datatype | `xsd:integer` | this class |
| [`ontosage:isolationPoint`]({{ '/ontology/property/isolationPoint/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:isolationProvenOn`]({{ '/ontology/property/isolationProvenOn/' | relative_url }}) | datatype | `xsd:date` | this class |
| [`ontosage:lastVisited`]({{ '/ontology/property/lastVisited/' | relative_url }}) | datatype | `xsd:date` | this class |
| [`ontosage:locationVerifiedOn`]({{ '/ontology/property/locationVerifiedOn/' | relative_url }}) | datatype | `xsd:date` | this class |
| [`ontosage:observedDuty`]({{ '/ontology/property/observedDuty/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:parentAsset`]({{ '/ontology/property/parentAsset/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:replaceability`]({{ '/ontology/property/replaceability/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:servesArea`]({{ '/ontology/property/servesArea/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:servicesInVoid`]({{ '/ontology/property/servicesInVoid/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:tagInBMS`]({{ '/ontology/property/tagInBMS/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:tagInMaintenance`]({{ '/ontology/property/tagInMaintenance/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:tagOnDrawings`]({{ '/ontology/property/tagOnDrawings/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:valueBand`]({{ '/ontology/property/valueBand/' | relative_url }}) | datatype | `xsd:string` | this class |

## Record document mapping

Record documents of type `asset_engineering` are lifted into instances of this class ([mapping]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#asset_engineering)).

## Turtle

Development notes were removed from one or more text values below; the source file holds the full text.

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:AssetEngineeringProfile a owl:Class ;
    rdfs:label "Asset engineering profile"@en ;
    ontosage:layTerms "asset chain",
        "asset hierarchy",
        "asset reconciliation",
        "asset record",
        "asset records",
        "asset register",
        "asset registers",
        "asset tag",
        "asset tags",
        "blind interval",
        "commissioned duty",
        "commissioned for",
        "commissioning",
        "commissioning record",
        "continuity critical",
        "criticality",
        "design duty",
        "design intent",
        "designed and commissioned",
        "designed for",
        "downstream dependencies",
        "engineering system",
        "engineering systems",
        "irreplaceable",
        "isolation",
        "isolation point",
        "isolation points",
        "location verified",
        "m and e asset",
        "mechanical and electrical asset",
        "parent asset",
        "plant item",
        "plant items",
        "rarely visited",
        "reconcile",
        "reconciled",
        "recorded location",
        "replacement value",
        "riser contents",
        "safe isolation",
        "served area",
        "serves area",
        "service dependencies",
        "service dependency",
        "services in the void",
        "tag consistency" ;
    rdfs:comment "The engineering truth about a plant item: what it was designed for, what commissioning proved, what it is observed to deliver, where it is isolated, what depends on it downstream, what it is called in every other system, how critical it is, and how long it goes unvisited. The building recorded that an AHU exists and never recorded what it was for."@en ;
    rdfs:subClassOf ontosage:Record ;
    skos:example "what duty was this designed for and what is it delivering? -> AssetEngineeringProfile, compare designDuty, commissionedDuty and observedDuty with their evidence." .
```
{% endraw %}
