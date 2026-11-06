---
title: "SHACL shapes"
layout: post
permalink: /ontology/vocabulary/shacl-shapes/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Vocabularies]({{ '/docs/ontology-browser/' | relative_url }}#vocabularies) › SHACL shapes

The schema declares 3 SHACL node shapes. Each targets a class and states the constraints an instance should meet.

## Concept shape {#ConceptShape}

`hbco:ConceptShape` targets [`hbco:Concept`]({{ '/ontology/class/Concept/' | relative_url }}).

| Path | Min | Max | Datatype | Message |
|---|---|---|---|---|
| [`hbco:requiresRecipe`]({{ '/ontology/property/requiresRecipe/' | relative_url }}) |  | 1 | `xsd:string` | hbco:requiresRecipe must be a single xsd:string if present. |
| [`hbco:layTerm`]({{ '/ontology/property/layTerm/' | relative_url }}) | 1 |  | `xsd:string` | Every hbco:Concept must have at least one hbco:layTerm. |
| [`hbco:personaDepth`]({{ '/ontology/property/personaDepth/' | relative_url }}) |  | 1 | `xsd:integer` | hbco:personaDepth must be a single integer if present. |

### Turtle

{% raw %}
```turtle
@prefix hbco: <http://ontosage.org/hbco#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

hbco:ConceptShape a sh:NodeShape ;
    rdfs:label "Concept shape"@en ;
    sh:property [ sh:datatype xsd:string ;
            sh:maxCount 1 ;
            sh:message "hbco:requiresRecipe must be a single xsd:string if present."@en ;
            sh:path hbco:requiresRecipe ],
        [ sh:datatype xsd:string ;
            sh:message "Every hbco:Concept must have at least one hbco:layTerm."@en ;
            sh:minCount 1 ;
            sh:path hbco:layTerm ],
        [ sh:datatype xsd:integer ;
            sh:maxCount 1 ;
            sh:message "hbco:personaDepth must be a single integer if present."@en ;
            sh:path hbco:personaDepth ] ;
    sh:targetClass hbco:Concept .
```
{% endraw %}

## Capability shape {#CapabilityShape}

`ontosage:CapabilityShape` targets [`ontosage:Capability`]({{ '/ontology/class/Capability/' | relative_url }}).

| Path | Min | Max | Datatype | Message |
|---|---|---|---|---|
| [`ontosage:layTerms`]({{ '/ontology/property/layTerms/' | relative_url }}) | 1 |  | `xsd:string` | Every ontosage:Capability should carry at least one ontosage:layTerms value — it is how a stakeholder question is matched to it. |

### Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:CapabilityShape a sh:NodeShape ;
    rdfs:label "Capability shape"@en ;
    sh:property [ sh:datatype xsd:string ;
            sh:message "Every ontosage:Capability should carry at least one ontosage:layTerms value — it is how a stakeholder question is matched to it."@en ;
            sh:minCount 1 ;
            sh:path ontosage:layTerms ] ;
    sh:targetClass ontosage:Capability .
```
{% endraw %}

## Report shape {#ReportShape}

`ontosage:ReportShape` targets [`ontosage:Report`]({{ '/ontology/class/Report/' | relative_url }}).

| Path | Min | Max | Datatype | Message |
|---|---|---|---|---|
| [`ontosage:reportSubjectText`]({{ '/ontology/property/reportSubjectText/' | relative_url }}) | 1 |  | `xsd:string` | Every ontosage:Report must record what is being reported (ontosage:reportSubjectText). |

### Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ontosage:ReportShape a sh:NodeShape ;
    rdfs:label "Report shape"@en ;
    sh:property [ sh:datatype xsd:string ;
            sh:message "Every ontosage:Report must record what is being reported (ontosage:reportSubjectText)."@en ;
            sh:minCount 1 ;
            sh:path ontosage:reportSubjectText ] ;
    sh:targetClass ontosage:Report .
```
{% endraw %}

