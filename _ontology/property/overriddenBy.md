---
title: "ontosage:overriddenBy"
layout: post
permalink: /ontology/property/overriddenBy/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › overriddenBy

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#overriddenBy` |
| Label | overridden by |
| Kind | datatype property |
| Domain | [`ontosage:AccessPermission`]({{ '/ontology/class/AccessPermission/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Global modes or controller rules that supersede the time profile. Recorded on the row they override, because that is where someone checking the group will look.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`access_permission`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#access_permission) | `override` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:overriddenBy a owl:DatatypeProperty ;
    rdfs:label "overridden by"@en ;
    rdfs:comment "Global modes or controller rules that supersede the time profile. Recorded on the row they override, because that is where someone checking the group will look."@en ;
    rdfs:domain ontosage:AccessPermission ;
    rdfs:range xsd:string .
```
{% endraw %}
