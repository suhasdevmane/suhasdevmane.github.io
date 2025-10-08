---
layout: post
title: Multi-Building Guide
date: 2025-10-08
---

# Multi-Building Guide

OntoBot supports three distinct smart buildings with different characteristics, sensor configurations, and use cases. This guide covers the differences, portability features, and how to switch between buildings.

## Building Overview

### Building Taxonomy

| Building | Type | Focus Area | Sensors | Data Store |
|----------|------|------------|---------|------------|
| **Building 1 (ABACWS)** | Real Testbed | Indoor Environmental Quality (IEQ) | 680 | MySQL |
| **Building 2 (Office)** | Synthetic | AHU + Thermal Comfort | 329 | TimescaleDB |
| **Building 3 (Data Center)** | Synthetic | Critical Cooling & Alarms | 597 | Cassandra |

### Total System Coverage

- **Total Sensors**: 1,606 sensors across all buildings
- **Total Models**: Shared T5 NL2SPARQL models
- **Shared Services**: NL2SPARQL, Ollama, Fuseki available to all

## Building 1: ABACWS (Real University Testbed)

### Overview

**Nature**: Real-world university building testbed  
**Location**: Cardiff University  
**Deployment**: `docker-compose.bldg1.yml`  
**Rasa Project**: `./rasa-bldg1`

### Characteristics

**Sensor Coverage (680 sensors):**
- **Air Quality**: CO2, TVOC, Formaldehyde, Particulates (PM1, PM2.5, PM10)
- **Multi-Gas Sensors**: 
  - MQ2 (Combustible Gas, Smoke)
  - MQ3 (Alcohol Vapor)
  - MQ5 (LPG, Natural Gas)
  - MQ9 (Carbon Monoxide, Coal Gas)
- **Environmental**: Temperature, Humidity, Illuminance, Sound/Noise
- **Specialized**: Ethyl Alcohol, NO2, O2 Percentage

**Per-Zone Breakdown:**
- 34 zones (5.01 through 5.34)
- 20 sensor types per zone
- Dense multi-parameter monitoring

**Strengths:**
- ✅ Real-world data with actual occupancy patterns
- ✅ Rich multi-gas sensor diversity
- ✅ Comprehensive IEQ monitoring
- ✅ Proven deployment and validation

**Use Cases:**
- Indoor air quality research
- Occupancy-based control
- Health and wellness monitoring
- Multi-parameter correlation studies

### Data Storage

**Primary Database**: MySQL (port 3307)
```sql
Database: telemetry
Tables:
  - sensor_data
  - equipment_status
  - zone_metadata
```

**Knowledge Graph**: Jena Fuseki (port 3030)
```sparql
Dataset: abacws
Ontology: Brick Schema 1.3
Sensors: 680 instances
```

### Sensor Examples

```yaml
Air_Quality_Level_Sensor_5.01
Air_Quality_Sensor_5.01
Air_Temperature_Sensor_5.01
Alcohol_Vapor_MQ3_Gas_Sensor_5.01
CO2_Level_Sensor_5.01
CO_Level_Sensor_5.01
Carbon_Monoxide_Coal_Gas_Liquefied_MQ9_Gas_Sensor_5.01
Combustible_Gas_Smoke_MQ2_Sensor_5.01
Ethyl_Alcohol_C2H5CH_Gas_Sensor_5.01
Formaldehyde_Level_Sensor_5.01
Illuminance_Sensor_5.01
LPG_Natural_Gas_Town_MQ5_Gas_Sensor_5.01
NO2_Level_Sensor_5.01
Oxygen_O2_Percentage_Gas_Sensor_5.01
PM10_Level_Sensor_Atmospheric_5.01
PM1_Level_Sensor_Atmospheric_5.01
PM2.5_Level_Sensor_Atmospheric_5.01
Sound_Noise_Sensor_MEMS_5.01
TVOC_Level_Sensor_5.01
Zone_Air_Humidity_Sensor_5.01
```

