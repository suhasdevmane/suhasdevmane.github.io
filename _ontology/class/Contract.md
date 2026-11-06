---
title: "ontosage:Contract"
layout: post
permalink: /ontology/class/Contract/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › Contract

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#Contract` |
| Label | Contract |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A service, maintenance or supply agreement with a provider, over a term, covering a named scope. Distinct from Warranty: a contract is bought, a warranty accompanies an asset — they have different owners and routinely disagree, which should be REPORTED rather than resolved.

## Examples

- who maintains the lifts and until when? -&gt; Contract whose coveredScope names the lift asset.

## Lay terms

Plain-language phrases declared on this term with `ontosage:layTerms`. A question that contains one of them can be matched to this term. (16)

`agreement`, `agreements`, `contract`, `contracts`, `framework`, `maintained by`, `maintenance contract`, `maintenance contractor`, `service agreement`, `service provider`, `service providers`, `serviced by`, `supplier`, `who looks after`, `who maintains`, `who services`

## Class hierarchy

Superclasses:

- [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) › **`ontosage:Contract`**

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:aboutPoint`]({{ '/ontology/property/aboutPoint/' | relative_url }}) | object | [`brick:Point`](https://ontology.brickschema.org/1.4/#brick:Point) | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:aboutSpace`]({{ '/ontology/property/aboutSpace/' | relative_url }}) | object | [`brick:Location`](https://ontology.brickschema.org/1.4/#brick:Location) | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:completedDate`]({{ '/ontology/property/completedDate/' | relative_url }}) | datatype | `xsd:dateTime` | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:coveredScope`]({{ '/ontology/property/coveredScope/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:coversAsset`]({{ '/ontology/property/coversAsset/' | relative_url }}) | object | [`brick:Equipment`](https://ontology.brickschema.org/1.4/#brick:Equipment) | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:derivedFromDocument`]({{ '/ontology/property/derivedFromDocument/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:liftedByMapping`]({{ '/ontology/property/liftedByMapping/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:owningAuthority`]({{ '/ontology/property/owningAuthority/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:providerName`]({{ '/ontology/property/providerName/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:recordId`]({{ '/ontology/property/recordId/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:recordOwner`]({{ '/ontology/property/recordOwner/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:recordStatus`]({{ '/ontology/property/recordStatus/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:recordVersion`]({{ '/ontology/property/recordVersion/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:responsibleRole`]({{ '/ontology/property/responsibleRole/' | relative_url }}) | datatype | `xsd:string` | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:retrievedAt`]({{ '/ontology/property/retrievedAt/' | relative_url }}) | datatype | `xsd:dateTime` | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |
| [`ontosage:supersedes`]({{ '/ontology/property/supersedes/' | relative_url }}) | object | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) | [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) |

## Record document mapping

Record documents of type `contract` are lifted into instances of this class ([mapping]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#contract)).

## Turtle

Development notes were removed from one or more text values below; the source file holds the full text.

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:Contract a owl:Class ;
    rdfs:label "Contract"@en ;
    ontosage:layTerms "agreement",
        "agreements",
        "contract",
        "contracts",
        "framework",
        "maintained by",
        "maintenance contract",
        "maintenance contractor",
        "service agreement",
        "service provider",
        "service providers",
        "serviced by",
        "supplier",
        "who looks after",
        "who maintains",
        "who services" ;
    rdfs:comment "A service, maintenance or supply agreement with a provider, over a term, covering a named scope. Distinct from Warranty: a contract is bought, a warranty accompanies an asset — they have different owners and routinely disagree, which should be REPORTED rather than resolved."@en ;
    rdfs:subClassOf ontosage:IntervalRecord ;
    skos:example "who maintains the lifts and until when? -> Contract whose coveredScope names the lift asset." .
```
{% endraw %}
