---
title: "ontosage:suitableForCalls"
layout: post
permalink: /ontology/property/suitableForCalls/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › suitableForCalls

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#suitableForCalls` |
| Label | suitable for calls |
| Kind | datatype property |
| Domain | [`ontosage:WorkspaceProfile`]({{ '/ontology/class/WorkspaceProfile/' | relative_url }}) |
| Range | `xsd:boolean` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Whether a video or confidential call can be taken here without disturbing others or being overheard. Requires acoustic separation, not merely a door.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`workspace_profile`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#workspace_profile) | `calls_ok` | `xsd:boolean` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:suitableForCalls a owl:DatatypeProperty ;
    rdfs:label "suitable for calls"@en ;
    rdfs:comment "Whether a video or confidential call can be taken here without disturbing others or being overheard. Requires acoustic separation, not merely a door."@en ;
    rdfs:domain ontosage:WorkspaceProfile ;
    rdfs:range xsd:boolean .
```
{% endraw %}