### Docker Configuration

```yaml
# docker-compose.bldg1.yml
services:
  rasa_bldg1:
    ports: ["5005:5005"]
  action_server_bldg1:
    ports: ["5055:5055"]
  microservices:
    ports: ["6001:6000"]
  mysqlserver:
    ports: ["3307:3306"]
  pgadmin:
    ports: ["5050:80"]
```

## Building 2: Synthetic Office Building

### Overview

**Nature**: Synthetic commercial office building  
**Deployment**: `docker-compose.bldg2.yml`  
**Rasa Project**: `./rasa-bldg2`

### Characteristics

**Sensor Coverage (329 sensors):**
- **AHU (Air Handling Unit) Variables**:
  - Supply/Return Air Temperature
  - Chilled Water Supply/Return Temperature
  - Flow rates and pressures
  - Filter status and alarms
  
- **Zone Thermal Comfort**:
  - Zone temperature setpoints
  - Actual zone temperatures
  - Occupancy sensors
  - Thermal comfort parameters

**Naming Structure:**
```
AHU_01_Supply_Air_Temp_Sensor
AHU_01_Return_Air_Temp_Sensor
AHU_01_Chilled_Water_Supply_Temp
Zone_101_Temp_Sensor
Zone_101_Temp_Setpoint
Zone_102_Occupancy_Sensor
```

**Strengths:**
- ✅ Structured AHU/Zone naming convention
- ✅ Process variable focus (HVAC operations)
- ✅ Clear hierarchical organization
- ✅ Thermal comfort queries

**Use Cases:**
- HVAC optimization research
- Building energy management
- Thermal comfort studies
- Process variable analysis

### Data Storage

**Primary Database**: TimescaleDB (port 5433)
```sql
Database: building2_telemetry
Hypertables:
  - sensor_timeseries (time-series optimized)
  - equipment_events
```

**Advantages:**
- Fast time-series queries
- Automatic data retention policies
- Efficient compression
- SQL-based analytics

**Knowledge Graph**: Shared Fuseki instance
```sparql
Dataset: building2
Ontology: Brick Schema + custom AHU classes
```

### Sensor Organization

**By System:**
- AHU Systems: 15 units
- Zones: 50 zones
- Chillers: 3 units
- Boilers: 2 units

**By Measurement Type:**
- Temperature: 120 sensors
- Pressure: 45 sensors
- Flow: 35 sensors
- Status: 89 sensors
- Occupancy: 40 sensors

### Docker Configuration

```yaml
# docker-compose.bldg2.yml
services:
  rasa_bldg2:
    ports: ["5005:5005"]
  timescaledb:
    ports: ["5433:5432"]
  thingsboard:
    ports: ["8082:9090"]
  pgadmin:
    ports: ["5050:80"]
    volumes:
      - ./bldg2/servers.json:/pgadmin4/servers.json
```

## Building 3: Synthetic Data Center

### Overview

**Nature**: Synthetic critical infrastructure (data center)  
**Deployment**: `docker-compose.bldg3.yml`  
**Rasa Project**: `./rasa-bldg3`

### Characteristics

**Sensor Coverage (597 sensors):**
- **Critical Cooling**:
  - CRAC (Computer Room Air Conditioning) units
  - Precision cooling systems
  - Hot/Cold aisle monitoring
  - Rack-level temperature sensors

- **Power & Infrastructure**:
  - UPS status and load
  - PDU (Power Distribution Unit) monitoring
  - Generator status
  - Battery health

- **Alarms & Parameters**:
  - Critical alarm sensors
  - Warning threshold monitoring
  - Environmental parameters
  - Equipment health indicators

**Brick Class Taxonomy:**
- Widest equipment vocabulary
- Extensive alarm/parameter coverage
- Complex equipment relationships
- Multi-level hierarchies

