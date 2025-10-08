---
layout: post
title: Quick Start Guide
date: 2025-10-08
---

# Quick Start Guide

Get OntoBot up and running in 30 minutes. This guide covers prerequisites, installation, and your first conversation with the chatbot.

## Prerequisites

### Required Software

| Software | Version | Purpose | Download |
|----------|---------|---------|----------|
| **Docker Desktop** | 20.10+ | Container runtime | [docker.com](https://www.docker.com/products/docker-desktop) |
| **Docker Compose** | 2.0+ | Multi-container orchestration | Included with Docker Desktop |
| **Git** | 2.30+ | Version control | [git-scm.com](https://git-scm.com/) |
| **Node.js** | 16+ | Frontend development (optional) | [nodejs.org](https://nodejs.org/) |
| **Python** | 3.8+ | Scripts & notebooks (optional) | [python.org](https://www.python.org/) |

### System Requirements

**Minimum:**
- CPU: 4 cores
- RAM: 8 GB
- Disk: 20 GB free space
- OS: Windows 10/11, macOS 11+, Ubuntu 20.04+

**Recommended:**
- CPU: 8 cores
- RAM: 16 GB
- Disk: 50 GB SSD
- OS: Windows 11, macOS 13+, Ubuntu 22.04+

### Docker Configuration

**Memory Allocation:**
```
Docker Desktop → Settings → Resources → Memory: 8 GB minimum
```

**File Sharing (Windows):**
```
Docker Desktop → Settings → Resources → File Sharing
Add: C:\Users\<username>\Documents\GitHub\OntoBot
```

**WSL2 Backend (Windows - Recommended):**
```
Docker Desktop → Settings → General → Use WSL 2 based engine: ✓
```

## Installation

### Step 1: Clone Repository

```bash
# Clone with submodules
git clone --recursive https://github.com/suhasdevmane/OntoBot.git

# Or if already cloned
cd OntoBot
git submodule update --init --recursive
```

**Repository Structure:**
```
OntoBot/
├── docker-compose.bldg1.yml    # Building 1 (ABACWS)
├── docker-compose.bldg2.yml    # Building 2 (Office)
├── docker-compose.bldg3.yml    # Building 3 (Data Center)
├── docker-compose.extras.yml   # AI services (optional)
├── rasa-bldg1/                 # Rasa project for Building 1
├── rasa-bldg2/                 # Rasa project for Building 2
├── rasa-bldg3/                 # Rasa project for Building 3
├── rasa-frontend/              # React UI
├── microservices/              # Analytics API
├── Transformers/               # T5 NL2SPARQL models
└── README.md
```

### Step 2: Choose a Building

For your first run, start with **Building 1 (ABACWS)** - it has real-world data and is the most validated.

```powershell
# Windows PowerShell
cd OntoBot

# Linux/macOS
cd OntoBot
```

### Step 3: Start Services

**Option A: Basic Stack (Fastest)**

Starts Rasa chatbot + database only:

```bash
# Windows PowerShell
docker-compose -f docker-compose.bldg1.yml up -d rasa_bldg1 action_server_bldg1 mysqlserver

# Linux/macOS
docker-compose -f docker-compose.bldg1.yml up -d rasa_bldg1 action_server_bldg1 mysqlserver
```

**Option B: Full Stack (Recommended)**

Includes analytics, frontend, and all features:

```bash
docker-compose -f docker-compose.bldg1.yml up -d
```

**Option C: With AI Services**

Adds NL2SPARQL and Mistral LLM:

```bash
docker-compose -f docker-compose.bldg1.yml -f docker-compose.extras.yml up -d
```

### Step 4: Wait for Services

Services take **2-3 minutes** to fully initialize:

```powershell
# Check status
docker ps

# Expected output:
# CONTAINER ID   IMAGE                    STATUS         PORTS
# abc123...      rasa_bldg1              Up 2 minutes   0.0.0.0:5005->5005/tcp
# def456...      action_server_bldg1     Up 2 minutes   0.0.0.0:5055->5055/tcp
# ghi789...      mysql:8.0               Up 2 minutes   0.0.0.0:3307->3306/tcp
# jkl012...      rasa_frontend           Up 2 minutes   0.0.0.0:3000->3000/tcp
```

**Health Check:**

```bash
# Windows
curl http://localhost:5005/version

# Linux/macOS
curl http://localhost:5005/version

# Expected: {"version": "3.6.12", "minimum_compatible_version": "3.0.0"}
```

### Step 5: Access the UI

Open your browser to: **http://localhost:3000**

You should see:

![OntoBot Home Dashboard](../images/home-dashboard.png)

**Service Cards:**
- 🤖 **Rasa Core**: Green (Ready)
- ⚙️ **Action Server**: Green (Ready)
- 🔌 **Analytics**: Green (Ready)
- 📊 **Decider**: Green (Ready)

## Your First Conversation

### Chat Interface

1. Click **"Chat"** in the top navigation
2. You'll see the chat interface with example questions
3. Try a simple query:

```
What is the temperature in zone 5.04?
```

**Expected Response:**
```
The current temperature in zone 5.04 is 22.5°C (measured at 2025-01-08 14:30:00).
```

### Example Questions

**Simple Queries:**
```
What is the CO2 level in zone 5.01?
Show me the humidity in zone 5.15
What's the air quality in zone 5.20?
```

**Time-Based Queries:**
```
What was the average temperature yesterday?
Show me CO2 levels for the last 3 hours
What's the peak humidity today?
```

**Comparative Queries:**
```
Which zone has the highest temperature?
Compare CO2 levels between zone 5.01 and 5.10
What's the correlation between temperature and humidity?
```

**Analytics Queries:**
```
Show me temperature trends for zone 5.04
Detect anomalies in CO2 levels
Predict the temperature for the next hour
```

### Understanding Responses

**Successful Query:**
```json
{
  "response": "The current temperature is 22.5°C",
  "data": {
    "sensor": "Air_Temperature_Sensor_5.04",
    "value": 22.5,
    "unit": "°C",
    "timestamp": "2025-01-08 14:30:00"
  },
  "visualization": "chart_url"
}
```

**Analytics Query:**
```json
{
  "response": "Here's the temperature trend analysis:",
  "analytics_result": {
    "mean": 22.3,
    "std_dev": 0.8,
    "trend": "increasing",
    "anomalies": []
  },
  "chart": "base64_encoded_image"
}
```

## Configuration

### Settings Page

Navigate to: **http://localhost:3000/settings**

#### Step 1: Select Building

The UI auto-detects the active building:
- **Building 1**: 680 sensors (ABACWS)
- **Building 2**: 329 sensors (Office)
- **Building 3**: 597 sensors (Data Center)

No configuration needed - it just works!

#### Step 2: Configure Endpoints

Default endpoints (usually don't need changes):

```yaml
Rasa Core: http://localhost:5005
Action Server: http://localhost:5055
Analytics: http://localhost:6001
Decider: http://localhost:6009
File Server: http://localhost:8080
NL2SPARQL: http://localhost:6005
Ollama: http://localhost:11434
Fuseki: http://localhost:3030
```

#### Step 3: Test Connectivity

Click **"Test All Endpoints"** button:

✅ All green = Ready to go  
❌ Red indicators = Check Docker containers

### Building Selection

To switch buildings:

```powershell
# Stop current building
docker-compose -f docker-compose.bldg1.yml down

# Start different building
docker-compose -f docker-compose.bldg2.yml up -d

# Wait for startup
Start-Sleep -Seconds 120

# Refresh browser
# Frontend auto-detects new building
```

## Training Your First Model

### T5 Model Training Tab

1. Navigate to **Settings** → **T5 Model Training** tab
2. Click **"Add New Training Example"**

### Add Training Example

**Form Fields:**

```yaml
Question: "What is the temperature in zone 5.04?"
Sensors: Air_Temperature_Sensor_5.04
SPARQL Query: |
  PREFIX brick: <https://brickschema.org/schema/Brick#>
  SELECT ?value ?timestamp WHERE {
    <sensor:Air_Temperature_Sensor_5.04> brick:hasValue ?value .
    <sensor:Air_Temperature_Sensor_5.04> brick:hasTimestamp ?timestamp .
  }
Category: Temperature Query
Notes: Basic temperature retrieval for single zone
```

**Click "Add Example"**

### Train Model

1. Set **Training Epochs**: 3 (default)
2. Click **"Train Model"** button
3. Monitor progress in real-time:

```
Epoch 1/3 - Loss: 0.245 (30%)
Epoch 2/3 - Loss: 0.189 (60%)
Epoch 3/3 - Loss: 0.142 (100%)
✓ Training complete!
```

### Start & Verify

1. **Start Service**: Click "Start NL2SPARQL Service"
   - Status changes to: 🟢 Running
   
2. **Verify**: Click "Test NL2SPARQL"
   - Test query gets translated
   - Response shows SPARQL output

**Congratulations!** Your model is trained and ready.

## Exploring Features

### Analytics

Query types available:

**Statistical Analysis:**
```
Show me the average temperature for the last week
What's the standard deviation of CO2 levels?
Calculate the correlation between temperature and humidity
```

**Trend Detection:**
```
Show me temperature trends for zone 5.04
Is the CO2 level increasing or decreasing?
What's the pattern in humidity over time?
```

**Anomaly Detection:**
```
Detect unusual temperature readings
Find CO2 spikes in the last 24 hours
Are there any anomalies in air quality?
```

**Forecasting:**
```
Predict the temperature for the next 2 hours
Forecast CO2 levels for tomorrow
What will the humidity be this evening?
```

### Data Visualization

Charts are automatically generated:

- **Line Charts**: Time-series data
- **Bar Charts**: Comparisons
- **Scatter Plots**: Correlations
- **Heatmaps**: Multi-sensor patterns

**View Options:**
- Zoom in/out
- Pan left/right
- Download as PNG
- View data table

### Health Monitoring

Monitor service health at: **http://localhost:3000/health**

**Metrics:**
- Request count
- Success rate
- Average response time
- Error rate
- Service uptime

**Alerts:**
- High error rate (>5%)
- Slow responses (>2s)
- Service down

## Common Issues & Solutions

### Issue 1: Containers Won't Start

**Symptom:**
```
Error response from daemon: Conflict. The container name "/rasa_bldg1" is already in use
```

**Solution:**
```powershell
# Stop all containers
docker-compose -f docker-compose.bldg1.yml down

# Remove orphaned containers
docker rm -f $(docker ps -aq)

# Start fresh
docker-compose -f docker-compose.bldg1.yml up -d
```

### Issue 2: Port Already in Use

**Symptom:**
```
Error: bind: address already in use (port 5005)
```

**Solution:**
```powershell
# Windows - Find process using port
netstat -ano | findstr :5005
taskkill /PID <process_id> /F

# Linux/macOS
lsof -ti:5005 | xargs kill -9

# Or change port in docker-compose.yml
ports:
  - "5006:5005"  # Use 5006 instead
```

### Issue 3: Services Unhealthy

**Symptom:**
```
Container status: unhealthy (health check failed)
```

**Solution:**
```bash
# Check logs
docker logs rasa_bldg1

# Common causes:
# 1. Database not ready → Wait longer
# 2. Missing files → Check volumes
# 3. Memory exhausted → Increase Docker memory

# Restart specific service
docker-compose -f docker-compose.bldg1.yml restart rasa_bldg1
```

### Issue 4: No Sensors in Dropdown

**Symptom:** T5 Training GUI shows "No options" for sensors

**Solution:**
```bash
# Verify microservices port (should be 6001, not 6000)
curl http://localhost:6001/api/t5/sensors

# Expected: {"sensors": [...], "count": 680}

# If port 6000: Chrome blocks it (ERR_UNSAFE_PORT)
# See T5_TRAINING_PORT_FIX.md for fix
```

### Issue 5: Frontend Won't Load

**Symptom:** Browser shows "Connection refused" at localhost:3000

**Solution:**
```bash
# Check if container is running
docker ps | grep rasa_frontend

# If not running, check logs
docker logs rasa_frontend

# Common causes:
# 1. npm install failed → Rebuild image
# 2. Port 3000 in use → Change to 3001
# 3. Missing dependencies → Check package.json

# Rebuild
docker-compose -f docker-compose.bldg1.yml up -d --build rasa_frontend
```

### Issue 6: Slow Responses

**Symptom:** Queries take 10+ seconds to respond

**Possible Causes:**
1. **Analytics computation heavy**
   - Use simpler queries first
   - Reduce time range
   
2. **Database slow**
   - Check database container health
   - Verify data loaded correctly
   
3. **Insufficient resources**
   - Increase Docker memory to 16 GB
   - Close other applications

**Solution:**
```bash
# Monitor resource usage
docker stats

# If memory exhausted:
# Docker Desktop → Settings → Resources → Memory: 16 GB
```

## Next Steps

### Learn More

1. **[Frontend UI Guide](./frontend_ui.md)** - Complete UI reference
2. **[T5 Training Guide](./t5_training_guide.md)** - Advanced model training
3. **[Backend Services](./backend_services.md)** - Technical deep dive
4. **[Multi-Building Guide](./multi_building.md)** - Working with different buildings
5. **[API Reference](./api_reference.md)** - REST API documentation

### Advanced Topics

**Add Custom Analytics:**
```python
# microservices/blueprints/custom_analytics.py
@app.route('/api/analytics/custom', methods=['POST'])
def custom_analysis():
    # Your analytics code here
    pass
```

**Extend Rasa Actions:**
```python
# rasa-bldg1/actions/actions.py
class ActionCustomQuery(Action):
    def name(self):
        return "action_custom_query"
    
    def run(self, dispatcher, tracker, domain):
        # Your custom logic
        pass
```

**Add Training Examples:**
```json
// Transformers/t5_base/training/bldg1/correlation_fixes.json
{
  "question": "Your new question",
  "sensors": ["Sensor_Name"],
  "sparql": "Your SPARQL query",
  "category": "Custom Category"
}
```

### Community & Support

- **GitHub Issues**: [github.com/suhasdevmane/OntoBot/issues](https://github.com/suhasdevmane/OntoBot/issues)
- **Documentation**: [suhasdevmane.github.io](https://suhasdevmane.github.io)
- **Email**: devmanesp1@cardiff.ac.uk

### Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## Cheat Sheet

### Essential Commands

```powershell
# Start Building 1
docker-compose -f docker-compose.bldg1.yml up -d

# Stop all services
docker-compose -f docker-compose.bldg1.yml down

# View logs
docker logs -f rasa_bldg1

# Restart service
docker-compose -f docker-compose.bldg1.yml restart rasa_bldg1

# Check health
curl http://localhost:5005/version

# List containers
docker ps

# Clean up
docker system prune -f
```

### Key URLs

| Service | URL |
|---------|-----|
| Frontend | http://localhost:3000 |
| Chat | http://localhost:3000/chat |
| Settings | http://localhost:3000/settings |
| Health | http://localhost:3000/health |
| Rasa Core | http://localhost:5005 |
| Analytics | http://localhost:6001 |
| File Server | http://localhost:8080 |
| Fuseki | http://localhost:3030 |
| ThingsBoard | http://localhost:8082 |

### Quick Tests

```bash
# Test Rasa
curl -X POST http://localhost:5005/webhooks/rest/webhook \
  -H "Content-Type: application/json" \
  -d '{"sender":"test","message":"hello"}'

# Test Analytics
curl http://localhost:6001/health

# Test NL2SPARQL
curl -X POST http://localhost:6005/predict \
  -H "Content-Type: application/json" \
  -d '{"question":"What is the temperature?"}'

# Test Sensors API
curl http://localhost:6001/api/t5/sensors
```

## Summary

You now have OntoBot running with:
- ✅ Docker containers deployed
- ✅ Rasa chatbot responding
- ✅ Frontend UI accessible
- ✅ Analytics working
- ✅ First model trained

**Total Setup Time:** ~30 minutes

**Next:** Explore the [Frontend UI](./frontend_ui.md) and try advanced queries!
