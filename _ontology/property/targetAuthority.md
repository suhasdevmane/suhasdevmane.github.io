---
title: "ontosage:targetAuthority"
layout: post
permalink: /ontology/property/targetAuthority/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › targetAuthority

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#targetAuthority` |
| Label | target authority |
| Kind | datatype property |
| Domain | [`ontosage:SustainabilityTarget`]({{ '/ontology/class/SustainabilityTarget/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Who set the target and stands behind it. Required for the same reason a potability statement needs an owner: an unattributed commitment cannot be relied on, and cannot be challenged.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`sustainability_target`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#sustainability_target) | `authority` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:targetAuthority a owl:DatatypeProperty ;
    rdfs:label "target authority"@en ;
    rdfs:comment "Who set the target and stands behind it. Required for the same reason a potability statement needs an owner: an unattributed commitment cannot be relied on, and cannot be challenged."@en ;
    rdfs:domain ontosage:SustainabilityTarget ;
    rdfs:range xsd:string .
```
{% endraw %}
