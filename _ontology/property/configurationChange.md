---
title: "ontosage:configurationChange"
layout: post
permalink: /ontology/property/configurationChange/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › configurationChange

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#configurationChange` |
| Label | configuration change |
| Kind | datatype property |
| Domain | [`ontosage:ConfigurationPeriod`]({{ '/ontology/class/ConfigurationPeriod/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

What changed at the start of this period: relocation | recalibration | replacement | firmware | commissioning. Reported alongside any trend that spans the boundary, so a measurement artefact is never presented as building behaviour.

## Examples

- "recalibration"

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:configurationChange a owl:DatatypeProperty ;
    rdfs:label "configuration change"@en ;
    rdfs:comment "What changed at the start of this period: relocation | recalibration | replacement | firmware | commissioning. Reported alongside any trend that spans the boundary, so a measurement artefact is never presented as building behaviour."@en ;
    rdfs:domain ontosage:ConfigurationPeriod ;
    rdfs:range xsd:string ;
    skos:example "\"recalibration\"" .
```
{% endraw %}
