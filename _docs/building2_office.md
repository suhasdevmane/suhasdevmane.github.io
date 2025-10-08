---
layout: post
title: Building 2 - Synthetic Office Building
date: 2025-10-08
categories: buildings
---

# Building 2 - Synthetic Office Building

**Rasa Conversational AI Stack for Building 2**

## Overview

Building 2 is a synthetic commercial office building designed for HVAC optimization and thermal comfort research. It features TimescaleDB for advanced time-series analytics and comprehensive HVAC system monitoring.

### Key Specifications

| Property | Details |
|----------|---------|
| **Building Type** | Synthetic Commercial Office |
| **Purpose** | HVAC Optimization & Thermal Comfort Research |
| **Sensor Coverage** | 329 sensors across multiple zones |
| **Focus Area** | HVAC Systems & Thermal Comfort |
| **Database** | TimescaleDB (PostgreSQL extension, port 5433) |
| **Knowledge Graph** | Brick Schema 1.3 via Jena Fuseki (port 3030) |
| **Compose File** | `docker-compose.bldg2.yml` |
| **Technology Stack** | Rasa 3.6.12, Python 3.10, Docker, TimescaleDB 2.11 |

## HVAC System Architecture

### Equipment Coverage

**Air Handling Units (AHUs):**
- **15 AHUs** serving different building zones
- Supply/Return air temperature sensors
- Airflow rate monitoring
- Fan speed control feedback
- Filter status indicators

**Zone-Level Monitoring:**
- **50 thermal zones** with individual control
- Zone temperature setpoints
- Occupancy sensors
- VAV box position sensors
- Damper positions

**Central Plant:**
- **3 Chillers** for cooling
- **2 Boilers** for heating
- Supply/Return water temperatures
- Flow rates & pressures
- Energy consumption meters

### Sensor Distribution (329 Total)

| System | Sensors | Measurements |
|--------|---------|--------------|
| **AHUs** | 75 | Supply/Return temps, airflow, fan speed, filters |
| **Zones** | 150 | Temperature, setpoint, occupancy, VAV position |
| **Chillers** | 36 | Temp, flow, pressure, power, COP |
| **Boilers** | 24 | Temp, flow, pressure, power, efficiency |
| **Other** | 44 | OA temp, humidity, outdoor air dampers |

## TimescaleDB Integration

### Why TimescaleDB?

TimescaleDB is a PostgreSQL extension optimized for time-series data, perfect for HVAC monitoring:

**Benefits:**
- ✅ **Automatic Partitioning** - Time-based chunks for better performance
- ✅ **Compression** - Reduces storage by 90%+
- ✅ **Continuous Aggregates** - Pre-computed rollups
- ✅ **Retention Policies** - Automatic old data deletion
- ✅ **PostgreSQL Compatibility** - All PostgreSQL features available
- ✅ **Time-Series Functions** - time_bucket, first, last, interpolate

### Database Configuration

```yaml
# docker-compose.bldg2.yml
timescale:
  image: timescale/timescaledb:2.11.0-pg15
  ports:
    - "5433:5432"
  environment:
    POSTGRES_DB: telemetry_bldg2
    POSTGRES_USER: postgres
    POSTGRES_PASSWORD: postgres
    TIMESCALEDB_TELEMETRY: off
  volumes:
    - timescale_data:/var/lib/postgresql/data
```

### Hypertable Schema

```sql
-- Create database
CREATE DATABASE telemetry_bldg2;
\c telemetry_bldg2

-- Enable TimescaleDB extension
CREATE EXTENSION IF NOT EXISTS timescaledb;

-- Create sensor readings table
CREATE TABLE sensor_readings (
    time TIMESTAMPTZ NOT NULL,
    sensor_id TEXT NOT NULL,
    sensor_type TEXT NOT NULL,
    zone_id TEXT,
    equipment_id TEXT,
    value DOUBLE PRECISION NOT NULL,
    unit TEXT,
    quality_flag INTEGER DEFAULT 0
);

-- Convert to hypertable (automatic time-based partitioning)
SELECT create_hypertable('sensor_readings', 'time');

-- Create indexes
CREATE INDEX idx_sensor_id_time ON sensor_readings (sensor_id, time DESC);
CREATE INDEX idx_zone_time ON sensor_readings (zone_id, time DESC);
CREATE INDEX idx_equipment_time ON sensor_readings (equipment_id, time DESC);
CREATE INDEX idx_type_time ON sensor_readings (sensor_type, time DESC);

-- Enable compression (90%+ space savings)
ALTER TABLE sensor_readings SET (
    timescaledb.compress,
    timescaledb.compress_segmentby = 'sensor_id, sensor_type',
    timescaledb.compress_orderby = 'time DESC'
);

-- Add compression policy (compress data older than 7 days)
SELECT add_compression_policy('sensor_readings', INTERVAL '7 days');

-- Add retention policy (drop data older than 1 year)
SELECT add_retention_policy('sensor_readings', INTERVAL '1 year');
```

