---
title: "ontosage:AccessibleRoute"
layout: post
permalink: /ontology/class/AccessibleRoute/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › AccessibleRoute

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#AccessibleRoute` |
| Label | Accessible route |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A SURVEYED journey between an arrival point and a destination, carrying the facts a disabled visitor actually asks for: entrance, step-free or not, seated rests, how the doors operate, which lift and whether it is in service, how much time to allow, how busy it is, and a non-telephone assistance contact. surveyedOn and surveyedBy are required because every question this answers uses the word 'verified' — a route inferred from geometry is a guess about somebody's journey, and a wrong guess costs them the journey. A route that is NOT step-free is published too, so it is never offered as an accessible option by omission.

## Examples

- which verified route from the drop-off has seated rests, and how long should I allow? -&gt; AccessibleRoute where routeFrom matches; read seatedRests and allowMinutes.

## Lay terms

Plain-language phrases declared on this term with `ontosage:layTerms`. A question that contains one of them can be matched to this term. (49)

`accessible entrance`, `accessible route`, `assistance`, `assistance dog`, `carer`, `have a pushchair`, `heavy door`, `how long should i allow`, `level access`, `lift fault`, `lift faults`, `lift out of service`, `low vision`, `lower stimulation`, `mobility`, `personal assistant`, `public route`, `public routes`, `pushchair access`, `pushchair friendly`, `pushchair route`, `pushchair-friendly`, `quiet route`, `ramp`, `route segment`, `route segments`, `route survey`, `seated rest`, `somewhere to sit`, `step free access to`, `step free alternative`, `step free route`, `step free routes`, `step-free access to`, `step-free alternative`, `step-free constraints`, `step-free entrance`, `step-free journey`, `step-free path`, `step-free route`, `step-free routes`, `surveyed route`, `surveyed routes`, `wheelchair`, `wheelchair access`, `which lift`, `with a buggy`, `with a pram`, `with a pushchair`

## Class hierarchy

Superclasses:

- [`ontosage:Record`]({{ '/ontology/class/Record/' | relative_url }}) › **`ontosage:AccessibleRoute`**

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:allowMinutes`]({{ '/ontology/property/allowMinutes/' | relative_url }}) | datatype | `xsd:integer` | this class |
| [`ontosage:doorOperation`]({{ '/ontology/property/doorOperation/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:isStepFree`]({{ '/ontology/property/isStepFree/' | relative_url }}) | datatype | `xsd:boolean` | this class |
| [`ontosage:routeDistanceMetres`]({{ '/ontology/property/routeDistanceMetres/' | relative_url }}) | datatype | `xsd:integer` | this class |
| [`ontosage:routeFrom`]({{ '/ontology/property/routeFrom/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:routeTo`]({{ '/ontology/property/routeTo/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:seatedRests`]({{ '/ontology/property/seatedRests/' | relative_url }}) | datatype | `xsd:integer` | this class |

## Record document mapping

Record documents of type `accessible_route` are lifted into instances of this class ([mapping]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#accessible_route)).

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:AccessibleRoute a owl:Class ;
    rdfs:label "Accessible route"@en ;
    ontosage:layTerms "accessible entrance",
        "accessible route",
        "assistance",
        "assistance dog",
        "carer",
        "have a pushchair",
        "heavy door",
        "how long should i allow",
        "level access",
        "lift fault",
        "lift faults",
        "lift out of service",
        "low vision",
        "lower stimulation",
        "mobility",
        "personal assistant",
        "public route",
        "public routes",
        "pushchair access",
        "pushchair friendly",
        "pushchair route",
        "pushchair-friendly",
        "quiet route",
        "ramp",
        "route segment",
        "route segments",
        "route survey",
        "seated rest",
        "somewhere to sit",
        "step free access to",
        "step free alternative",
        "step free route",
        "step free routes",
        "step-free access to",
        "step-free alternative",
        "step-free constraints",
        "step-free entrance",
        "step-free journey",
        "step-free path",
        "step-free route",
        "step-free routes",
        "surveyed route",
        "surveyed routes",
        "wheelchair",
        "wheelchair access",
        "which lift",
        "with a buggy",
        "with a pram",
        "with a pushchair" ;
    rdfs:comment "A SURVEYED journey between an arrival point and a destination, carrying the facts a disabled visitor actually asks for: entrance, step-free or not, seated rests, how the doors operate, which lift and whether it is in service, how much time to allow, how busy it is, and a non-telephone assistance contact. surveyedOn and surveyedBy are required because every question this answers uses the word 'verified' — a route inferred from geometry is a guess about somebody's journey, and a wrong guess costs them the journey. A route that is NOT step-free is published too, so it is never offered as an accessible option by omission."@en ;
    rdfs:subClassOf ontosage:Record ;
    skos:example "which verified route from the drop-off has seated rests, and how long should I allow? -> AccessibleRoute where routeFrom matches; read seatedRests and allowMinutes." .
```
{% endraw %}
