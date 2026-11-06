---
title: "ontosage:dependsOnSpace"
layout: post
permalink: /ontology/property/dependsOnSpace/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › dependsOnSpace

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#dependsOnSpace` |
| Label | depends on space |
| Kind | datatype property |
| Domain | [`ontosage:ContinuityProvision`]({{ '/ontology/class/ContinuityProvision/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The space or system the service normally runs from. The thing whose loss the rest of the row answers.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`continuity_provision`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#continuity_provision) | `depends_on` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:dependsOnSpace a owl:DatatypeProperty ;
    rdfs:label "depends on space"@en ;
    rdfs:comment "The space or system the service normally runs from. The thing whose loss the rest of the row answers."@en ;
    rdfs:domain ontosage:ContinuityProvision ;
    rdfs:range xsd:string .
```
{% endraw %}
