---
title: "Measurands"
layout: post
permalink: /ontology/vocabulary/measurands/
---

[Ontology Browser]({{ '/docs/ontology-browser/' | relative_url }}) › [Vocabularies]({{ '/docs/ontology-browser/' | relative_url }}#vocabularies) › Measurands

A [`ontosage:Measurand`]({{ '/ontology/class/Measurand/' | relative_url }}) is a quantity a sensor can measure, at the granularity that tells one gas from another. Each carries the physical range a reading can take (a value outside it is not treated as a measurement) and a typical range. [`ontosage:measuresQuantityKind`]({{ '/ontology/property/measuresQuantityKind/' | relative_url }}) states which measurand a sensor class measures, independent of where Brick places the class in its hierarchy.

Source: [`ontology/measurand_kinds.ttl`](https://github.com/suhasdevmane/OntoSage/blob/main/ontology/measurand_kinds.ttl). It declares 30 measurands and 63 class-to-measurand statements.

## Measurands

| Measurand | Label | Unit | Physical range | Typical range | Decimals | Measured by |
|---|---|---|---|---|---|---|
| <span id="AirFlow"></span>`AirFlow` | air flow rate | L/s | 0 to 20000 | 0 to 500 | 0 | [`brick:Air_Flow_Sensor`](https://ontology.brickschema.org/1.4/#brick:Air_Flow_Sensor), [`brick:Flow_Sensor`](https://ontology.brickschema.org/1.4/#brick:Flow_Sensor) |
| <span id="AirQualityIndex"></span>`AirQualityIndex` | air quality index | index | 0 to 500 | 0 to 150 | 0 |  |
| <span id="AirTemperature"></span>`AirTemperature` | air temperature | degC | -30 to 70 | 18 to 28 | 2 | [`brick:Air_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Air_Temperature_Sensor), [`brick:Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Temperature_Sensor), [`brick:Zone_Air_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Zone_Air_Temperature_Sensor) |
| <span id="BinaryState"></span>`BinaryState` | binary state | state | 0 to 1 | 0 to 1 | 0 | [`brick:Contact_Sensor`](https://ontology.brickschema.org/1.4/#brick:Contact_Sensor), [`brick:Leak_Detector_Equipment`](https://ontology.brickschema.org/1.4/#brick:Leak_Detector_Equipment), [`brick:Motion_Sensor`](https://ontology.brickschema.org/1.4/#brick:Motion_Sensor), [`brick:Occupancy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Sensor), [`brick:Occupancy_Status`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Status), [`brick:Smoke_Detector`](https://ontology.brickschema.org/1.4/#brick:Smoke_Detector) |
| <span id="CarbonDioxide"></span>`CarbonDioxide` | carbon dioxide | ppm | 350 to 40000 | 400 to 1200 | 0 | [`brick:CO2_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO2_Level_Sensor), [`brick:CO2_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO2_Sensor) |
| <span id="CarbonMonoxide"></span>`CarbonMonoxide` | carbon monoxide | ppm | 0 to 1500 | 0 to 5 | 1 | [`brick:CO_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO_Level_Sensor), [`brick:CO_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO_Sensor) |
| <span id="ColourTemperature"></span>`ColourTemperature` | correlated colour temperature | K | 1000 to 10000 | 2700 to 6500 | 0 | [`brick:Lighting_Correlated_Color_Temperature_Command`](https://ontology.brickschema.org/1.4/#brick:Lighting_Correlated_Color_Temperature_Command), [`brick:Lighting_Correlated_Color_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Lighting_Correlated_Color_Temperature_Sensor) |
| <span id="ElectricalEnergy"></span>`ElectricalEnergy` | electrical energy | kWh | 0 to 1000000 | 0 to 8 | 2 | [`brick:Electrical_Energy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Electrical_Energy_Sensor), [`brick:Electrical_Meter`](https://ontology.brickschema.org/1.4/#brick:Electrical_Meter), [`brick:Energy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Energy_Sensor) |
| <span id="ElectricalPower"></span>`ElectricalPower` | electrical power | kW | 0 to 5000 | 0 to 6 | 2 | [`brick:Active_Power_Sensor`](https://ontology.brickschema.org/1.4/#brick:Active_Power_Sensor), [`brick:Electric_Power_Sensor`](https://ontology.brickschema.org/1.4/#brick:Electric_Power_Sensor), [`brick:Power_Sensor`](https://ontology.brickschema.org/1.4/#brick:Power_Sensor) |
| <span id="EventCount"></span>`EventCount` | event count | events | 0 to 100000 | 0 to 40 | 0 | [`brick:Access_Reader`](https://ontology.brickschema.org/1.4/#brick:Access_Reader) |
| <span id="Formaldehyde"></span>`Formaldehyde` | formaldehyde | ppb | 0 to 20000 | 5 to 50 | 1 | [`brick:Formaldehyde_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:Formaldehyde_Level_Sensor) |
| <span id="Illuminance"></span>`Illuminance` | illuminance | lux | 0 to 150000 | 0 to 1000 | 0 | [`brick:Illuminance_Sensor`](https://ontology.brickschema.org/1.4/#brick:Illuminance_Sensor), [`brick:Luminance_Sensor`](https://ontology.brickschema.org/1.4/#brick:Luminance_Sensor) |
| <span id="LinearPositionPercent"></span>`LinearPositionPercent` | position, percent open | % | 0 to 100 | 0 to 100 | 0 | [`brick:Damper_Position_Sensor`](https://ontology.brickschema.org/1.4/#brick:Damper_Position_Sensor), [`brick:Position_Sensor`](https://ontology.brickschema.org/1.4/#brick:Position_Sensor), [`brick:Valve_Position_Sensor`](https://ontology.brickschema.org/1.4/#brick:Valve_Position_Sensor) |
| <span id="Methane"></span>`Methane` | methane | ppm | 0 to 50000 | 0 to 10 | 1 | [`brick:Methane_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:Methane_Level_Sensor) |
| <span id="NitrogenDioxide"></span>`NitrogenDioxide` | nitrogen dioxide | ppb | 0 to 20000 | 5 to 40 | 0 | [`brick:NO2_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:NO2_Level_Sensor) |
| <span id="OccupancyCount"></span>`OccupancyCount` | occupancy count | people | 0 to 10000 | 0 to 30 | 0 | [`brick:Occupancy_Count_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Count_Sensor) |
| <span id="OxygenFraction"></span>`OxygenFraction` | oxygen fraction | % | 0 to 25 | 20.6 to 20.95 | 2 |  |
| <span id="Ozone"></span>`Ozone` | ozone | ppb | 0 to 5000 | 0 to 60 | 0 | [`brick:Ozone_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:Ozone_Level_Sensor) |
| <span id="ParticulateMatter"></span>`ParticulateMatter` | particulate matter | ug/m3 | 0 to 2000 | 2 to 35 | 0 | [`brick:Particulate_Matter_Sensor`](https://ontology.brickschema.org/1.4/#brick:Particulate_Matter_Sensor), [`brick:PM10_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:PM10_Level_Sensor), [`brick:PM10_Sensor`](https://ontology.brickschema.org/1.4/#brick:PM10_Sensor), [`brick:PM1_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:PM1_Level_Sensor), [`brick:PM1_Sensor`](https://ontology.brickschema.org/1.4/#brick:PM1_Sensor), [`brick:PM2.5_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:PM2.5_Level_Sensor), [`brick:PM2.5_Sensor`](https://ontology.brickschema.org/1.4/#brick:PM2.5_Sensor) |
| <span id="Rainfall"></span>`Rainfall` | rainfall | mm | 0 to 500 | 0 to 10 | 1 | [`ontosage:Rainfall_Sensor`]({{ '/ontology/class/Rainfall_Sensor/' | relative_url }}) |
| <span id="RelativeHumidity"></span>`RelativeHumidity` | relative humidity | %RH | 0 to 100 | 30 to 70 | 2 | [`brick:Humidity_Sensor`](https://ontology.brickschema.org/1.4/#brick:Humidity_Sensor), [`brick:Relative_Humidity_Sensor`](https://ontology.brickschema.org/1.4/#brick:Relative_Humidity_Sensor), [`brick:Zone_Air_Humidity_Sensor`](https://ontology.brickschema.org/1.4/#brick:Zone_Air_Humidity_Sensor) |
| <span id="SoilMoisture"></span>`SoilMoisture` | soil moisture | %VWC | 0 to 100 | 10 to 45 | 1 | [`ontosage:Soil_Moisture_Sensor`]({{ '/ontology/class/Soil_Moisture_Sensor/' | relative_url }}) |
| <span id="SolarIrradiance"></span>`SolarIrradiance` | solar irradiance | W/m2 | 0 to 1400 | 0 to 900 | 0 | [`brick:Solar_Irradiance_Sensor`](https://ontology.brickschema.org/1.4/#brick:Solar_Irradiance_Sensor) |
| <span id="SoundPressureLevel"></span>`SoundPressureLevel` | sound pressure level | dB(A) | 0 to 140 | 30 to 80 | 0 | [`brick:Noise_Sensor`](https://ontology.brickschema.org/1.4/#brick:Noise_Sensor), [`brick:Sound_Sensor`](https://ontology.brickschema.org/1.4/#brick:Sound_Sensor) |
| <span id="VibrationVelocity"></span>`VibrationVelocity` | vibration velocity | mm/s | 0 to 100 | 0 to 7 | 2 | [`brick:Vibration_Sensor`](https://ontology.brickschema.org/1.4/#brick:Vibration_Sensor), [`brick:Vibration_Sensor_Equipment`](https://ontology.brickschema.org/1.4/#brick:Vibration_Sensor_Equipment) |
| <span id="VolatileOrganicCompounds"></span>`VolatileOrganicCompounds` | volatile organic compounds | ppb | 0 to 60000 | 0 to 500 | 0 | [`brick:TVOC_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:TVOC_Level_Sensor), [`brick:TVOC_Sensor`](https://ontology.brickschema.org/1.4/#brick:TVOC_Sensor) |
| <span id="WaterFlow"></span>`WaterFlow` | water flow rate | L/min | 0 to 2000 | 0 to 50 | 1 | [`brick:Water_Flow_Sensor`](https://ontology.brickschema.org/1.4/#brick:Water_Flow_Sensor) |
| <span id="WaterLevel"></span>`WaterLevel` | water level | % | 0 to 100 | 10 to 95 | 0 | [`brick:Water_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:Water_Level_Sensor) |
| <span id="WaterTemperature"></span>`WaterTemperature` | water temperature | degC | -10 to 120 | 5 to 80 | 1 | [`brick:Chilled_Water_Supply_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Chilled_Water_Supply_Temperature_Sensor), [`brick:Entering_Water_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Entering_Water_Temperature_Sensor), [`brick:Hot_Water_Supply_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Hot_Water_Supply_Temperature_Sensor), [`brick:Leaving_Water_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Leaving_Water_Temperature_Sensor), [`brick:Water_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Water_Temperature_Sensor) |
| <span id="WaterVolume"></span>`WaterVolume` | water volume | L | 0 to 10000000 | 0 to 500 | 0 | [`brick:Building_Water_Meter`](https://ontology.brickschema.org/1.4/#brick:Building_Water_Meter), [`brick:Water_Meter`](https://ontology.brickschema.org/1.4/#brick:Water_Meter), [`brick:Water_Usage_Sensor`](https://ontology.brickschema.org/1.4/#brick:Water_Usage_Sensor) |

## Band sources

Where each physical range comes from, as the schema states it.

- **air flow rate** (`AirFlow`): Judgement: an AHU-scale duct.
- **air quality index** (`AirQualityIndex`): US EPA AQI runs 0-500.
- **air temperature** (`AirTemperature`): Judgement: covers a cold store and a plant room. A building air temperature outside it is a fault or a unit error -- 70 degC would read as 158 degF.
- **binary state** (`BinaryState`): Definitional.
- **carbon dioxide** (`CarbonDioxide`): Lower bound: outdoor background is ~420 ppm and falling below ~350 indoors is not achievable, so a sub-350 reading is a different quantity. Upper bound: NIOSH IDLH 40,000 ppm -- an emergency, and still a reading.
- **carbon monoxide** (`CarbonMonoxide`): NIOSH IDLH for CO is 1,200 ppm; the bound sits just above it.
- **correlated colour temperature** (`ColourTemperature`): Candlelight is about 1,800 K; the bluest commercial white is about 8,000 K.
- **electrical energy** (`ElectricalEnergy`): Measured: interval reads on this building's floor submeters, 2026-09-03..16, ran 1.9-4.9 kWh per 15 minutes. Only the lower bound is physical.
- **electrical power** (`ElectricalPower`): Judgement: a building-scale feed. Negative would mean export, which these meters do not measure.
- **event count** (`EventCount`): Judgement: only the lower bound is physical. Negative is impossible; the upper bound catches a wrapped counter.
- **formaldehyde** (`Formaldehyde`): NIOSH IDLH for formaldehyde is 20 ppm = 20,000 ppb.
- **illuminance** (`Illuminance`): Direct sunlight is about 120,000 lux; the bound sits above it for a sensor in a rooflight.
- **position, percent open** (`LinearPositionPercent`): Definitional: a damper or valve position as a percentage of travel.
- **methane** (`Methane`): Lower explosive limit for methane in air is 5% by volume = 50,000 ppm.
- **nitrogen dioxide** (`NitrogenDioxide`): NIOSH IDLH for NO2 is 20 ppm = 20,000 ppb.
- **occupancy count** (`OccupancyCount`): Judgement: a per-space counter. Negative is impossible; the upper bound catches a counter that has wrapped or is reporting a different quantity.
- **oxygen fraction** (`OxygenFraction`): Ambient air is 20.95%; enriched atmospheres above 25% are outside building HVAC.
- **ozone** (`Ozone`): NIOSH IDLH for ozone is 5 ppm = 5,000 ppb.
- **particulate matter** (`ParticulateMatter`): Judgement: severe wildfire-smoke indoor PM2.5 has been measured in the high hundreds; 2,000 leaves headroom without admitting a scale error.
- **rainfall** (`Rainfall`): Judgement: an interval accumulation. The world record for 24 hours is about 1,825 mm; a building gauge reporting above 500 mm in an interval is faulty.
- **relative humidity** (`RelativeHumidity`): Definitional: relative humidity is a percentage of saturation.
- **soil moisture** (`SoilMoisture`): Volumetric water content as a percentage; saturation is the definitional ceiling.
- **solar irradiance** (`SolarIrradiance`): The solar constant at the top of the atmosphere is about 1,361 W/m2; nothing at ground level exceeds it.
- **sound pressure level** (`SoundPressureLevel`): 0 dB is the threshold of hearing; 140 dB is the threshold of pain and the ceiling of building-grade meters.
- **vibration velocity** (`VibrationVelocity`): ISO 10816 machine-vibration severity bands top out well below 100 mm/s RMS.
- **volatile organic compounds** (`VolatileOrganicCompounds`): Judgement, not a standard: consumer TVOC sensors saturate in the tens of thousands of ppb and no single IDLH covers a mixture.
- **water flow rate** (`WaterFlow`): Judgement: a building main. Negative flow would mean backflow, which these meters do not report.
- **water level** (`WaterLevel`): Definitional: tank level as a percentage of capacity.
- **water temperature** (`WaterTemperature`): Judgement: covers a chilled circuit at 4 degC, a glycol loop below zero, and a heating flow at 82 degC, with headroom to the boiling point at atmospheric pressure. A heating flow of 72 degC is ordinary and was being excluded as impossible because the water points inherited the AIR band from Temperature\_Sensor.
- **water volume** (`WaterVolume`): Judgement: a cumulative register; only the lower bound is physical.

## Sensor classes and what they measure

| Class | Measures |
|---|---|
| [`brick:Access_Reader`](https://ontology.brickschema.org/1.4/#brick:Access_Reader) | [`ontosage:EventCount`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#EventCount) |
| [`brick:Active_Power_Sensor`](https://ontology.brickschema.org/1.4/#brick:Active_Power_Sensor) | [`ontosage:ElectricalPower`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#ElectricalPower) |
| [`brick:Air_Flow_Sensor`](https://ontology.brickschema.org/1.4/#brick:Air_Flow_Sensor) | [`ontosage:AirFlow`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#AirFlow) |
| [`brick:Air_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Air_Temperature_Sensor) | [`ontosage:AirTemperature`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#AirTemperature) |
| [`brick:Building_Water_Meter`](https://ontology.brickschema.org/1.4/#brick:Building_Water_Meter) | [`ontosage:WaterVolume`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#WaterVolume) |
| [`brick:Chilled_Water_Supply_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Chilled_Water_Supply_Temperature_Sensor) | [`ontosage:WaterTemperature`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#WaterTemperature) |
| [`brick:CO2_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO2_Level_Sensor) | [`ontosage:CarbonDioxide`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#CarbonDioxide) |
| [`brick:CO2_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO2_Sensor) | [`ontosage:CarbonDioxide`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#CarbonDioxide) |
| [`brick:CO_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO_Level_Sensor) | [`ontosage:CarbonMonoxide`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#CarbonMonoxide) |
| [`brick:CO_Sensor`](https://ontology.brickschema.org/1.4/#brick:CO_Sensor) | [`ontosage:CarbonMonoxide`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#CarbonMonoxide) |
| [`brick:Contact_Sensor`](https://ontology.brickschema.org/1.4/#brick:Contact_Sensor) | [`ontosage:BinaryState`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#BinaryState) |
| [`brick:Damper_Position_Sensor`](https://ontology.brickschema.org/1.4/#brick:Damper_Position_Sensor) | [`ontosage:LinearPositionPercent`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#LinearPositionPercent) |
| [`brick:Electric_Power_Sensor`](https://ontology.brickschema.org/1.4/#brick:Electric_Power_Sensor) | [`ontosage:ElectricalPower`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#ElectricalPower) |
| [`brick:Electrical_Energy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Electrical_Energy_Sensor) | [`ontosage:ElectricalEnergy`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#ElectricalEnergy) |
| [`brick:Electrical_Meter`](https://ontology.brickschema.org/1.4/#brick:Electrical_Meter) | [`ontosage:ElectricalEnergy`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#ElectricalEnergy) |
| [`brick:Energy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Energy_Sensor) | [`ontosage:ElectricalEnergy`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#ElectricalEnergy) |
| [`brick:Entering_Water_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Entering_Water_Temperature_Sensor) | [`ontosage:WaterTemperature`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#WaterTemperature) |
| [`brick:Flow_Sensor`](https://ontology.brickschema.org/1.4/#brick:Flow_Sensor) | [`ontosage:AirFlow`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#AirFlow) |
| [`brick:Formaldehyde_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:Formaldehyde_Level_Sensor) | [`ontosage:Formaldehyde`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#Formaldehyde) |
| [`brick:Hot_Water_Supply_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Hot_Water_Supply_Temperature_Sensor) | [`ontosage:WaterTemperature`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#WaterTemperature) |
| [`brick:Humidity_Sensor`](https://ontology.brickschema.org/1.4/#brick:Humidity_Sensor) | [`ontosage:RelativeHumidity`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#RelativeHumidity) |
| [`brick:Illuminance_Sensor`](https://ontology.brickschema.org/1.4/#brick:Illuminance_Sensor) | [`ontosage:Illuminance`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#Illuminance) |
| [`brick:Leak_Detector_Equipment`](https://ontology.brickschema.org/1.4/#brick:Leak_Detector_Equipment) | [`ontosage:BinaryState`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#BinaryState) |
| [`brick:Leaving_Water_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Leaving_Water_Temperature_Sensor) | [`ontosage:WaterTemperature`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#WaterTemperature) |
| [`brick:Lighting_Correlated_Color_Temperature_Command`](https://ontology.brickschema.org/1.4/#brick:Lighting_Correlated_Color_Temperature_Command) | [`ontosage:ColourTemperature`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#ColourTemperature) |
| [`brick:Lighting_Correlated_Color_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Lighting_Correlated_Color_Temperature_Sensor) | [`ontosage:ColourTemperature`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#ColourTemperature) |
| [`brick:Luminance_Sensor`](https://ontology.brickschema.org/1.4/#brick:Luminance_Sensor) | [`ontosage:Illuminance`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#Illuminance) |
| [`brick:Methane_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:Methane_Level_Sensor) | [`ontosage:Methane`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#Methane) |
| [`brick:Motion_Sensor`](https://ontology.brickschema.org/1.4/#brick:Motion_Sensor) | [`ontosage:BinaryState`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#BinaryState) |
| [`brick:NO2_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:NO2_Level_Sensor) | [`ontosage:NitrogenDioxide`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#NitrogenDioxide) |
| [`brick:Noise_Sensor`](https://ontology.brickschema.org/1.4/#brick:Noise_Sensor) | [`ontosage:SoundPressureLevel`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#SoundPressureLevel) |
| [`brick:Occupancy_Count_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Count_Sensor) | [`ontosage:OccupancyCount`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#OccupancyCount) |
| [`brick:Occupancy_Sensor`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Sensor) | [`ontosage:BinaryState`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#BinaryState) |
| [`brick:Occupancy_Status`](https://ontology.brickschema.org/1.4/#brick:Occupancy_Status) | [`ontosage:BinaryState`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#BinaryState) |
| [`brick:Ozone_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:Ozone_Level_Sensor) | [`ontosage:Ozone`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#Ozone) |
| [`brick:Particulate_Matter_Sensor`](https://ontology.brickschema.org/1.4/#brick:Particulate_Matter_Sensor) | [`ontosage:ParticulateMatter`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#ParticulateMatter) |
| [`brick:PM10_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:PM10_Level_Sensor) | [`ontosage:ParticulateMatter`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#ParticulateMatter) |
| [`brick:PM10_Sensor`](https://ontology.brickschema.org/1.4/#brick:PM10_Sensor) | [`ontosage:ParticulateMatter`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#ParticulateMatter) |
| [`brick:PM1_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:PM1_Level_Sensor) | [`ontosage:ParticulateMatter`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#ParticulateMatter) |
| [`brick:PM1_Sensor`](https://ontology.brickschema.org/1.4/#brick:PM1_Sensor) | [`ontosage:ParticulateMatter`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#ParticulateMatter) |
| [`brick:PM2.5_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:PM2.5_Level_Sensor) | [`ontosage:ParticulateMatter`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#ParticulateMatter) |
| [`brick:PM2.5_Sensor`](https://ontology.brickschema.org/1.4/#brick:PM2.5_Sensor) | [`ontosage:ParticulateMatter`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#ParticulateMatter) |
| [`brick:Position_Sensor`](https://ontology.brickschema.org/1.4/#brick:Position_Sensor) | [`ontosage:LinearPositionPercent`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#LinearPositionPercent) |
| [`brick:Power_Sensor`](https://ontology.brickschema.org/1.4/#brick:Power_Sensor) | [`ontosage:ElectricalPower`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#ElectricalPower) |
| [`brick:Relative_Humidity_Sensor`](https://ontology.brickschema.org/1.4/#brick:Relative_Humidity_Sensor) | [`ontosage:RelativeHumidity`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#RelativeHumidity) |
| [`brick:Smoke_Detector`](https://ontology.brickschema.org/1.4/#brick:Smoke_Detector) | [`ontosage:BinaryState`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#BinaryState) |
| [`brick:Solar_Irradiance_Sensor`](https://ontology.brickschema.org/1.4/#brick:Solar_Irradiance_Sensor) | [`ontosage:SolarIrradiance`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#SolarIrradiance) |
| [`brick:Sound_Sensor`](https://ontology.brickschema.org/1.4/#brick:Sound_Sensor) | [`ontosage:SoundPressureLevel`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#SoundPressureLevel) |
| [`brick:Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Temperature_Sensor) | [`ontosage:AirTemperature`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#AirTemperature) |
| [`brick:TVOC_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:TVOC_Level_Sensor) | [`ontosage:VolatileOrganicCompounds`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#VolatileOrganicCompounds) |
| [`brick:TVOC_Sensor`](https://ontology.brickschema.org/1.4/#brick:TVOC_Sensor) | [`ontosage:VolatileOrganicCompounds`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#VolatileOrganicCompounds) |
| [`brick:Valve_Position_Sensor`](https://ontology.brickschema.org/1.4/#brick:Valve_Position_Sensor) | [`ontosage:LinearPositionPercent`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#LinearPositionPercent) |
| [`brick:Vibration_Sensor`](https://ontology.brickschema.org/1.4/#brick:Vibration_Sensor) | [`ontosage:VibrationVelocity`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#VibrationVelocity) |
| [`brick:Vibration_Sensor_Equipment`](https://ontology.brickschema.org/1.4/#brick:Vibration_Sensor_Equipment) | [`ontosage:VibrationVelocity`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#VibrationVelocity) |
| [`brick:Water_Flow_Sensor`](https://ontology.brickschema.org/1.4/#brick:Water_Flow_Sensor) | [`ontosage:WaterFlow`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#WaterFlow) |
| [`brick:Water_Level_Sensor`](https://ontology.brickschema.org/1.4/#brick:Water_Level_Sensor) | [`ontosage:WaterLevel`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#WaterLevel) |
| [`brick:Water_Meter`](https://ontology.brickschema.org/1.4/#brick:Water_Meter) | [`ontosage:WaterVolume`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#WaterVolume) |
| [`brick:Water_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Water_Temperature_Sensor) | [`ontosage:WaterTemperature`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#WaterTemperature) |
| [`brick:Water_Usage_Sensor`](https://ontology.brickschema.org/1.4/#brick:Water_Usage_Sensor) | [`ontosage:WaterVolume`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#WaterVolume) |
| [`brick:Zone_Air_Humidity_Sensor`](https://ontology.brickschema.org/1.4/#brick:Zone_Air_Humidity_Sensor) | [`ontosage:RelativeHumidity`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#RelativeHumidity) |
| [`brick:Zone_Air_Temperature_Sensor`](https://ontology.brickschema.org/1.4/#brick:Zone_Air_Temperature_Sensor) | [`ontosage:AirTemperature`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#AirTemperature) |
| [`ontosage:Rainfall_Sensor`]({{ '/ontology/class/Rainfall_Sensor/' | relative_url }}) | [`ontosage:Rainfall`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#Rainfall) |
| [`ontosage:Soil_Moisture_Sensor`]({{ '/ontology/class/Soil_Moisture_Sensor/' | relative_url }}) | [`ontosage:SoilMoisture`]({{ '/ontology/vocabulary/measurands/' | relative_url }}#SoilMoisture) |

## Properties of a measurand

- [`ontosage:physicalMax`]({{ '/ontology/property/physicalMax/' | relative_url }}): physical maximum
- [`ontosage:physicalMin`]({{ '/ontology/property/physicalMin/' | relative_url }}): physical minimum
- [`ontosage:physicalUnit`]({{ '/ontology/property/physicalUnit/' | relative_url }}): physical unit
- [`ontosage:typicalDecimals`]({{ '/ontology/property/typicalDecimals/' | relative_url }}): typical decimals
- [`ontosage:typicalMax`]({{ '/ontology/property/typicalMax/' | relative_url }}): typical maximum
- [`ontosage:typicalMin`]({{ '/ontology/property/typicalMin/' | relative_url }}): typical minimum

