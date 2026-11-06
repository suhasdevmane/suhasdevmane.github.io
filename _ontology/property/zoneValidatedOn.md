---
title: "ontosage:zoneValidatedOn"
layout: post
permalink: /ontology/property/zoneValidatedOn/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › zoneValidatedOn

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#zoneValidatedOn` |
| Label | zone validated on |
| Kind | datatype property |
| Domain | [`ontosage:ServedZone`]({{ '/ontology/class/ServedZone/' | relative_url }}) |
| Range | `xsd:date` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

When the serving relation was last verified. A zone validated against a mechanical schedule from before a refurbishment describes a building that no longer exists.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:zoneValidatedOn a owl:DatatypeProperty ;
    rdfs:label "zone validated on"@en ;
    rdfs:comment "When the serving relation was last verified. A zone validated against a mechanical schedule from before a refurbishment describes a building that no longer exists."@en ;
    rdfs:domain ontosage:ServedZone ;
    rdfs:range xsd:date .
```
{% endraw %}
