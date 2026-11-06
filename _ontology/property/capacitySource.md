---
title: "ontosage:capacitySource"
layout: post
permalink: /ontology/property/capacitySource/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › capacitySource

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#capacitySource` |
| Label | capacity source |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Which source a retained hbco:roomCapacity record came from: "ttl" (the building's own model) or "drawing" (the architect's drawing, a second source). The reader takes the TTL figure for a space whenever the TTL holds one, and reads a drawing only when it holds none. Carried by the record, not the space, so a superseded TTL figure and a drawing figure stay distinguishable.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:capacitySource a owl:DatatypeProperty ;
    rdfs:label "capacity source"@en ;
    rdfs:comment "Which source a retained hbco:roomCapacity record came from: \"ttl\" (the building's own model) or \"drawing\" (the architect's drawing, a second source). The reader takes the TTL figure for a space whenever the TTL holds one, and reads a drawing only when it holds none. Carried by the record, not the space, so a superseded TTL figure and a drawing figure stay distinguishable."@en ;
    rdfs:range xsd:string .
```
{% endraw %}
