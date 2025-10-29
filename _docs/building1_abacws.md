---
layout: post
title: Building 1 - ABACWS Real Testbed
date: 2025-10-08
categories: buildings
---

# Building 1 - ABACWS (Real University Testbed)


<figure class="doc-figure" style="text-align:center;">
    <a href="/assets/images/bldg1_visulizer.png" target="_blank" rel="noopener">
        <img src="/assets/images/bldg1_visulizer.png" alt="Testbed Visualizer UI"
                 style="max-width:100%; height:auto; border-radius:6px; box-shadow:0 2px 12px rgba(0,0,0,0.08);"
                 width="960" />
    </a>
    <figcaption style="font-size:0.95rem; color:#666; margin-top:8px;">Testbed Visualizer UI (Building 1 — ABACWS)</figcaption>
  
</figure>


**Rasa Conversational AI Stack for Building 1**

## Overview

Building 1 (ABACWS) is a real-world university testbed building at Cardiff University, Wales, UK, with comprehensive Indoor Environmental Quality (IEQ) monitoring. This building serves as the primary demonstration and research platform for OntoBot's capabilities.

### Key Specifications

| Property | Details |
|----------|---------|
| **Building Type** | Real University Testbed |
| **Location** | Cardiff University, Wales, UK |
| **Sensor Coverage** | 680 sensors across 34 zones (5.01–5.34) |
| **Focus Area** | Indoor Environmental Quality (IEQ) |
| **Database** | MySQL (port 3307) |
| **Knowledge Graph** | Brick Schema 1.3 via Jena Fuseki (port 3030) |
| **Compose File** | `docker-compose.bldg1.yml` |
| **Technology Stack** | Rasa 3.6.12, Python 3.10, Docker, MySQL 8.0 |

## Sensor Infrastructure

### Sensor Distribution

ABACWS features **20 sensors per zone** across 34 zones on the 5th floor, providing comprehensive environmental monitoring:

- **Total Sensors**: 680
- **Zones**: 5.01 through 5.34
- **Sensors per Zone**: 20
- **Data Collection**: Real-time telemetry stored in MySQL

### Sensor Types

#### Air Quality Monitoring

**Primary Air Quality Metrics:**
- **CO2 Sensors** - Carbon dioxide concentration (ppm)
- **TVOC** - Total Volatile Organic Compounds (ppb)
- **Formaldehyde** - CH₂O concentration (µg/m³)

**Particulate Matter Sensors:**
- **PM1** - Particles < 1µm diameter (µg/m³)
- **PM2.5** - Particles < 2.5µm diameter (µg/m³)
- **PM10** - Particles < 10µm diameter (µg/m³)

#### Multi-Gas Sensors

**MQ Series Sensors:**
- **MQ2** - Combustible Gas & Smoke detection
- **MQ3** - Alcohol Vapor detection
- **MQ5** - LPG & Natural Gas detection
- **MQ9** - Carbon Monoxide & Coal Gas detection

**Additional Gas Sensors:**
- **NO2** - Nitrogen Dioxide concentration
- **O2** - Oxygen percentage
- **C2H5OH** - Ethyl Alcohol concentration

#### Environmental Parameters

- **Air Temperature** - °C with 0.1°C precision
- **Relative Humidity** - % RH
- **Illuminance** - Light levels (lux)
- **Sound Level** - MEMS noise sensor (dB)
- **Air Quality Index** - Composite IEQ score

## Database Integration

### MySQL Configuration

Building 1 uses MySQL 8.0 for telemetry storage, optimized for time-series queries:

```yaml
# docker-compose.bldg1.yml
mysqlserver:
  image: mysql:8.0
  ports:
    - "3307:3306"
  environment:
    MYSQL_ROOT_PASSWORD: password
    MYSQL_DATABASE: telemetry
    MYSQL_USER: rasa_user
    MYSQL_PASSWORD: rasa_pass
  volumes:
    - mysql_data:/var/lib/mysql
```

### Database Schema

