---
title: "ontosage:operatingWindow"
layout: post
permalink: /ontology/property/operatingWindow/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › operatingWindow

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#operatingWindow` |
| Label | operating window |
| Kind | datatype property |
| Domain | [`ontosage:OperatingRegime`]({{ '/ontology/class/OperatingRegime/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The hours the system is approved to run. A reading outside this window is only a fault once this says so.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`operating_regime`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#operating_regime) | `operating_window` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:operatingWindow a owl:DatatypeProperty ;
    rdfs:label "operating window"@en ;
    rdfs:comment "The hours the system is approved to run. A reading outside this window is only a fault once this says so."@en ;
    rdfs:domain ontosage:OperatingRegime ;
    rdfs:range xsd:string .
```
{% endraw %}
