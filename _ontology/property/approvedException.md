---
title: "ontosage:approvedException"
layout: post
permalink: /ontology/property/approvedException/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › approvedException

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#approvedException` |
| Label | approved exception |
| Kind | datatype property |
| Domain | [`ontosage:OperatingRegime`]({{ '/ontology/class/OperatingRegime/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A deviation that has been authorised, with its reason. Without this field every legitimate exception reads as a fault, which is how an alarm list becomes noise.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`operating_regime`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#operating_regime) | `approved_exception` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:approvedException a owl:DatatypeProperty ;
    rdfs:label "approved exception"@en ;
    rdfs:comment "A deviation that has been authorised, with its reason. Without this field every legitimate exception reads as a fault, which is how an alarm list becomes noise."@en ;
    rdfs:domain ontosage:OperatingRegime ;
    rdfs:range xsd:string .
```
{% endraw %}
