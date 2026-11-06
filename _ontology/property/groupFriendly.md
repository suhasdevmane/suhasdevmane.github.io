---
title: "ontosage:groupFriendly"
layout: post
permalink: /ontology/property/groupFriendly/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › groupFriendly

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#groupFriendly` |
| Label | group friendly |
| Kind | datatype property |
| Domain | [`ontosage:WorkspaceProfile`]({{ '/ontology/class/WorkspaceProfile/' | relative_url }}) |
| Range | `xsd:boolean` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Whether two or more people may work together here without breaching the space's own noise expectation.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`workspace_profile`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#workspace_profile) | `group_ok` | `xsd:boolean` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:groupFriendly a owl:DatatypeProperty ;
    rdfs:label "group friendly"@en ;
    rdfs:comment "Whether two or more people may work together here without breaching the space's own noise expectation."@en ;
    rdfs:domain ontosage:WorkspaceProfile ;
    rdfs:range xsd:boolean .
```
{% endraw %}
