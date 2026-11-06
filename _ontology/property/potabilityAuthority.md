---
title: "ontosage:potabilityAuthority"
layout: post
permalink: /ontology/property/potabilityAuthority/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › potabilityAuthority

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#potabilityAuthority` |
| Label | issuing authority |
| Kind | datatype property |
| Domain | [`ontosage:PotabilityStatement`]({{ '/ontology/class/PotabilityStatement/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Who published the statement and stands behind it. Required, because a drinkability claim with no owner is exactly the kind of confident unattributable assertion the evidence discipline exists to prevent.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:potabilityAuthority a owl:DatatypeProperty ;
    rdfs:label "issuing authority"@en ;
    rdfs:comment "Who published the statement and stands behind it. Required, because a drinkability claim with no owner is exactly the kind of confident unattributable assertion the evidence discipline exists to prevent."@en ;
    rdfs:domain ontosage:PotabilityStatement ;
    rdfs:range xsd:string .
```
{% endraw %}
