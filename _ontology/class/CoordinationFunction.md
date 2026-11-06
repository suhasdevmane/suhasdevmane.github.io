---
title: "ontosage:CoordinationFunction"
layout: post
permalink: /ontology/class/CoordinationFunction/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › CoordinationFunction

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#CoordinationFunction` |
| Label | Emergency coordination function |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

One coordination function for one operational period: its accountable role, primary system and that system's state, the approved fallback, the activation criterion and whether that criterion is evidenced as met. UNKNOWN IS A FIRST-CLASS STATE. In an incident, 'we have not established whether this is met' and 'this is not met' lead to different decisions, and a register collapsing them into one empty cell would be actively dangerous -- so criterionState carries an explicit unknown, and a row without an evidence reference cannot be recorded as met. The approved fallback sits beside the function it replaces, because a fallback that must be looked up elsewhere during an incident is not a fallback.

## Examples

- which coordination systems are ready, degraded or unavailable, and what fallback applies? -&gt; CoordinationFunction for the current period; read systemState and approvedFallback.

## Lay terms

Plain-language phrases declared on this term with `ontosage:layTerms`. A question that contains one of them can be matched to this term. (15)

`activation`, `are we ready for an incident`, `coordination`, `coordination function`, `emergency coordination`, `emergency coordinator`, `emergency coordinators`, `emergency response role`, `emergency response roles`, `evacuation control`, `incident command`, `manual fallback`, `operational period`, `roll call`, `who is on call`

## Class hierarchy

Superclasses:

- [`ontosage:Record`]({{ '/ontology/class/Record/' | relative_url }}) › **`ontosage:CoordinationFunction`**

Subclasses: none.

## Properties

No property declares this class (or a superclass) as its domain.

## Record document mapping

Record documents of type `coordination_function` are lifted into instances of this class ([mapping]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#coordination_function)).

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:CoordinationFunction a owl:Class ;
    rdfs:label "Emergency coordination function"@en ;
    ontosage:layTerms "activation",
        "are we ready for an incident",
        "coordination",
        "coordination function",
        "emergency coordination",
        "emergency coordinator",
        "emergency coordinators",
        "emergency response role",
        "emergency response roles",
        "evacuation control",
        "incident command",
        "manual fallback",
        "operational period",
        "roll call",
        "who is on call" ;
    rdfs:comment "One coordination function for one operational period: its accountable role, primary system and that system's state, the approved fallback, the activation criterion and whether that criterion is evidenced as met. UNKNOWN IS A FIRST-CLASS STATE. In an incident, 'we have not established whether this is met' and 'this is not met' lead to different decisions, and a register collapsing them into one empty cell would be actively dangerous -- so criterionState carries an explicit unknown, and a row without an evidence reference cannot be recorded as met. The approved fallback sits beside the function it replaces, because a fallback that must be looked up elsewhere during an incident is not a fallback."@en ;
    rdfs:subClassOf ontosage:Record ;
    skos:example "which coordination systems are ready, degraded or unavailable, and what fallback applies? -> CoordinationFunction for the current period; read systemState and approvedFallback." .
```
{% endraw %}
