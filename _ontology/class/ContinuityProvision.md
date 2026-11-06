---
title: "ontosage:ContinuityProvision"
layout: post
permalink: /ontology/class/ContinuityProvision/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › ContinuityProvision

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#ContinuityProvision` |
| Label | Service continuity provision |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

One service, the space or system it normally depends on, and what happens when that is unavailable: the alternative location, the path to it, the capacity that alternative can carry, how long the service can run before the alternative is needed, and when the arrangement was last proved. recordStatus is the owner's recorded state; an alternative with no proving evidence is recorded as unverified rather than as a provision, because a continuity answer that offers an untested option is worse than one that says there is none.

## Examples

- which services have a verified alternative if the server room is unavailable? -&gt; ContinuityProvision where dependsOnSpace matches and recordStatus is verified.

## Lay terms

Plain-language phrases declared on this term with `ontosage:layTerms`. A question that contains one of them can be matched to this term. (36)

`alternative location`, `alternative site`, `backup location`, `backup site`, `business continuity`, `continuity`, `critical service`, `critical services`, `critical systems`, `disaster recovery`, `displaced`, `displacement`, `during an outage`, `essential systems`, `failover`, `fallback location`, `if it becomes unavailable`, `if it is unavailable`, `if power fails`, `if the power fails`, `if unavailable`, `important systems`, `in an outage`, `keep operating`, `keep running`, `keeps operating`, `keeps running`, `operating capacity`, `priority services`, `priority systems`, `resilient`, `ride through`, `ride-through`, `standby location`, `stay running`, `stays running`

## Class hierarchy

Superclasses:

- [`ontosage:Record`]({{ '/ontology/class/Record/' | relative_url }}) › **`ontosage:ContinuityProvision`**

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:alternativeCapacity`]({{ '/ontology/property/alternativeCapacity/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:alternativeLocation`]({{ '/ontology/property/alternativeLocation/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:alternativePath`]({{ '/ontology/property/alternativePath/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:dependsOnSpace`]({{ '/ontology/property/dependsOnSpace/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:lastProvedOn`]({{ '/ontology/property/lastProvedOn/' | relative_url }}) | datatype | `xsd:date` | this class |
| [`ontosage:rideThroughMinutes`]({{ '/ontology/property/rideThroughMinutes/' | relative_url }}) | datatype | `xsd:integer` | this class |
| [`ontosage:servesService`]({{ '/ontology/property/servesService/' | relative_url }}) | datatype | `xsd:string` | this class |

## Record document mapping

Record documents of type `continuity_provision` are lifted into instances of this class ([mapping]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#continuity_provision)).

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:ContinuityProvision a owl:Class ;
    rdfs:label "Service continuity provision"@en ;
    ontosage:layTerms "alternative location",
        "alternative site",
        "backup location",
        "backup site",
        "business continuity",
        "continuity",
        "critical service",
        "critical services",
        "critical systems",
        "disaster recovery",
        "displaced",
        "displacement",
        "during an outage",
        "essential systems",
        "failover",
        "fallback location",
        "if it becomes unavailable",
        "if it is unavailable",
        "if power fails",
        "if the power fails",
        "if unavailable",
        "important systems",
        "in an outage",
        "keep operating",
        "keep running",
        "keeps operating",
        "keeps running",
        "operating capacity",
        "priority services",
        "priority systems",
        "resilient",
        "ride through",
        "ride-through",
        "standby location",
        "stay running",
        "stays running" ;
    rdfs:comment "One service, the space or system it normally depends on, and what happens when that is unavailable: the alternative location, the path to it, the capacity that alternative can carry, how long the service can run before the alternative is needed, and when the arrangement was last proved. recordStatus is the owner's recorded state; an alternative with no proving evidence is recorded as unverified rather than as a provision, because a continuity answer that offers an untested option is worse than one that says there is none."@en ;
    rdfs:subClassOf ontosage:Record ;
    skos:example "which services have a verified alternative if the server room is unavailable? -> ContinuityProvision where dependsOnSpace matches and recordStatus is verified." .
```
{% endraw %}