### Continuous Aggregates (Rollups)

```sql
-- Hourly averages (pre-computed for fast queries)
CREATE MATERIALIZED VIEW sensor_readings_hourly
WITH (timescaledb.continuous) AS
SELECT 
    time_bucket('1 hour', time) AS bucket,
    sensor_id,
    sensor_type,
    zone_id,
    AVG(value) AS avg_value,
    MIN(value) AS min_value,
    MAX(value) AS max_value,
    COUNT(*) AS reading_count
FROM sensor_readings
GROUP BY bucket, sensor_id, sensor_type, zone_id;

-- Refresh policy (update every hour)
SELECT add_continuous_aggregate_policy('sensor_readings_hourly',
    start_offset => INTERVAL '3 hours',
    end_offset => INTERVAL '1 hour',
    schedule_interval => INTERVAL '1 hour');

-- Daily aggregates
CREATE MATERIALIZED VIEW sensor_readings_daily
WITH (timescaledb.continuous) AS
SELECT 
    time_bucket('1 day', time) AS bucket,
    sensor_id,
    sensor_type,
    zone_id,
    AVG(value) AS avg_value,
    MIN(value) AS min_value,
    MAX(value) AS max_value,
    STDDEV(value) AS stddev_value
FROM sensor_readings
GROUP BY bucket, sensor_id, sensor_type, zone_id;
```

### Time-Series Queries

**Recent Zone Temperature:**
```sql
SELECT 
    time,
    sensor_id,
    zone_id,
    value AS temperature
FROM sensor_readings
WHERE sensor_type = 'ZoneTemp'
    AND zone_id = 'Zone-01'
    AND time > NOW() - INTERVAL '1 hour'
ORDER BY time DESC;
```

**Hourly Average with time_bucket:**
```sql
SELECT 
    time_bucket('1 hour', time) AS hour,
    zone_id,
    AVG(value) AS avg_temp,
    MIN(value) AS min_temp,
    MAX(value) AS max_temp
FROM sensor_readings
WHERE sensor_type = 'ZoneTemp'
    AND time > NOW() - INTERVAL '24 hours'
GROUP BY hour, zone_id
ORDER BY hour DESC, zone_id;
```

**HVAC Efficiency Analysis:**
```sql
-- Calculate COP (Coefficient of Performance) for chillers
WITH chiller_data AS (
    SELECT 
        time_bucket('15 minutes', time) AS bucket,
        equipment_id,
        AVG(CASE WHEN sensor_type = 'CoolingOutput' THEN value END) AS cooling_kw,
        AVG(CASE WHEN sensor_type = 'PowerInput' THEN value END) AS power_kw
    FROM sensor_readings
    WHERE equipment_id LIKE 'Chiller-%'
        AND time > NOW() - INTERVAL '24 hours'
    GROUP BY bucket, equipment_id
)
SELECT 
    bucket,
    equipment_id,
    cooling_kw,
    power_kw,
    CASE 
        WHEN power_kw > 0 THEN cooling_kw / power_kw 
        ELSE NULL 
    END AS cop
FROM chiller_data
WHERE cooling_kw IS NOT NULL AND power_kw IS NOT NULL
ORDER BY bucket DESC;
```

**Thermal Comfort Analysis:**
```sql
-- Find zones outside comfort range
SELECT 
    zone_id,
    AVG(value) AS avg_temp,
    STDDEV(value) AS temp_variance,
    COUNT(*) AS reading_count,
    COUNT(*) FILTER (WHERE value < 20 OR value > 24) AS out_of_comfort
FROM sensor_readings
WHERE sensor_type = 'ZoneTemp'
    AND time > NOW() - INTERVAL '1 day'
GROUP BY zone_id
HAVING AVG(value) < 20 OR AVG(value) > 24
ORDER BY out_of_comfort DESC;
```

## HVAC Optimization Features

### Thermal Comfort Monitoring

**Predicted Mean Vote (PMV) Calculation:**
- Air temperature
- Relative humidity
- Air velocity
- Metabolic rate (occupancy-based)
- Clothing insulation (seasonal)

