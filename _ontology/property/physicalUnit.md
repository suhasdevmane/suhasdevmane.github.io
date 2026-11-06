---
title: "ontosage:physicalUnit"
layout: post
permalink: /ontology/property/physicalUnit/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › physicalUnit

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#physicalUnit` |
| Label | physical unit |
| Kind | datatype property |
| Domain | [`ontosage:Measurand`]({{ '/ontology/class/Measurand/' | relative_url }}) |
| Range | not declared |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/measurand_kinds.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/measurand_kinds.ttl) |

## Definition

The unit the band is expressed in. A band without its unit is how a ppm range comes to be applied to a stream in ppb.

## Used in the schema

30 schema term(s) carry this property:

- [`ontosage:AirFlow`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#AirFlow)
- [`ontosage:AirQualityIndex`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#AirQualityIndex)
- [`ontosage:AirTemperature`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#AirTemperature)
- [`ontosage:BinaryState`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#BinaryState)
- [`ontosage:CarbonDioxide`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#CarbonDioxide)
- [`ontosage:CarbonMonoxide`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#CarbonMonoxide)
- [`ontosage:ColourTemperature`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#ColourTemperature)
- [`ontosage:ElectricalEnergy`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#ElectricalEnergy)
- [`ontosage:ElectricalPower`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#ElectricalPower)
- [`ontosage:EventCount`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#EventCount)
- [`ontosage:Formaldehyde`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#Formaldehyde)
- [`ontosage:Illuminance`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#Illuminance)
- [`ontosage:LinearPositionPercent`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#LinearPositionPercent)
- [`ontosage:Methane`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#Methane)
- [`ontosage:NitrogenDioxide`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#NitrogenDioxide)
- [`ontosage:OccupancyCount`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#OccupancyCount)
- [`ontosage:OxygenFraction`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#OxygenFraction)
- [`ontosage:Ozone`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#Ozone)
- [`ontosage:ParticulateMatter`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#ParticulateMatter)
- [`ontosage:Rainfall`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#Rainfall)
- [`ontosage:RelativeHumidity`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#RelativeHumidity)
- [`ontosage:SoilMoisture`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#SoilMoisture)
- [`ontosage:SolarIrradiance`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#SolarIrradiance)
- [`ontosage:SoundPressureLevel`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#SoundPressureLevel)
- [`ontosage:VibrationVelocity`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#VibrationVelocity)
- [`ontosage:VolatileOrganicCompounds`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#VolatileOrganicCompounds)
- [`ontosage:WaterFlow`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#WaterFlow)
- [`ontosage:WaterLevel`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#WaterLevel)
- [`ontosage:WaterTemperature`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#WaterTemperature)
- [`ontosage:WaterVolume`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#WaterVolume)

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ontosage:physicalUnit a owl:DatatypeProperty ;
    rdfs:label "physical unit"@en ;
    rdfs:comment "The unit the band is expressed in. A band without its unit is how a ppm range comes to be applied to a stream in ppb."@en ;
    rdfs:domain ontosage:Measurand .
```
{% endraw %}
