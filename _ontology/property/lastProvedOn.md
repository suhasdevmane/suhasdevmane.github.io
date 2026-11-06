---
title: "ontosage:lastProvedOn"
layout: post
permalink: /ontology/property/lastProvedOn/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › lastProvedOn

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#lastProvedOn` |
| Label | last proved on |
| Kind | datatype property |
| Domain | [`ontosage:ContinuityProvision`]({{ '/ontology/class/ContinuityProvision/' | relative_url }}) |
| Range | `xsd:date` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

When the arrangement was last exercised end to end. Without a date and an evidence reference the row is unverified, whatever the plan says.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`continuity_provision`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#continuity_provision) | `last_proved_on` | `xsd:date` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:lastProvedOn a owl:DatatypeProperty ;
    rdfs:label "last proved on"@en ;
    rdfs:comment "When the arrangement was last exercised end to end. Without a date and an evidence reference the row is unverified, whatever the plan says."@en ;
    rdfs:domain ontosage:ContinuityProvision ;
    rdfs:range xsd:date .
```
{% endraw %}
