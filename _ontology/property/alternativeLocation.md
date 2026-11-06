---
title: "ontosage:alternativeLocation"
layout: post
permalink: /ontology/property/alternativeLocation/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › alternativeLocation

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#alternativeLocation` |
| Label | alternative location |
| Kind | datatype property |
| Domain | [`ontosage:ContinuityProvision`]({{ '/ontology/class/ContinuityProvision/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Where the service runs instead, or 'none identified' where nothing has been arranged. Recorded either way: a missing alternative is the answer somebody needs.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`continuity_provision`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#continuity_provision) | `alternative_location` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:alternativeLocation a owl:DatatypeProperty ;
    rdfs:label "alternative location"@en ;
    rdfs:comment "Where the service runs instead, or 'none identified' where nothing has been arranged. Recorded either way: a missing alternative is the answer somebody needs."@en ;
    rdfs:domain ontosage:ContinuityProvision ;
    rdfs:range xsd:string .
```
{% endraw %}
