---
title: "ontosage:dependsOnLift"
layout: post
permalink: /ontology/property/dependsOnLift/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › dependsOnLift

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#dependsOnLift` |
| Label | depends on lift |
| Kind | datatype property |
| Domain | [`ontosage:CirculationTime`]({{ '/ontology/class/CirculationTime/' | relative_url }}) |
| Range | `xsd:boolean` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Whether the step-free time assumes the lift. When it fails, every journey marked true has no step-free alternative at all rather than a slower one.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`circulation_time`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#circulation_time) | `depends_on_lift` | `xsd:boolean` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:dependsOnLift a owl:DatatypeProperty ;
    rdfs:label "depends on lift"@en ;
    rdfs:comment "Whether the step-free time assumes the lift. When it fails, every journey marked true has no step-free alternative at all rather than a slower one."@en ;
    rdfs:domain ontosage:CirculationTime ;
    rdfs:range xsd:boolean .
```
{% endraw %}
