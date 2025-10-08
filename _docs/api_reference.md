---
layout: post
title: API Reference
date: 2025-10-08
---

# API Reference

Complete REST API documentation for all OntoBot services. This reference covers authentication, request/response formats, and detailed endpoint specifications.

## Table of Contents

1. [Authentication](#authentication)
2. [Rasa Core API (Port 5005)](#rasa-core-api)
3. [Action Server API (Port 5055)](#action-server-api)
4. [Analytics Microservices (Port 6001)](#analytics-microservices)
5. [Decider Service (Port 6009)](#decider-service)
6. [File Server (Port 8080)](#file-server)
7. [NL2SPARQL Service (Port 6005)](#nl2sparql-service)
8. [Ollama/Mistral (Port 11434)](#ollama-api)
9. [Fuseki SPARQL (Port 3030)](#fuseki-sparql)
10. [Error Handling](#error-handling)
11. [Rate Limiting](#rate-limiting)
12. [Webhooks](#webhooks)

## Authentication

### Current Status

**Internal Services**: No authentication required (development mode)

**Production Recommendations**:
- Implement JWT tokens for frontend-to-backend
- Use API keys for service-to-service
- Enable HTTPS/TLS for all endpoints
- Add rate limiting per client

### Future Authentication

```http
POST /api/auth/login
Content-Type: application/json

{
  "username": "user@example.com",
  "password": "secure_password"
}

Response:
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

**Usage:**
```http
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

## Rasa Core API

**Base URL**: `http://localhost:5005`

### Version Info

```http
GET /version
```

**Response:**
```json
{
  "version": "3.6.12",
  "minimum_compatible_version": "3.0.0",
  "python": "3.10.12"
}
```

### Health Check

```http
GET /
```

**Response:**
```json
{
  "status": "ok",
  "message": "Rasa Core is running"
}
```

### Webhook - Send Message

```http
POST /webhooks/rest/webhook
Content-Type: application/json
```

**Request:**
```json
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
    "text": "The current temperature in zone 5.04 is 22.5°C (measured at 2025-01-08 14:30:00)."
  }
]
```

**Response with Custom Payload:**
```json
[
  {
    "recipient_id": "user123",
    "text": "Here's the temperature trend:",
    "custom": {
      "type": "chart",
      "data": {
        "sensor": "Air_Temperature_Sensor_5.04",
        "values": [22.1, 22.3, 22.5, 22.4, 22.6],
        "timestamps": ["14:00", "14:15", "14:30", "14:45", "15:00"]
      },
      "chart_url": "http://localhost:6001/chart/temp_trend_123.png"
    }
  }
]
```

### Tracker State

```http
GET /conversations/{sender_id}/tracker
```

**Response:**
```json
{
  "sender_id": "user123",
  "slots": {
    "sensor_name": "Air_Temperature_Sensor_5.04",
    "zone": "5.04",
    "time_range": "current"
  },
  "latest_message": {
    "intent": {
      "name": "query_temperature",
      "confidence": 0.98
    },
    "entities": [
      {
        "entity": "zone",
        "value": "5.04",
        "start": 32,
        "end": 36
      }
    ]
  },
  "events": [...]
}
```

### Continue Conversation

```http
POST /conversations/{sender_id}/execute
Content-Type: application/json
```

**Request:**
```json
{
  "action": "action_query_sensor"
}
```

**Response:**
```json
{
  "tracker": {...},
  "messages": [...]
}
```

### Model Info

```http
GET /status
```

**Response:**
```json
{
  "model_file": "models/20250108-143000.tar.gz",
  "model_id": "20250108-143000",
  "training_data": "data/nlu.yml",
  "num_active_training_jobs": 0
}
```

### Parse Message (NLU only)

```http
POST /model/parse
Content-Type: application/json
```

**Request:**
```json
{
  "text": "What is the temperature in zone 5.04?"
}
```

**Response:**
```json
{
  "intent": {
    "name": "query_temperature",
    "confidence": 0.982
  },
  "entities": [
    {
      "entity": "zone",
      "value": "5.04",
      "confidence": 0.95,
      "start": 32,
      "end": 36,
      "extractor": "DIETClassifier"
    }
  ],
  "intent_ranking": [
    {"name": "query_temperature", "confidence": 0.982},
    {"name": "query_humidity", "confidence": 0.012},
    {"name": "query_co2", "confidence": 0.006}
  ],
  "text": "What is the temperature in zone 5.04?"
}
```

## Action Server API

**Base URL**: `http://localhost:5055`

### Health Check

```http
GET /health
```

**Response:**
```json
{
  "status": "ok"
}
```

### Webhook - Execute Action

```http
POST /webhook
Content-Type: application/json
```

**Request:**
```json
{
  "next_action": "action_query_sensor",
  "sender_id": "user123",
  "tracker": {
    "sender_id": "user123",
    "slots": {
      "sensor_name": "Air_Temperature_Sensor_5.04"
    },
    "latest_message": {
      "intent": {"name": "query_temperature"}
    }
  },
  "domain": {...}
}
```

**Response:**
```json
{
  "events": [
    {
      "event": "slot",
      "name": "sensor_value",
      "value": "22.5"
    }
  ],
  "responses": [
    {
      "text": "The current temperature is 22.5°C"
    }
  ]
}
```

### Actions List

```http
GET /actions
```

**Response:**
```json
{
  "actions": [
    "action_query_sensor",
    "action_analytics_request",
    "action_list_sensors",
    "action_compare_sensors",
    "action_fetch_historical_data"
  ]
}
```

## Analytics Microservices

**Base URL**: `http://localhost:6001`

### Health Check

```http
GET /health
```

**Response:**
```json
{
  "status": "ok",
  "service": "analytics-microservices",
  "version": "1.0.0",
  "timestamp": "2025-01-08T14:30:00Z"
}
```

### Statistical Analysis

```http
POST /api/analytics/statistics
Content-Type: application/json
```

**Request:**
```json
{
  "sensor": "Air_Temperature_Sensor_5.04",
  "start_time": "2025-01-08T00:00:00Z",
  "end_time": "2025-01-08T23:59:59Z",
  "metrics": ["mean", "std", "min", "max", "median"]
}
```

**Response:**
```json
{
  "sensor": "Air_Temperature_Sensor_5.04",
  "period": {
    "start": "2025-01-08T00:00:00Z",
    "end": "2025-01-08T23:59:59Z",
    "duration_hours": 24
  },
  "statistics": {
    "mean": 22.3,
    "std": 0.8,
    "min": 20.5,
    "max": 24.1,
    "median": 22.4,
    "count": 288
  }
}
```

### Trend Analysis

```http
POST /api/analytics/trend
Content-Type: application/json
```

**Request:**
```json
{
  "sensor": "CO2_Level_Sensor_5.01",
  "start_time": "2025-01-08T00:00:00Z",
  "end_time": "2025-01-08T23:59:59Z",
  "method": "linear_regression"
}
```

**Response:**
```json
{
  "sensor": "CO2_Level_Sensor_5.01",
  "trend": {
    "direction": "increasing",
    "slope": 2.3,
    "r_squared": 0.87,
    "p_value": 0.001,
    "confidence": 0.95
  },
  "interpretation": "Significant upward trend detected",
  "recommendation": "Increase ventilation during peak hours"
}
```

### Anomaly Detection

```http
POST /api/analytics/anomalies
Content-Type: application/json
```

**Request:**
```json
{
  "sensor": "Air_Temperature_Sensor_5.04",
  "start_time": "2025-01-08T00:00:00Z",
  "end_time": "2025-01-08T23:59:59Z",
  "method": "isolation_forest",
  "sensitivity": 0.1
}
```

**Response:**
```json
{
  "sensor": "Air_Temperature_Sensor_5.04",
  "anomalies": [
    {
      "timestamp": "2025-01-08T03:15:00Z",
      "value": 18.2,
      "score": -0.65,
      "severity": "high",
      "expected_range": [21.5, 23.5]
    },
    {
      "timestamp": "2025-01-08T15:45:00Z",
      "value": 26.3,
      "score": -0.58,
      "severity": "medium",
      "expected_range": [21.5, 23.5]
    }
  ],
  "total_anomalies": 2,
  "anomaly_rate": 0.69
}
```

### Forecasting

```http
POST /api/analytics/forecast
Content-Type: application/json
```

**Request:**
```json
{
  "sensor": "Zone_Air_Humidity_Sensor_5.04",
  "historical_hours": 48,
  "forecast_hours": 4,
  "model": "prophet"
}
```

**Response:**
```json
{
  "sensor": "Zone_Air_Humidity_Sensor_5.04",
  "forecast": [
    {
      "timestamp": "2025-01-08T15:00:00Z",
      "predicted_value": 45.2,
      "confidence_lower": 42.1,
      "confidence_upper": 48.3,
      "confidence_level": 0.95
    },
    {
      "timestamp": "2025-01-08T16:00:00Z",
      "predicted_value": 46.1,
      "confidence_lower": 42.8,
      "confidence_upper": 49.4,
      "confidence_level": 0.95
    }
  ],
  "model_metrics": {
    "mae": 1.2,
    "rmse": 1.8,
    "mape": 2.3
  }
}
```

### Correlation Analysis

```http
POST /api/analytics/correlation
Content-Type: application/json
```

**Request:**
```json
{
  "sensor1": "Air_Temperature_Sensor_5.04",
  "sensor2": "Zone_Air_Humidity_Sensor_5.04",
  "start_time": "2025-01-08T00:00:00Z",
  "end_time": "2025-01-08T23:59:59Z",
  "method": "pearson"
}
```

**Response:**
```json
{
  "sensor1": "Air_Temperature_Sensor_5.04",
  "sensor2": "Zone_Air_Humidity_Sensor_5.04",
  "correlation": {
    "coefficient": -0.68,
    "p_value": 0.0001,
    "method": "pearson",
    "interpretation": "Strong negative correlation"
  },
  "relationship": "As temperature increases, humidity decreases",
  "strength": "strong"
}
```

### Visualization

```http
POST /api/analytics/visualize
Content-Type: application/json
```

**Request:**
```json
{
  "sensor": "Air_Temperature_Sensor_5.04",
  "start_time": "2025-01-08T00:00:00Z",
  "end_time": "2025-01-08T23:59:59Z",
  "chart_type": "line",
  "options": {
    "title": "Temperature Trend - Zone 5.04",
    "width": 800,
    "height": 400,
    "format": "png"
  }
}
```

**Response:**
```json
{
  "chart_url": "http://localhost:6001/charts/temp_trend_20250108_143000.png",
  "chart_base64": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA...",
  "metadata": {
    "width": 800,
    "height": 400,
    "format": "png",
    "created_at": "2025-01-08T14:30:00Z"
  }
}
```

### T5 Training - Get Sensors

```http
GET /api/t5/sensors
```

**Response:**
```json
{
  "sensors": [
    "Air_Quality_Level_Sensor_5.01",
    "Air_Quality_Sensor_5.01",
    "Air_Temperature_Sensor_5.01",
    ...
  ],
  "count": 680,
  "building": "bldg1"
}
```

### T5 Training - Get Examples

```http
GET /api/t5/examples
```

**Response:**
```json
{
  "examples": [
    {
      "id": 1,
      "question": "What is the temperature in zone 5.04?",
      "sensors": ["Air_Temperature_Sensor_5.04"],
      "sparql": "PREFIX brick: ...",
      "category": "Temperature Query",
      "notes": "Basic temperature retrieval",
      "created_at": "2025-01-08T10:00:00Z"
    }
  ],
  "count": 45
}
```

### T5 Training - Add Example

```http
POST /api/t5/examples
Content-Type: application/json
```

**Request:**
```json
{
  "question": "What is the temperature in zone 5.04?",
  "sensors": ["Air_Temperature_Sensor_5.04"],
  "sparql": "PREFIX brick: <https://brickschema.org/schema/Brick#>\nSELECT ?value WHERE { ... }",
  "category": "Temperature Query",
  "notes": "Basic temperature retrieval"
}
```

**Response:**
```json
{
  "status": "success",
  "example_id": 46,
  "message": "Training example added successfully"
}
```

### T5 Training - Update Example

```http
PUT /api/t5/examples/{example_id}
Content-Type: application/json
```

**Request:**
```json
{
  "question": "What is the current temperature in zone 5.04?",
  "sensors": ["Air_Temperature_Sensor_5.04"],
  "sparql": "PREFIX brick: ...",
  "category": "Temperature Query",
  "notes": "Updated with 'current' keyword"
}
```

**Response:**
```json
{
  "status": "success",
  "example_id": 46,
  "message": "Training example updated successfully"
}
```

### T5 Training - Delete Example

```http
DELETE /api/t5/examples/{example_id}
```

**Response:**
```json
{
  "status": "success",
  "example_id": 46,
  "message": "Training example deleted successfully"
}
```

### T5 Training - Train Model

```http
POST /api/t5/train
Content-Type: application/json
```

**Request:**
```json
{
  "epochs": 3,
  "batch_size": 4,
  "learning_rate": 5e-5,
  "output_dir": "checkpoint-3"
}
```

**Response (SSE Stream):**
```
data: {"type": "progress", "epoch": 1, "total_epochs": 3, "loss": 0.245, "percentage": 30}

data: {"type": "progress", "epoch": 2, "total_epochs": 3, "loss": 0.189, "percentage": 60}

data: {"type": "progress", "epoch": 3, "total_epochs": 3, "loss": 0.142, "percentage": 100}

data: {"type": "complete", "message": "Training complete", "output_dir": "checkpoint-3"}
```

### T5 Training - Get Training Status

```http
GET /api/t5/training/status
```

**Response:**
```json
{
  "status": "training",
  "current_epoch": 2,
  "total_epochs": 3,
  "current_loss": 0.189,
  "progress_percentage": 60,
  "estimated_completion": "2025-01-08T14:45:00Z"
}
```

### T5 Training - Deploy Model

```http
POST /api/t5/deploy
Content-Type: application/json
```

**Request:**
```json
{
  "checkpoint": "checkpoint-3"
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Model deployed successfully",
  "checkpoint": "checkpoint-3",
  "deployed_at": "2025-01-08T14:50:00Z"
}
```

## Decider Service

**Base URL**: `http://localhost:6009`

### Health Check

```http
GET /health
```

**Response:**
```json
{
  "status": "ok",
  "service": "decider-service"
}
```

### Decide Analytics Method

```http
POST /decide
Content-Type: application/json
```

**Request:**
```json
{
  "query": "Show me the temperature trend for zone 5.04",
  "intent": "analytics_request",
  "entities": {
    "sensor": "Air_Temperature_Sensor_5.04",
    "analysis_type": "trend"
  }
}
```

**Response:**
```json
{
  "decision": {
    "method": "trend_analysis",
    "parameters": {
      "sensor": "Air_Temperature_Sensor_5.04",
      "start_time": "2025-01-07T14:30:00Z",
      "end_time": "2025-01-08T14:30:00Z",
      "method": "linear_regression"
    },
    "endpoint": "http://localhost:6001/api/analytics/trend",
    "confidence": 0.92
  },
  "alternatives": [
    {
      "method": "moving_average",
      "confidence": 0.78
    }
  ]
}
```

## File Server

**Base URL**: `http://localhost:8080`

### Health Check

```http
GET /health
```

**Response:**
```json
{
  "status": "ok",
  "service": "file-server"
}
```

### List Files

```http
GET /files
```

**Response:**
```json
{
  "files": [
    {
      "name": "20250108-143000.tar.gz",
      "type": "rasa_model",
      "size": 145678901,
      "created_at": "2025-01-08T14:30:00Z",
      "path": "/app/models/20250108-143000.tar.gz"
    }
  ],
  "count": 1
}
```

### Download File

```http
GET /files/{filename}
```

**Response:** Binary file content

### Upload File

```http
POST /upload
Content-Type: multipart/form-data
```

**Request:**
```
------WebKitFormBoundary
Content-Disposition: form-data; name="file"; filename="model.tar.gz"
Content-Type: application/gzip

<binary content>
------WebKitFormBoundary--
```

**Response:**
```json
{
  "status": "success",
  "filename": "model.tar.gz",
  "size": 145678901,
  "path": "/app/models/model.tar.gz"
}
```

### Delete File

```http
DELETE /files/{filename}
```

**Response:**
```json
{
  "status": "success",
  "message": "File deleted successfully",
  "filename": "model.tar.gz"
}
```

### Get Model Info

```http
GET /models/{model_id}
```

**Response:**
```json
{
  "model_id": "20250108-143000",
  "filename": "20250108-143000.tar.gz",
  "size": 145678901,
  "metadata": {
    "trained_at": "2025-01-08T14:30:00Z",
    "training_data": "data/nlu.yml",
    "config": "config.yml",
    "version": "3.6.12"
  }
}
```

## NL2SPARQL Service

**Base URL**: `http://localhost:6005`

### Health Check

```http
GET /health
```

**Response:**
```json
{
  "status": "ok",
  "service": "nl2sparql",
  "model": "t5-base",
  "checkpoint": "checkpoint-3"
}
```

### Translate Natural Language to SPARQL

```http
POST /predict
Content-Type: application/json
```

**Request:**
```json
{
  "question": "What is the temperature in zone 5.04?"
}
```

**Response:**
```json
{
  "question": "What is the temperature in zone 5.04?",
  "sparql": "PREFIX brick: <https://brickschema.org/schema/Brick#>\nSELECT ?value ?timestamp WHERE {\n  <sensor:Air_Temperature_Sensor_5.04> brick:hasValue ?value .\n  <sensor:Air_Temperature_Sensor_5.04> brick:hasTimestamp ?timestamp .\n}",
  "confidence": 0.95,
  "model": "checkpoint-3"
}
```

### Batch Prediction

```http
POST /predict/batch
Content-Type: application/json
```

**Request:**
```json
{
  "questions": [
    "What is the temperature in zone 5.04?",
    "Show me CO2 levels in zone 5.01",
    "What's the humidity in zone 5.15?"
  ]
}
```

**Response:**
```json
{
  "predictions": [
    {
      "question": "What is the temperature in zone 5.04?",
      "sparql": "PREFIX brick: ...",
      "confidence": 0.95
    },
    {
      "question": "Show me CO2 levels in zone 5.01",
      "sparql": "PREFIX brick: ...",
      "confidence": 0.92
    },
    {
      "question": "What's the humidity in zone 5.15?",
      "sparql": "PREFIX brick: ...",
      "confidence": 0.97
    }
  ],
  "count": 3
}
```

## Ollama API

**Base URL**: `http://localhost:11434`

### List Models

```http
GET /api/tags
```

**Response:**
```json
{
  "models": [
    {
      "name": "mistral:latest",
      "modified_at": "2025-01-08T10:00:00Z",
      "size": 4109856401,
      "digest": "sha256:abc123...",
      "details": {
        "format": "gguf",
        "family": "mistral",
        "parameter_size": "7B"
      }
    }
  ]
}
```

### Generate Response

```http
POST /api/generate
Content-Type: application/json
```

**Request:**
```json
{
  "model": "mistral:latest",
  "prompt": "Explain the temperature reading of 22.5°C in a building context",
  "stream": false
}
```

**Response:**
```json
{
  "model": "mistral:latest",
  "created_at": "2025-01-08T14:30:00Z",
  "response": "A temperature of 22.5°C (72.5°F) is within the comfortable range for most indoor environments...",
  "done": true,
  "context": [1234, 5678, ...],
  "total_duration": 1234567890,
  "load_duration": 123456789,
  "prompt_eval_count": 45,
  "eval_count": 89
}
```

### Chat Completion

```http
POST /api/chat
Content-Type: application/json
```

**Request:**
```json
{
  "model": "mistral:latest",
  "messages": [
    {
      "role": "system",
      "content": "You are a building management assistant."
    },
    {
      "role": "user",
      "content": "Is 22.5°C a good temperature for an office?"
    }
  ],
  "stream": false
}
```

**Response:**
```json
{
  "model": "mistral:latest",
  "created_at": "2025-01-08T14:30:00Z",
  "message": {
    "role": "assistant",
    "content": "Yes, 22.5°C is an excellent temperature for an office environment..."
  },
  "done": true
}
```

## Fuseki SPARQL

**Base URL**: `http://localhost:3030`

### Query (GET)

```http
GET /abacws/query?query={encoded_query}
Accept: application/sparql-results+json
```

**Example:**
```http
GET /abacws/query?query=PREFIX%20brick%3A%20%3Chttps%3A%2F%2Fbrickschema.org%2Fschema%2FBrick%23%3E%0ASELECT%20%3Fsensor%20WHERE%20%7B%0A%20%20%3Fsensor%20a%20brick%3ATemperature_Sensor%20.%0A%7D
```

### Query (POST)

```http
POST /abacws/query
Content-Type: application/sparql-query
Accept: application/sparql-results+json
```

**Request:**
```sparql
PREFIX brick: <https://brickschema.org/schema/Brick#>
SELECT ?sensor ?location WHERE {
  ?sensor a brick:Temperature_Sensor .
  ?sensor brick:hasLocation ?location .
}
```

**Response:**
```json
{
  "head": {
    "vars": ["sensor", "location"]
  },
  "results": {
    "bindings": [
      {
        "sensor": {
          "type": "uri",
          "value": "http://example.org/sensor/Air_Temperature_Sensor_5.04"
        },
        "location": {
          "type": "uri",
          "value": "http://example.org/location/zone_5.04"
        }
      }
    ]
  }
}
```

### Update

```http
POST /abacws/update
Content-Type: application/sparql-update
```

**Request:**
```sparql
PREFIX brick: <https://brickschema.org/schema/Brick#>
INSERT DATA {
  <sensor:New_Sensor_5.35> a brick:Temperature_Sensor .
  <sensor:New_Sensor_5.35> brick:hasLocation <zone:5.35> .
}
```

**Response:** 204 No Content (success)

## Error Handling

### Standard Error Response

```json
{
  "error": {
    "code": "INVALID_REQUEST",
    "message": "Invalid sensor name provided",
    "details": {
      "field": "sensor",
      "received": "Invalid_Sensor",
      "expected": "Valid sensor from sensor_list.txt"
    },
    "timestamp": "2025-01-08T14:30:00Z",
    "request_id": "req_abc123"
  }
}
```

### Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `INVALID_REQUEST` | 400 | Malformed request or invalid parameters |
| `UNAUTHORIZED` | 401 | Authentication required |
| `FORBIDDEN` | 403 | Insufficient permissions |
| `NOT_FOUND` | 404 | Resource not found |
| `METHOD_NOT_ALLOWED` | 405 | HTTP method not supported |
| `CONFLICT` | 409 | Resource conflict (e.g., duplicate) |
| `UNPROCESSABLE_ENTITY` | 422 | Valid syntax but semantic error |
| `RATE_LIMIT_EXCEEDED` | 429 | Too many requests |
| `INTERNAL_ERROR` | 500 | Server-side error |
| `SERVICE_UNAVAILABLE` | 503 | Service temporarily unavailable |
| `GATEWAY_TIMEOUT` | 504 | Upstream service timeout |

### Example Errors

**Invalid Sensor:**
```json
{
  "error": {
    "code": "NOT_FOUND",
    "message": "Sensor 'Invalid_Sensor' not found",
    "details": {
      "sensor": "Invalid_Sensor",
      "available_count": 680
    }
  }
}
```

**Missing Parameter:**
```json
{
  "error": {
    "code": "INVALID_REQUEST",
    "message": "Missing required parameter: sensor",
    "details": {
      "missing_fields": ["sensor"]
    }
  }
}
```

**Service Unavailable:**
```json
{
  "error": {
    "code": "SERVICE_UNAVAILABLE",
    "message": "Analytics service is temporarily unavailable",
    "details": {
      "service": "analytics-microservices",
      "retry_after": 30
    }
  }
}
```

## Rate Limiting

### Future Implementation

**Headers:**
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1704723600
```

**Limits (Planned):**
- Anonymous: 60 requests/minute
- Authenticated: 1000 requests/minute
- Admin: Unlimited

**Rate Limit Response:**
```json
{
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Rate limit exceeded. Try again in 45 seconds.",
    "details": {
      "limit": 60,
      "remaining": 0,
      "reset_at": "2025-01-08T14:31:00Z"
    }
  }
}
```

## Webhooks

### Rasa Webhook Events

Subscribe to conversation events:

```http
POST /webhooks/callback
Content-Type: application/json
```

**Event: Message Received**
```json
{
  "event": "user_message",
  "sender_id": "user123",
  "message": "What is the temperature?",
  "timestamp": "2025-01-08T14:30:00Z"
}
```

**Event: Bot Response**
```json
{
  "event": "bot_response",
  "sender_id": "user123",
  "response": "The current temperature is 22.5°C",
  "timestamp": "2025-01-08T14:30:05Z"
}
```

**Event: Action Executed**
```json
{
  "event": "action_executed",
  "action_name": "action_query_sensor",
  "sender_id": "user123",
  "success": true,
  "duration_ms": 234,
  "timestamp": "2025-01-08T14:30:03Z"
}
```

## SDK Examples

### Python SDK

```python
import requests

class OntoBot:
    def __init__(self, base_url="http://localhost:5005"):
        self.base_url = base_url
        self.session = requests.Session()
    
    def send_message(self, user_id, message):
        """Send a message to the chatbot"""
        response = self.session.post(
            f"{self.base_url}/webhooks/rest/webhook",
            json={"sender": user_id, "message": message}
        )
        return response.json()
    
    def get_analytics(self, sensor, analysis_type="statistics"):
        """Get analytics for a sensor"""
        response = self.session.post(
            "http://localhost:6001/api/analytics/statistics",
            json={"sensor": sensor}
        )
        return response.json()
    
    def translate_query(self, question):
        """Translate natural language to SPARQL"""
        response = self.session.post(
            "http://localhost:6005/predict",
            json={"question": question}
        )
        return response.json()

# Usage
bot = OntoBot()
response = bot.send_message("user123", "What is the temperature?")
print(response)
```

### JavaScript/Node.js SDK

```javascript
class OntoBot {
  constructor(baseUrl = 'http://localhost:5005') {
    this.baseUrl = baseUrl;
  }
  
  async sendMessage(userId, message) {
    const response = await fetch(`${this.baseUrl}/webhooks/rest/webhook`, {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({sender: userId, message})
    });
    return response.json();
  }
  
  async getAnalytics(sensor, analysisType = 'statistics') {
    const response = await fetch('http://localhost:6001/api/analytics/statistics', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({sensor})
    });
    return response.json();
  }
  
  async translateQuery(question) {
    const response = await fetch('http://localhost:6005/predict', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({question})
    });
    return response.json();
  }
}

// Usage
const bot = new OntoBot();
const response = await bot.sendMessage('user123', 'What is the temperature?');
console.log(response);
```

### cURL Examples

**Send Message:**
```bash
curl -X POST http://localhost:5005/webhooks/rest/webhook \
  -H "Content-Type: application/json" \
  -d '{"sender":"user123","message":"What is the temperature?"}'
```

**Get Analytics:**
```bash
curl -X POST http://localhost:6001/api/analytics/statistics \
  -H "Content-Type: application/json" \
  -d '{"sensor":"Air_Temperature_Sensor_5.04","metrics":["mean","std"]}'
```

**Translate Query:**
```bash
curl -X POST http://localhost:6005/predict \
  -H "Content-Type: application/json" \
  -d '{"question":"What is the temperature in zone 5.04?"}'
```

**SPARQL Query:**
```bash
curl -X POST http://localhost:3030/abacws/query \
  -H "Content-Type: application/sparql-query" \
  -H "Accept: application/sparql-results+json" \
  -d 'PREFIX brick: <https://brickschema.org/schema/Brick#>
SELECT ?sensor WHERE { ?sensor a brick:Temperature_Sensor . }'
```

## Postman Collection

Download the complete API collection:
- [OntoBot.postman_collection.json](../postman/OntoBot.postman_collection.json)

Import into Postman for easy testing and exploration.

## Next Steps

- [Frontend UI Guide](./frontend_ui.md)
- [Backend Services Documentation](./backend_services.md)
- [T5 Training Guide](./t5_training_guide.md)
- [Multi-Building Guide](./multi_building.md)
- [Quick Start Guide](./quickstart.md)
