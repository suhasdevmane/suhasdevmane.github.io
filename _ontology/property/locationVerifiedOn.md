---
title: "ontosage:locationVerifiedOn"
layout: post
permalink: /ontology/property/locationVerifiedOn/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › locationVerifiedOn

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#locationVerifiedOn` |
| Label | location verified on |
| Kind | datatype property |
| Domain | [`ontosage:AssetEngineeringProfile`]({{ '/ontology/class/AssetEngineeringProfile/' | relative_url }}) |
| Range | `xsd:date` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

When the recorded location was last confirmed against the asset's actual position. A location nobody has checked is a record, not a fact — and 'does the recorded location match where the asset can currently be found?' is a question about this field, not about the location field.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`asset_engineering`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#asset_engineering) | `location_verified_on` | `xsd:date` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:locationVerifiedOn a owl:DatatypeProperty ;
    rdfs:label "location verified on"@en ;
    rdfs:comment "When the recorded location was last confirmed against the asset's actual position. A location nobody has checked is a record, not a fact — and 'does the recorded location match where the asset can currently be found?' is a question about this field, not about the location field."@en ;
    rdfs:domain ontosage:AssetEngineeringProfile ;
    rdfs:range xsd:date .
```
{% endraw %}
