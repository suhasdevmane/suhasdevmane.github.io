---
title: "ontosage:potabilityValue"
layout: post
permalink: /ontology/property/potabilityValue/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › potabilityValue

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#potabilityValue` |
| Label | potability |
| Kind | datatype property |
| Domain | [`ontosage:PotabilityStatement`]({{ '/ontology/class/PotabilityStatement/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

potable | not\_potable | unknown. UNKNOWN is the default and is a legitimate answer: 'nobody has published a statement about this outlet' is honest, whereas assuming either value is a health claim nobody made.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:potabilityValue a owl:DatatypeProperty ;
    rdfs:label "potability"@en ;
    rdfs:comment "potable | not_potable | unknown. UNKNOWN is the default and is a legitimate answer: 'nobody has published a statement about this outlet' is honest, whereas assuming either value is a health claim nobody made."@en ;
    rdfs:domain ontosage:PotabilityStatement ;
    rdfs:range xsd:string .
```
{% endraw %}