**Comfort Metrics:**
- PMV: -3 (cold) to +3 (hot), target: -0.5 to +0.5
- PPD: Percentage of People Dissatisfied
- Operative temperature
- Thermal sensation

### Energy Efficiency Analytics

**Performance Indicators:**
- **COP** (Coefficient of Performance) - Chillers
- **Boiler Efficiency** - Combustion efficiency %
- **AHU Energy Consumption** - kWh per CFM
- **Zone Temperature Variance** - Comfort stability

**Optimization Strategies:**
- Optimal start/stop times
- Supply air temperature reset
- Static pressure reset
- Economizer operation
- Demand-controlled ventilation

### Predictive Maintenance

**Equipment Monitoring:**
- Filter differential pressure trends
- Fan vibration analysis
- Bearing temperature monitoring
- Valve position feedback
- Compressor runtime tracking

**Maintenance Alerts:**
- Filter replacement due (ΔP > threshold)
- Fan bearing wear detection
- Valve stuck detection
- Refrigerant leak indicators

## Usage Examples

### Zone Comfort Queries

```
"What's the temperature in Zone 01?"
"Show me thermal comfort for all zones"
"Which zones are too hot?"
"Display temperature trends for Zone 05 today"
"Compare setpoint vs actual temperature"
```

### HVAC System Queries

```
"Show me AHU-1 performance"
"What's the supply air temperature from AHU-3?"
"Display chiller efficiency"
"Show all AHU fan speeds"
"What's the current cooling load?"
```

### Energy & Efficiency

```
"Calculate building energy consumption today"
"What's the COP of Chiller 2?"
"Show me boiler efficiency trends"
"Compare energy use this week vs last week"
"Display power consumption by system"
```

### Maintenance & Alerts

```
"Which filters need replacement?"
"Show equipment alarms"
"Display maintenance due items"
"What's the runtime on AHU-5?"
"Show me valve position feedback"
```

## pgAdmin Integration

Building 2 includes pgAdmin for web-based database management:

```yaml
# Pre-configured pgAdmin
pgadmin:
  image: dpage/pgadmin4:latest
  ports:
    - "5050:80"
  environment:
    PGADMIN_DEFAULT_EMAIL: admin@admin.com
    PGADMIN_DEFAULT_PASSWORD: admin
  volumes:
    - ./bldg2/servers.json:/pgadmin4/servers.json
```

**Access:** http://localhost:5050 (admin@admin.com / admin)

**Pre-configured Connection:**
- Host: timescale
- Port: 5432
- Database: telemetry_bldg2
- Username: postgres

## Analytics Integration

### HVAC-Specific Analytics

**Thermal Analysis:**
- Zone temperature profiling
- Setpoint tracking
- Comfort index calculation
- Thermal lag analysis

**Equipment Performance:**
- COP/EER calculation
- Runtime analysis
- Cycling frequency
- Load profiles

**Energy Analytics:**
- Baseline consumption
- Energy signatures
- Degree-day normalization
- Peak demand analysis

### API Examples

```python
import requests

# Get zone thermal comfort analysis
response = requests.post(
    'http://localhost:6001/analytics/run',
    json={
        'analysis_type': 'thermal_comfort',
        'zone_id': 'Zone-01',
        'start_time': '2025-10-01T00:00:00Z',
        'end_time': '2025-10-08T23:59:59Z',
        'comfort_range': {'min': 20, 'max': 24}
    }
)

# Calculate HVAC efficiency
response = requests.post(
    'http://localhost:6001/analytics/run',
    json={
        'analysis_type': 'hvac_efficiency',
        'equipment_id': 'Chiller-01',
        'metric': 'cop',
        'aggregation': '15min'
    }
)
```

## Development

### Custom Actions

```python
# actions/actions.py
import psycopg2
from psycopg2.extras import RealDictCursor

class ActionQueryZoneTemp(Action):
    def name(self) -> Text:
        return "action_query_zone_temp"

    def run(self, dispatcher, tracker, domain):
        zone = tracker.get_slot("zone_id")
        
        # Connect to TimescaleDB
        conn = psycopg2.connect(
            host='timescale',
            database='telemetry_bldg2',
            user='postgres',
            password='postgres'
        )
        
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        query = """
            SELECT 
                time,
                value AS temperature,
                unit
            FROM sensor_readings
            WHERE sensor_type = 'ZoneTemp'
              AND zone_id = %s
            ORDER BY time DESC
            LIMIT 1
        """
        cursor.execute(query, (zone,))
        result = cursor.fetchone()
        
        if result:
            message = f"Temperature in {zone}: {result['temperature']:.1f}°C"
        else:
            message = f"No temperature data for {zone}"
        
        dispatcher.utter_message(text=message)
        return []
```

