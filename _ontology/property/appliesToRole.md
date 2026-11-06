---
title: "ontosage:appliesToRole"
layout: post
permalink: /ontology/property/appliesToRole/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › appliesToRole

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#appliesToRole` |
| Label | applies to role |
| Kind | datatype property |
| Domain | [`ontosage:AccessPolicy`]({{ '/ontology/class/AccessPolicy/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Canonical RBAC role name. Personas NEVER map to policies.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`competency`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#competency) | `applies_to_role` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:appliesToRole a owl:DatatypeProperty ;
    rdfs:label "applies to role"@en ;
    rdfs:comment "Canonical RBAC role name. Personas NEVER map to policies."@en ;
    rdfs:domain ontosage:AccessPolicy ;
    rdfs:range xsd:string .
```
{% endraw %}
