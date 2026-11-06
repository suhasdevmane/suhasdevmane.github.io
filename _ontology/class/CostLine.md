---
title: "ontosage:CostLine"
layout: post
permalink: /ontology/class/CostLine/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › CostLine

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#CostLine` |
| Label | Building cost line |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

One line of the building's ledger, carrying budget, actual, committed and accrued as SEPARATE amounts. Free balance is budget minus all three, and a register that folded commitments into actuals could report money as available when a purchase order has already claimed it -- 'decision-ready free balance' is precisely the figure after all three. varianceCause is recorded rather than inferred, because a line can move on price, quantity, timing or scope and the number alone cannot say which, while the remedies differ.

## Examples

- what is the decision-ready free balance? -&gt; sum(budgetAmount) - sum(actualAmount) - sum(committedAmount) - sum(accruedAmount) over the period.

## Lay terms

Plain-language phrases declared on this term with `ontosage:layTerms`. A question that contains one of them can be matched to this term. (21)

`accrual`, `accruals`, `actuals`, `budget`, `budgets`, `committed spend`, `cost`, `cost centre`, `costs`, `free balance`, `invoice`, `open commitments`, `overspend`, `procurement`, `purchase`, `spend`, `spending`, `supplier spend`, `underspend`, `variance`, `what did it cost`

## Class hierarchy

Superclasses:

- [`ontosage:Record`]({{ '/ontology/class/Record/' | relative_url }}) › **`ontosage:CostLine`**

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:accruedAmount`]({{ '/ontology/property/accruedAmount/' | relative_url }}) | datatype | `xsd:decimal` | this class |
| [`ontosage:actualAmount`]({{ '/ontology/property/actualAmount/' | relative_url }}) | datatype | `xsd:decimal` | this class |
| [`ontosage:budgetAmount`]({{ '/ontology/property/budgetAmount/' | relative_url }}) | datatype | `xsd:decimal` | this class |
| [`ontosage:codingCheckRequired`]({{ '/ontology/property/codingCheckRequired/' | relative_url }}) | datatype | `xsd:boolean` | this class |
| [`ontosage:committedAmount`]({{ '/ontology/property/committedAmount/' | relative_url }}) | datatype | `xsd:decimal` | this class |
| [`ontosage:costCentre`]({{ '/ontology/property/costCentre/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:spendCategory`]({{ '/ontology/property/spendCategory/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:varianceCause`]({{ '/ontology/property/varianceCause/' | relative_url }}) | datatype | `xsd:string` | this class |

## Record document mapping

Record documents of type `cost_line` are lifted into instances of this class ([mapping]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#cost_line)).

## Turtle

Development notes were removed from one or more text values below; the source file holds the full text.

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:CostLine a owl:Class ;
    rdfs:label "Building cost line"@en ;
    ontosage:layTerms "accrual",
        "accruals",
        "actuals",
        "budget",
        "budgets",
        "committed spend",
        "cost",
        "cost centre",
        "costs",
        "free balance",
        "invoice",
        "open commitments",
        "overspend",
        "procurement",
        "purchase",
        "spend",
        "spending",
        "supplier spend",
        "underspend",
        "variance",
        "what did it cost" ;
    rdfs:comment "One line of the building's ledger, carrying budget, actual, committed and accrued as SEPARATE amounts. Free balance is budget minus all three, and a register that folded commitments into actuals could report money as available when a purchase order has already claimed it -- 'decision-ready free balance' is precisely the figure after all three. varianceCause is recorded rather than inferred, because a line can move on price, quantity, timing or scope and the number alone cannot say which, while the remedies differ."@en ;
    rdfs:subClassOf ontosage:Record ;
    skos:example "what is the decision-ready free balance? -> sum(budgetAmount) - sum(actualAmount) - sum(committedAmount) - sum(accruedAmount) over the period." .
```
{% endraw %}
