---
title: "ontosage:amenityStatus"
layout: post
permalink: /ontology/property/amenityStatus/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › amenityStatus

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#amenityStatus` |
| Label | amenity service status |
| Kind | object property |
| Domain | [`ontosage:Amenity`]({{ '/ontology/class/Amenity/' | relative_url }}) |
| Range | [`ontosage:AssetStatus`]({{ '/ontology/class/AssetStatus/' | relative_url }}) |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Links an amenity to its current ontosage:AssetStatus record. An amenity whose status is out\_of\_service must be EXCLUDED from recommendations rather than listed with a caveat: somebody who walks to a broken fountain has been given a wrong answer, however well hedged.

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ontosage:amenityStatus a owl:ObjectProperty ;
    rdfs:label "amenity service status"@en ;
    rdfs:comment "Links an amenity to its current ontosage:AssetStatus record. An amenity whose status is out_of_service must be EXCLUDED from recommendations rather than listed with a caveat: somebody who walks to a broken fountain has been given a wrong answer, however well hedged."@en ;
    rdfs:domain ontosage:Amenity ;
    rdfs:range ontosage:AssetStatus .
```
{% endraw %}
