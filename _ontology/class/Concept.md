---
title: "hbco:Concept"
layout: post
permalink: /ontology/class/Concept/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › Concept

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#Concept` |
| Label | HBCO Concept |
| Defined in | [`ontology/hbco_core.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/hbco_core.ttl), [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

An environment/comfort concept an occupant expresses in lay language, mapped to Brick sensor classes.

## Description

A building-condition or environment concept that occupants express in natural language (e.g. 'stuffy', 'too warm', 'noisy'). Each concept maps to one or more Brick sensor classes whose readings satisfy it — the bridge from lay language to live data.

## Examples

- `hbco:Concept_Stuffy hbco:layTerm "stuffy" ; hbco:mapsToBrickClass brick:CO2_Sensor .`

## Class hierarchy

Superclasses: none (a root class).

Direct subclasses (1; 1 descendants in all):

- [`hbco:CompositeConcept`]({{ '/ontology/class/CompositeConcept/' | relative_url }}) Composite HBCO Concept

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`hbco:componentOf`]({{ '/ontology/property/componentOf/' | relative_url }}) | object | [`hbco:CompositeConcept`]({{ '/ontology/class/CompositeConcept/' | relative_url }}) | this class |
| [`hbco:conceptId`]({{ '/ontology/property/conceptId/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`hbco:confidence`]({{ '/ontology/property/confidence/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`hbco:defaultUnit`]({{ '/ontology/property/defaultUnit/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`hbco:layTerm`]({{ '/ontology/property/layTerm/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`hbco:mapsToBrickClass`]({{ '/ontology/property/mapsToBrickClass/' | relative_url }}) | object | `owl:Class` | this class |
| [`hbco:personaDepth`]({{ '/ontology/property/personaDepth/' | relative_url }}) | datatype | `xsd:integer` | this class |
| [`hbco:requiresRecipe`]({{ '/ontology/property/requiresRecipe/' | relative_url }}) | datatype | `xsd:string` | this class |

## SHACL shapes

- [`hbco:ConceptShape`]({{ '/ontology/vocabulary/shacl-shapes/' | relative_url }}#ConceptShape) targets [`hbco:Concept`]({{ '/ontology/class/Concept/' | relative_url }})
  - path [`hbco:requiresRecipe`]({{ '/ontology/property/requiresRecipe/' | relative_url }}); max `1`; datatype `xsd:string`. hbco:requiresRecipe must be a single xsd:string if present.
  - path [`hbco:layTerm`]({{ '/ontology/property/layTerm/' | relative_url }}); min `1`; datatype `xsd:string`. Every hbco:Concept must have at least one hbco:layTerm.
  - path [`hbco:personaDepth`]({{ '/ontology/property/personaDepth/' | relative_url }}); max `1`; datatype `xsd:integer`. hbco:personaDepth must be a single integer if present.

## Alignments

| Mapping | Term |
|---|---|
| `skos:closeMatch` | [`sosa:ObservableProperty`](http://www.w3.org/ns/sosa/ObservableProperty) |

## Members

`ontology/hbco_mappings.ttl` declares 90 individuals typed with this class directly, and 13 typed with its subclass `hbco:CompositeConcept`: see [HBCO concepts]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}).

## Competency questions

- Is it stuffy / too warm / too noisy in here?

## Example SPARQL

{% raw %}
```sparql
# "is it stuffy?" — resolve the lay concept to its Brick sensor class,
# then find those sensors + UUIDs to fetch live readings from the time-series DB.
SELECT ?sensor ?uuid WHERE {
  ?concept a hbco:Concept ; hbco:layTerm ?term ; hbco:mapsToBrickClass ?cls .
  FILTER(CONTAINS(LCASE(?term), "stuffy"))
  ?sensor a ?cls ; ?anyRefPred ?ref .
  ?ref ref:hasTimeseriesId ?uuid .
  FILTER(?anyRefPred IN (ref:hasExternalReference, ashrae:hasExternalReference, brick:hasExternalReference))
} LIMIT 25
```
{% endraw %}

## Turtle

{% raw %}
```turtle
@prefix hbco: <http://ontosage.org/hbco#> .
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .

hbco:Concept a owl:Class ;
    rdfs:label "HBCO Concept"@en ;
    ontosage:competencyQuestion "Is it stuffy / too warm / too noisy in here?" ;
    ontosage:exampleSparql """
        # "is it stuffy?" — resolve the lay concept to its Brick sensor class,
        # then find those sensors + UUIDs to fetch live readings from the time-series DB.
        SELECT ?sensor ?uuid WHERE {
          ?concept a hbco:Concept ; hbco:layTerm ?term ; hbco:mapsToBrickClass ?cls .
          FILTER(CONTAINS(LCASE(?term), "stuffy"))
          ?sensor a ?cls ; ?anyRefPred ?ref .
          ?ref ref:hasTimeseriesId ?uuid .
          FILTER(?anyRefPred IN (ref:hasExternalReference, ashrae:hasExternalReference, brick:hasExternalReference))
        } LIMIT 25""" ;
    rdfs:comment "A building-condition or environment concept that occupants express in natural language (e.g. 'stuffy', 'too warm', 'noisy'). Each concept maps to one or more Brick sensor classes whose readings satisfy it — the bridge from lay language to live data."@en ;
    rdfs:isDefinedBy <http://ontosage.org/ontology> ;
    skos:closeMatch sosa:ObservableProperty ;
    skos:definition "An environment/comfort concept an occupant expresses in lay language, mapped to Brick sensor classes."@en ;
    skos:example "hbco:Concept_Stuffy hbco:layTerm \"stuffy\" ; hbco:mapsToBrickClass brick:CO2_Sensor ." .
```
{% endraw %}
