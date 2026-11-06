---
title: "ontosage:OperatingRegime"
layout: post
permalink: /ontology/class/OperatingRegime/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › OperatingRegime

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#OperatingRegime` |
| Label | Operating regime |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

How a building system is SUPPOSED to run: its setpoints, its occupied and unoccupied schedules, its seasonal changeover and the deviations that are approved rather than faults.

## Examples

- is this zone running outside its approved window, and is the exception justified? -&gt; OperatingRegime for the system, compare with the live reading.

## Lay terms

Plain-language phrases declared on this term with `ontosage:layTerms`. A question that contains one of them can be matched to this term. (34)

`approved exception`, `approved exceptions`, `beyond approved`, `control strategy`, `cooling season`, `heating schedule`, `heating season`, `how is it supposed to run`, `hvac schedule`, `normal hours`, `occupied hours`, `operating condition`, `operating conditions`, `operating regime`, `operating window`, `operating windows`, `outside approved hours`, `outside its window`, `outside normal hours`, `plant schedule`, `ran early`, `ran late`, `runs outside`, `seasonal changeover`, `service window`, `service windows`, `setpoint`, `setpoints`, `start late`, `started late`, `stop late`, `stopped late`, `unoccupied`, `ventilation schedule`

## Class hierarchy

Superclasses:

- [`ontosage:Record`]({{ '/ontology/class/Record/' | relative_url }}) › **`ontosage:OperatingRegime`**

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:approvedException`]({{ '/ontology/property/approvedException/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:occupiedSetpoint`]({{ '/ontology/property/occupiedSetpoint/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:operatingWindow`]({{ '/ontology/property/operatingWindow/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:seasonalChangeover`]({{ '/ontology/property/seasonalChangeover/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:unoccupiedSetpoint`]({{ '/ontology/property/unoccupiedSetpoint/' | relative_url }}) | datatype | `xsd:string` | this class |

## Record document mapping

Record documents of type `operating_regime` are lifted into instances of this class ([mapping]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#operating_regime)).

## Turtle

Development notes were removed from one or more text values below; the source file holds the full text.

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:OperatingRegime a owl:Class ;
    rdfs:label "Operating regime"@en ;
    ontosage:layTerms "approved exception",
        "approved exceptions",
        "beyond approved",
        "control strategy",
        "cooling season",
        "heating schedule",
        "heating season",
        "how is it supposed to run",
        "hvac schedule",
        "normal hours",
        "occupied hours",
        "operating condition",
        "operating conditions",
        "operating regime",
        "operating window",
        "operating windows",
        "outside approved hours",
        "outside its window",
        "outside normal hours",
        "plant schedule",
        "ran early",
        "ran late",
        "runs outside",
        "seasonal changeover",
        "service window",
        "service windows",
        "setpoint",
        "setpoints",
        "start late",
        "started late",
        "stop late",
        "stopped late",
        "unoccupied",
        "ventilation schedule" ;
    rdfs:comment "How a building system is SUPPOSED to run: its setpoints, its occupied and unoccupied schedules, its seasonal changeover and the deviations that are approved rather than faults."@en ;
    rdfs:subClassOf ontosage:Record ;
    skos:example "is this zone running outside its approved window, and is the exception justified? -> OperatingRegime for the system, compare with the live reading." .
```
{% endraw %}
