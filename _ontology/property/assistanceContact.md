---
title: "ontosage:assistanceContact"
layout: post
permalink: /ontology/property/assistanceContact/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › assistanceContact

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#assistanceContact` |
| Label | assistance contact |
| Kind | datatype property |
| Domain | not declared (any subject) |
| Range | `xsd:string` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A non-telephone arrival contact.

Who to contact when this asset is unavailable. Present so a decline can be USEFUL: 'the lift is out of service, and step-free access to level 5 is via the estates helpdesk on x1234' is an answer; 'the lift is out of service' strands someone.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`accessible_route`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#accessible_route) | `assistance_contact` | `xsd:string` |

## Turtle

Development notes were removed from one or more text values below; the source file holds the full text.

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:assistanceContact a owl:DatatypeProperty ;
    rdfs:label "assistance contact"@en ;
    rdfs:comment "A non-telephone arrival contact."@en,
        "Who to contact when this asset is unavailable. Present so a decline can be USEFUL: 'the lift is out of service, and step-free access to level 5 is via the estates helpdesk on x1234' is an answer; 'the lift is out of service' strands someone."@en ;
    rdfs:range xsd:string .
```
{% endraw %}