```sql
-- Telemetry table structure
CREATE TABLE sensor_readings (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    sensor_uuid VARCHAR(36) NOT NULL,
    sensor_name VARCHAR(255),
    zone_id VARCHAR(10),
    timestamp DATETIME(6) NOT NULL,
    value DOUBLE NOT NULL,
    unit VARCHAR(20),
    sensor_type VARCHAR(50),
    INDEX idx_sensor_time (sensor_uuid, timestamp),
    INDEX idx_zone_time (zone_id, timestamp),
    INDEX idx_type (sensor_type)
) ENGINE=InnoDB;

-- Sensor metadata
CREATE TABLE sensors (
    uuid VARCHAR(36) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    zone_id VARCHAR(10) NOT NULL,
    sensor_type VARCHAR(50) NOT NULL,
    unit VARCHAR(20),
    location_description TEXT,
    brick_class VARCHAR(100),
    last_reading DATETIME(6),
    UNIQUE KEY unique_name (name)
) ENGINE=InnoDB;

-- Zone information
CREATE TABLE zones (
    zone_id VARCHAR(10) PRIMARY KEY,
    floor INT NOT NULL,
    building VARCHAR(50) NOT NULL,
    zone_type VARCHAR(50),
    area_sqm DOUBLE,
    occupancy_capacity INT,
    description TEXT
) ENGINE=InnoDB;
```

### Query Examples

**Get Recent CO2 Readings:**
```sql
SELECT 
    s.name AS sensor_name,
    s.zone_id,
    sr.timestamp,
    sr.value AS co2_ppm
FROM sensor_readings sr
JOIN sensors s ON sr.sensor_uuid = s.uuid
WHERE s.sensor_type = 'CO2'
    AND sr.timestamp >= NOW() - INTERVAL 1 HOUR
ORDER BY sr.timestamp DESC
LIMIT 100;
```

**Calculate Zone Average Temperature:**
```sql
SELECT 
    s.zone_id,
    AVG(sr.value) AS avg_temp,
    MIN(sr.value) AS min_temp,
    MAX(sr.value) AS max_temp,
    COUNT(*) AS reading_count
FROM sensor_readings sr
JOIN sensors s ON sr.sensor_uuid = s.uuid
WHERE s.sensor_type = 'Temperature'
    AND sr.timestamp >= NOW() - INTERVAL 24 HOUR
GROUP BY s.zone_id
ORDER BY s.zone_id;
```

**Detect Threshold Violations:**
```sql
SELECT 
    s.name,
    s.zone_id,
    sr.timestamp,
    sr.value AS co2_ppm
FROM sensor_readings sr
JOIN sensors s ON sr.sensor_uuid = s.uuid
WHERE s.sensor_type = 'CO2'
    AND sr.value > 1000  -- CO2 threshold
    AND sr.timestamp >= NOW() - INTERVAL 1 HOUR
ORDER BY sr.value DESC;
```

## Service Architecture

### Core Services

Building 1 runs 8 core services:

| Service | Port | Purpose | Health Endpoint |
|---------|------|---------|-----------------|
| **Rasa Core** | 5005 | NLU/Dialogue engine | `GET /version` |
| **Action Server** | 5055 | Custom actions & integrations | `GET /health` |
| **Duckling** | 8000 | Entity extraction (dates, times) | `GET /` |
| **File Server** | 8080 | Artifact hosting (charts, CSV) | `GET /health` |
| **Rasa Editor** | 6080 | Web-based NLU editor | `GET /health` |
| **Frontend UI** | 3000 | React chat interface | N/A |
| **Analytics** | 6001 | Time-series analytics microservice | `GET /health` |
| **Decider** | 6009 | Analytics selection logic | `GET /health` |

### Data Flow

```
User Query → Frontend (3000)
    ↓
Rasa Core (5005) → NLU Processing
    ↓
Action Server (5055)
    ├── MySQL (3307) → Telemetry Data
    ├── Fuseki (3030) → Knowledge Graph (SPARQL)
    ├── Analytics (6001) → Time-series Analysis
    ├── Decider (6009) → Analytics Selection
    └── NL2SPARQL (6005) → Query Translation
    ↓
File Server (8080) ← Generated Artifacts
    ↓
Frontend (3000) ← Rich Response + Media
```

