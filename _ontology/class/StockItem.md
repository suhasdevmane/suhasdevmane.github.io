---
title: "ontosage:StockItem"
layout: post
permalink: /ontology/class/StockItem/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Classes]({{ '/docs/ontology-browser/' | relative_url }}#class-hierarchy) › StockItem

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#StockItem` |
| Label | Stock item |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

One stock line: a kind of item held in one store, with the quantity on hand, the level below which it is reordered, who is accountable for it and when it was last counted. FOUR KINDS ARE KEPT APART because they answer different questions: a consumable is used up, a spare is held against a named asset, loan equipment is lent and returned, and surplus is withdrawn stock available for reuse. Quantity on hand is what is on the shelf now -- anything out on loan is stated in the note and never counted as stock, and a loan line never says who has an item. STATUS FOLLOWS THE NUMBERS: a line is in stock only when quantity on hand is at or above its minimum, so a shortage is a comparison the reader can check rather than an adjective. Safety-critical stock (fire extinguishers, emergency lighting parts, first-aid supplies, hazardous chemicals) is deliberately not held here.

## Examples

- which consumables are running low? -&gt; StockItem where stockKind = consumable and quantityOnHand &lt; minimumLevel; read nextDue for the delivery or reorder date.

## Lay terms

Plain-language phrases declared on this term with `ontosage:layTerms`. A question that contains one of them can be matched to this term. (55)

`any spares`, `available for redeployment`, `available for reuse`, `bin liners`, `borrow an adapter`, `borrow equipment`, `caretaker store`, `central stores`, `cleaning supplies`, `consumable`, `consumables`, `critical spares`, `equipment loan`, `goods store`, `hand soap`, `have spares`, `hdmi adapter`, `hdmi adapters`, `in stock`, `listening receivers`, `loan equipment`, `loan pool`, `loan stock`, `low on stock`, `low stock`, `on loan`, `out of stock`, `paper towels`, `presenter adapters`, `re-order`, `re-stock`, `reorder`, `reorder level`, `restock`, `running low on`, `spare part`, `spare parts`, `spares and consumables`, `spares available`, `spares should`, `spares staged`, `stock count`, `stock level`, `stock levels`, `stock take`, `stocktake`, `surplus equipment`, `surplus furniture`, `surplus items`, `surplus stock`, `toilet rolls`, `toilet tissue`, `washroom supplies`, `what spares`, `which spares`

## Class hierarchy

Superclasses:

- [`ontosage:Record`]({{ '/ontology/class/Record/' | relative_url }}) › **`ontosage:StockItem`**

Subclasses: none.

## Properties

Properties whose `rdfs:domain` is this class or one of its superclasses.

| Property | Kind | Range | Domain |
|---|---|---|---|
| [`ontosage:lastCounted`]({{ '/ontology/property/lastCounted/' | relative_url }}) | datatype | `xsd:date` | this class |
| [`ontosage:leadTimeDays`]({{ '/ontology/property/leadTimeDays/' | relative_url }}) | datatype | `xsd:integer` | this class |
| [`ontosage:minimumLevel`]({{ '/ontology/property/minimumLevel/' | relative_url }}) | datatype | `xsd:integer` | this class |
| [`ontosage:quantityOnHand`]({{ '/ontology/property/quantityOnHand/' | relative_url }}) | datatype | `xsd:integer` | this class |
| [`ontosage:stockCategory`]({{ '/ontology/property/stockCategory/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:stockKind`]({{ '/ontology/property/stockKind/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:stockUnit`]({{ '/ontology/property/stockUnit/' | relative_url }}) | datatype | `xsd:string` | this class |
| [`ontosage:usedFor`]({{ '/ontology/property/usedFor/' | relative_url }}) | datatype | `xsd:string` | this class |

## Record document mapping

Record documents of type `stock_item` are lifted into instances of this class ([mapping]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#stock_item)).

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:StockItem a owl:Class ;
    rdfs:label "Stock item"@en ;
    ontosage:layTerms "any spares",
        "available for redeployment",
        "available for reuse",
        "bin liners",
        "borrow an adapter",
        "borrow equipment",
        "caretaker store",
        "central stores",
        "cleaning supplies",
        "consumable",
        "consumables",
        "critical spares",
        "equipment loan",
        "goods store",
        "hand soap",
        "have spares",
        "hdmi adapter",
        "hdmi adapters",
        "in stock",
        "listening receivers",
        "loan equipment",
        "loan pool",
        "loan stock",
        "low on stock",
        "low stock",
        "on loan",
        "out of stock",
        "paper towels",
        "presenter adapters",
        "re-order",
        "re-stock",
        "reorder",
        "reorder level",
        "restock",
        "running low on",
        "spare part",
        "spare parts",
        "spares and consumables",
        "spares available",
        "spares should",
        "spares staged",
        "stock count",
        "stock level",
        "stock levels",
        "stock take",
        "stocktake",
        "surplus equipment",
        "surplus furniture",
        "surplus items",
        "surplus stock",
        "toilet rolls",
        "toilet tissue",
        "washroom supplies",
        "what spares",
        "which spares" ;
    rdfs:comment "One stock line: a kind of item held in one store, with the quantity on hand, the level below which it is reordered, who is accountable for it and when it was last counted. FOUR KINDS ARE KEPT APART because they answer different questions: a consumable is used up, a spare is held against a named asset, loan equipment is lent and returned, and surplus is withdrawn stock available for reuse. Quantity on hand is what is on the shelf now -- anything out on loan is stated in the note and never counted as stock, and a loan line never says who has an item. STATUS FOLLOWS THE NUMBERS: a line is in stock only when quantity on hand is at or above its minimum, so a shortage is a comparison the reader can check rather than an adjective. Safety-critical stock (fire extinguishers, emergency lighting parts, first-aid supplies, hazardous chemicals) is deliberately not held here."@en ;
    rdfs:subClassOf ontosage:Record ;
    skos:example "which consumables are running low? -> StockItem where stockKind = consumable and quantityOnHand < minimumLevel; read nextDue for the delivery or reorder date." .
```
{% endraw %}
