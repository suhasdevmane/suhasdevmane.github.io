---
title: "ontosage:FireSafetyAsset"
layout: post
permalink: /ontology/class/FireSafetyAsset/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › FireSafetyAsset

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#FireSafetyAsset` |
| Label | Fire safety asset |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A physical fire precaution — detection, alarm, suppression, a fire door, a compartment penetration or an escape provision — with the date it was last tested, the evidence for that test, the standard it is held to and the defects open against it. Recorded separately from general plant because a fire precaution that is merely PRESENT proves nothing: the question is always when it was last proved to work.

## Examples

- which suppression assets need service, retest or evidence close-out? -&gt; FireSafetyAsset where nextTestDue has passed or evidenceReference is blank.

## Lay terms

Plain-language phrases declared on this term with `ontosage:layTerms`. A question that contains one of them can be matched to this term. (26)

`compartmentation`, `detection asset`, `detection assets`, `detection system`, `detection systems`, `emergency lighting`, `escape route`, `escape routes`, `extinguisher`, `extinguishers`, `fire alarm`, `fire compartment`, `fire detection`, `fire door`, `fire doors`, `fire precaution`, `fire precautions`, `fire safety asset`, `fire stopping`, `means of escape`, `smoke detection`, `smoke detector`, `smoke detectors`, `sprinkler`, `sprinklers`, `suppression`

## Class hierarchy

Superclasses:

- [`ontosage:Record`]({{ '/ontology/class/Record/' | relative_url }}) › **`ontosage:FireSafetyAsset`**

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:fireAssetKind`]({{ '/ontology/property/fireAssetKind/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:lastTestedOn`]({{ '/ontology/property/lastTestedOn/' | relative_url }}) | datatype | `xsd:date` | this class |
| [`ontosage:nextTestDue`]({{ '/ontology/property/nextTestDue/' | relative_url }}) | datatype | `xsd:date` | this class |
| [`ontosage:openDefect`]({{ '/ontology/property/openDefect/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:testStandard`]({{ '/ontology/property/testStandard/' | relative_url }}) | datatype | `xsd:string` | this class |

## Record document mapping

Record documents of type `fire_safety_asset` are lifted into instances of this class ([mapping]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#fire_safety_asset)).

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:FireSafetyAsset a owl:Class ;
    rdfs:label "Fire safety asset"@en ;
    ontosage:layTerms "compartmentation",
        "detection asset",
        "detection assets",
        "detection system",
        "detection systems",
        "emergency lighting",
        "escape route",
        "escape routes",
        "extinguisher",
        "extinguishers",
        "fire alarm",
        "fire compartment",
        "fire detection",
        "fire door",
        "fire doors",
        "fire precaution",
        "fire precautions",
        "fire safety asset",
        "fire stopping",
        "means of escape",
        "smoke detection",
        "smoke detector",
        "smoke detectors",
        "sprinkler",
        "sprinklers",
        "suppression" ;
    rdfs:comment "A physical fire precaution — detection, alarm, suppression, a fire door, a compartment penetration or an escape provision — with the date it was last tested, the evidence for that test, the standard it is held to and the defects open against it. Recorded separately from general plant because a fire precaution that is merely PRESENT proves nothing: the question is always when it was last proved to work."@en ;
    rdfs:subClassOf ontosage:Record ;
    skos:example "which suppression assets need service, retest or evidence close-out? -> FireSafetyAsset where nextTestDue has passed or evidenceReference is blank." .
```
{% endraw %}
