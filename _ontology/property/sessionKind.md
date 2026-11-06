---
title: "ontosage:sessionKind"
layout: post
permalink: /ontology/property/sessionKind/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › sessionKind

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#sessionKind` |
| Label | session kind |
| Kind | datatype property |
| Domain | [`ontosage:TimetabledSession`]({{ '/ontology/class/TimetabledSession/' | relative_url }}) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

lecture | seminar | lab | exam | event | meeting.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`timetabled_session`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#timetabled_session) | `session_kind` | `xsd:string` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:sessionKind a owl:DatatypeProperty ;
    rdfs:label "session kind"@en ;
    rdfs:comment "lecture | seminar | lab | exam | event | meeting."@en ;
    rdfs:domain ontosage:TimetabledSession ;
    rdfs:range xsd:string .
```
{% endraw %}
