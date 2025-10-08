---
layout: post
title: Backend Services
date: 2025-10-08
---

# Backend Services Documentation

Complete reference for all OntoBot backend services, their APIs, configuration, and integration patterns.

## Service Overview

OntoBot's backend consists of multiple microservices, each responsible for specific functionality:

| Service | Port | Purpose | Health Check |
|---------|------|---------|--------------|
| **Rasa Core** | 5005 | Conversational AI engine | `/version` |
| **Action Server** | 5055 | Custom action logic | `/health` |
| **Duckling** | 8000 | Entity extraction | `/` (HTML) |
| **Analytics Microservices** | 6001→6000 | Time-series analytics | `/health` |
| **Decider Service** | 6009 | Analytics type selection | `/health` |
| **File Server** | 8080 | Artifact storage & management | `/health` |
| **NL2SPARQL** | 6005 | NL→SPARQL translation | `/health` |
| **Ollama (Mistral)** | 11434 | Local LLM summarization | `/` |

## 1. Rasa Core Service

**Port**: 5005  
**Container**: `rasa_bldg1` (or bldg2/bldg3)  
**Technology**: Python, Rasa 3.6.12

### Purpose

The Rasa service is the conversational AI engine that:
- Processes natural language user input
- Identifies intents and extracts entities
- Manages dialogue state
- Triggers custom actions
- Generates responses

### Key Endpoints

#### Get Rasa Version
```http
GET http://localhost:5005/version
```

**Response:**
```json
{
  "version": "3.6.12",
  "minimum_compatible_version": "3.0.0",
  "rasa": "3.6.12"
}
```

#### Send Message (Webhook)
```http
POST http://localhost:5005/webhooks/rest/webhook
Content-Type: application/json

{
  "sender": "user123",
  "message": "What is the temperature in zone 5.04?"
}
```

**Response:**
```json
[
  {
    "recipient_id": "user123",
    "text": "The current temperature in zone 5.04 is 22.3°C."
  }
]
```

#### Model Management
```http
# Get current model
GET http://localhost:5005/status

# Load specific model
PUT http://localhost:5005/model
Content-Type: application/json

{
  "model_file": "/app/models/20250108-123045-ancient-dust.tar.gz"
}
```

### Configuration

**File**: `rasa-bldg1/config.yml`

```yaml
language: en
pipeline:
  - name: WhitespaceTokenizer
  - name: RegexFeaturizer
  - name: LexicalSyntacticFeaturizer
  - name: CountVectorsFeaturizer
  - name: DIETClassifier
    epochs: 100
  - name: DucklingEntityExtractor
    url: http://duckling_server:8000
    dimensions: ["time", "number"]
  - name: EntitySynonymMapper
  - name: ResponseSelector
    epochs: 100

policies:
  - name: MemoizationPolicy
  - name: RulePolicy
  - name: TEDPolicy
    max_history: 5
    epochs: 100
```

### Docker Configuration

```yaml
services:
  rasa_bldg1:
    image: rasa/rasa:3.6.12-full
    ports:
      - "5005:5005"
    volumes:
      - ./rasa-bldg1:/app
    command:
      - run
      - --enable-api
      - --cors
      - "*"
      - --debug
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5005/version"]
      interval: 30s
      timeout: 10s
      retries: 5
```

## 2. Action Server

**Port**: 5055  
**Container**: `action_server_bldg1`  
**Technology**: Python, Rasa SDK

### Purpose

Executes custom Python actions that:
- Query databases (MySQL, TimescaleDB, Cassandra)
- Call SPARQL endpoints (Fuseki)
- Invoke analytics microservices
- Fetch sensor data from ThingsBoard
- Format responses with artifacts

### Custom Actions

Located in: `rasa-bldg1/actions/actions.py`

**Available Actions:**

1. **`ActionGetSensorValue`**: Retrieve latest sensor reading
2. **`ActionGetAnalytics`**: Perform time-series analysis
3. **`ActionListSensors`**: Show all available sensors
4. **`ActionShowTrend`**: Generate trend visualizations
5. **`ActionCompare`**: Compare multiple sensors
6. **`ActionCheckAnomaly`**: Detect anomalies
7. **`ActionForecast`**: Predict future values
8. **`ActionSummarize`**: Generate natural language summaries

