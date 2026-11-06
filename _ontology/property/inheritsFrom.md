---
title: "ontosage:inheritsFrom"
layout: post
permalink: /ontology/property/inheritsFrom/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › inheritsFrom

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#inheritsFrom` |
| Label | inherits from |
| Kind | datatype property |
| Domain | [`ontosage:AccessPermission`]({{ '/ontology/class/AccessPermission/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The parent group whose grant this one extends. Empty means the group stands alone; the chain is data so an inherited path can be reported rather than described.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`access_permission`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#access_permission) | `inherits_from` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:inheritsFrom a owl:DatatypeProperty ;
    rdfs:label "inherits from"@en ;
    rdfs:comment "The parent group whose grant this one extends. Empty means the group stands alone; the chain is data so an inherited path can be reported rather than described."@en ;
    rdfs:domain ontosage:AccessPermission ;
    rdfs:range xsd:string .
```
{% endraw %}
