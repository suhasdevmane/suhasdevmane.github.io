---
title: "ontosage:effectiveTo"
layout: post
permalink: /ontology/property/effectiveTo/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › effectiveTo

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#effectiveTo` |
| Label | effective until |
| Kind | datatype property |
| Domain | [`ontosage:ConfigurationPeriod`]({{ '/ontology/class/ConfigurationPeriod/' | relative_url }}) |
| Range | `xsd:dateTime` |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

End of the period. ABSENT means still in force — the open interval is the normal case, and writing a far-future date instead would silently expire.

## Used in record document mappings

| Record type | Column | Datatype |
|---|---|---|
| [`access_permission`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#access_permission) | `valid_to` | `xsd:date` |
| [`approval_evidence`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#approval_evidence) | `valid_until` | `xsd:date` |
| [`booking`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#booking) | `end` | `xsd:dateTime` |
| [`contract`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#contract) | `end` | `xsd:date` |
| [`permit_to_work`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#permit_to_work) | `expires` | `xsd:date` |
| [`tariff`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#tariff) | `end` | `xsd:date` |
| [`warranty`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#warranty) | `end` | `xsd:date` |
| [`waste_return`]({{ '/ontology/vocabulary/record-document-mappings/' | relative_url }}#waste_return) | `period_end` | `xsd:date` |

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:effectiveTo a owl:DatatypeProperty ;
    rdfs:label "effective until"@en ;
    rdfs:comment "End of the period. ABSENT means still in force — the open interval is the normal case, and writing a far-future date instead would silently expire."@en ;
    rdfs:domain ontosage:ConfigurationPeriod ;
    rdfs:range xsd:dateTime .
```
{% endraw %}