**Strengths:**
- ✅ Comprehensive alarm monitoring
- ✅ Wide Brick class coverage
- ✅ Critical infrastructure focus
- ✅ Semantic generalization training

**Use Cases:**
- Data center efficiency research
- Critical cooling optimization
- Predictive maintenance
- Alarm correlation analysis

### Data Storage

**Primary Database**: Cassandra (port 9042)
```cql
Keyspace: datacenter_telemetry
Tables:
  - sensor_data_by_time
  - sensor_data_by_equipment
  - alarm_events
```

**Advantages:**
- Massive scalability
- High write throughput
- Multi-datacenter replication
- No single point of failure

**Metadata Database**: PostgreSQL (port 5434)
```sql
Database: thingsboard
Purpose: ThingsBoard entities & metadata
```

**Knowledge Graph**: Shared Fuseki instance
```sparql
Dataset: datacenter
Ontology: Brick Schema + data center extensions
```

### Sensor Organization

**By Criticality:**
- Critical: 89 sensors (immediate action)
- Warning: 156 sensors (monitoring needed)
- Normal: 352 sensors (routine monitoring)

**By System:**
- Cooling: 245 sensors
- Power: 134 sensors
- Environmental: 98 sensors
- Network: 67 sensors
- Security: 53 sensors

### Docker Configuration

```yaml
# docker-compose.bldg3.yml
services:
  rasa_bldg3:
    ports: ["5005:5005"]
  cassandra:
    ports: ["9042:9042"]
  postgres:
    ports: ["5434:5432"]
  thingsboard:
    ports: ["8082:9090"]
  pgadmin:
    ports: ["5051:80"]  # Note: 5051 to avoid conflict
```

## Switching Between Buildings

### One Building at a Time

**Important**: Only one building can run at a time because they share the same host ports (5005, 6001, 8080, etc.)

### Switch from Building 1 to Building 2

```powershell
# 1. Stop Building 1
docker-compose -f docker-compose.bldg1.yml down

# 2. Start Building 2
docker-compose -f docker-compose.bldg2.yml up -d

# 3. Wait for services to be healthy (~2 minutes)
Start-Sleep -Seconds 120

# 4. Verify
docker ps
curl http://localhost:5005/version
```

### Switch from Building 2 to Building 3

```powershell
# 1. Stop Building 2
docker-compose -f docker-compose.bldg2.yml down

# 2. Start Building 3
docker-compose -f docker-compose.bldg3.yml up -d

# 3. Wait for services
Start-Sleep -Seconds 120

# 4. Verify
docker ps
```

### Quick Switch Script

Create `switch-building.ps1`:

```powershell
param(
    [Parameter(Mandatory=$true)]
    [ValidateSet("1", "2", "3")]
    [string]$Building
)

Write-Host "Stopping all buildings..." -ForegroundColor Yellow
docker-compose -f docker-compose.bldg1.yml down 2>$null
docker-compose -f docker-compose.bldg2.yml down 2>$null
docker-compose -f docker-compose.bldg3.yml down 2>$null

Write-Host "Starting Building $Building..." -ForegroundColor Green
docker-compose -f "docker-compose.bldg$Building.yml" up -d

Write-Host "Waiting for services to start..." -ForegroundColor Cyan
Start-Sleep -Seconds 120

Write-Host "Verifying services..." -ForegroundColor Cyan
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

Write-Host "`nBuilding $Building is ready!" -ForegroundColor Green
Write-Host "Frontend: http://localhost:3000" -ForegroundColor Magenta
Write-Host "Rasa: http://localhost:5005" -ForegroundColor Magenta
```

**Usage:**
```powershell
.\switch-building.ps1 -Building 2
```

## Frontend Auto-Detection

The frontend and T5 Training GUI automatically detect which building is active:

### Sensor Detection

The microservices API checks for sensor lists in order:

```python
# In microservices/blueprints/t5_training.py
for building in ['bldg1', 'bldg2', 'bldg3']:
    sensor_file = f'/app/rasa-{building}/actions/sensor_list.txt'
    if os.path.exists(sensor_file):
        load_sensors(sensor_file)
        logger.info(f"Loaded {building} sensors")
        break
