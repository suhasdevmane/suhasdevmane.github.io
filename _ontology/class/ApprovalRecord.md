---
title: "ontosage:ApprovalRecord"
layout: post
permalink: /ontology/class/ApprovalRecord/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › ApprovalRecord

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#ApprovalRecord` |
| Label | Approval and evidence record |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Whether a subject is approved, by which ROLE, under whose authority and until when; what evidence substantiates it, referenced and dated; who is accountable and when it is next reviewed. APPROVAL AND EVIDENCE ARE SEPARATE: a subject can be approved with no evidence recorded, or evidenced but never approved, and collapsing them into one 'verified' flag would hide exactly the gap an auditor is looking for. Roles, never people.

## Examples

- is this route approved and what evidence supports it? -&gt; ApprovalRecord whose label names the route; read approvalDecision, evidenceKind and evidenceDate.

## Lay terms

Plain-language phrases declared on this term with `ontosage:layTerms`. A question that contains one of them can be matched to this term. (26)

`approval`, `approval decision`, `approval evidence`, `approval expiry`, `approval record`, `approval records`, `approval status`, `approvals`, `approved`, `approved by`, `authorisation`, `authorised by`, `authorized by`, `evidence of approval`, `formally approved`, `officially approved`, `review due`, `sign off`, `sign-off`, `signed off`, `who approved`, `who authorised`, `who authorized`, `who is accountable`, `who owns`, `who signed off`

## Qualifier terms

Terms that name this class only when used of it, declared with `ontosage:qualifierTerms`. (7)

`approved`, `authorised`, `authorized`, `confirmed`, `evidenced`, `permitted`, `verified`

## Class hierarchy

Superclasses:

- [`ontosage:IntervalRecord`]({{ '/ontology/class/IntervalRecord/' | relative_url }}) › **`ontosage:ApprovalRecord`**

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:approvalDecision`]({{ '/ontology/property/approvalDecision/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:approvalSubjectKind`]({{ '/ontology/property/approvalSubjectKind/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:approvedByRole`]({{ '/ontology/property/approvedByRole/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:evidenceKind`]({{ '/ontology/property/evidenceKind/' | relative_url }}) | datatype | `xsd:string` | this class |
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

Record documents of type `approval_evidence` are lifted into instances of this class ([mapping]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#approval_evidence)).

## Turtle

Development notes were removed from one or more text values below; the source file holds the full text.

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:ApprovalRecord a owl:Class ;
    rdfs:label "Approval and evidence record"@en ;
    ontosage:layTerms "approval",
        "approval decision",
        "approval evidence",
        "approval expiry",
        "approval record",
        "approval records",
        "approval status",
        "approvals",
        "approved",
        "approved by",
        "authorisation",
        "authorised by",
        "authorized by",
        "evidence of approval",
        "formally approved",
        "officially approved",
        "review due",
        "sign off",
        "sign-off",
        "signed off",
        "who approved",
        "who authorised",
        "who authorized",
        "who is accountable",
        "who owns",
        "who signed off" ;
    ontosage:qualifierTerms "approved",
        "authorised",
        "authorized",
        "confirmed",
        "evidenced",
        "permitted",
        "verified" ;
    rdfs:comment "Whether a subject is approved, by which ROLE, under whose authority and until when; what evidence substantiates it, referenced and dated; who is accountable and when it is next reviewed. APPROVAL AND EVIDENCE ARE SEPARATE: a subject can be approved with no evidence recorded, or evidenced but never approved, and collapsing them into one 'verified' flag would hide exactly the gap an auditor is looking for. Roles, never people."@en ;
    rdfs:subClassOf ontosage:IntervalRecord ;
    skos:example "is this route approved and what evidence supports it? -> ApprovalRecord whose label names the route; read approvalDecision, evidenceKind and evidenceDate." .
```
{% endraw %}
