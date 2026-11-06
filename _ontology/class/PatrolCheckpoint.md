---
title: "ontosage:PatrolCheckpoint"
layout: post
permalink: /ontology/class/PatrolCheckpoint/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › PatrolCheckpoint

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#PatrolCheckpoint` |
| Label | Patrol checkpoint |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A point on a security circuit, with its position, the shift that walks it, when it was last verified and when it is next due. recordStatus is RECORDED rather than derived from the due time, because overdue and unverifiable are different facts with different remedies -- one needs walking, the other needs a lock or a tag fixed -- and a date alone collapses them into 'late'. expectedMinutes exists so a circuit's feasibility in a patrol window is a sum rather than a judgement.

## Examples

- which checkpoints are overdue or unverifiable this shift? -&gt; PatrolCheckpoint where shiftName matches and recordStatus in (overdue, unverifiable).

## Lay terms

Plain-language phrases declared on this term with `ontosage:layTerms`. A question that contains one of them can be matched to this term. (16)

`checkpoint`, `checkpoints`, `circuit`, `guard`, `my shift`, `overdue check`, `patrol`, `patrols`, `post`, `posts`, `rounds`, `security officer`, `security round`, `shift handover`, `this shift`, `walk the building`

## Class hierarchy

Superclasses:

- [`ontosage:Record`]({{ '/ontology/class/Record/' | relative_url }}) › **`ontosage:PatrolCheckpoint`**

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:circuitSequence`]({{ '/ontology/property/circuitSequence/' | relative_url }}) | datatype | `xsd:integer` | this class |
| [`ontosage:patrolCircuit`]({{ '/ontology/property/patrolCircuit/' | relative_url }}) | datatype | `xsd:string` | this class |

## Record document mapping

Record documents of type `patrol_checkpoint` are lifted into instances of this class ([mapping]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#patrol_checkpoint)).

## Turtle

Development notes were removed from one or more text values below; the source file holds the full text.

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:PatrolCheckpoint a owl:Class ;
    rdfs:label "Patrol checkpoint"@en ;
    ontosage:layTerms "checkpoint",
        "checkpoints",
        "circuit",
        "guard",
        "my shift",
        "overdue check",
        "patrol",
        "patrols",
        "post",
        "posts",
        "rounds",
        "security officer",
        "security round",
        "shift handover",
        "this shift",
        "walk the building" ;
    rdfs:comment "A point on a security circuit, with its position, the shift that walks it, when it was last verified and when it is next due. recordStatus is RECORDED rather than derived from the due time, because overdue and unverifiable are different facts with different remedies -- one needs walking, the other needs a lock or a tag fixed -- and a date alone collapses them into 'late'. expectedMinutes exists so a circuit's feasibility in a patrol window is a sum rather than a judgement."@en ;
    rdfs:subClassOf ontosage:Record ;
    skos:example "which checkpoints are overdue or unverifiable this shift? -> PatrolCheckpoint where shiftName matches and recordStatus in (overdue, unverifiable)." .
```
{% endraw %}