### Optional Services

- **NL2SPARQL** (6005) - T5-based NL→SPARQL translator
- **Ollama** (11434) - Mistral LLM for summarization
- **Fuseki** (3030) - SPARQL endpoint for Brick knowledge graph
- **MySQL** (3307) - Primary telemetry database
- **pgAdmin** (5050) - Web-based database administration

## Installation & Setup

### Quick Start

```powershell
# From repository root
cd C:\Users\<username>\Documents\GitHub\OntoBot

# Start Building 1 stack
docker-compose -f docker-compose.bldg1.yml up -d --build

# Wait for services to be healthy (~2-3 minutes)
Start-Sleep -Seconds 180

# Verify services
docker-compose -f docker-compose.bldg1.yml ps
```

### Access Points

- **Frontend**: http://localhost:3000
- **Rasa Core**: http://localhost:5005/version
- **Action Server**: http://localhost:5055/health
- **File Server**: http://localhost:8080/health
- **Editor**: http://localhost:6080
- **Duckling**: http://localhost:8000
- **pgAdmin**: http://localhost:5050 (admin@admin.com / admin)
- **Fuseki**: http://localhost:3030

### Environment Configuration

```yaml
# Action Server Environment Variables
environment:
  # File Server
  BASE_URL: http://localhost:8080
  BUNDLE_MEDIA: "true"
  
  # MySQL Database
  DB_HOST: mysqlserver
  DB_NAME: telemetry
  DB_USER: root
  DB_PASSWORD: password
  DB_PORT: 3306
  
  # Service Integrations
  ANALYTICS_URL: http://microservices:6000/analytics/run
  DECIDER_URL: http://decider-service:6009/decide
  NL2SPARQL_URL: http://nl2sparql:6005/predict
  FUSEKI_URL: http://fuseki:3030/abacws/query
  
  # Feature Flags
  ENABLE_SUMMARIZATION: "true"
  ENABLE_ANALYTICS: "true"
```

## Usage Examples

### Indoor Environmental Quality Queries

**CO2 Monitoring:**
```
"What's the CO2 level in zone 5.12?"
"Show me CO2 trends for the past hour in zone 5.15"
"Which zones have high CO2 levels?"
"Alert me if CO2 exceeds 1000 ppm"
```

**Air Quality:**
```
"Show PM2.5 levels across all zones"
"What's the air quality in zone 5.20?"
"Display TVOC trends for today"
"Compare air quality between zones 5.10 and 5.20"
```

**Temperature & Humidity:**
```
"What's the temperature in zone 5.08?"
"Show humidity trends for the past week"
"Which zones are too warm?"
"Compare temperature across all zones"
```

**Multi-Parameter Queries:**
```
"Show me all environmental parameters for zone 5.15"
"What zones have poor air quality?"
"Display IEQ summary for floor 5"
"Compare comfort metrics across zones"
```

### Analytics Capabilities

Building 1 supports 30+ analytics types via the Analytics Microservice:

**Statistical Analysis:**
- Mean, median, mode
- Standard deviation
- Min/max values
- Quartiles & percentiles

**Time-Series Analysis:**
- Moving averages
- Exponential smoothing
- Trend detection
- Seasonality analysis

**Advanced Analytics:**
- Anomaly detection (Isolation Forest, Z-score)
- Forecasting (ARIMA, Prophet)
- Correlation analysis
- Threshold violation detection

**Example Request:**
```python
import requests

# Get CO2 forecast
response = requests.post(
    'http://localhost:6001/analytics/run',
    json={
        'analysis_type': 'forecast',
        'sensor_id': 'CO2-Zone-5.12',
        'method': 'prophet',
        'periods': 24,
        'interval': '1h'
    }
)
```

## Knowledge Graph Integration

### Brick Schema

Building 1 uses Brick Schema 1.3 for semantic building representation:

