---
title: "ontosage:concernsIssue"
layout: post
permalink: /ontology/property/concernsIssue/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › concernsIssue

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#concernsIssue` |
| Label | concerns issue |
| Kind | object property |
| Domain | [`ontosage:Report`]({{ '/ontology/class/Report/' | relative_url }}) |
| Range | [`ontosage:MaintenanceIssue`]({{ '/ontology/class/MaintenanceIssue/' | relative_url }}) |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/ontosage_schema.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/ontosage_schema.ttl) |

## Definition

Links a report to the Module A ontosage:MaintenanceIssue it is an instance of, so its report route / priority are inherited.

## Examples

- `bldg:Report_042 ontosage:concernsIssue bldg:Issue_WaterLeak .`

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ontosage:concernsIssue a owl:ObjectProperty ;
    rdfs:label "concerns issue"@en ;
    rdfs:comment "Links a report to the Module A ontosage:MaintenanceIssue it is an instance of, so its report route / priority are inherited."@en ;
    rdfs:domain ontosage:Report ;
    rdfs:range ontosage:MaintenanceIssue ;
    skos:example "bldg:Report_042 ontosage:concernsIssue bldg:Issue_WaterLeak ." .
```
{% endraw %}