### Integration Pattern

```python
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionGetSensorValue(Action):
    def name(self) -> str:
        return "action_get_sensor_value"
    
    def run(self, dispatcher, tracker, domain):
        # 1. Extract entities
        sensor_name = tracker.get_slot("sensor")
        
        # 2. Query database or API
        value = get_latest_value(sensor_name)
        
        # 3. Optional: Call analytics
        payload = build_payload(sensor_name, value)
        analytics_result = requests.post(
            "http://microservices:6000/analytics/run",
            json=payload
        ).json()
        
        # 4. Format response
        response = f"The {sensor_name} reads {value}."
        
        # 5. Dispatch to user
        dispatcher.utter_message(text=response)
        
        return []
```

### Environment Variables

```bash
# Database connections
DB_HOST=mysqlserver
DB_PORT=3306
DB_NAME=telemetry
DB_USER=rasa
DB_PASSWORD=secure_password

# Service URLs
ANALYTICS_URL=http://microservices:6000/analytics/run
DECIDER_URL=http://decider-service:6009/decide
BASE_URL=http://http_server:8080
FUSEKI_URL=http://jena-fuseki-rdf-store:3030/abacws/sparql

# Optional services
NL2SPARQL_URL=http://nl2sparql:6005/nl2sparql
OLLAMA_URL=http://ollama:11434/api/generate
```

## 3. Analytics Microservices

**Port**: 6001 (host) → 6000 (container)  
**Container**: `microservices_container`  
**Technology**: Python, Flask

### Purpose

Provides time-series analytics for sensor data:
- Statistical analysis (min, max, avg, std)
- Trend detection
- Anomaly detection
- Forecasting
- Correlation analysis
- Aggregation

### Architecture

```
Flask App (app.py)
├── Analytics Blueprint (/analytics/run)
├── Decider Blueprint (/decider)
└── T5 Training Blueprint (/api/t5/*)
```

### API Reference

#### Run Analytics
```http
POST http://localhost:6001/analytics/run
Content-Type: application/json

{
  "action": "analyze_sensor_trend",
  "sensor_keys": ["Air_Temperature_Sensor_5.04"],
  "timeRange": "24h",
  "locationFilter": "zone_5_04",
  "unit": "degC",
  "aggregation": "avg"
}
```

**Response:**
```json
{
  "ok": true,
  "analysis_type": "trend",
  "summary": "Temperature trend is stable over the last 24 hours.",
  "data": [
    {"timestamp": "2025-01-08T00:00:00", "value": 22.1},
    {"timestamp": "2025-01-08T01:00:00", "value": 22.3},
    ...
  ],
  "statistics": {
    "min": 21.8,
    "max": 23.1,
    "avg": 22.4,
    "std": 0.4
  },
  "artifact_url": "http://localhost:8080/artifacts/trend_12345.png"
}
```

### Available Analysis Types

1. **`retrieve_latest_value`**: Get most recent sensor reading
   ```json
   {
     "action": "retrieve_latest_value",
     "sensor_keys": ["CO2_Level_Sensor_5.04"]
   }
   ```

2. **`analyze_sensor_trend`**: Time-series trend analysis
   ```json
   {
     "action": "analyze_sensor_trend",
     "sensor_keys": ["Air_Temperature_Sensor_5.04"],
     "timeRange": "7d"
   }
   ```

3. **`detect_anomalies`**: Statistical anomaly detection
   ```json
   {
     "action": "detect_anomalies",
     "sensor_keys": ["Zone_Air_Humidity_Sensor_5.04"],
     "threshold": 2.0
   }
   ```

4. **`compare_sensors`**: Multi-sensor comparison
   ```json
   {
     "action": "compare_sensors",
     "sensor_keys": [
       "Air_Temperature_Sensor_5.01",
       "Air_Temperature_Sensor_5.02"
     ],
     "metric": "avg"
   }
   ```

