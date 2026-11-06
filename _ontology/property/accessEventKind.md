---
title: "ontosage:accessEventKind"
layout: post
permalink: /ontology/property/accessEventKind/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › accessEventKind

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#accessEventKind` |
| Label | access event kind |
| Kind | datatype property |
| Domain | [`ontosage:AccessEvent`]({{ '/ontology/class/AccessEvent/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

What happened at the opening: access\_denied | held\_open | forced\_door. An exception log, not a movement log — routine granted entries are not recorded as events.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:accessEventKind a owl:DatatypeProperty ;
    rdfs:label "access event kind"@en ;
    rdfs:comment "What happened at the opening: access_denied | held_open | forced_door. An exception log, not a movement log — routine granted entries are not recorded as events."@en ;
    rdfs:domain ontosage:AccessEvent ;
    rdfs:range xsd:string .
```
{% endraw %}
