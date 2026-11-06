---
title: "ontosage:criterionState"
layout: post
permalink: /ontology/property/criterionState/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › criterionState

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#criterionState` |
| Label | criterion state |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Met, not met, conflicting or UNKNOWN. Unknown is not a blank: it is the statement that nobody has established this, which is a different decision from 'not met'.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`coordination_function`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#coordination_function) | `criterion_state` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:criterionState a owl:DatatypeProperty ;
    rdfs:label "criterion state"@en ;
    rdfs:comment "Met, not met, conflicting or UNKNOWN. Unknown is not a blank: it is the statement that nobody has established this, which is a different decision from 'not met'."@en ;
    rdfs:range xsd:string .
```
{% endraw %}
