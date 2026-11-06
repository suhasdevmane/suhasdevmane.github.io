---
title: "ontosage:denialReason"
layout: post
permalink: /ontology/property/denialReason/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › denialReason

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#denialReason` |
| Label | denial reason |
| Kind | datatype property |
| Domain | [`ontosage:AccessEvent`]({{ '/ontology/class/AccessEvent/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Why access was refused, as the controller recorded it (outside the role's time profile, zone not in the permission group). Blank on events that were not refusals.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:denialReason a owl:DatatypeProperty ;
    rdfs:label "denial reason"@en ;
    rdfs:comment "Why access was refused, as the controller recorded it (outside the role's time profile, zone not in the permission group). Blank on events that were not refusals."@en ;
    rdfs:domain ontosage:AccessEvent ;
    rdfs:range xsd:string .
```
{% endraw %}