```turtle
# ABACWS Building Model (excerpt)
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix abacws: <http://example.org/abacws#> .

abacws:Building1 a brick:Building ;
    brick:hasFloor abacws:Floor5 .

abacws:Floor5 a brick:Floor ;
    brick:hasZone abacws:Zone_5_12 .

abacws:Zone_5_12 a brick:HVAC_Zone ;
    brick:hasPoint abacws:CO2_Sensor_5_12 ,
                   abacws:Temp_Sensor_5_12 ,
                   abacws:Humidity_Sensor_5_12 .

abacws:CO2_Sensor_5_12 a brick:CO2_Level_Sensor ;
    brick:hasUnit "ppm" ;
    brick:uuid "uuid-co2-5-12" .
```

### SPARQL Queries

**Find All CO2 Sensors:**
```sparql
PREFIX brick: <https://brickschema.org/schema/Brick#>
PREFIX abacws: <http://example.org/abacws#>

SELECT ?sensor ?zone ?uuid
WHERE {
    ?sensor a brick:CO2_Level_Sensor ;
            brick:isPointOf ?zone ;
            brick:uuid ?uuid .
}
```

**Get Zone Equipment:**
```sparql
PREFIX brick: <https://brickschema.org/schema/Brick#>

SELECT ?equipment ?type
WHERE {
    <http://example.org/abacws#Zone_5_12> brick:hasPoint ?equipment .
    ?equipment a ?type .
}
```

## Development

### Project Structure

```
rasa-bldg1/
├── actions/
│   ├── actions.py           # Custom actions (live reload)
│   └── mysql_client.py      # MySQL integration
├── data/
│   ├── nlu.yml             # NLU training data (IEQ specific)
│   ├── rules.yml           # Conversation rules
│   └── stories.yml         # Conversation flows
├── models/                  # Trained Rasa models
├── shared_data/
│   ├── artifacts/          # Generated charts, CSV files
│   └── sensor_mappings/    # UUID to sensor name mappings
├── config.yml              # Rasa pipeline configuration
├── domain.yml              # Intents, entities, responses
├── endpoints.yml           # Action server & event broker
└── credentials.yml         # Channel credentials
```

### Custom Actions

```python
# actions/actions.py
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import mysql.connector

class ActionQueryCO2(Action):
    def name(self) -> Text:
        return "action_query_co2"

    def run(
        self, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        
        zone = tracker.get_slot("zone_id")
        
        # Connect to MySQL
        conn = mysql.connector.connect(
            host='mysqlserver',
            database='telemetry',
            user='root',
            password='password'
        )
        
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT sr.value, sr.timestamp, s.unit
            FROM sensor_readings sr
            JOIN sensors s ON sr.sensor_uuid = s.uuid
            WHERE s.zone_id = %s 
              AND s.sensor_type = 'CO2'
            ORDER BY sr.timestamp DESC
            LIMIT 1
        """
        cursor.execute(query, (zone,))
        result = cursor.fetchone()
        
        if result:
            message = f"CO2 level in zone {zone}: {result['value']:.1f} {result['unit']}"
        else:
            message = f"No CO2 data found for zone {zone}"
        
        dispatcher.utter_message(text=message)
        return []
```

### Adding IEQ-Specific Intents

```yaml
# data/nlu.yml
- intent: query_co2
  examples: |
    - what's the CO2 in [zone 5.12](zone_id)
    - show me CO2 levels in [5.15](zone_id)
    - CO2 reading for [zone 5.20](zone_id)
    - carbon dioxide level in [5.08](zone_id)

- intent: query_air_quality
  examples: |
    - how's the air quality in [zone 5.12](zone_id)
    - show PM2.5 levels in [5.15](zone_id)
    - what's the AQI for [zone 5.20](zone_id)
    - air quality status in [5.08](zone_id)

- intent: query_temperature
  examples: |
    - what's the temperature in [zone 5.12](zone_id)
    - show me temp for [5.15](zone_id)
    - how warm is [zone 5.20](zone_id)
    - temperature reading for [5.08](zone_id)
```

## Testing & Monitoring

### Health Checks

