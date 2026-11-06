---
title: "ontosage:MaintenanceIssue"
layout: post
permalink: /ontology/class/MaintenanceIssue/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › MaintenanceIssue

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#MaintenanceIssue` |
| Label | Maintenance / fault issue |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A fault type and who to report it to: leak, broken light, broken lift, heating fault. MAY reference the brick:Equipment it concerns via ontosage:aboutEquipment.

## Examples

- "there is a water leak" -&gt; the leak maintenance issue (report route = Estates).

## Class hierarchy

Superclasses:

- [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}) › [`ontosage:KnowledgeTopic`]({{ '/ontology/class/KnowledgeTopic/' | relative_url }}) › **`ontosage:MaintenanceIssue`**

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:priority`]({{ '/ontology/property/priority/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:answerText`]({{ '/ontology/property/answerText/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:KnowledgeTopic`]({{ '/ontology/class/KnowledgeTopic/' | relative_url }}) |
| [`ontosage:contactEmail`]({{ '/ontology/property/contactEmail/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:KnowledgeTopic`]({{ '/ontology/class/KnowledgeTopic/' | relative_url }}) |
| [`ontosage:contactPhone`]({{ '/ontology/property/contactPhone/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:KnowledgeTopic`]({{ '/ontology/class/KnowledgeTopic/' | relative_url }}) |
| [`ontosage:documentRef`]({{ '/ontology/property/documentRef/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:KnowledgeTopic`]({{ '/ontology/class/KnowledgeTopic/' | relative_url }}) |
| [`ontosage:effectiveDate`]({{ '/ontology/property/effectiveDate/' | relative_url }}) | datatype | `xsd:date` | [`ontosage:KnowledgeTopic`]({{ '/ontology/class/KnowledgeTopic/' | relative_url }}) |
| [`ontosage:infoUrl`]({{ '/ontology/property/infoUrl/' | relative_url }}) | datatype | `xsd:anyURI` | [`ontosage:KnowledgeTopic`]({{ '/ontology/class/KnowledgeTopic/' | relative_url }}) |
| [`ontosage:policyOwner`]({{ '/ontology/property/policyOwner/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:KnowledgeTopic`]({{ '/ontology/class/KnowledgeTopic/' | relative_url }}) |
| [`ontosage:reportTo`]({{ '/ontology/property/reportTo/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:KnowledgeTopic`]({{ '/ontology/class/KnowledgeTopic/' | relative_url }}) |
| [`ontosage:capabilityCategory`]({{ '/ontology/property/capabilityCategory/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}) |
| [`ontosage:layTerms`]({{ '/ontology/property/layTerms/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}) |
| [`ontosage:locatedIn`]({{ '/ontology/property/locatedIn/' | relative_url }}) | object | [`brick:Location`](https://ontology.brickschema.org/1.4/#brick:Location) | [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}) |
| [`ontosage:note`]({{ '/ontology/property/note/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}) |
| [`ontosage:openingHours`]({{ '/ontology/property/openingHours/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}) |
| [`ontosage:relatedTopic`]({{ '/ontology/property/relatedTopic/' | relative_url }}) | object | [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}) | [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}) |
| [`ontosage:servesFloor`]({{ '/ontology/property/servesFloor/' | relative_url }}) | object | [`brick:Floor`](https://ontology.brickschema.org/1.4/#brick:Floor) | [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}) |
| [`ontosage:usageFee`]({{ '/ontology/property/usageFee/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}) |

## Used as the range of

| Property | Kind | Domain |
|---|---|---|
| [`ontosage:concernsIssue`]({{ '/ontology/property/concernsIssue/' | relative_url }}) | object | [`ontosage:Report`]({{ '/ontology/class/Report/' | relative_url }}) |

## SHACL shapes

- [`ontosage:CapabilityShape`]({{ '/ontology/vocabulary/shacl-shapes/' | relative_url }}#CapabilityShape) targets [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }})
  - path [`ontosage:layTerms`]({{ '/ontology/property/layTerms/' | relative_url }}); min `1`; datatype `xsd:string`. Every ontosage:Capability should carry at least one ontosage:layTerms value — it is how a stakeholder question is matched to it.

## Competency questions

- The toilet is leaking — who do I tell, and how urgent is it?

## Example SPARQL

{% raw %}
```sparql
# Match a stated fault to its issue and return the report route + priority.
SELECT ?issue ?reportTo ?priority WHERE {
  ?issue a ontosage:MaintenanceIssue ; ontosage:layTerms ?lt .
  OPTIONAL { ?issue ontosage:reportTo ?reportTo }
  OPTIONAL { ?issue ontosage:priority ?priority }
  FILTER(CONTAINS(LCASE(?lt), "leak"))
} LIMIT 1
```
{% endraw %}

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:MaintenanceIssue a owl:Class ;
    rdfs:label "Maintenance / fault issue"@en ;
    ontosage:competencyQuestion "The toilet is leaking — who do I tell, and how urgent is it?" ;
    ontosage:exampleSparql """
        # Match a stated fault to its issue and return the report route + priority.
        SELECT ?issue ?reportTo ?priority WHERE {
          ?issue a ontosage:MaintenanceIssue ; ontosage:layTerms ?lt .
          OPTIONAL { ?issue ontosage:reportTo ?reportTo }
          OPTIONAL { ?issue ontosage:priority ?priority }
          FILTER(CONTAINS(LCASE(?lt), "leak"))
        } LIMIT 1""" ;
    rdfs:comment "A fault type and who to report it to: leak, broken light, broken lift, heating fault. MAY reference the brick:Equipment it concerns via ontosage:aboutEquipment."@en ;
    rdfs:subClassOf ontosage:KnowledgeTopic ;
    skos:example "\"there is a water leak\" -> the leak maintenance issue (report route = Estates)." .
```
{% endraw %}