```

### Frontend Behavior

When you access `http://localhost:3000/settings`:

1. **Settings Page** loads T5 Training tab
2. **API Call** to `http://localhost:6001/api/t5/sensors`
3. **Auto-Detection** determines active building
4. **Dropdown Populates** with correct sensor count:
   - Building 1: 680 options
   - Building 2: 329 options
   - Building 3: 597 options

**No frontend code changes needed!** The same UI works for all buildings.

## Portability Features

### Shared Services (Extras)

These services work with any building:

```powershell
# Start Building 1 with AI services
docker-compose -f docker-compose.bldg1.yml -f docker-compose.extras.yml up -d

# Start Building 2 with AI services
docker-compose -f docker-compose.bldg2.yml -f docker-compose.extras.yml up -d
```

**Extras Include:**
- **NL2SPARQL** (port 6005): T5 translator
- **Ollama** (port 11434): Mistral LLM
- **Jupyter** (port 8888): Notebooks
- **GraphDB** (port 7200): Alternative RDF store
- **Adminer** (port 8282): Database UI

### Shared Data Structures

All buildings use consistent:

**1. Rasa Project Structure**
```
rasa-bldgX/
├── domain.yml
├── config.yml
├── data/
│   ├── nlu.yml
│   ├── rules.yml
│   └── stories.yml
├── actions/
│   ├── actions.py
│   ├── sensor_list.txt
│   └── sensor_uuids.txt
└── models/
```

**2. API Contracts**
All buildings use the same:
- Analytics payload format
- Decider request/response
- Rasa webhook structure
- File server endpoints

**3. Knowledge Graph (Brick Schema)**
All buildings use Brick 1.3+:
- Consistent predicates
- Standard classes
- Compatible queries

## Configuration Differences

### Environment Variables

**Building 1 (`.env.bldg1`):**
```bash
BUILDING_ID=bldg1
DB_HOST=mysqlserver
DB_PORT=3306
DB_TYPE=mysql
SENSOR_COUNT=680
```

**Building 2 (`.env.bldg2`):**
```bash
BUILDING_ID=bldg2
DB_HOST=timescaledb
DB_PORT=5432
DB_TYPE=timescale
SENSOR_COUNT=329
```

**Building 3 (`.env.bldg3`):**
```bash
BUILDING_ID=bldg3
DB_HOST=cassandra
DB_PORT=9042
DB_TYPE=cassandra
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
SENSOR_COUNT=597
```

### Docker Compose Differences

| Feature | Building 1 | Building 2 | Building 3 |
|---------|-----------|-----------|-----------|
| **Database** | MySQL | TimescaleDB | Cassandra + Postgres |
| **TB Storage** | MySQL | Postgres | Postgres + Cassandra |
| **pgAdmin Port** | 5050 | 5050 | 5051 |
| **MQTT Port** | 1883 | 1883 | 1884 |
| **TB Alt Port** | 7070 | 7070 | 7071 |

## Model Training Across Buildings

### Separate Training Data

Each building maintains its own training examples:

```
Transformers/t5_base/training/
├── bldg1/
│   └── correlation_fixes.json  # 680-sensor examples
├── bldg2/
│   └── correlation_fixes.json  # 329-sensor examples
└── bldg3/
    └── correlation_fixes.json  # 597-sensor examples
```

### Shared Models

All buildings can use the same trained model:

```
Transformers/t5_base/trained/
└── checkpoint-3/  # Works with all buildings
```

### Training Strategy

**Option 1: Separate Models**
```bash
# Train for each building separately
# Switch to Building 1
docker-compose -f docker-compose.bldg1.yml up -d microservices
# Train with Building 1 sensors
# Deploy to checkpoint-bldg1/

# Switch to Building 2
docker-compose -f docker-compose.bldg2.yml up -d microservices
# Train with Building 2 sensors
# Deploy to checkpoint-bldg2/
```