5. **`forecast_downtimes`**: Predictive maintenance
   ```json
   {
     "action": "forecast_downtimes",
     "equipment_id": "AHU_01",
     "horizon": "7d"
   }
   ```

6. **`aggregate_sensor_data`**: Statistical aggregation
   ```json
   {
     "action": "aggregate_sensor_data",
     "sensor_keys": ["Air_Temperature_Sensor_*"],
     "aggregation": "avg",
     "groupBy": "hour"
   }
   ```

### UK Defaults & Units

The analytics service applies UK-specific defaults:

**Temperature:**
- Default: °C
- Thresholds: 18-24°C (comfort)
- Alert: <16°C or >28°C

**CO2:**
- Default: ppm
- Threshold: 1000 ppm (HSE guideline)
- Alert: >1500 ppm

**Humidity:**
- Default: %RH
- Threshold: 40-60%
- Alert: <30% or >70%

**Illuminance:**
- Default: lux
- Office: 500 lux minimum
- Alert: <300 lux

### Health Check
```http
GET http://localhost:6001/health
```

**Response:**
```json
{
  "status": "ok",
  "components": ["analytics", "decider", "t5_training"],
  "timestamp": "2025-01-08T10:30:15Z"
}
```

## 4. Decider Service

**Port**: 6009  
**Container**: `decider_service`  
**Technology**: Python, FastAPI

### Purpose

Determines:
1. **Should analytics be performed?** (Yes/No)
2. **Which analytics function?** (trend, anomaly, compare, etc.)

### Decision Logic

**ML-Based** (when models available):
- Binary classifier: perform analytics or not
- Multi-class classifier: which analytics type
- Trained on question-label pairs

**Rule-Based** (fallback):
- Keyword matching
- Pattern recognition
- Intent classification

### API Reference

#### Decide
```http
POST http://localhost:6009/decide
Content-Type: application/json

{
  "question": "What is the temperature trend in zone 5.04?"
}
```

**Response:**
```json
{
  "perform_analytics": true,
  "analytics": "analyze_sensor_trend"
}
```

**Analytics Labels:**
- `retrieve_latest_value`: Simple value retrieval
- `analyze_sensor_trend`: Trend over time
- `detect_anomalies`: Anomaly detection
- `compare_sensors`: Multi-sensor comparison
- `forecast_downtimes`: Predictive maintenance
- `aggregate_sensor_data`: Statistical aggregation
- `null`: No analytics needed (TTL query only)

### Training

Located in: `decider-service/data/`

**Training Data Generation:**
```bash
cd decider-service/data
python build_decider_training_direct.py
```

**Model Training:**
```bash
cd decider-service
python train.py
```

**Files:**
- `decider_training.direct.jsonl`: Training data
- `model/perform_model.pkl`: Binary classifier
- `model/label_model.pkl`: Multi-class classifier
- `model/*_vectorizer.pkl`: Feature extractors

### Environment Variables

```bash
# Model paths
DECIDER_PERFORM_MODEL_PATH=model/perform_model.pkl
DECIDER_LABEL_MODEL_PATH=model/label_model.pkl

# Feature settings
MAX_FEATURES=1000
MIN_DF=1
MAX_DF=0.9
```

## 5. File Server (HTTP Server)

**Port**: 8080  
**Container**: `http_server_bldg1`  
**Technology**: Python, Flask

### Purpose

Serves:
- Trained Rasa models
- Analysis artifacts (charts, CSVs)
- Static files
- API for Rasa management

### Directory Structure

```
/app/
├── artifacts/           ← Analysis results
│   ├── trend_12345.png
│   ├── data_12345.csv
│   └── summary_12345.json
├── models/              ← Rasa models
│   ├── 20250108-123045.tar.gz
│   └── 20250107-183012.tar.gz
└── static/              ← Web assets
```

### API Reference

#### Serve Artifact
```http
GET http://localhost:8080/artifacts/trend_12345.png
```

**Response**: Binary file (image, CSV, JSON, etc.)

