---
title: "ontosage:owningAuthority"
layout: post
permalink: /ontology/property/owningAuthority/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › owningAuthority

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#owningAuthority` |
| Label | owning authority |
| Kind | datatype property |
| Domain | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

The organisation whose system of record this is (Estates, HR, the maintainer). Distinct from recordOwner, which is the accountable role inside it.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`approval_evidence`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#approval_evidence) | `authority` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:owningAuthority a owl:DatatypeProperty ;
    rdfs:label "owning authority"@en ;
    rdfs:comment "The organisation whose system of record this is (Estates, HR, the maintainer). Distinct from recordOwner, which is the accountable role inside it."@en ;
    rdfs:domain ontosage:IntervalRecord ;
    rdfs:range xsd:string .
```
{% endraw %}
