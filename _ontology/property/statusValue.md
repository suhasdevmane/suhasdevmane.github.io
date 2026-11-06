---
title: "ontosage:statusValue"
layout: post
permalink: /ontology/property/statusValue/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › statusValue

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#statusValue` |
| Label | status value |
| Kind | datatype property |
| Domain | [`ontosage:AssetStatus`]({{ '/ontology/class/AssetStatus/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

operational | degraded | out\_of\_service | unverified. UNVERIFIED is the default for anything no authoritative source has reported, and is deliberately NOT the same as operational: 'nobody has told me it is broken' is not evidence that it works, and answering as though it were is how a step-free route gets recommended through a failed lift.

## Examples

- "out\_of\_service"

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:statusValue a owl:DatatypeProperty ;
    rdfs:label "status value"@en ;
    rdfs:comment "operational | degraded | out_of_service | unverified. UNVERIFIED is the default for anything no authoritative source has reported, and is deliberately NOT the same as operational: 'nobody has told me it is broken' is not evidence that it works, and answering as though it were is how a step-free route gets recommended through a failed lift."@en ;
    rdfs:domain ontosage:AssetStatus ;
    rdfs:range xsd:string ;
    skos:example "\"out_of_service\"" .
```
{% endraw %}
