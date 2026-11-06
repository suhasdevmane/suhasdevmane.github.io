---
title: "ontosage:qualifierTerms"
layout: post
permalink: /ontology/property/qualifierTerms/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › qualifierTerms

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#qualifierTerms` |
| Label | qualifier terms |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The subset of a record class's layTerms that name the class only when used OF it, not when describing something else. 'Is this route approved?' is about approval; 'the approved schedule' is about a schedule. A qualifier followed directly by a content word is read as describing that word and does not count as evidence for the class. Declare a term here when its adjective use is common and names a property of other things.

## Examples

- `ontosage:ApprovalRecord ontosage:qualifierTerms "approved", "verified" .`

## Used in the schema

1 schema term(s) carry this property:

- [`ontosage:ApprovalRecord`]({{ '/ontology/class/ApprovalRecord/' | relative_url }})

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:qualifierTerms a owl:DatatypeProperty ;
    rdfs:label "qualifier terms"@en ;
    rdfs:comment "The subset of a record class's layTerms that name the class only when used OF it, not when describing something else. 'Is this route approved?' is about approval; 'the approved schedule' is about a schedule. A qualifier followed directly by a content word is read as describing that word and does not count as evidence for the class. Declare a term here when its adjective use is common and names a property of other things."@en ;
    rdfs:range xsd:string ;
    skos:example "ontosage:ApprovalRecord ontosage:qualifierTerms \"approved\", \"verified\" ." .
```
{% endraw %}