#### List Models
```http
GET http://localhost:8080/api/rasa/models
```

**Response:**
```json
{
  "models": [
    {
      "name": "20250108-123045-ancient-dust.tar.gz",
      "mtime": 1704709845,
      "size": 45678901,
      "active": true
    }
  ],
  "current": "20250108-123045-ancient-dust.tar.gz"
}
```

#### Train Model (Job-based)
```http
POST http://localhost:8080/api/rasa/train_job2
Content-Type: application/json

{}
```

**Response:**
```json
{
  "ok": true,
  "jobId": "train_20250108_103015",
  "message": "Training job started"
}
```

#### Get Training Status
```http
GET http://localhost:8080/api/rasa/train_job2/{jobId}/status
```

**Response:**
```json
{
  "ok": true,
  "status": "running",
  "progress": "training_core",
  "logs": "Step 50/500 - Loss: 1.234...",
  "eta": 180
}
```

#### Start Rasa Server
```http
POST http://localhost:8080/api/rasa/start
Content-Type: application/json

{}
```

#### Stop Rasa Server
```http
POST http://localhost:8080/api/rasa/stop
Content-Type: application/json

{}
```

### Health Check
```http
GET http://localhost:8080/health
```

**Response:**
```json
{
  "status": "ok",
  "disk_space": {
    "total": 500000000000,
    "used": 250000000000,
    "free": 250000000000
  },
  "models_count": 5,
  "artifacts_count": 127
}
```

## 6. NL2SPARQL Service

**Port**: 6005  
**Container**: `nl2sparql_service`  
**Technology**: Python, Flask, Transformers

### Purpose

Translates natural language questions to SPARQL queries using fine-tuned T5 model.

### API Reference

#### Translate Question
```http
POST http://localhost:6005/nl2sparql
Content-Type: application/json

{
  "question": "What is the temperature in zone 5.04?"
}
```

**Response:**
```json
{
  "sparql": "PREFIX brick: <https://brickschema.org/schema/Brick#>\nSELECT ?value WHERE {\n  <http://example.org/sensor/Air_Temperature_Sensor_5.04> brick:hasValue ?value .\n}",
  "confidence": 0.95,
  "execution_time_ms": 125
}
```

### Model Configuration

**Environment Variables:**
```bash
MODEL_PATH=/app/checkpoint-3
DEVICE=cuda  # or cpu
MAX_LENGTH=512
```

### Query Log

The service maintains a log of recent translations:

```http
GET http://localhost:6005/
```

**Response**: HTML page showing last 50 queries with:
- Input question
- Generated SPARQL
- Timestamp
- Execution time

### Health Check
```http
GET http://localhost:6005/health
```

**Response:**
```json
{
  "status": "ok",
  "model_path": "/app/checkpoint-3",
  "device": "cpu",
  "queries_cached": 50
}
```

## 7. Ollama (Mistral) Service

**Port**: 11434  
**Container**: `ollama`  
**Technology**: Ollama runtime, Mistral 7B model

### Purpose

Provides local LLM capabilities for:
- Text summarization
- Response generation
- Natural language explanations
- Context-aware recommendations

### API Reference

#### Generate Completion
```http
POST http://localhost:11434/api/generate
Content-Type: application/json

{
  "model": "mistral",
  "prompt": "Summarize the following sensor data: ...",
  "stream": false
}
```

**Response:**
```json
{
  "model": "mistral",
  "created_at": "2025-01-08T10:30:15Z",
  "response": "The sensor data shows...",
  "done": true
}
```

#### List Models
```http
GET http://localhost:11434/api/tags
```

**Response:**
```json
{
  "models": [
    {
      "name": "mistral:latest",
      "modified_at": "2025-01-08T10:00:00Z",
      "size": 4109856768
    }
  ]
}
```

### Auto-Pull Configuration

Models are automatically pulled on container start:

```yaml
services:
  ollama:
    environment:
      - OLLAMA_MODELS=mistral
    command: >
      sh -c "
        ollama serve &
        sleep 10;
        ollama pull mistral;
        wait
      "
```