```powershell
# Check all services
docker-compose -f docker-compose.bldg1.yml ps

# Individual health checks
curl http://localhost:5005/version        # Rasa
curl http://localhost:5055/health         # Actions
curl http://localhost:8080/health         # File Server
curl http://localhost:6001/health         # Analytics
curl http://localhost:6009/health         # Decider

# MySQL connectivity
docker-compose -f docker-compose.bldg1.yml exec mysqlserver mysql -u root -ppassword -e "SELECT 1"
```

### Test Conversations

```powershell
# Start interactive shell
docker-compose -f docker-compose.bldg1.yml exec rasa rasa shell

# Example conversation:
# You: what's the CO2 in zone 5.12?
# Bot: [Displays CO2 reading with timestamp]
# You: show me temperature trends
# Bot: [Generates chart and displays link]
# You: which zones have high CO2?
# Bot: [Lists zones with CO2 > threshold]
```

### Performance Monitoring

**MySQL Query Performance:**
```sql
-- Enable slow query log
SET GLOBAL slow_query_log = 'ON';
SET GLOBAL long_query_time = 2;

-- Check table sizes
SELECT 
    table_name,
    ROUND((data_length + index_length) / 1024 / 1024, 2) AS size_mb
FROM information_schema.tables
WHERE table_schema = 'telemetry'
ORDER BY (data_length + index_length) DESC;

-- Analyze queries
EXPLAIN SELECT * FROM sensor_readings WHERE sensor_uuid = 'uuid-123';
```

## Troubleshooting

### Common Issues

**Problem: MySQL container fails to start**
```powershell
# Check logs
docker-compose -f docker-compose.bldg1.yml logs mysqlserver

# Solution: Reset MySQL volume
docker-compose -f docker-compose.bldg1.yml down -v
docker volume rm ontobot_mysql_data
docker-compose -f docker-compose.bldg1.yml up -d mysqlserver
```

**Problem: Slow queries**
```sql
-- Add indexes
CREATE INDEX idx_sensor_type_time ON sensor_readings(sensor_type, timestamp);
CREATE INDEX idx_zone_type_time ON sensor_readings(zone_id, sensor_type, timestamp);

-- Optimize table
OPTIMIZE TABLE sensor_readings;
```

**Problem: Action server can't connect to MySQL**
```yaml
# Check environment variables in docker-compose.bldg1.yml
environment:
  DB_HOST: mysqlserver  # Must match service name
  DB_PORT: 3306         # Internal port, not host port
```

## Research & Academic Use

### Data Collection

ABACWS serves as a real-world testbed for:
- Indoor air quality research
- Occupant comfort studies
- Energy efficiency optimization
- HVAC control strategies
- Sensor network deployment

### Publications

Building 1 data has been used in research on:
- CO2-based ventilation control
- Particulate matter health impacts
- Multi-sensor data fusion
- Predictive maintenance
- Occupancy detection

### Data Access

For academic research access to ABACWS data, contact the Building Management Systems team at Cardiff University.

## Related Documentation

- [Building 2 - Office Building](/docs/building2/) - Synthetic HVAC-focused building
- [Building 3 - Data Center](/docs/building3/) - Critical infrastructure monitoring
- [MySQL Integration Guide](/docs/mysql_integration/) - Detailed database guide
- [Analytics API Reference](/docs/analytics_api/) - Analytics capabilities
- [Multi-Building Support](/docs/multi_building/) - Switching between buildings

## Support & Resources

- **Main Documentation**: [OntoBot GitHub](https://github.com/suhasdevmane/OntoBot)
- **MySQL Documentation**: [MySQL 8.0 Reference](https://dev.mysql.com/doc/)
- **Brick Schema**: [brickschema.org](https://brickschema.org/)
- **Rasa Documentation**: [rasa.com/docs](https://rasa.com/docs/)

---

**Building 1 (ABACWS)** represents real-world deployment with:
- ✅ 680 real sensors across 34 zones
- ✅ Comprehensive IEQ monitoring
- ✅ MySQL time-series storage
- ✅ Brick Schema knowledge graph
- ✅ Academic research platform
