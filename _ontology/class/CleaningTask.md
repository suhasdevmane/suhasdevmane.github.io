---
title: "ontosage:CleaningTask"
layout: post
permalink: /ontology/class/CleaningTask/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › CleaningTask

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#CleaningTask` |
| Label | Cleaning task |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

One unit of cleaning work: a zone, an area within it, the standard that applies, how often it recurs, the shift that owns it and the time the area must be ready. Status is READ from the register, never inferred from dates: a caretaker sent to a suspended area wastes a shift, and a suspended area silently omitted is worse.

## Examples

- what is my zone and task list for this shift? -&gt; CleaningTask where shiftName matches and recordStatus is not suspended.

## Lay terms

Plain-language phrases declared on this term with `ontosage:layTerms`. A question that contains one of them can be matched to this term. (24)

`caretaker`, `caretaking`, `cleaned`, `cleaner`, `cleaning`, `cleaning schedule`, `cleaning standard`, `cleans`, `housekeeping`, `janitorial`, `my round`, `my shift`, `my zone`, `task list`, `washroom cleaning`, `washroom service`, `washroom servicing`, `washroom should i service`, `washrooms cleaning`, `washrooms service`, `washrooms servicing`, `washrooms should i service`, `which rooms must be ready`, `who cleans`

## Class hierarchy

Superclasses:

- [`ontosage:Record`]({{ '/ontology/class/Record/' | relative_url }}) › **`ontosage:CleaningTask`**

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:cleaningStandard`]({{ '/ontology/property/cleaningStandard/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:cleaningZone`]({{ '/ontology/property/cleaningZone/' | relative_url }}) | datatype | `xsd:string` | this class |

## Record document mapping

Record documents of type `cleaning_task` are lifted into instances of this class ([mapping]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#cleaning_task)).

## Turtle

Development notes were removed from one or more text values below; the source file holds the full text.

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:CleaningTask a owl:Class ;
    rdfs:label "Cleaning task"@en ;
    ontosage:layTerms "caretaker",
        "caretaking",
        "cleaned",
        "cleaner",
        "cleaning",
        "cleaning schedule",
        "cleaning standard",
        "cleans",
        "housekeeping",
        "janitorial",
        "my round",
        "my shift",
        "my zone",
        "task list",
        "washroom cleaning",
        "washroom service",
        "washroom servicing",
        "washroom should i service",
        "washrooms cleaning",
        "washrooms service",
        "washrooms servicing",
        "washrooms should i service",
        "which rooms must be ready",
        "who cleans" ;
    rdfs:comment "One unit of cleaning work: a zone, an area within it, the standard that applies, how often it recurs, the shift that owns it and the time the area must be ready. Status is READ from the register, never inferred from dates: a caretaker sent to a suspended area wastes a shift, and a suspended area silently omitted is worse."@en ;
    rdfs:subClassOf ontosage:Record ;
    skos:example "what is my zone and task list for this shift? -> CleaningTask where shiftName matches and recordStatus is not suspended." .
```
{% endraw %}