**Option 2: Merged Training** (Recommended)
```bash
# Combine all training data
python merge_training_data.py

# Train once with all examples
# Model learns patterns from all buildings
# Deploy to checkpoint-3/

# Test with all buildings
```

**Advantages of Merged Training:**
- Better generalization
- Single model to maintain
- Cross-building knowledge transfer
- More training examples

## Database Queries by Building

### Building 1 (MySQL)

```sql
-- Latest sensor value
SELECT ts, value 
FROM sensor_data 
WHERE sensor_name = 'Air_Temperature_Sensor_5.04'
ORDER BY ts DESC 
LIMIT 1;

-- Average per zone
SELECT 
  SUBSTRING(sensor_name, -4) as zone,
  AVG(value) as avg_temp
FROM sensor_data
WHERE sensor_name LIKE 'Air_Temperature_Sensor%'
  AND ts > NOW() - INTERVAL 1 HOUR
GROUP BY zone;
```

### Building 2 (TimescaleDB)

```sql
-- Time-bucketed averages
SELECT 
  time_bucket('1 hour', ts) AS hour,
  sensor_name,
  AVG(value) as avg_value
FROM sensor_timeseries
WHERE sensor_name = 'AHU_01_Supply_Air_Temp_Sensor'
  AND ts > NOW() - INTERVAL 24 HOURS
GROUP BY hour, sensor_name
ORDER BY hour;

-- Automatic retention
SELECT show_chunks('sensor_timeseries', older_than => INTERVAL '30 days');
```

### Building 3 (Cassandra)

```cql
-- Query by time (partition key)
SELECT * FROM sensor_data_by_time
WHERE date = '2025-01-08'
  AND sensor_id = 'CRAC_01_Supply_Temp'
  AND ts > '2025-01-08 10:00:00';

-- Query by equipment
SELECT * FROM sensor_data_by_equipment
WHERE equipment_type = 'CRAC'
  AND equipment_id = 'CRAC_01'
  AND ts > 1704709200000;
```

## SPARQL Queries (All Buildings)

All buildings share Brick Schema queries:

```sparql
# Find all temperature sensors
PREFIX brick: <https://brickschema.org/schema/Brick#>
SELECT ?sensor ?location WHERE {
  ?sensor a/rdfs:subClassOf* brick:Temperature_Sensor .
  ?sensor brick:hasLocation ?location .
}

# Find sensors in specific zone
PREFIX brick: <https://brickschema.org/schema/Brick#>
SELECT ?sensor ?type WHERE {
  ?sensor brick:isPartOf <zone:5.04> .
  ?sensor a ?type .
}

# Find all AHU equipment (Building 2 specific)
PREFIX brick: <https://brickschema.org/schema/Brick#>
SELECT ?ahu ?sensor WHERE {
  ?ahu a brick:AHU .
  ?sensor brick:isPointOf ?ahu .
}
```

## Testing Across Buildings

### Smoke Test Script

```powershell
# test-all-buildings.ps1

$buildings = @(1, 2, 3)
$results = @{}

foreach ($bldg in $buildings) {
    Write-Host "`nTesting Building $bldg..." -ForegroundColor Cyan
    
    # Stop all
    docker-compose -f docker-compose.bldg1.yml down 2>$null
    docker-compose -f docker-compose.bldg2.yml down 2>$null
    docker-compose -f docker-compose.bldg3.yml down 2>$null
    
    # Start target building
    docker-compose -f "docker-compose.bldg$bldg.yml" up -d
    Start-Sleep -Seconds 120
    
    # Test endpoints
    $rasa = curl -s http://localhost:5005/version | ConvertFrom-Json
    $analytics = curl -s http://localhost:6001/health | ConvertFrom-Json
    $sensors = curl -s http://localhost:6001/api/t5/sensors | ConvertFrom-Json
    
    $results["Building$bldg"] = @{
        Rasa = $rasa.version
        Analytics = $analytics.status
        SensorCount = $sensors.sensors.Count
    }
    
    Write-Host "Building $bldg - Sensors: $($sensors.sensors.Count)" -ForegroundColor Green
}

