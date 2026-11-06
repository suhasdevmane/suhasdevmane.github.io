---
title: "ontosage:AccessPermission"
layout: post
permalink: /ontology/class/AccessPermission/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › AccessPermission

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#AccessPermission` |
| Label | Access permission group |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

A named grant over one controlled opening to a ROLE TEMPLATE, under a time profile, with its inheritance and overrides recorded as data. NO INDIVIDUAL IS MODELLED, deliberately: identity is held at role level, so 'which entitlements does this role justify' is answerable and 'who can open this door' is not.

## Examples

- which permission group controls this opening, and through which inherited paths? -&gt; AccessPermission where controlsOpening matches, then follow inheritsFrom.

## Lay terms

Plain-language phrases declared on this term with `ontosage:layTerms`. A question that contains one of them can be matched to this term. (37)

`access card`, `access cards`, `access control`, `access group`, `access groups`, `access level`, `access levels`, `access reinstatement`, `access request`, `access restoration`, `access rights`, `access suspended`, `access suspension`, `badge`, `card access`, `credential`, `door access`, `entitlement`, `entitlements`, `erroneous suspension`, `escorted access`, `lockdown`, `permission`, `permission group`, `permission suspended`, `permission suspension`, `permissions`, `reinstate access`, `restore access`, `suspend access`, `suspended permission`, `suspension was wrong`, `swipe`, `time profile`, `who can get in`, `who has access`, `withdrawn permission`

## Class hierarchy

Superclasses:

- [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) › **`ontosage:AccessPermission`**

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:controlsOpening`]({{ '/ontology/property/controlsOpening/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:grantedToRole`]({{ '/ontology/property/grantedToRole/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:inheritsFrom`]({{ '/ontology/property/inheritsFrom/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:overriddenBy`]({{ '/ontology/property/overriddenBy/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:timeProfile`]({{ '/ontology/property/timeProfile/' | relative_url }}) | datatype | `xsd:string` | this class |
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

Record documents of type `access_permission` are lifted into instances of this class ([mapping]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#access_permission)).

## Turtle

Development notes were removed from one or more text values below; the source file holds the full text.

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:AccessPermission a owl:Class ;
    rdfs:label "Access permission group"@en ;
    ontosage:layTerms "access card",
        "access cards",
        "access control",
        "access group",
        "access groups",
        "access level",
        "access levels",
        "access reinstatement",
        "access request",
        "access restoration",
        "access rights",
        "access suspended",
        "access suspension",
        "badge",
        "card access",
        "credential",
        "door access",
        "entitlement",
        "entitlements",
        "erroneous suspension",
        "escorted access",
        "lockdown",
        "permission",
        "permission group",
        "permission suspended",
        "permission suspension",
        "permissions",
        "reinstate access",
        "restore access",
        "suspend access",
        "suspended permission",
        "suspension was wrong",
        "swipe",
        "time profile",
        "who can get in",
        "who has access",
        "withdrawn permission" ;
    rdfs:comment "A named grant over one controlled opening to a ROLE TEMPLATE, under a time profile, with its inheritance and overrides recorded as data. NO INDIVIDUAL IS MODELLED, deliberately: identity is held at role level, so 'which entitlements does this role justify' is answerable and 'who can open this door' is not."@en ;
    rdfs:subClassOf ontosage:IntervalRecord ;
    skos:example "which permission group controls this opening, and through which inherited paths? -> AccessPermission where controlsOpening matches, then follow inheritsFrom." .
```
{% endraw %}