## 8. Duckling Entity Extractor

**Port**: 8000  
**Container**: `duckling_server_bldg1`  
**Technology**: Haskell, Duckling

### Purpose

Extracts structured entities from text:
- **Time**: dates, times, durations
- **Number**: integers, floats, ordinals
- **Temperature**: temperatures with units
- **Distance**: distances with units

### API Reference

#### Parse Text
```http
POST http://localhost:8000/parse
Content-Type: application/json

{
  "text": "What was the temperature yesterday at 3pm?",
  "locale": "en_GB",
  "tz": "Europe/London"
}
```

**Response:**
```json
[
  {
    "body": "yesterday",
    "start": 25,
    "end": 34,
    "dim": "time",
    "latent": false,
    "value": {
      "type": "value",
      "value": "2025-01-07T00:00:00.000Z",
      "grain": "day"
    }
  },
  {
    "body": "3pm",
    "start": 38,
    "end": 41,
    "dim": "time",
    "value": {
      "type": "value",
      "value": "2025-01-08T15:00:00.000Z",
      "grain": "hour"
    }
  }
]
```

### Supported Dimensions

- `time`: Dates, times, ranges
- `number`: Numeric values
- `temperature`: With units (°C, °F)
- `distance`: With units (m, km, miles)
- `volume`: With units (L, ml, gallons)
- `amount-of-money`: Currency
- `duration`: Time spans
- `ordinal`: First, second, third...

## Service Integration Patterns

### 1. Rasa → Action Server → Analytics

```
User: "Show me the temperature trend"
  ↓
Rasa identifies intent: get_trend
  ↓
Action Server: ActionGetTrend
  ↓
Decider Service: "analyze_sensor_trend"
  ↓
Analytics Microservices: Run analysis
  ↓
Action Server: Format response + artifact
  ↓
Rasa: Send to user
```

### 2. NL2SPARQL → Fuseki Query

```
User: "What sensors are in zone 5?"
  ↓
NL2SPARQL: Translate to SPARQL
  ↓
Query Fuseki: Execute SPARQL
  ↓
Parse Results: Extract sensor list
  ↓
Format Response: Natural language
```

### 3. Ollama Summarization

```
Analytics Result: Large JSON dataset
  ↓
Ollama: "Summarize this data for a non-technical user"
  ↓
Generated Summary: Natural language explanation
  ↓
Include in Response: User-friendly text
```

## Deployment Considerations

### Resource Requirements

| Service | CPU | Memory | Disk |
|---------|-----|--------|------|
| Rasa | 2 cores | 4 GB | 2 GB |
| Actions | 1 core | 2 GB | 500 MB |
| Analytics | 2 cores | 4 GB | 1 GB |
| NL2SPARQL | 4 cores | 8 GB | 4 GB (model) |
| Ollama | 4 cores | 8 GB | 8 GB (model) |
| Duckling | 1 core | 1 GB | 100 MB |

### Network Configuration

All services use internal Docker network `ontobot-network`:

```yaml
networks:
  ontobot-network:
    driver: bridge
```

**Internal DNS:**
- `rasa_bldg1:5005`
- `action_server_bldg1:5055`
- `microservices:6000`
- `decider-service:6009`
- `nl2sparql:6005`

### Health Monitoring

Setup health checks for all services:

```bash
# Check all services
curl http://localhost:5005/version
curl http://localhost:5055/health
curl http://localhost:6001/health
curl http://localhost:6009/health
curl http://localhost:6005/health
curl http://localhost:8080/health
```

### Logging

View logs for debugging:

```bash
# Rasa
docker logs rasa_bldg1 --tail 100 -f

# Actions
docker logs action_server_bldg1 --tail 100 -f

# Analytics
docker logs microservices_container --tail 100 -f

# All services
docker-compose -f docker-compose.bldg1.yml logs -f
```

## Next Steps

- [Frontend UI Guide](./frontend_ui.md)
- [Multi-Building Guide](./multi_building.md)
- [T5 Training Guide](./t5_training_guide.md)
- [API Reference](./api_reference.md)
