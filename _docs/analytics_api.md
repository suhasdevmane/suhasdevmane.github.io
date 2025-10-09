---
layout: post
title: Analytics API Reference
date: 2025-09-28
---

# Analytics API Reference

Base: `http://localhost:6001`

## POST /analytics/run

Body fields:

- `analysis_type` (string, required)
- Sensor data: flat or nested payload (see Data & Payloads)
- Optional parameters vary per function, e.g.:
  - `acceptable_range`: `[min, max]` for temperature/humidity
  - `thresholds`: object with pollutant limits or AQI weights
  - `method`: `zscore` or `iqr` for anomalies
  - `window`: integer for rolling computations

Response:

```json
{
  "analysis_type": "analyze_temperatures",
  "timestamp": "2025-02-10T06:00:00Z",
  "results": { "..." }
}
```

Notes:

- Results include `unit` and UK defaults metadata wherever applicable (e.g., `acceptable_range`, `acceptable_max`).
- Keys are derived from sensor names; robust matching avoids false positives (e.g., excludes "attempt" for temperature).

## Analysis catalog (highlights)

- Environmental:
  - `analyze_temperatures`, `analyze_humidity`, `analyze_co2_levels`, `analyze_pm_levels`, `analyze_formaldehyde_levels`, `analyze_noise_levels`, `analyze_air_quality`, `compute_air_quality_index`
- HVAC/air:
  - `analyze_supply_return_temp_difference`, `analyze_air_flow_variation`, `analyze_pressure_trend`, `analyze_air_quality_trends`, `analyze_hvac_anomalies`
- Generic:
  - `aggregate_sensor_data`, `correlate_sensors`, `analyze_sensor_trend`, `detect_anomalies`, `detect_potential_failures`, `forecast_downtimes`
- Ops:
  - `analyze_device_deviation`, `analyze_failure_trends`, `analyze_recalibration_frequency`

For per-function inputs/outputs see `microservices/README.md` or the source `microservices/blueprints/analytics_service.py`.
