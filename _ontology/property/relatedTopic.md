---
title: "ontosage:relatedTopic"
layout: post
permalink: /ontology/property/relatedTopic/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › relatedTopic

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#relatedTopic` |
| Label | related topic |
| Kind | object property |
| Domain | [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}) |
| Range | [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}) |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Links a capability to a related capability/topic (e.g. a broken-lift issue relates to the lift amenity).

## Examples

- `bldg:Issue_BrokenLift ontosage:relatedTopic bldg:Lift_Main .`

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:relatedTopic a owl:ObjectProperty ;
    rdfs:label "related topic"@en ;
    rdfs:comment "Links a capability to a related capability/topic (e.g. a broken-lift issue relates to the lift amenity)."@en ;
    rdfs:domain ontosage:Capability ;
    rdfs:range ontosage:Capability ;
    skos:example "bldg:Issue_BrokenLift ontosage:relatedTopic bldg:Lift_Main ." .
```
{% endraw %}
