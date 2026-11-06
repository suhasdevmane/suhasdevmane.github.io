---
title: "ontosage:measuresQuantityKind"
layout: post
permalink: /ontology/property/measuresQuantityKind/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Properties]({{ '/docs/ontology-browser/' | relative_url }}#property-index) › measuresQuantityKind

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/capabilities#measuresQuantityKind` |
| Label | measures quantity kind |
| Kind | object property |
| Domain | not declared (any subject) |
| Range | not declared |
| Inverse | none declared |
| Sub-property of | none |
| Defined in | [`ontology/measurand_kinds.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/measurand_kinds.ttl) |

## Definition

The physical quantity a sensor class measures, stated by OntoSage rather than inferred from a class hierarchy. Two classes related by rdfs:subClassOf may still measure different quantities: Brick puts TVOC under Particulate\_Matter\_Sensor because that class means 'pollutant sensor' in Brick's own definition, not because a VOC is a particulate. Where they differ, a count rolled up the hierarchy has to say what it included.

## Used in the schema

63 schema term(s) carry this property:

- [`brick:Access_Reader`](https://ontology.brickschema.org/1.4/#brick:Access_Reader)
- [`brick:Active_Power_Sensor`](https://ontology.brickschema.org/1.4/#brick:Active_Power_Sensor)
- [`brick:Air_Flow_Sensor`](https://ontology.brickschema.org/1.4/#brick:Air_Flow_Sensor)
- [`brick:Air_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Air_Temperature_Sensor)
- [`brick:Building_Water_Meter`](https://ontology.brickschema.org/1.4/#brick:Building_Water_Meter)
- [`brick:Chilled_Water_Supply_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Chilled_Water_Supply_Temperature_Sensor)
- [`brick:CO2_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO2_Level_Sensor)
- [`brick:CO2_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO2_Sensor)
- [`brick:CO_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO_Level_Sensor)
- [`brick:CO_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO_Sensor)
- [`brick:Contact_Sensor`](https://ontology.brickschema.org/1.4/#brick:Contact_Sensor)
- [`brick:Damper_Position_Sensor`](https://ontology.brickschema.org/1.4/#brick:Damper_Position_Sensor)
- [`brick:Electric_Power_Sensor`](https://ontology.brickschema.org/1.4/#brick:Electric_Power_Sensor)
- [`brick:Electrical_Energy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Electrical_Energy_Sensor)
- [`brick:Electrical_Meter`](https://ontology.brickschema.org/1.4/#brick:Electrical_Meter)
- [`brick:Energy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Energy_Sensor)
- [`brick:Entering_Water_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Entering_Water_Temperature_Sensor)
- [`brick:Flow_Sensor`](https://ontology.brickschema.org/1.4/#brick:Flow_Sensor)
- [`brick:Formaldehyde_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:Formaldehyde_Level_Sensor)
- [`brick:Hot_Water_Supply_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Hot_Water_Supply_Temperature_Sensor)
- [`brick:Humidity_Sensor`](https://ontology.brickschema.org/1.4/#brick:Humidity_Sensor)
- [`brick:Illuminance_Sensor`](https://ontology.brickschema.org/1.4/#brick:Illuminance_Sensor)
- [`brick:Leak_Detector_Equipment`](https://ontology.brickschema.org/1.4/#brick:Leak_Detector_Equipment)
- [`brick:Leaving_Water_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Leaving_Water_Temperature_Sensor)
- [`brick:Lighting_Correlated_Color_Temperature_Command`](https://ontology.brickschema.org/1.4/#brick:Lighting_Correlated_Color_Temperature_Command)
- [`brick:Lighting_Correlated_Color_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Lighting_Correlated_Color_Temperature_Sensor)
- [`brick:Luminance_Sensor`](https://ontology.brickschema.org/1.4/#brick:Luminance_Sensor)
- [`brick:Methane_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:Methane_Level_Sensor)
- [`brick:Motion_Sensor`](https://ontology.brickschema.org/1.4/#brick:Motion_Sensor)
- [`brick:NO2_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:NO2_Level_Sensor)
- [`brick:Noise_Sensor`](https://ontology.brickschema.org/1.4/#brick:Noise_Sensor)
- [`brick:Occupancy_Count_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Count_Sensor)
- [`brick:Occupancy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Sensor)
- [`brick:Occupancy_Status`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Status)
- [`brick:Ozone_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:Ozone_Level_Sensor)
- [`brick:Particulate_Matter_Sensor`](https://ontology.brickschema.org/1.4/#brick:Particulate_Matter_Sensor)
- [`brick:PM10_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:PM10_Level_Sensor)
- [`brick:PM10_Sensor`](https://ontology.brickschema.org/1.4/#brick:PM10_Sensor)
- [`brick:PM1_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:PM1_Level_Sensor)
- [`brick:PM1_Sensor`](https://ontology.brickschema.org/1.4/#brick:PM1_Sensor)
- [`brick:PM2.5_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:PM2.5_Level_Sensor)
- [`brick:PM2.5_Sensor`](https://ontology.brickschema.org/1.4/#brick:PM2.5_Sensor)
- [`brick:Position_Sensor`](https://ontology.brickschema.org/1.4/#brick:Position_Sensor)
- [`brick:Power_Sensor`](https://ontology.brickschema.org/1.4/#brick:Power_Sensor)
- [`brick:Relative_Humidity_Sensor`](https://ontology.brickschema.org/1.4/#brick:Relative_Humidity_Sensor)
- [`brick:Smoke_Detector`](https://ontology.brickschema.org/1.4/#brick:Smoke_Detector)
- [`brick:Solar_Irradiance_Sensor`](https://ontology.brickschema.org/1.4/#brick:Solar_Irradiance_Sensor)
- [`brick:Sound_Sensor`](https://ontology.brickschema.org/1.4/#brick:Sound_Sensor)
- [`brick:Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Temperature_Sensor)
- [`brick:TVOC_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:TVOC_Level_Sensor)
- [`brick:TVOC_Sensor`](https://ontology.brickschema.org/1.4/#brick:TVOC_Sensor)
- [`brick:Valve_Position_Sensor`](https://ontology.brickschema.org/1.4/#brick:Valve_Position_Sensor)
- [`brick:Vibration_Sensor`](https://ontology.brickschema.org/1.4/#brick:Vibration_Sensor)
- [`brick:Vibration_Sensor_Equipment`](https://ontology.brickschema.org/1.4/#brick:Vibration_Sensor_Equipment)
- [`brick:Water_Flow_Sensor`](https://ontology.brickschema.org/1.4/#brick:Water_Flow_Sensor)
- [`brick:Water_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:Water_Level_Sensor)
- [`brick:Water_Meter`](https://ontology.brickschema.org/1.4/#brick:Water_Meter)
- [`brick:Water_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Water_Temperature_Sensor)
- [`brick:Water_Usage_Sensor`](https://ontology.brickschema.org/1.4/#brick:Water_Usage_Sensor)
- [`brick:Zone_Air_Humidity_Sensor`](https://ontology.brickschema.org/1.4/#brick:Zone_Air_Humidity_Sensor)
- [`brick:Zone_Air_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Zone_Air_Temperature_Sensor)
- [`ontosage:Rainfall_Sensor`]({{ '/ontology/class/Rainfall_Sensor/' | relative_url }})
- [`ontosage:Soil_Moisture_Sensor`]({{ '/ontology/class/Soil_Moisture_Sensor/' | relative_url }})

## Turtle

{% raw %}
```turtle
@prefix ontosage: <http://ontosage.org/capabilities#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ontosage:measuresQuantityKind a owl:ObjectProperty ;
    rdfs:label "measures quantity kind"@en ;
    rdfs:comment "The physical quantity a sensor class measures, stated by OntoSage rather than inferred from a class hierarchy. Two classes related by rdfs:subClassOf may still measure different quantities: Brick puts TVOC under Particulate_Matter_Sensor because that class means 'pollutant sensor' in Brick's own definition, not because a VOC is a particulate. Where they differ, a count rolled up the hierarchy has to say what it included."@en .
```
{% endraw %}