# Summary
Write-Host "`n=== Test Summary ===" -ForegroundColor Yellow
$results | ConvertTo-Json -Depth 3
```

**Expected Output:**
```json
{
  "Building1": {
    "Rasa": "3.6.12",
    "Analytics": "ok",
    "SensorCount": 680
  },
  "Building2": {
    "Rasa": "3.6.12",
    "Analytics": "ok",
    "SensorCount": 329
  },
  "Building3": {
    "Rasa": "3.6.12",
    "Analytics": "ok",
    "SensorCount": 597
  }
}
```

## Troubleshooting Multi-Building Issues

### Problem: Services Won't Start

**Symptom**: Containers fail to start after switching

**Causes:**
1. Previous building not fully stopped
2. Port conflicts
3. Volume mount issues

**Solution:**
```powershell
# Nuclear option - stop everything
docker-compose -f docker-compose.bldg1.yml down -v
docker-compose -f docker-compose.bldg2.yml down -v
docker-compose -f docker-compose.bldg3.yml down -v

# Clean up
docker system prune -f

# Start fresh
docker-compose -f docker-compose.bldg2.yml up -d --build
```

### Problem: Wrong Sensors Showing

**Symptom**: Building 2 active but showing Building 1 sensors

**Cause**: Cached data or frontend not refreshed

**Solution:**
```powershell
# Restart microservices
docker-compose -f docker-compose.bldg2.yml restart microservices

# Clear browser cache
# Ctrl+Shift+R (hard refresh)

# Verify
curl http://localhost:6001/api/t5/sensors | ConvertFrom-Json | Select-Object -ExpandProperty sensors | Measure-Object
# Should show 329 for Building 2
```

### Problem: Database Connection Errors

**Symptom**: Actions fail with database errors

**Cause**: Wrong database configuration for active building

**Solution:**
```powershell
# Check environment variables
docker exec action_server_bldg2 env | grep DB_

# Should show:
# DB_HOST=timescaledb
# DB_PORT=5432
# DB_TYPE=timescale

# If wrong, rebuild
docker-compose -f docker-compose.bldg2.yml up -d --build action_server
```

## Best Practices

### Development Workflow

1. **Choose Primary Building**: Start with Building 1 (real data)
2. **Train Base Model**: Use Building 1 sensors
3. **Test Portability**: Switch to Buildings 2 & 3
4. **Refine Training**: Add examples from each building
5. **Merge Models**: Combine all training data
6. **Deploy Unified**: Single model works everywhere

### Production Deployment

**Isolated Buildings:**
```bash
# Separate servers/VMs
server1: Building 1 only
server2: Building 2 only
server3: Building 3 only
```

**Shared Infrastructure:**
```bash
# Same server, different containers
- Run one building per environment
- Use separate Docker networks
- Different port mappings
```

### Backup Strategy

```bash
# Backup per building
for bldg in 1 2 3; do
  tar -czf "backup-bldg${bldg}-$(date +%Y%m%d).tar.gz" \
    "rasa-bldg${bldg}/" \
    "bldg${bldg}/" \
    "docker-compose.bldg${bldg}.yml"
done

# Backup shared components
tar -czf "backup-shared-$(date +%Y%m%d).tar.gz" \
  Transformers/ \
  microservices/ \
  decider-service/
```

## Next Steps

- [Frontend UI Guide](./frontend_ui.md)
- [Backend Services Documentation](./backend_services.md)
- [T5 Training Guide](./t5_training_guide.md)
- [Quick Start Guide](./quickstart.md)
- [API Reference](./api_reference.md)
