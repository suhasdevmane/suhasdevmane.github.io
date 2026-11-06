---
title: "hbco:CompositeConcept"
layout: post
permalink: /ontology/class/CompositeConcept/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › CompositeConcept

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#CompositeConcept` |
| Label | Composite HBCO Concept |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A concept whose measurement requires combining multiple atomic concepts (e.g. 'thermal comfort' = temperature + humidity).

## Examples

- hbco:Concept\_ThermalComfort a hbco:CompositeConcept .

## Class hierarchy

Superclasses:

- [`hbco:Concept`]({{ '/ontology/class/Concept/' | relative_url }}) › **`hbco:CompositeConcept`**

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`hbco:componentOf`]({{ '/ontology/property/componentOf/' | relative_url }}) | object | [`hbco:CompositeConcept`]({{ '/ontology/class/CompositeConcept/' | relative_url }}) | [`hbco:Concept`]({{ '/ontology/class/Concept/' | relative_url }}) |
| [`hbco:conceptId`]({{ '/ontology/property/conceptId/' | relative_url }}) | datatype | `xsd:string` | [`hbco:Concept`]({{ '/ontology/class/Concept/' | relative_url }}) |
| [`hbco:confidence`]({{ '/ontology/property/confidence/' | relative_url }}) | datatype | `xsd:string` | [`hbco:Concept`]({{ '/ontology/class/Concept/' | relative_url }}) |
| [`hbco:defaultUnit`]({{ '/ontology/property/defaultUnit/' | relative_url }}) | datatype | `xsd:string` | [`hbco:Concept`]({{ '/ontology/class/Concept/' | relative_url }}) |
| [`hbco:layTerm`]({{ '/ontology/property/layTerm/' | relative_url }}) | datatype | `xsd:string` | [`hbco:Concept`]({{ '/ontology/class/Concept/' | relative_url }}) |
| [`hbco:mapsToBrickClass`]({{ '/ontology/property/mapsToBrickClass/' | relative_url }}) | object | `owl:Class` | [`hbco:Concept`]({{ '/ontology/class/Concept/' | relative_url }}) |
| [`hbco:personaDepth`]({{ '/ontology/property/personaDepth/' | relative_url }}) | datatype | `xsd:integer` | [`hbco:Concept`]({{ '/ontology/class/Concept/' | relative_url }}) |
| [`hbco:requiresRecipe`]({{ '/ontology/property/requiresRecipe/' | relative_url }}) | datatype | `xsd:string` | [`hbco:Concept`]({{ '/ontology/class/Concept/' | relative_url }}) |

## Used as the range of

| Property | Kind | Domain |
|---|---|---|
| [`hbco:componentOf`]({{ '/ontology/property/componentOf/' | relative_url }}) | object | [`hbco:Concept`]({{ '/ontology/class/Concept/' | relative_url }}) |

## SHACL shapes

- [`hbco:ConceptShape`]({{ '/ontology/vocabulary/shacl-shapes/' | relative_url }}#ConceptShape) targets [`hbco:Concept`]({{ '/ontology/class/Concept/' | relative_url }})
  - path [`hbco:requiresRecipe`]({{ '/ontology/property/requiresRecipe/' | relative_url }}); max `1`; datatype `xsd:string`. hbco:requiresRecipe must be a single xsd:string if present.
  - path [`hbco:layTerm`]({{ '/ontology/property/layTerm/' | relative_url }}); min `1`; datatype `xsd:string`. Every hbco:Concept must have at least one hbco:layTerm.
  - path [`hbco:personaDepth`]({{ '/ontology/property/personaDepth/' | relative_url }}); max `1`; datatype `xsd:integer`. hbco:personaDepth must be a single integer if present.

## Members

`ontology/hbco_mappings.ttl` declares 13 individuals typed with this class directly: see [HBCO concepts]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}).

## Turtle

{% raw %}
```turtle
@prefix hbco: <http://ontosage.org/hbco#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

hbco:CompositeConcept a owl:Class ;
    rdfs:label "Composite HBCO Concept"@en ;
    rdfs:comment "A concept whose measurement requires combining multiple atomic concepts (e.g. 'thermal comfort' = temperature + humidity)."@en ;
    rdfs:isDefinedBy <http://ontosage.org/ontology> ;
    rdfs:subClassOf hbco:Concept ;
    skos:example "hbco:Concept_ThermalComfort a hbco:CompositeConcept ." .
```
{% endraw %}
