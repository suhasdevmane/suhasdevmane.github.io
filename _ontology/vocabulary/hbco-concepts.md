---
title: "HBCO concepts"
layout: post
permalink: /ontology/vocabulary/hbco-concepts/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Vocabularies]({{ '/docs/ontology-browser/' | relative_url }}#vocabularies) › HBCO concepts

The Human-Building Conversation Ontology (HBCO) maps the words occupants use for the indoor environment to the Brick sensor classes whose readings answer them. Each concept is an individual of [`hbco:Concept`]({{ '/ontology/class/Concept/' | relative_url }}); a [`hbco:CompositeConcept`]({{ '/ontology/class/CompositeConcept/' | relative_url }}) combines several. The concept resolver matches a question against the lay terms, then uses `hbco:mapsToBrickClass` to find sensors and `hbco:requiresRecipe` to choose how to evaluate the readings.

Source: [`ontology/hbco_mappings.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/hbco_mappings.ttl). It declares 103 concepts (90 atomic, 13 composite) with 728 lay terms, mapped to 68 distinct sensor or point classes (60 in the Brick namespace, the rest OntoSage's own).

## Index

| Concept | Type | Maps to | Recipe |
|---|---|---|---|
| [`hbco:acoustic_comfort`](#acoustic_comfort) | composite | [`ontosage:Sound_Level_Sensor`]({{ '/ontology/class/Sound_Level_Sensor/' | relative_url }}) | `range` |
| [`hbco:after_hours`](#after_hours) | atomic | [`brick:Energy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Energy_Sensor), [`brick:Occupancy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Sensor) | `aggregate` |
| [`hbco:air_flow_rate`](#air_flow_rate) | atomic | [`brick:Air_Flow_Sensor`](https://ontology.brickschema.org/1.4/#brick:Air_Flow_Sensor) | `aggregate` |
| [`hbco:ashrae_compliance`](#ashrae_compliance) | atomic | [`brick:Humidity_Sensor`](https://ontology.brickschema.org/1.4/#brick:Humidity_Sensor), [`brick:Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Temperature_Sensor) | `range` |
| [`hbco:busy`](#busy) | atomic | [`brick:Occupancy_Count_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Count_Sensor), [`brick:Occupancy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Sensor) | `aggregate` |
| [`hbco:busyness`](#busyness) | composite | [`brick:Occupancy_Count_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Count_Sensor), [`brick:Occupancy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Sensor) | `aggregate` |
| [`hbco:carbon_footprint`](#carbon_footprint) | atomic | [`brick:Energy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Energy_Sensor) | `aggregate` |
| [`hbco:carbon_monoxide`](#carbon_monoxide) | atomic | [`brick:CO_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO_Level_Sensor), [`brick:CO_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO_Sensor) | `threshold` |
| [`hbco:chilled_water_return`](#chilled_water_return) | atomic | [`brick:Entering_Chilled_Water_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Entering_Chilled_Water_Temperature_Sensor) | `aggregate` |
| [`hbco:chilled_water_supply`](#chilled_water_supply) | atomic | [`brick:Leaving_Chilled_Water_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Leaving_Chilled_Water_Temperature_Sensor) | `aggregate` |
| [`hbco:co2_compliance`](#co2_compliance) | atomic | [`brick:CO2_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO2_Level_Sensor) | `threshold` |
| [`hbco:co2_level`](#co2_level) | composite | [`brick:CO2_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO2_Level_Sensor), [`brick:CO2_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO2_Sensor) | `threshold` |
| [`hbco:congestion_hotspot`](#congestion_hotspot) | atomic | [`brick:Motion_Sensor`](https://ontology.brickschema.org/1.4/#brick:Motion_Sensor), [`brick:Occupancy_Count_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Count_Sensor), [`brick:Occupancy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Sensor) | `aggregate` |
| [`hbco:crowded`](#crowded) | atomic | [`brick:Motion_Sensor`](https://ontology.brickschema.org/1.4/#brick:Motion_Sensor), [`brick:Occupancy_Count_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Count_Sensor), [`brick:Occupancy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Sensor) | `threshold` |
| [`hbco:damper_position`](#damper_position) | atomic | [`brick:Damper_Position_Command`](https://ontology.brickschema.org/1.4/#brick:Damper_Position_Command), [`brick:Damper_Position_Sensor`](https://ontology.brickschema.org/1.4/#brick:Damper_Position_Sensor) | `aggregate` |
| [`hbco:data_privacy`](#data_privacy) | atomic |  | `aggregate` |
| [`hbco:draft`](#draft) | atomic | [`brick:Supply_Air_Flow_Sensor`](https://ontology.brickschema.org/1.4/#brick:Supply_Air_Flow_Sensor), [`brick:Supply_Air_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Supply_Air_Temperature_Sensor), [`brick:Zone_Air_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Zone_Air_Temperature_Sensor) | `correlate` |
| [`hbco:electric_power`](#electric_power) | atomic | [`brick:Electric_Power_Sensor`](https://ontology.brickschema.org/1.4/#brick:Electric_Power_Sensor) | `aggregate` |
| [`hbco:emergency_exit`](#emergency_exit) | atomic | [`brick:Smoke_Detector`](https://ontology.brickschema.org/1.4/#brick:Smoke_Detector) | `threshold` |
| [`hbco:empty_space`](#empty_space) | atomic | [`brick:Motion_Sensor`](https://ontology.brickschema.org/1.4/#brick:Motion_Sensor), [`brick:Occupancy_Count_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Count_Sensor), [`brick:Occupancy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Sensor), [`brick:Occupancy_Status`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Status) | `threshold` |
| [`hbco:energy_consumption`](#energy_consumption) | composite | [`brick:Energy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Energy_Sensor) | `aggregate` |
| [`hbco:energy_cost`](#energy_cost) | atomic | [`brick:Energy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Energy_Sensor) | `aggregate` |
| [`hbco:energy_saving_tip`](#energy_saving_tip) | atomic | [`brick:Energy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Energy_Sensor) | `aggregate` |
| [`hbco:energy_trend`](#energy_trend) | atomic | [`brick:Energy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Energy_Sensor) | `trend` |
| [`hbco:energy_waste`](#energy_waste) | atomic | [`brick:Energy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Energy_Sensor) | `threshold` |
| [`hbco:equipment_condition`](#equipment_condition) | composite | [`brick:Fault_Status`](https://ontology.brickschema.org/1.4/#brick:Fault_Status) | `threshold` |
| [`hbco:equipment_working`](#equipment_working) | composite | [`brick:Fault_Status`](https://ontology.brickschema.org/1.4/#brick:Fault_Status) | `threshold` |
| [`hbco:fan_status`](#fan_status) | atomic | [`brick:Fan_Status`](https://ontology.brickschema.org/1.4/#brick:Fan_Status) | `aggregate` |
| [`hbco:filter_pressure`](#filter_pressure) | atomic | [`brick:Filter_Differential_Pressure_Sensor`](https://ontology.brickschema.org/1.4/#brick:Filter_Differential_Pressure_Sensor) | `threshold` |
| [`hbco:fire_safety`](#fire_safety) | composite | [`brick:Fire_Alarm`](https://ontology.brickschema.org/1.4/#brick:Fire_Alarm), [`brick:Smoke_Detector`](https://ontology.brickschema.org/1.4/#brick:Smoke_Detector) | `threshold` |
| [`hbco:focus_environment`](#focus_environment) | atomic | [`brick:CO2_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO2_Level_Sensor), [`brick:Illuminance_Sensor`](https://ontology.brickschema.org/1.4/#brick:Illuminance_Sensor), [`ontosage:Sound_Level_Sensor`]({{ '/ontology/class/Sound_Level_Sensor/' | relative_url }}) | `range` |
| [`hbco:formaldehyde`](#formaldehyde) | atomic | [`brick:Formaldehyde_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:Formaldehyde_Level_Sensor) | `threshold` |
| [`hbco:future_energy`](#future_energy) | atomic | [`brick:Energy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Energy_Sensor) | `trend` |
| [`hbco:future_temperature`](#future_temperature) | atomic | [`brick:Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Temperature_Sensor) | `trend` |
| [`hbco:gas_level`](#gas_level) | atomic | [`brick:Gas_Sensor`](https://ontology.brickschema.org/1.4/#brick:Gas_Sensor) | `threshold` |
| [`hbco:green_certification`](#green_certification) | atomic |  | `aggregate` |
| [`hbco:humidity_reading`](#humidity_reading) | atomic | [`brick:Humidity_Sensor`](https://ontology.brickschema.org/1.4/#brick:Humidity_Sensor), [`brick:Relative_Humidity_Sensor`](https://ontology.brickschema.org/1.4/#brick:Relative_Humidity_Sensor) | `aggregate` |
| [`hbco:humidity_setpoint`](#humidity_setpoint) | atomic | [`brick:Humidity_Setpoint`](https://ontology.brickschema.org/1.4/#brick:Humidity_Setpoint) | `range` |
| [`hbco:hvac_performance`](#hvac_performance) | atomic | [`brick:Air_Handling_Unit`](https://ontology.brickschema.org/1.4/#brick:Air_Handling_Unit), [`brick:Zone_Air_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Zone_Air_Temperature_Sensor) | `threshold` |
| [`hbco:iaq_composite`](#iaq_composite) | composite | [`brick:Air_Quality_Sensor`](https://ontology.brickschema.org/1.4/#brick:Air_Quality_Sensor), [`brick:CO2_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO2_Level_Sensor), [`brick:PM2.5_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:PM2.5_Level_Sensor), [`brick:TVOC_Sensor`](https://ontology.brickschema.org/1.4/#brick:TVOC_Sensor) | `aggregate` |
| [`hbco:inside_vs_outside`](#inside_vs_outside) | atomic | [`brick:Outside_Air_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Outside_Air_Temperature_Sensor), [`brick:Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Temperature_Sensor) | `correlate` |
| [`hbco:last_service`](#last_service) | atomic |  | `aggregate` |
| [`hbco:lift_status`](#lift_status) | atomic | [`brick:Availability_Status`](https://ontology.brickschema.org/1.4/#brick:Availability_Status), [`brick:Fault_Status`](https://ontology.brickschema.org/1.4/#brick:Fault_Status) | `threshold` |
| [`hbco:light_colour_temperature`](#light_colour_temperature) | atomic | [`brick:Lighting_Correlated_Color_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Lighting_Correlated_Color_Temperature_Sensor) | `aggregate` |
| [`hbco:lighting_comfort`](#lighting_comfort) | composite | [`brick:Illuminance_Sensor`](https://ontology.brickschema.org/1.4/#brick:Illuminance_Sensor), [`brick:Luminance_Sensor`](https://ontology.brickschema.org/1.4/#brick:Luminance_Sensor) | `range` |
| [`hbco:lighting_state`](#lighting_state) | atomic | [`ontosage:Lighting_Command`]({{ '/ontology/class/Lighting_Command/' | relative_url }}) | `aggregate` |
| [`hbco:meeting_room_condition`](#meeting_room_condition) | atomic | [`brick:CO2_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO2_Level_Sensor), [`brick:Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Temperature_Sensor) | `range` |
| [`hbco:motion_detected`](#motion_detected) | atomic | [`brick:Motion_Sensor`](https://ontology.brickschema.org/1.4/#brick:Motion_Sensor) | `threshold` |
| [`hbco:natural_light`](#natural_light) | atomic | [`brick:Illuminance_Sensor`](https://ontology.brickschema.org/1.4/#brick:Illuminance_Sensor) | `range` |
| [`hbco:nitrogen_dioxide`](#nitrogen_dioxide) | atomic | [`brick:NO2_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:NO2_Level_Sensor) | `threshold` |
| [`hbco:noisy`](#noisy) | atomic | [`ontosage:Sound_Level_Sensor`]({{ '/ontology/class/Sound_Level_Sensor/' | relative_url }}) | `threshold` |
| [`hbco:occupancy_status`](#occupancy_status) | atomic | [`brick:Occupancy_Status`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Status) | `aggregate` |
| [`hbco:occupancy_trend`](#occupancy_trend) | atomic | [`brick:Occupancy_Count_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Count_Sensor), [`brick:Occupancy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Sensor) | `trend` |
| [`hbco:outdoor_humidity`](#outdoor_humidity) | atomic | [`brick:Outside_Air_Humidity_Sensor`](https://ontology.brickschema.org/1.4/#brick:Outside_Air_Humidity_Sensor) | `aggregate` |
| [`hbco:outdoor_temperature`](#outdoor_temperature) | atomic | [`brick:Outside_Air_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Outside_Air_Temperature_Sensor) | `aggregate` |
| [`hbco:outdoor_wind`](#outdoor_wind) | atomic | [`brick:Wind_Speed_Sensor`](https://ontology.brickschema.org/1.4/#brick:Wind_Speed_Sensor) | `threshold` |
| [`hbco:overall_comfort`](#overall_comfort) | composite | [`brick:CO2_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO2_Level_Sensor), [`brick:Humidity_Sensor`](https://ontology.brickschema.org/1.4/#brick:Humidity_Sensor), [`brick:Illuminance_Sensor`](https://ontology.brickschema.org/1.4/#brick:Illuminance_Sensor), [`brick:Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Temperature_Sensor) | `range` |
| [`hbco:parking_availability`](#parking_availability) | atomic | [`brick:Occupancy_Count_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Count_Sensor), [`ontosage:Parking_Occupancy_Sensor`]({{ '/ontology/class/Parking_Occupancy_Sensor/' | relative_url }}) | `aggregate` |
| [`hbco:peak_demand`](#peak_demand) | atomic | [`brick:Electric_Power_Sensor`](https://ontology.brickschema.org/1.4/#brick:Electric_Power_Sensor), [`brick:Energy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Energy_Sensor) | `threshold` |
| [`hbco:pm10_level`](#pm10_level) | atomic | [`brick:PM10_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:PM10_Level_Sensor), [`brick:PM10_Sensor`](https://ontology.brickschema.org/1.4/#brick:PM10_Sensor) | `threshold` |
| [`hbco:pm1_level`](#pm1_level) | atomic | [`brick:PM1_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:PM1_Level_Sensor), [`brick:PM1_Sensor`](https://ontology.brickschema.org/1.4/#brick:PM1_Sensor) | `threshold` |
| [`hbco:pm25_level`](#pm25_level) | atomic | [`brick:PM2.5_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:PM2.5_Level_Sensor) | `threshold` |
| [`hbco:quiet_space`](#quiet_space) | atomic | [`ontosage:Sound_Level_Sensor`]({{ '/ontology/class/Sound_Level_Sensor/' | relative_url }}) | `threshold` |
| [`hbco:quiet_time`](#quiet_time) | atomic | [`brick:Motion_Sensor`](https://ontology.brickschema.org/1.4/#brick:Motion_Sensor), [`brick:Occupancy_Count_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Count_Sensor), [`brick:Occupancy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Sensor) | `trend` |
| [`hbco:quiet_zone`](#quiet_zone) | atomic | [`ontosage:Sound_Level_Sensor`]({{ '/ontology/class/Sound_Level_Sensor/' | relative_url }}) | `threshold` |
| [`hbco:rainfall`](#rainfall) | atomic | [`brick:Rain_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:Rain_Level_Sensor), [`ontosage:Rainfall_Sensor`]({{ '/ontology/class/Rainfall_Sensor/' | relative_url }}) | `aggregate` |
| [`hbco:return_air_temperature`](#return_air_temperature) | atomic | [`brick:Return_Air_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Return_Air_Temperature_Sensor) | `aggregate` |
| [`hbco:room_booking`](#room_booking) | atomic |  | `aggregate` |
| [`hbco:run_time`](#run_time) | atomic | [`brick:Duration_Sensor`](https://ontology.brickschema.org/1.4/#brick:Duration_Sensor), [`brick:On_Timer_Sensor`](https://ontology.brickschema.org/1.4/#brick:On_Timer_Sensor) | `aggregate` |
| [`hbco:sensor_anomaly`](#sensor_anomaly) | atomic | [`brick:CO2_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO2_Level_Sensor), [`brick:Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Temperature_Sensor) | `threshold` |
| [`hbco:setpoint_recommendation`](#setpoint_recommendation) | atomic | [`brick:Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Temperature_Sensor), [`brick:Temperature_Setpoint`](https://ontology.brickschema.org/1.4/#brick:Temperature_Setpoint) | `range` |
| [`hbco:smell_odour`](#smell_odour) | atomic | [`brick:CO2_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO2_Sensor), [`brick:TVOC_Sensor`](https://ontology.brickschema.org/1.4/#brick:TVOC_Sensor) | `threshold` |
| [`hbco:soil_moisture`](#soil_moisture) | atomic | [`ontosage:Soil_Moisture_Sensor`]({{ '/ontology/class/Soil_Moisture_Sensor/' | relative_url }}) | `threshold` |
| [`hbco:solar_irradiance`](#solar_irradiance) | atomic | [`brick:Solar_Irradiance_Sensor`](https://ontology.brickschema.org/1.4/#brick:Solar_Irradiance_Sensor) | `aggregate` |
| [`hbco:solar_output`](#solar_output) | atomic | [`ontosage:PV_Generation_Power_Sensor`]({{ '/ontology/class/PV_Generation_Power_Sensor/' | relative_url }}) | `aggregate` |
| [`hbco:space_availability`](#space_availability) | atomic | [`brick:Occupancy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Sensor), [`brick:Occupancy_Status`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Status) | `threshold` |
| [`hbco:stuffiness`](#stuffiness) | atomic | [`brick:CO2_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO2_Level_Sensor), [`brick:CO2_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO2_Sensor) | `threshold` |
| [`hbco:supply_air_temperature`](#supply_air_temperature) | atomic | [`brick:Supply_Air_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Supply_Air_Temperature_Sensor) | `aggregate` |
| [`hbco:system_capability`](#system_capability) | atomic |  | `aggregate` |
| [`hbco:temperature_reading`](#temperature_reading) | composite | [`brick:Outside_Air_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Outside_Air_Temperature_Sensor), [`brick:Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Temperature_Sensor), [`brick:Zone_Air_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Zone_Air_Temperature_Sensor) | `aggregate` |
| [`hbco:temperature_trend`](#temperature_trend) | atomic | [`brick:Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Temperature_Sensor) | `trend` |
| [`hbco:thermal_comfort`](#thermal_comfort) | composite | [`brick:Humidity_Sensor`](https://ontology.brickschema.org/1.4/#brick:Humidity_Sensor), [`brick:Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Temperature_Sensor) | `range` |
| [`hbco:too_bright`](#too_bright) | atomic | [`brick:Illuminance_Sensor`](https://ontology.brickschema.org/1.4/#brick:Illuminance_Sensor), [`brick:Luminance_Sensor`](https://ontology.brickschema.org/1.4/#brick:Luminance_Sensor) | `threshold` |
| [`hbco:too_cold`](#too_cold) | atomic | [`brick:Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Temperature_Sensor), [`brick:Zone_Air_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Zone_Air_Temperature_Sensor) | `threshold` |
| [`hbco:too_dark`](#too_dark) | atomic | [`brick:Illuminance_Sensor`](https://ontology.brickschema.org/1.4/#brick:Illuminance_Sensor), [`brick:Luminance_Sensor`](https://ontology.brickschema.org/1.4/#brick:Luminance_Sensor) | `threshold` |
| [`hbco:too_dry`](#too_dry) | atomic | [`brick:Humidity_Sensor`](https://ontology.brickschema.org/1.4/#brick:Humidity_Sensor), [`brick:Relative_Humidity_Sensor`](https://ontology.brickschema.org/1.4/#brick:Relative_Humidity_Sensor) | `threshold` |
| [`hbco:too_humid`](#too_humid) | atomic | [`brick:Humidity_Sensor`](https://ontology.brickschema.org/1.4/#brick:Humidity_Sensor), [`brick:Relative_Humidity_Sensor`](https://ontology.brickschema.org/1.4/#brick:Relative_Humidity_Sensor) | `threshold` |
| [`hbco:too_warm`](#too_warm) | atomic | [`brick:Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Temperature_Sensor), [`brick:Zone_Air_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Zone_Air_Temperature_Sensor) | `threshold` |
| [`hbco:tvoc_level`](#tvoc_level) | atomic | [`brick:TVOC_Sensor`](https://ontology.brickschema.org/1.4/#brick:TVOC_Sensor) | `threshold` |
| [`hbco:underutilized_space`](#underutilized_space) | atomic | [`brick:Occupancy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Sensor) | `threshold` |
| [`hbco:unexpected_open_window`](#unexpected_open_window) | atomic | [`brick:Contact_Sensor`](https://ontology.brickschema.org/1.4/#brick:Contact_Sensor), [`brick:Open_Close_Status`](https://ontology.brickschema.org/1.4/#brick:Open_Close_Status) | `threshold` |
| [`hbco:ventilation_quality`](#ventilation_quality) | atomic | [`brick:CO2_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO2_Level_Sensor), [`brick:Damper_Position_Sensor`](https://ontology.brickschema.org/1.4/#brick:Damper_Position_Sensor), [`brick:Supply_Air_Flow_Sensor`](https://ontology.brickschema.org/1.4/#brick:Supply_Air_Flow_Sensor) | `threshold` |
| [`hbco:waste_fill`](#waste_fill) | atomic | [`ontosage:Waste_Fill_Sensor`]({{ '/ontology/class/Waste_Fill_Sensor/' | relative_url }}) | `threshold` |
| [`hbco:waste_weight`](#waste_weight) | atomic | [`ontosage:Waste_Weight_Sensor`]({{ '/ontology/class/Waste_Weight_Sensor/' | relative_url }}) | `aggregate` |
| [`hbco:water_flow`](#water_flow) | atomic | [`brick:Water_Flow_Sensor`](https://ontology.brickschema.org/1.4/#brick:Water_Flow_Sensor) | `aggregate` |
| [`hbco:water_leak`](#water_leak) | atomic | [`brick:Leak_Alarm`](https://ontology.brickschema.org/1.4/#brick:Leak_Alarm), [`brick:Water_Flow_Sensor`](https://ontology.brickschema.org/1.4/#brick:Water_Flow_Sensor) | `threshold` |
| [`hbco:water_level`](#water_level) | atomic | [`brick:Water_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:Water_Level_Sensor) | `aggregate` |
| [`hbco:water_quality`](#water_quality) | atomic |  | `threshold` |
| [`hbco:water_temperature`](#water_temperature) | atomic | [`brick:Water_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Water_Temperature_Sensor) | `aggregate` |
| [`hbco:water_usage`](#water_usage) | composite | [`brick:Building_Water_Meter`](https://ontology.brickschema.org/1.4/#brick:Building_Water_Meter), [`brick:Water_Meter`](https://ontology.brickschema.org/1.4/#brick:Water_Meter) | `aggregate` |
| [`hbco:water_usage_rate`](#water_usage_rate) | atomic | [`brick:Water_Usage_Sensor`](https://ontology.brickschema.org/1.4/#brick:Water_Usage_Sensor) | `aggregate` |
| [`hbco:wayfinding`](#wayfinding) | atomic |  | `aggregate` |
| [`hbco:window_guidance`](#window_guidance) | atomic | [`brick:CO2_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO2_Level_Sensor), [`brick:Outside_Air_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Outside_Air_Temperature_Sensor) | `correlate` |

## Composite concepts

### acoustic comfort {#acoustic_comfort}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#acoustic_comfort` |
| Concept ID | `acoustic_comfort` |
| Maps to Brick class | [`ontosage:Sound_Level_Sensor`]({{ '/ontology/class/Sound_Level_Sensor/' | relative_url }}) |
| Recipe | `range` |
| Confidence | high |
| Components | [`hbco:noisy`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#noisy), [`hbco:quiet_space`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#quiet_space), [`hbco:quiet_zone`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#quiet_zone) |
| Lay terms (6) | `acoustic comfort`, `comfortable for focus`, `noise environment`, `noise level`, `noise levels`, `sound environment` |

### occupancy {#busyness}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#busyness` |
| Concept ID | `busyness` |
| Maps to Brick class | [`brick:Occupancy_Count_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Count_Sensor), [`brick:Occupancy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Sensor) |
| Recipe | `aggregate` |
| Confidence | high |
| Components | [`hbco:busy`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#busy), [`hbco:congestion_hotspot`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#congestion_hotspot), [`hbco:crowded`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#crowded), [`hbco:empty_space`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#empty_space), [`hbco:motion_detected`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#motion_detected), [`hbco:occupancy_status`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#occupancy_status), [`hbco:occupancy_trend`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#occupancy_trend), [`hbco:quiet_time`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#quiet_time), [`hbco:space_availability`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#space_availability), [`hbco:underutilized_space`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#underutilized_space) |
| Lay terms (22) | `busy periods`, `footfall`, `head count`, `how full is it`, `how occupied`, `occupancy`, `occupancy peaks`, `occupancy rate`, `peak periods`, `peak times`, `peaks and troughs`, `people count`, `people counter`, `people counting`, `quiet periods`, `room utilisation`, `room utilization`, `space utilisation`, `space utilization`, `usage peaks`, `utilisation rate`, `workplace occupancy` |

### CO2 {#co2_level}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#co2_level` |
| Concept ID | `co2_level` |
| Maps to Brick class | [`brick:CO2_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO2_Level_Sensor), [`brick:CO2_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO2_Sensor) |
| Recipe | `threshold` |
| Confidence | high |
| Components | [`hbco:co2_compliance`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#co2_compliance) |
| Lay terms (6) | `carbon dioxide`, `carbon dioxide level`, `CO2`, `co2 concentration`, `co2 level`, `co₂` |

### energy use {#energy_consumption}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#energy_consumption` |
| Concept ID | `energy_consumption` |
| Maps to Brick class | [`brick:Energy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Energy_Sensor) |
| Recipe | `aggregate` |
| Confidence | high |
| Components | [`hbco:carbon_footprint`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#carbon_footprint), [`hbco:electric_power`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#electric_power), [`hbco:energy_cost`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#energy_cost), [`hbco:energy_saving_tip`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#energy_saving_tip), [`hbco:energy_trend`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#energy_trend), [`hbco:energy_waste`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#energy_waste), [`hbco:future_energy`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#future_energy), [`hbco:peak_demand`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#peak_demand), [`hbco:solar_output`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#solar_output) |
| Lay terms (26) | `consumes energy`, `consuming energy`, `electrical usage`, `electricity consumption`, `electricity usage`, `electricity use`, `energy consumption`, `energy hungry`, `energy intensive`, `energy usage`, `energy use`, `energy used`, `energy-intensive`, `how much electricity`, `how much energy`, `how much power`, `kilowatt hours`, `kilowatt-hours`, `kWh`, `least energy`, `less energy`, `more energy`, `most energy`, `power consumption`, `power usage`, `power use` |

### equipment condition {#equipment_condition}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#equipment_condition` |
| Concept ID | `equipment_condition` |
| Maps to Brick class | [`brick:Fault_Status`](https://ontology.brickschema.org/1.4/#brick:Fault_Status) |
| Recipe | `threshold` |
| Confidence | medium |
| Component of | [`hbco:equipment_working`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#equipment_working) |
| Components | [`hbco:filter_pressure`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#filter_pressure) |
| Lay terms (4) | `equipment condition`, `equipment health`, `equipment status`, `needs repair` |

### working {#equipment_working}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#equipment_working` |
| Concept ID | `equipment_working` |
| Maps to Brick class | [`brick:Fault_Status`](https://ontology.brickschema.org/1.4/#brick:Fault_Status) |
| Recipe | `threshold` |
| Confidence | medium |
| Components | [`hbco:equipment_condition`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#equipment_condition), [`hbco:fan_status`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#fan_status), [`hbco:hvac_performance`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#hvac_performance), [`hbco:lift_status`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#lift_status) |
| Lay terms (6) | `equipment fault`, `functioning`, `is it broken`, `not working`, `operational`, `working` |

### fire {#fire_safety}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#fire_safety` |
| Concept ID | `fire_safety` |
| Maps to Brick class | [`brick:Fire_Alarm`](https://ontology.brickschema.org/1.4/#brick:Fire_Alarm), [`brick:Smoke_Detector`](https://ontology.brickschema.org/1.4/#brick:Smoke_Detector) |
| Recipe | `threshold` |
| Confidence | high |
| Components | [`hbco:emergency_exit`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#emergency_exit) |
| Lay terms (7) | `emergency`, `evacuation`, `fire`, `fire alarm`, `fire exit`, `fire hazard`, `smoke` |

### indoor air quality {#iaq_composite}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#iaq_composite` |
| Concept ID | `iaq_composite` |
| Maps to Brick class | [`brick:Air_Quality_Sensor`](https://ontology.brickschema.org/1.4/#brick:Air_Quality_Sensor), [`brick:CO2_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO2_Level_Sensor), [`brick:PM2.5_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:PM2.5_Level_Sensor), [`brick:TVOC_Sensor`](https://ontology.brickschema.org/1.4/#brick:TVOC_Sensor) |
| Recipe | `aggregate` |
| Confidence | high |
| Components | [`hbco:carbon_monoxide`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#carbon_monoxide), [`hbco:formaldehyde`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#formaldehyde), [`hbco:gas_level`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#gas_level), [`hbco:nitrogen_dioxide`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#nitrogen_dioxide), [`hbco:pm10_level`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#pm10_level), [`hbco:pm1_level`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#pm1_level), [`hbco:pm25_level`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#pm25_level), [`hbco:smell_odour`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#smell_odour), [`hbco:stuffiness`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#stuffiness), [`hbco:tvoc_level`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#tvoc_level), [`hbco:ventilation_quality`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#ventilation_quality) |
| Lay terms (11) | `air pollution`, `air quality`, `air quality index`, `AQI`, `how clean is the air`, `IAQ`, `indoor air quality`, `indoor pollution`, `pollutant`, `pollutant levels`, `pollution` |

### lighting {#lighting_comfort}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#lighting_comfort` |
| Concept ID | `lighting_comfort` |
| Maps to Brick class | [`brick:Illuminance_Sensor`](https://ontology.brickschema.org/1.4/#brick:Illuminance_Sensor), [`brick:Luminance_Sensor`](https://ontology.brickschema.org/1.4/#brick:Luminance_Sensor) |
| Recipe | `range` |
| Confidence | high |
| Components | [`hbco:light_colour_temperature`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#light_colour_temperature), [`hbco:natural_light`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#natural_light), [`hbco:too_bright`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#too_bright), [`hbco:too_dark`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#too_dark) |
| Lay terms (13) | `adequate lighting`, `ambient light`, `brightest`, `brightness`, `darkest`, `dimmest`, `illuminance`, `light intensity`, `light level`, `lighting`, `lighting conditions`, `lux`, `lux level` |

### comfortable {#overall_comfort}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#overall_comfort` |
| Concept ID | `overall_comfort` |
| Maps to Brick class | [`brick:CO2_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO2_Level_Sensor), [`brick:Humidity_Sensor`](https://ontology.brickschema.org/1.4/#brick:Humidity_Sensor), [`brick:Illuminance_Sensor`](https://ontology.brickschema.org/1.4/#brick:Illuminance_Sensor), [`brick:Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Temperature_Sensor) |
| Recipe | `range` |
| Confidence | high |
| Components | [`hbco:focus_environment`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#focus_environment), [`hbco:meeting_room_condition`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#meeting_room_condition) |
| Lay terms (4) | `comfort level`, `comfortable`, `pleasant environment`, `working conditions` |

### temperature {#temperature_reading}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#temperature_reading` |
| Concept ID | `temperature_reading` |
| Maps to Brick class | [`brick:Outside_Air_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Outside_Air_Temperature_Sensor), [`brick:Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Temperature_Sensor), [`brick:Zone_Air_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Zone_Air_Temperature_Sensor) |
| Recipe | `aggregate` |
| Confidence | high |
| Components | [`hbco:future_temperature`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#future_temperature), [`hbco:temperature_trend`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#temperature_trend) |
| Lay terms (7) | `current temperature`, `degrees`, `how cold`, `how hot`, `how warm`, `temp`, `temperature` |

### thermal comfort {#thermal_comfort}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#thermal_comfort` |
| Concept ID | `thermal_comfort` |
| Maps to Brick class | [`brick:Humidity_Sensor`](https://ontology.brickschema.org/1.4/#brick:Humidity_Sensor), [`brick:Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Temperature_Sensor) |
| Recipe | `range` |
| Confidence | high |
| Components | [`hbco:ashrae_compliance`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#ashrae_compliance), [`hbco:draft`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#draft), [`hbco:too_cold`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#too_cold), [`hbco:too_dry`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#too_dry), [`hbco:too_humid`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#too_humid), [`hbco:too_warm`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#too_warm) |
| Lay terms (5) | `comfortable temperature`, `is it comfortable`, `temperature comfort`, `temperature okay`, `thermal comfort` |

### water use {#water_usage}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#water_usage` |
| Concept ID | `water_usage` |
| Maps to Brick class | [`brick:Building_Water_Meter`](https://ontology.brickschema.org/1.4/#brick:Building_Water_Meter), [`brick:Water_Meter`](https://ontology.brickschema.org/1.4/#brick:Water_Meter) |
| Recipe | `aggregate` |
| Confidence | medium |
| Components | [`hbco:water_leak`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#water_leak) |
| Lay terms (12) | `how much water`, `litres of water`, `use of water`, `water bill`, `water consumed`, `water consumption`, `water cost`, `water efficiency`, `water usage`, `water use`, `water used`, `water waste` |

## Atomic concepts

### after hours {#after_hours}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#after_hours` |
| Concept ID | `after_hours` |
| Maps to Brick class | [`brick:Energy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Energy_Sensor), [`brick:Occupancy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Sensor) |
| Recipe | `aggregate` |
| Confidence | medium |
| Lay terms (5) | `after hours`, `outside business hours`, `outside working hours`, `overnight`, `weekend` |

### airflow {#air_flow_rate}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#air_flow_rate` |
| Concept ID | `air_flow_rate` |
| Maps to Brick class | [`brick:Air_Flow_Sensor`](https://ontology.brickschema.org/1.4/#brick:Air_Flow_Sensor) |
| Recipe | `aggregate` |
| Confidence | medium |
| Lay terms (6) | `air flow rate`, `air flow rates`, `air volume`, `airflow`, `airflow rate`, `supply airflow` |

### ASHRAE {#ashrae_compliance}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#ashrae_compliance` |
| Concept ID | `ashrae_compliance` |
| Maps to Brick class | [`brick:Humidity_Sensor`](https://ontology.brickschema.org/1.4/#brick:Humidity_Sensor), [`brick:Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Temperature_Sensor) |
| Recipe | `range` |
| Confidence | medium |
| Component of | [`hbco:thermal_comfort`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#thermal_comfort) |
| Lay terms (5) | `ASHRAE`, `ASHRAE 55`, `ASHRAE compliance`, `comfort standard`, `thermal standard` |

### busy {#busy}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#busy` |
| Concept ID | `busy` |
| Maps to Brick class | [`brick:Occupancy_Count_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Count_Sensor), [`brick:Occupancy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Sensor) |
| Recipe | `aggregate` |
| Confidence | high |
| Component of | [`hbco:busyness`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#busyness) |
| Lay terms (7) | `busier`, `busiest`, `busy`, `busyness`, `high occupancy`, `how busy`, `how many people` |

### carbon {#carbon_footprint}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#carbon_footprint` |
| Concept ID | `carbon_footprint` |
| Maps to Brick class | [`brick:Energy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Energy_Sensor) |
| Recipe | `aggregate` |
| Confidence | medium |
| Component of | [`hbco:energy_consumption`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#energy_consumption) |
| Lay terms (7) | `carbon`, `carbon footprint`, `CO2 emissions`, `eco-friendly`, `emissions`, `green`, `greenhouse gas` |

### carbon monoxide {#carbon_monoxide}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#carbon_monoxide` |
| Concept ID | `carbon_monoxide` |
| Maps to Brick class | [`brick:CO_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO_Level_Sensor), [`brick:CO_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO_Sensor) |
| Recipe | `threshold` |
| Confidence | high |
| Component of | [`hbco:iaq_composite`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#iaq_composite) |
| Lay terms (8) | `carbon monoxide`, `co alarm`, `co concentration`, `co detector`, `co level`, `co levels`, `co sensor`, `co sensors` |

### chilled water return temperature {#chilled_water_return}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#chilled_water_return` |
| Concept ID | `chilled_water_return` |
| Maps to Brick class | [`brick:Entering_Chilled_Water_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Entering_Chilled_Water_Temperature_Sensor) |
| Recipe | `aggregate` |
| Confidence | high |
| Lay terms (6) | `chilled water return`, `chilled water return temperature`, `chiller entering water temperature`, `chiller inlet temperature`, `chiller return temperature`, `chw return` |

### chilled water supply temperature {#chilled_water_supply}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#chilled_water_supply` |
| Concept ID | `chilled_water_supply` |
| Maps to Brick class | [`brick:Leaving_Chilled_Water_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Leaving_Chilled_Water_Temperature_Sensor) |
| Recipe | `aggregate` |
| Confidence | high |
| Lay terms (8) | `chilled water flow`, `chilled water flow temperature`, `chilled water supply`, `chilled water supply temperature`, `chiller leaving water temperature`, `chiller outlet temperature`, `chiller supply temperature`, `chw supply` |

### WHO limit {#co2_compliance}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#co2_compliance` |
| Concept ID | `co2_compliance` |
| Maps to Brick class | [`brick:CO2_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO2_Level_Sensor) |
| Recipe | `threshold` |
| Confidence | medium |
| Component of | [`hbco:co2_level`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#co2_level) |
| Lay terms (5) | `air quality standard`, `CO2 regulation`, `CO2 standard`, `ventilation standard`, `WHO limit` |

### congestion {#congestion_hotspot}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#congestion_hotspot` |
| Concept ID | `congestion_hotspot` |
| Maps to Brick class | [`brick:Motion_Sensor`](https://ontology.brickschema.org/1.4/#brick:Motion_Sensor), [`brick:Occupancy_Count_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Count_Sensor), [`brick:Occupancy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Sensor) |
| Recipe | `aggregate` |
| Confidence | medium |
| Component of | [`hbco:busyness`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#busyness) |
| Lay terms (5) | `bottleneck`, `busy area`, `congestion`, `crowded corridor`, `flow problem` |

### crowded {#crowded}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#crowded` |
| Concept ID | `crowded` |
| Maps to Brick class | [`brick:Motion_Sensor`](https://ontology.brickschema.org/1.4/#brick:Motion_Sensor), [`brick:Occupancy_Count_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Count_Sensor), [`brick:Occupancy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Sensor) |
| Recipe | `threshold` |
| Confidence | high |
| Component of | [`hbco:busyness`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#busyness) |
| Lay terms (9) | `congested`, `crowd`, `crowded`, `crowding`, `crowds`, `no space`, `over capacity`, `packed`, `too many people` |

### damper {#damper_position}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#damper_position` |
| Concept ID | `damper_position` |
| Maps to Brick class | [`brick:Damper_Position_Command`](https://ontology.brickschema.org/1.4/#brick:Damper_Position_Command), [`brick:Damper_Position_Sensor`](https://ontology.brickschema.org/1.4/#brick:Damper_Position_Sensor) |
| Recipe | `aggregate` |
| Confidence | high |
| Lay terms (10) | `air damper`, `damper`, `damper position`, `dampers`, `economiser`, `economizer`, `fresh air damper`, `louver`, `louvre`, `outside air damper` |

### what do you monitor {#data_privacy}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#data_privacy` |
| Concept ID | `data_privacy` |
| Maps to Brick class | none |
| Recipe | `aggregate` |
| Confidence | medium |
| Lay terms (5) | `data about me`, `data collected`, `privacy`, `what do you monitor`, `who sees my data` |

### drafty {#draft}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#draft` |
| Concept ID | `draft` |
| Maps to Brick class | [`brick:Supply_Air_Flow_Sensor`](https://ontology.brickschema.org/1.4/#brick:Supply_Air_Flow_Sensor), [`brick:Supply_Air_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Supply_Air_Temperature_Sensor), [`brick:Zone_Air_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Zone_Air_Temperature_Sensor) |
| Recipe | `correlate` |
| Confidence | medium |
| Component of | [`hbco:thermal_comfort`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#thermal_comfort) |
| Lay terms (6) | `cold air blowing`, `cold draft`, `drafty`, `draught`, `draughty`, `windy inside` |

### power draw {#electric_power}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#electric_power` |
| Concept ID | `electric_power` |
| Maps to Brick class | [`brick:Electric_Power_Sensor`](https://ontology.brickschema.org/1.4/#brick:Electric_Power_Sensor) |
| Recipe | `aggregate` |
| Confidence | high |
| Component of | [`hbco:energy_consumption`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#energy_consumption) |
| Lay terms (8) | `electric load`, `electric power`, `electrical load`, `electrical power`, `kilowatts`, `kw`, `power demand`, `power draw` |

### emergency exit {#emergency_exit}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#emergency_exit` |
| Concept ID | `emergency_exit` |
| Maps to Brick class | [`brick:Smoke_Detector`](https://ontology.brickschema.org/1.4/#brick:Smoke_Detector) |
| Recipe | `threshold` |
| Confidence | medium |
| Component of | [`hbco:fire_safety`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#fire_safety) |
| Lay terms (4) | `emergency exit`, `evacuation route`, `exit`, `safe exit` |

### empty {#empty_space}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#empty_space` |
| Concept ID | `empty_space` |
| Maps to Brick class | [`brick:Motion_Sensor`](https://ontology.brickschema.org/1.4/#brick:Motion_Sensor), [`brick:Occupancy_Count_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Count_Sensor), [`brick:Occupancy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Sensor), [`brick:Occupancy_Status`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Status) |
| Recipe | `threshold` |
| Confidence | high |
| Component of | [`hbco:busyness`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#busyness) |
| Lay terms (8) | `available`, `available desk`, `emptiest`, `empty`, `free space`, `nobody there`, `unoccupied`, `vacant` |

### energy cost {#energy_cost}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#energy_cost` |
| Concept ID | `energy_cost` |
| Maps to Brick class | [`brick:Energy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Energy_Sensor) |
| Recipe | `aggregate` |
| Confidence | high |
| Component of | [`hbco:energy_consumption`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#energy_consumption) |
| Lay terms (6) | `cost of electricity`, `electricity bill`, `electricity cost`, `energy cost`, `energy spend`, `tariff` |

### save energy {#energy_saving_tip}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#energy_saving_tip` |
| Concept ID | `energy_saving_tip` |
| Maps to Brick class | [`brick:Energy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Energy_Sensor) |
| Recipe | `aggregate` |
| Confidence | medium |
| Component of | [`hbco:energy_consumption`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#energy_consumption) |
| Lay terms (8) | `efficiency improvement`, `energy efficiency`, `energy efficient`, `energy saving`, `energy-efficient`, `lower energy use`, `reduce energy`, `save energy` |

### energy trend {#energy_trend}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#energy_trend` |
| Concept ID | `energy_trend` |
| Maps to Brick class | [`brick:Energy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Energy_Sensor) |
| Recipe | `trend` |
| Confidence | high |
| Component of | [`hbco:energy_consumption`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#energy_consumption) |
| Lay terms (5) | `energy history`, `energy increasing`, `energy over time`, `energy pattern`, `energy trend` |

### wasting energy {#energy_waste}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#energy_waste` |
| Concept ID | `energy_waste` |
| Maps to Brick class | [`brick:Energy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Energy_Sensor) |
| Recipe | `threshold` |
| Confidence | high |
| Component of | [`hbco:energy_consumption`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#energy_consumption) |
| Lay terms (5) | `energy inefficiency`, `energy waste`, `high energy use`, `inefficient energy`, `wasting energy` |

### fan status {#fan_status}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#fan_status` |
| Concept ID | `fan_status` |
| Maps to Brick class | [`brick:Fan_Status`](https://ontology.brickschema.org/1.4/#brick:Fan_Status) |
| Recipe | `aggregate` |
| Confidence | high |
| Component of | [`hbco:equipment_working`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#equipment_working) |
| Lay terms (8) | `exhaust fan`, `extract fan`, `fan running`, `fan state`, `fan status`, `fans running`, `is the fan on`, `supply fan` |

### filter differential pressure {#filter_pressure}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#filter_pressure` |
| Concept ID | `filter_pressure` |
| Maps to Brick class | [`brick:Filter_Differential_Pressure_Sensor`](https://ontology.brickschema.org/1.4/#brick:Filter_Differential_Pressure_Sensor) |
| Recipe | `threshold` |
| Confidence | high |
| Component of | [`hbco:equipment_condition`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#equipment_condition) |
| Lay terms (9) | `blocked filter`, `clogged filter`, `dirty filter`, `dirty filters`, `filter condition`, `filter differential pressure`, `filter dp`, `filter pressure`, `filter pressure drop` |

### suitable for study {#focus_environment}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#focus_environment` |
| Concept ID | `focus_environment` |
| Maps to Brick class | [`brick:CO2_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO2_Level_Sensor), [`brick:Illuminance_Sensor`](https://ontology.brickschema.org/1.4/#brick:Illuminance_Sensor), [`ontosage:Sound_Level_Sensor`]({{ '/ontology/class/Sound_Level_Sensor/' | relative_url }}) |
| Recipe | `range` |
| Confidence | medium |
| Component of | [`hbco:overall_comfort`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#overall_comfort) |
| Lay terms (5) | `good for focus`, `productive space`, `study environment`, `suitable for study`, `work environment` |

### formaldehyde {#formaldehyde}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#formaldehyde` |
| Concept ID | `formaldehyde` |
| Maps to Brick class | [`brick:Formaldehyde_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:Formaldehyde_Level_Sensor) |
| Recipe | `threshold` |
| Confidence | high |
| Component of | [`hbco:iaq_composite`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#iaq_composite) |
| Lay terms (4) | `formaldehyde`, `formaldehyde level`, `formaldehyde levels`, `hcho` |

### energy forecast {#future_energy}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#future_energy` |
| Concept ID | `future_energy` |
| Maps to Brick class | [`brick:Energy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Energy_Sensor) |
| Recipe | `trend` |
| Confidence | medium |
| Component of | [`hbco:energy_consumption`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#energy_consumption) |
| Lay terms (4) | `energy forecast`, `expected energy use`, `future energy demand`, `predict energy` |

### will it warm up {#future_temperature}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#future_temperature` |
| Concept ID | `future_temperature` |
| Maps to Brick class | [`brick:Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Temperature_Sensor) |
| Recipe | `trend` |
| Confidence | high |
| Component of | [`hbco:temperature_reading`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#temperature_reading) |
| Lay terms (5) | `expected temperature`, `forecast temperature`, `predict temperature`, `temperature forecast`, `will it warm up` |

### gas level {#gas_level}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#gas_level` |
| Concept ID | `gas_level` |
| Maps to Brick class | [`brick:Gas_Sensor`](https://ontology.brickschema.org/1.4/#brick:Gas_Sensor) |
| Recipe | `threshold` |
| Confidence | medium |
| Component of | [`hbco:iaq_composite`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#iaq_composite) |
| Lay terms (10) | `gas concentration`, `gas concentrations`, `gas detection`, `gas detector`, `gas level`, `gas levels`, `gas reading`, `gas readings`, `gas sensor`, `gas sensors` |

### BREEAM {#green_certification}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#green_certification` |
| Concept ID | `green_certification` |
| Maps to Brick class | none |
| Recipe | `aggregate` |
| Confidence | low |
| Lay terms (5) | `BREEAM`, `energy certificate`, `green building`, `LEED`, `sustainability rating` |

### humidity {#humidity_reading}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#humidity_reading` |
| Concept ID | `humidity_reading` |
| Maps to Brick class | [`brick:Humidity_Sensor`](https://ontology.brickschema.org/1.4/#brick:Humidity_Sensor), [`brick:Relative_Humidity_Sensor`](https://ontology.brickschema.org/1.4/#brick:Relative_Humidity_Sensor) |
| Recipe | `aggregate` |
| Confidence | high |
| Lay terms (5) | `how humid`, `humidity`, `moisture`, `moisture level`, `relative humidity` |

### humidity setpoint {#humidity_setpoint}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#humidity_setpoint` |
| Concept ID | `humidity_setpoint` |
| Maps to Brick class | [`brick:Humidity_Setpoint`](https://ontology.brickschema.org/1.4/#brick:Humidity_Setpoint) |
| Recipe | `range` |
| Confidence | medium |
| Lay terms (5) | `humidity set point`, `humidity setpoint`, `humidity threshold`, `mold risk threshold`, `mould risk threshold` |

### HVAC {#hvac_performance}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#hvac_performance` |
| Concept ID | `hvac_performance` |
| Maps to Brick class | [`brick:Air_Handling_Unit`](https://ontology.brickschema.org/1.4/#brick:Air_Handling_Unit), [`brick:Zone_Air_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Zone_Air_Temperature_Sensor) |
| Recipe | `threshold` |
| Confidence | high |
| Component of | [`hbco:equipment_working`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#equipment_working) |
| Lay terms (10) | `AC working`, `air conditioning`, `cooling status`, `cooling system`, `heating and cooling`, `heating or cooling`, `heating status`, `heating system`, `heating working`, `HVAC` |

### warmer inside {#inside_vs_outside}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#inside_vs_outside` |
| Concept ID | `inside_vs_outside` |
| Maps to Brick class | [`brick:Outside_Air_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Outside_Air_Temperature_Sensor), [`brick:Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Temperature_Sensor) |
| Recipe | `correlate` |
| Confidence | medium |
| Lay terms (4) | `compare inside outside`, `inside vs outside`, `temperature difference`, `warmer inside` |

### last serviced {#last_service}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#last_service` |
| Concept ID | `last_service` |
| Maps to Brick class | none |
| Recipe | `aggregate` |
| Confidence | medium |
| Lay terms (5) | `last maintenance`, `last serviced`, `maintenance history`, `service record`, `when was it serviced` |

### lift {#lift_status}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#lift_status` |
| Concept ID | `lift_status` |
| Maps to Brick class | [`brick:Availability_Status`](https://ontology.brickschema.org/1.4/#brick:Availability_Status), [`brick:Fault_Status`](https://ontology.brickschema.org/1.4/#brick:Fault_Status) |
| Recipe | `threshold` |
| Confidence | high |
| Component of | [`hbco:equipment_working`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#equipment_working) |
| Lay terms (5) | `elevator`, `elevator out of service`, `is the lift working`, `lift`, `lift broken` |

### colour temperature {#light_colour_temperature}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#light_colour_temperature` |
| Concept ID | `light_colour_temperature` |
| Maps to Brick class | [`brick:Lighting_Correlated_Color_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Lighting_Correlated_Color_Temperature_Sensor) |
| Recipe | `aggregate` |
| Confidence | medium |
| Component of | [`hbco:lighting_comfort`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#lighting_comfort) |
| Lay terms (10) | `cct`, `color temperature`, `colour temperature`, `cool white`, `correlated color temperature`, `correlated colour temperature`, `kelvin`, `light color`, `light colour`, `warm white` |

### lights left on {#lighting_state}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#lighting_state` |
| Concept ID | `lighting_state` |
| Maps to Brick class | [`ontosage:Lighting_Command`]({{ '/ontology/class/Lighting_Command/' | relative_url }}) |
| Recipe | `aggregate` |
| Confidence | medium |
| Lay terms (7) | `are the lights on`, `is the light on`, `lighting state`, `lighting status`, `lights left on`, `lights still on`, `lights switched on` |

### meeting room ready {#meeting_room_condition}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#meeting_room_condition` |
| Concept ID | `meeting_room_condition` |
| Maps to Brick class | [`brick:CO2_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO2_Level_Sensor), [`brick:Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Temperature_Sensor) |
| Recipe | `range` |
| Confidence | medium |
| Component of | [`hbco:overall_comfort`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#overall_comfort) |
| Lay terms (4) | `AV working`, `conference room condition`, `meeting room comfortable`, `meeting room ready` |

### motion detected {#motion_detected}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#motion_detected` |
| Concept ID | `motion_detected` |
| Maps to Brick class | [`brick:Motion_Sensor`](https://ontology.brickschema.org/1.4/#brick:Motion_Sensor) |
| Recipe | `threshold` |
| Confidence | medium |
| Component of | [`hbco:busyness`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#busyness) |
| Lay terms (7) | `motion detected`, `motion detection`, `motion sensor`, `movement detected`, `movement sensor`, `pir motion`, `pir sensor` |

### natural light {#natural_light}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#natural_light` |
| Concept ID | `natural_light` |
| Maps to Brick class | [`brick:Illuminance_Sensor`](https://ontology.brickschema.org/1.4/#brick:Illuminance_Sensor) |
| Recipe | `range` |
| Confidence | medium |
| Component of | [`hbco:lighting_comfort`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#lighting_comfort) |
| Lay terms (7) | `daylight`, `daylighting`, `daylit`, `natural light`, `sunlight`, `sunlit`, `sunniest` |

### nitrogen dioxide {#nitrogen_dioxide}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#nitrogen_dioxide` |
| Concept ID | `nitrogen_dioxide` |
| Maps to Brick class | [`brick:NO2_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:NO2_Level_Sensor) |
| Recipe | `threshold` |
| Confidence | high |
| Component of | [`hbco:iaq_composite`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#iaq_composite) |
| Lay terms (5) | `nitrogen dioxide`, `no2`, `no2 level`, `no2 levels`, `no₂` |

### noisy {#noisy}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#noisy` |
| Concept ID | `noisy` |
| Maps to Brick class | [`ontosage:Sound_Level_Sensor`]({{ '/ontology/class/Sound_Level_Sensor/' | relative_url }}) |
| Recipe | `threshold` |
| Confidence | high |
| Component of | [`hbco:acoustic_comfort`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#acoustic_comfort) |
| Lay terms (18) | `db(a)`, `decibel`, `decibels`, `disruptive noise`, `disturbing sounds`, `high noise level`, `how loud`, `loud`, `louder`, `loudest`, `noise`, `noise pollution`, `noisier`, `noisiest`, `noisy`, `sound level`, `sound levels`, `too loud` |

### anyone in there {#occupancy_status}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#occupancy_status` |
| Concept ID | `occupancy_status` |
| Maps to Brick class | [`brick:Occupancy_Status`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Status) |
| Recipe | `aggregate` |
| Confidence | medium |
| Component of | [`hbco:busyness`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#busyness) |
| Lay terms (10) | `anybody in there`, `anyone in there`, `currently occupied`, `in use right now`, `is the room occupied`, `occupancy status`, `occupied or free`, `occupied or vacant`, `occupied right now`, `room in use` |

### occupancy trend {#occupancy_trend}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#occupancy_trend` |
| Concept ID | `occupancy_trend` |
| Maps to Brick class | [`brick:Occupancy_Count_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Count_Sensor), [`brick:Occupancy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Sensor) |
| Recipe | `trend` |
| Confidence | high |
| Component of | [`hbco:busyness`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#busyness) |
| Lay terms (5) | `busier over time`, `occupancy history`, `occupancy pattern`, `occupancy trend`, `when peak occupancy` |

### outside humidity {#outdoor_humidity}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#outdoor_humidity` |
| Concept ID | `outdoor_humidity` |
| Maps to Brick class | [`brick:Outside_Air_Humidity_Sensor`](https://ontology.brickschema.org/1.4/#brick:Outside_Air_Humidity_Sensor) |
| Recipe | `aggregate` |
| Confidence | high |
| Lay terms (4) | `external humidity`, `humidity outside`, `outdoor humidity`, `outside humidity` |

### outside temperature {#outdoor_temperature}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#outdoor_temperature` |
| Concept ID | `outdoor_temperature` |
| Maps to Brick class | [`brick:Outside_Air_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Outside_Air_Temperature_Sensor) |
| Recipe | `aggregate` |
| Confidence | high |
| Lay terms (4) | `external temperature`, `outdoor temperature`, `outside temperature`, `outside weather` |

### wind {#outdoor_wind}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#outdoor_wind` |
| Concept ID | `outdoor_wind` |
| Maps to Brick class | [`brick:Wind_Speed_Sensor`](https://ontology.brickschema.org/1.4/#brick:Wind_Speed_Sensor) |
| Recipe | `threshold` |
| Confidence | high |
| Lay terms (11) | `gusty`, `how strong is the wind`, `how windy`, `is it windy`, `strong wind`, `wind`, `wind speed`, `wind strong`, `windiest`, `windy`, `windy outside` |

### parking bays {#parking_availability}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#parking_availability` |
| Concept ID | `parking_availability` |
| Maps to Brick class | [`brick:Occupancy_Count_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Count_Sensor), [`ontosage:Parking_Occupancy_Sensor`]({{ '/ontology/class/Parking_Occupancy_Sensor/' | relative_url }}) |
| Recipe | `aggregate` |
| Confidence | high |
| Lay terms (13) | `bays free`, `car park full`, `car park occupancy`, `car park spaces`, `free parking`, `parking area full`, `parking availability`, `parking bays`, `parking full`, `parking occupancy`, `parking spaces`, `parking spots`, `spaces in the car park` |

### peak demand {#peak_demand}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#peak_demand` |
| Concept ID | `peak_demand` |
| Maps to Brick class | [`brick:Electric_Power_Sensor`](https://ontology.brickschema.org/1.4/#brick:Electric_Power_Sensor), [`brick:Energy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Energy_Sensor) |
| Recipe | `threshold` |
| Confidence | high |
| Component of | [`hbco:energy_consumption`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#energy_consumption) |
| Lay terms (5) | `demand charges`, `peak demand`, `peak energy`, `peak hours`, `peak load` |

### pm10 {#pm10_level}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#pm10_level` |
| Concept ID | `pm10_level` |
| Maps to Brick class | [`brick:PM10_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:PM10_Level_Sensor), [`brick:PM10_Sensor`](https://ontology.brickschema.org/1.4/#brick:PM10_Sensor) |
| Recipe | `threshold` |
| Confidence | high |
| Component of | [`hbco:iaq_composite`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#iaq_composite) |
| Lay terms (4) | `coarse particles`, `coarse particulate`, `pm10`, `pm₁₀` |

### pm1 {#pm1_level}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#pm1_level` |
| Concept ID | `pm1_level` |
| Maps to Brick class | [`brick:PM1_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:PM1_Level_Sensor), [`brick:PM1_Sensor`](https://ontology.brickschema.org/1.4/#brick:PM1_Sensor) |
| Recipe | `threshold` |
| Confidence | high |
| Component of | [`hbco:iaq_composite`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#iaq_composite) |
| Lay terms (4) | `pm1`, `pm1.0`, `ultrafine particles`, `ultrafine particulate` |

### particulate matter {#pm25_level}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#pm25_level` |
| Concept ID | `pm25_level` |
| Maps to Brick class | [`brick:PM2.5_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:PM2.5_Level_Sensor) |
| Recipe | `threshold` |
| Confidence | medium |
| Component of | [`hbco:iaq_composite`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#iaq_composite) |
| Lay terms (7) | `aerosols`, `dust`, `fine particles`, `particle`, `particulate`, `particulate matter`, `PM2.5` |

### quiet spot {#quiet_space}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#quiet_space` |
| Concept ID | `quiet_space` |
| Maps to Brick class | [`ontosage:Sound_Level_Sensor`]({{ '/ontology/class/Sound_Level_Sensor/' | relative_url }}) |
| Recipe | `threshold` |
| Confidence | high |
| Component of | [`hbco:acoustic_comfort`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#acoustic_comfort) |
| Lay terms (10) | `how quiet`, `quiet place`, `quiet place to work`, `quiet room`, `quiet spot`, `quiet spot to work`, `quiet zone`, `quieter`, `quietest`, `somewhere quiet` |

### when is it quiet {#quiet_time}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#quiet_time` |
| Concept ID | `quiet_time` |
| Maps to Brick class | [`brick:Motion_Sensor`](https://ontology.brickschema.org/1.4/#brick:Motion_Sensor), [`brick:Occupancy_Count_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Count_Sensor), [`brick:Occupancy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Sensor) |
| Recipe | `trend` |
| Confidence | high |
| Component of | [`hbco:busyness`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#busyness) |
| Lay terms (5) | `best time to visit`, `least busy time`, `off-peak`, `quietest time`, `when is it quiet` |

### quiet {#quiet_zone}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#quiet_zone` |
| Concept ID | `quiet_zone` |
| Maps to Brick class | [`ontosage:Sound_Level_Sensor`]({{ '/ontology/class/Sound_Level_Sensor/' | relative_url }}) |
| Recipe | `threshold` |
| Confidence | high |
| Component of | [`hbco:acoustic_comfort`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#acoustic_comfort) |
| Lay terms (7) | `low noise`, `peaceful`, `quiet`, `quiet area`, `quiet floor`, `quiet for study`, `silent` |

### rain {#rainfall}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#rainfall` |
| Concept ID | `rainfall` |
| Maps to Brick class | [`brick:Rain_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:Rain_Level_Sensor), [`ontosage:Rainfall_Sensor`]({{ '/ontology/class/Rainfall_Sensor/' | relative_url }}) |
| Recipe | `aggregate` |
| Confidence | high |
| Lay terms (7) | `how much rain`, `precipitation`, `rain`, `rain gauge`, `rainfall`, `raining`, `rainy` |

### return air temperature {#return_air_temperature}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#return_air_temperature` |
| Concept ID | `return_air_temperature` |
| Maps to Brick class | [`brick:Return_Air_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Return_Air_Temperature_Sensor) |
| Recipe | `aggregate` |
| Confidence | high |
| Lay terms (3) | `extract air temperature`, `return air temp`, `return air temperature` |

### booked {#room_booking}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#room_booking` |
| Concept ID | `room_booking` |
| Maps to Brick class | none |
| Recipe | `aggregate` |
| Confidence | high |
| Lay terms (6) | `booked`, `booking`, `is room booked`, `reserved`, `room calendar`, `room schedule` |

### run time {#run_time}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#run_time` |
| Concept ID | `run_time` |
| Maps to Brick class | [`brick:Duration_Sensor`](https://ontology.brickschema.org/1.4/#brick:Duration_Sensor), [`brick:On_Timer_Sensor`](https://ontology.brickschema.org/1.4/#brick:On_Timer_Sensor) |
| Recipe | `aggregate` |
| Confidence | medium |
| Lay terms (5) | `hours run`, `run hours`, `run time`, `running hours`, `runtime` |

### unusual reading {#sensor_anomaly}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#sensor_anomaly` |
| Concept ID | `sensor_anomaly` |
| Maps to Brick class | [`brick:CO2_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO2_Level_Sensor), [`brick:Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Temperature_Sensor) |
| Recipe | `threshold` |
| Confidence | medium |
| Lay terms (5) | `abnormal value`, `outlier`, `sensor fault`, `unexpected spike`, `unusual reading` |

### setpoint {#setpoint_recommendation}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#setpoint_recommendation` |
| Concept ID | `setpoint_recommendation` |
| Maps to Brick class | [`brick:Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Temperature_Sensor), [`brick:Temperature_Setpoint`](https://ontology.brickschema.org/1.4/#brick:Temperature_Setpoint) |
| Recipe | `range` |
| Confidence | medium |
| Lay terms (4) | `adjust temperature`, `recommended temperature`, `setpoint`, `target temperature` |

### smell {#smell_odour}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#smell_odour` |
| Concept ID | `smell_odour` |
| Maps to Brick class | [`brick:CO2_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO2_Sensor), [`brick:TVOC_Sensor`](https://ontology.brickschema.org/1.4/#brick:TVOC_Sensor) |
| Recipe | `threshold` |
| Confidence | medium |
| Component of | [`hbco:iaq_composite`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#iaq_composite) |
| Lay terms (8) | `bad smell`, `chemical odour`, `foul smell`, `musty`, `odor`, `odour`, `smell`, `stinks` |

### soil moisture {#soil_moisture}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#soil_moisture` |
| Concept ID | `soil_moisture` |
| Maps to Brick class | [`ontosage:Soil_Moisture_Sensor`]({{ '/ontology/class/Soil_Moisture_Sensor/' | relative_url }}) |
| Recipe | `threshold` |
| Confidence | high |
| Lay terms (7) | `how dry is the soil`, `is the soil dry`, `need watering`, `needs watering`, `soil dryness`, `soil moisture`, `substrate moisture` |

### solar irradiance {#solar_irradiance}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#solar_irradiance` |
| Concept ID | `solar_irradiance` |
| Maps to Brick class | [`brick:Solar_Irradiance_Sensor`](https://ontology.brickschema.org/1.4/#brick:Solar_Irradiance_Sensor) |
| Recipe | `aggregate` |
| Confidence | high |
| Lay terms (6) | `how sunny`, `irradiance`, `solar irradiance`, `solar radiation`, `sun intensity`, `sunlight intensity` |

### solar {#solar_output}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#solar_output` |
| Concept ID | `solar_output` |
| Maps to Brick class | [`ontosage:PV_Generation_Power_Sensor`]({{ '/ontology/class/PV_Generation_Power_Sensor/' | relative_url }}) |
| Recipe | `aggregate` |
| Confidence | medium |
| Component of | [`hbco:energy_consumption`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#energy_consumption) |
| Lay terms (6) | `photovoltaic`, `PV output`, `renewable energy`, `solar`, `solar energy`, `solar panels` |

### available room {#space_availability}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#space_availability` |
| Concept ID | `space_availability` |
| Maps to Brick class | [`brick:Occupancy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Sensor), [`brick:Occupancy_Status`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Status) |
| Recipe | `threshold` |
| Confidence | high |
| Component of | [`hbco:busyness`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#busyness) |
| Lay terms (6) | `available room`, `available space`, `desk available`, `find a desk`, `free room`, `room available` |

### stuffy {#stuffiness}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#stuffiness` |
| Concept ID | `stuffiness` |
| Maps to Brick class | [`brick:CO2_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO2_Level_Sensor), [`brick:CO2_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO2_Sensor) |
| Recipe | `threshold` |
| Confidence | high |
| Component of | [`hbco:iaq_composite`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#iaq_composite) |
| Lay terms (9) | `airless`, `close air`, `needs fresh air`, `poor ventilation`, `stale air`, `stifling`, `stuffier`, `stuffiest`, `stuffy` |

### supply air temperature {#supply_air_temperature}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#supply_air_temperature` |
| Concept ID | `supply_air_temperature` |
| Maps to Brick class | [`brick:Supply_Air_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Supply_Air_Temperature_Sensor) |
| Recipe | `aggregate` |
| Confidence | high |
| Lay terms (5) | `discharge air temperature`, `off coil temperature`, `off-coil temperature`, `supply air temp`, `supply air temperature` |

### can you {#system_capability}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#system_capability` |
| Concept ID | `system_capability` |
| Maps to Brick class | none |
| Recipe | `aggregate` |
| Confidence | high |
| Lay terms (5) | `are you able to`, `can you`, `system capability`, `what can you do`, `what do you measure` |

### temperature trend {#temperature_trend}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#temperature_trend` |
| Concept ID | `temperature_trend` |
| Maps to Brick class | [`brick:Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Temperature_Sensor) |
| Recipe | `trend` |
| Confidence | high |
| Component of | [`hbco:temperature_reading`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#temperature_reading) |
| Lay terms (5) | `cooling down`, `getting warmer`, `temperature history`, `temperature trend`, `warming up` |

### too bright {#too_bright}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#too_bright` |
| Concept ID | `too_bright` |
| Maps to Brick class | [`brick:Illuminance_Sensor`](https://ontology.brickschema.org/1.4/#brick:Illuminance_Sensor), [`brick:Luminance_Sensor`](https://ontology.brickschema.org/1.4/#brick:Luminance_Sensor) |
| Recipe | `threshold` |
| Confidence | high |
| Component of | [`hbco:lighting_comfort`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#lighting_comfort) |
| Lay terms (6) | `blinding`, `glare`, `harsh light`, `overly lit`, `too bright`, `too much light` |

### too cold {#too_cold}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#too_cold` |
| Concept ID | `too_cold` |
| Maps to Brick class | [`brick:Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Temperature_Sensor), [`brick:Zone_Air_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Zone_Air_Temperature_Sensor) |
| Recipe | `threshold` |
| Confidence | high |
| Component of | [`hbco:thermal_comfort`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#thermal_comfort) |
| Lay terms (8) | `chilly`, `cold in here`, `coldest`, `feels cold`, `freezing`, `too cold`, `too cool`, `uncomfortably cold` |

### too dark {#too_dark}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#too_dark` |
| Concept ID | `too_dark` |
| Maps to Brick class | [`brick:Illuminance_Sensor`](https://ontology.brickschema.org/1.4/#brick:Illuminance_Sensor), [`brick:Luminance_Sensor`](https://ontology.brickschema.org/1.4/#brick:Luminance_Sensor) |
| Recipe | `threshold` |
| Confidence | high |
| Component of | [`hbco:lighting_comfort`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#lighting_comfort) |
| Lay terms (6) | `dark`, `dim`, `low light`, `not enough light`, `poor lighting`, `too dark` |

### dry air {#too_dry}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#too_dry` |
| Concept ID | `too_dry` |
| Maps to Brick class | [`brick:Humidity_Sensor`](https://ontology.brickschema.org/1.4/#brick:Humidity_Sensor), [`brick:Relative_Humidity_Sensor`](https://ontology.brickschema.org/1.4/#brick:Relative_Humidity_Sensor) |
| Recipe | `threshold` |
| Confidence | high |
| Component of | [`hbco:thermal_comfort`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#thermal_comfort) |
| Lay terms (5) | `driest`, `dry`, `dry air`, `dryness`, `low humidity` |

### too humid {#too_humid}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#too_humid` |
| Concept ID | `too_humid` |
| Maps to Brick class | [`brick:Humidity_Sensor`](https://ontology.brickschema.org/1.4/#brick:Humidity_Sensor), [`brick:Relative_Humidity_Sensor`](https://ontology.brickschema.org/1.4/#brick:Relative_Humidity_Sensor) |
| Recipe | `threshold` |
| Confidence | high |
| Component of | [`hbco:thermal_comfort`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#thermal_comfort) |
| Lay terms (9) | `clammy`, `damp feeling`, `high humidity`, `humid`, `moist air`, `muggy`, `muggy air`, `sticky air`, `too humid` |

### too warm {#too_warm}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#too_warm` |
| Concept ID | `too_warm` |
| Maps to Brick class | [`brick:Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Temperature_Sensor), [`brick:Zone_Air_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Zone_Air_Temperature_Sensor) |
| Recipe | `threshold` |
| Confidence | high |
| Component of | [`hbco:thermal_comfort`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#thermal_comfort) |
| Lay terms (10) | `feels warm`, `hottest`, `overheating`, `stuffy heat`, `sweltering`, `too hot`, `too warm`, `uncomfortably hot`, `warm in here`, `warmest` |

### VOC {#tvoc_level}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#tvoc_level` |
| Concept ID | `tvoc_level` |
| Maps to Brick class | [`brick:TVOC_Sensor`](https://ontology.brickschema.org/1.4/#brick:TVOC_Sensor) |
| Recipe | `threshold` |
| Confidence | medium |
| Component of | [`hbco:iaq_composite`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#iaq_composite) |
| Lay terms (6) | `chemical fumes`, `chemical smell`, `organic pollutants`, `TVOC`, `VOC`, `volatile organic compound` |

### under-utilized {#underutilized_space}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#underutilized_space` |
| Concept ID | `underutilized_space` |
| Maps to Brick class | [`brick:Occupancy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Sensor) |
| Recipe | `threshold` |
| Confidence | medium |
| Component of | [`hbco:busyness`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#busyness) |
| Lay terms (5) | `empty room`, `under-utilized`, `underused`, `unused space`, `wasted space` |

### window left open {#unexpected_open_window}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#unexpected_open_window` |
| Concept ID | `unexpected_open_window` |
| Maps to Brick class | [`brick:Contact_Sensor`](https://ontology.brickschema.org/1.4/#brick:Contact_Sensor), [`brick:Open_Close_Status`](https://ontology.brickschema.org/1.4/#brick:Open_Close_Status) |
| Recipe | `threshold` |
| Confidence | medium |
| Lay terms (22) | `are the doors open`, `are the windows open`, `contact sensor`, `door contact`, `door held open`, `door left open`, `door open`, `door sensor`, `doors held open`, `doors left open`, `doors open`, `held open`, `is the door open`, `is the window open`, `open window`, `propped open`, `window contact`, `window left open`, `window open`, `window sensor`, `windows left open`, `windows open` |

### ventilation {#ventilation_quality}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#ventilation_quality` |
| Concept ID | `ventilation_quality` |
| Maps to Brick class | [`brick:CO2_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO2_Level_Sensor), [`brick:Damper_Position_Sensor`](https://ontology.brickschema.org/1.4/#brick:Damper_Position_Sensor), [`brick:Supply_Air_Flow_Sensor`](https://ontology.brickschema.org/1.4/#brick:Supply_Air_Flow_Sensor) |
| Recipe | `threshold` |
| Confidence | high |
| Component of | [`hbco:iaq_composite`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#iaq_composite) |
| Lay terms (6) | `air circulation`, `air exchange`, `air flow`, `fresh air`, `freshest air`, `ventilation` |

### bin {#waste_fill}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#waste_fill` |
| Concept ID | `waste_fill` |
| Maps to Brick class | [`ontosage:Waste_Fill_Sensor`]({{ '/ontology/class/Waste_Fill_Sensor/' | relative_url }}) |
| Recipe | `threshold` |
| Confidence | high |
| Lay terms (11) | `bin`, `bin capacity`, `bin fill`, `bin level`, `bins`, `fill level`, `full bins`, `needs emptying`, `recycling bin`, `rubbish bin`, `waste bin` |

### bin weight {#waste_weight}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#waste_weight` |
| Concept ID | `waste_weight` |
| Maps to Brick class | [`ontosage:Waste_Weight_Sensor`]({{ '/ontology/class/Waste_Weight_Sensor/' | relative_url }}) |
| Recipe | `aggregate` |
| Confidence | high |
| Lay terms (10) | `bin weight`, `how much rubbish`, `how much waste`, `landfill weight`, `recycling weight`, `waste generated`, `waste produced`, `waste tonnage`, `waste weight`, `weight of waste` |

### water flow {#water_flow}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#water_flow` |
| Concept ID | `water_flow` |
| Maps to Brick class | [`brick:Water_Flow_Sensor`](https://ontology.brickschema.org/1.4/#brick:Water_Flow_Sensor) |
| Recipe | `aggregate` |
| Confidence | medium |
| Lay terms (4) | `flow rate of water`, `water flow`, `water flow rate`, `water flowing` |

### water leak {#water_leak}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#water_leak` |
| Concept ID | `water_leak` |
| Maps to Brick class | [`brick:Leak_Alarm`](https://ontology.brickschema.org/1.4/#brick:Leak_Alarm), [`brick:Water_Flow_Sensor`](https://ontology.brickschema.org/1.4/#brick:Water_Flow_Sensor) |
| Recipe | `threshold` |
| Confidence | medium |
| Component of | [`hbco:water_usage`]({{ '/ontology/vocabulary/hbco-concepts/' | relative_url }}#water_usage) |
| Lay terms (6) | `dripping`, `flooding`, `leak`, `pipe leak`, `water leak`, `water running` |

### water level {#water_level}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#water_level` |
| Concept ID | `water_level` |
| Maps to Brick class | [`brick:Water_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:Water_Level_Sensor) |
| Recipe | `aggregate` |
| Confidence | medium |
| Lay terms (5) | `cistern level`, `tank level`, `tank levels`, `water level`, `water levels` |

### water quality {#water_quality}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#water_quality` |
| Concept ID | `water_quality` |
| Maps to Brick class | none |
| Recipe | `threshold` |
| Confidence | medium |
| Lay terms (4) | `drinking water`, `potable water`, `water quality`, `water safety` |

### water temperature {#water_temperature}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#water_temperature` |
| Concept ID | `water_temperature` |
| Maps to Brick class | [`brick:Water_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Water_Temperature_Sensor) |
| Recipe | `aggregate` |
| Confidence | high |
| Lay terms (9) | `chilled water temperature`, `delta t`, `delta-t`, `entering water temperature`, `flow temperature`, `hot water temperature`, `leaving water temperature`, `return water temperature`, `water temperature` |

### water usage rate {#water_usage_rate}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#water_usage_rate` |
| Concept ID | `water_usage_rate` |
| Maps to Brick class | [`brick:Water_Usage_Sensor`](https://ontology.brickschema.org/1.4/#brick:Water_Usage_Sensor) |
| Recipe | `aggregate` |
| Confidence | medium |
| Lay terms (4) | `daily water rate`, `litres per day`, `water usage rate`, `water use rate` |

### how do I get to {#wayfinding}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#wayfinding` |
| Concept ID | `wayfinding` |
| Maps to Brick class | none |
| Recipe | `aggregate` |
| Confidence | high |
| Lay terms (6) | `directions to`, `find room`, `how do I get to`, `navigate to`, `route to`, `where is` |

### should windows be opened {#window_guidance}

| Field | Value |
|---|---|
| IRI | `http://ontosage.org/hbco#window_guidance` |
| Concept ID | `window_guidance` |
| Maps to Brick class | [`brick:CO2_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO2_Level_Sensor), [`brick:Outside_Air_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Outside_Air_Temperature_Sensor) |
| Recipe | `correlate` |
| Confidence | medium |
| Lay terms (3) | `natural ventilation recommendation`, `open windows`, `should windows be opened` |