### HVAC-Specific Intents

```yaml
# data/nlu.yml
- intent: query_zone_temperature
  examples: |
    - what's the temperature in [Zone 01](zone_id)
    - show me [Zone 05](zone_id) temp
    - temperature reading for [Zone 12](zone_id)
    - how warm is [Zone 03](zone_id)

- intent: query_ahu_status
  examples: |
    - show me [AHU-1](equipment_id) status
    - what's [AHU-3](equipment_id) supply air temp
    - display [AHU-5](equipment_id) fan speed
    - [AHU-2](equipment_id) performance

- intent: query_hvac_efficiency
  examples: |
    - what's the COP of [Chiller 1](equipment_id)
    - show [Chiller 2](equipment_id) efficiency
    - [Boiler 1](equipment_id) combustion efficiency
    - calculate building energy use
```

## Testing & Monitoring

### TimescaleDB Health

```powershell
# Check TimescaleDB version
docker-compose -f docker-compose.bldg2.yml exec timescale psql -U postgres -d telemetry_bldg2 -c "SELECT extversion FROM pg_extension WHERE extname = 'timescaledb';"

# Check hypertable stats
docker-compose -f docker-compose.bldg2.yml exec timescale psql -U postgres -d telemetry_bldg2 -c "SELECT * FROM timescaledb_information.hypertables;"

# Check compression stats
docker-compose -f docker-compose.bldg2.yml exec timescale psql -U postgres -d telemetry_bldg2 -c "SELECT * FROM timescaledb_information.compression_settings;"
```

### Query Performance

```sql
-- Analyze query plan
EXPLAIN ANALYZE
SELECT time_bucket('1 hour', time), AVG(value)
FROM sensor_readings
WHERE time > NOW() - INTERVAL '24 hours'
GROUP BY 1;

-- Check chunk size
SELECT * FROM timescaledb_information.chunks;

-- Monitor continuous aggregates
SELECT * FROM timescaledb_information.continuous_aggregates;
```

## Troubleshooting

### Common Issues

**Problem: Slow queries**
```sql
-- Ensure hypertable is created
SELECT * FROM timescaledb_information.hypertables;

-- Check if compression is enabled
SELECT * FROM timescaledb_information.compression_settings;

-- Reindex if needed
REINDEX TABLE sensor_readings;
```

**Problem: High disk usage**
```sql
-- Check table sizes
SELECT 
    hypertable_name,
    pg_size_pretty(hypertable_size(hypertable_name::regclass)) AS total_size,
    pg_size_pretty(hypertable_size(hypertable_name::regclass, 'uncompressed')) AS uncompressed,
    pg_size_pretty(hypertable_size(hypertable_name::regclass, 'compressed')) AS compressed
FROM timescaledb_information.hypertables;

-- Manually compress chunks
SELECT compress_chunk(i) FROM show_chunks('sensor_readings') i;

-- Adjust retention policy
SELECT remove_retention_policy('sensor_readings');
SELECT add_retention_policy('sensor_readings', INTERVAL '6 months');
```

## Related Documentation

- [Building 1 - ABACWS](/docs/building1_abacws/) - Real university testbed
- [Building 3 - Data Center](/docs/building3_datacenter/) - Critical infrastructure
- [TimescaleDB Integration Guide](/docs/timescaledb_integration/) - Detailed database guide
- [HVAC Analytics Guide](/docs/hvac_analytics/) - Thermal comfort & efficiency
- [Multi-Building Support](/docs/multi_building/) - Switching between buildings

## Support & Resources

- **TimescaleDB Documentation**: [docs.timescale.com](https://docs.timescale.com/)
- **HVAC Best Practices**: [ASHRAE Standards](https://www.ashrae.org/)
- **Thermal Comfort**: [ISO 7730](https://www.iso.org/standard/39155.html)
- **Building Automation**: [BACnet Standard](http://www.bacnet.org/)

---

**Building 2 (Office)** represents HVAC optimization with:
- ✅ 329 sensors across AHUs, zones, chillers, boilers
- ✅ TimescaleDB time-series optimization
- ✅ HVAC efficiency monitoring
- ✅ Thermal comfort analytics
- ✅ Energy optimization research
