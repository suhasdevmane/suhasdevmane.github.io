---
layout: post
title: Frontend User Interface
date: 2025-10-08
---

# Frontend User Interface

The OntoBot frontend is a React-based web application that provides an intuitive interface for interacting with your smart building. It runs on **port 3000** and serves as the main entry point for users.

## Overview

The frontend consists of several key pages:
- **Home Dashboard**: Service overview and quick access
- **Chat Interface**: Conversational interaction with the building
- **Settings**: Model training and Rasa configuration
- **Health Monitoring**: Service status checks
- **Editor**: Rasa project file editor

## Home Dashboard

Access: `http://localhost:3000`

### Features

The home dashboard provides a visual overview of all available services with quick-launch buttons:

#### Data & Semantics
- **Jena Fuseki Server** (port 3030): Semantic Web Framework for SPARQL queries
- **GraphDB** (port 7200): Graph database management system

#### IoT Platform & Database Tools
- **ThingsBoard Server** (port 8082): IoT platform for device management
- **pgAdmin** (port 5050/5051): PostgreSQL administration interface
- **Adminer** (port 8282): Lightweight database management tool
- **MySQL Server** (port 3307): Legacy telemetry database

#### Microservices & APIs
- **Microservices** (port 6001): Analytics and utility services
- **File Server** (port 8080): Shared artifacts server for models and results
- **3D API** (port 8091): API for 3D visualization services
- **Visualiser** (port 8090): 3D building visualization

#### Conversational Stack
- **Rasa Server** (port 5005): Conversational AI engine
- **Rasa Editor** (port 6080): Project file editor and configuration
- **Duckling Server** (port 8000): Entity extraction for dates, times, and numbers

#### AI & ML Services
- **NL2SPARQL Service** (port 6005): T5-based natural language to SPARQL translator
- **Ollama (Mistral)** (port 11434): Local LLM for summarization
- **Jupyter Lab** (port 8888): Interactive notebook environment

### Usage

Click any service card to open it in a new browser tab. Services show their current status and purpose.

## Chat Interface

Access: `http://localhost:3000/chat` or click "Open Chatbot" from the home page

### Features

#### Conversation Panel
- **Message Input**: Type natural language questions about your building
- **Response Display**: View formatted responses with:
  - Text answers with UK-oriented units
  - Interactive charts and visualizations
  - Data tables
  - Downloadable artifacts

#### Example Questions
```
What is the CO2 level in zone 5.04?
Show me the temperature trend for room 2.11 today
Are there any anomalies in the HVAC system?
What sensors are in the building?
Compare humidity between zones 5.01 and 5.02
```

#### Response Types

**1. Direct Answers**
- Latest sensor values
- Sensor locations and metadata
- Equipment status

**2. Analytics Results**
- Time-series charts
- Statistical summaries (min, max, average)
- Trend analysis
- Anomaly detection

**3. Downloadable Artifacts**
- CSV data exports
- JSON analysis results
- Chart images

### Chat Features

- **Message History**: Scroll through previous conversations
- **Copy Response**: Copy answers to clipboard
- **Export Chat**: Download conversation history
- **Clear Chat**: Reset conversation

## Settings Page

Access: `http://localhost:3000/settings`

The Settings page is the command center for training and managing your Rasa models. It provides a 3-step workflow with real-time progress monitoring.

### Tabs

#### 1. Model Training (Main Tab)

**Step-by-Step Workflow:**

**Step 1: Train Model**
- Click **"Train"** button to start training job
- Real-time logs stream in the console below
- Progress indicators show training status:
  - `idle`: Ready to train
  - `starting`: Initializing training
  - `preparing_data`: Loading training data
  - `training_core`: Training dialogue model
  - `training_nlu`: Training NLU model
  - `packaging`: Creating model archive
  - `done`: Training complete ✓
  - `error`: Training failed

**Step 2: Start Rasa Server**
- After training, click **"Start Rasa"** to launch the Rasa server
- Monitor startup logs in real-time
- Status indicators:
  - `starting`: Server initializing
  - `healthy`: Server ready ✓

**Step 3: Verification**
- Once both training and startup are complete, the green checkmark confirms the model is active
- Chat interface is now ready to use

**Log Management:**
- **Append Mode** (default): New logs are added to existing ones
- **Replace Mode**: Each status check replaces the log window
- Toggle with the "Append" checkbox
- Auto-scrolling keeps latest logs visible

#### 2. Model Management

**Available Models List**
Shows all trained models with:
- Model name (e.g., `20250108-123045-ancient-dust.tar.gz`)
- Creation timestamp
- File size in MB
- Active status (✓ if currently loaded)

**Model Actions:**
- **Activate**: Load and restart Rasa with selected model
  - Takes ~5 minutes (300 seconds)
  - Countdown timer shows estimated time remaining
  - Automatically restarts Rasa server

- **Delete**: Remove unused models
  - Confirmation required
  - Cannot delete currently active model
  - Frees up disk space

**Refresh Models**
Click "Refresh" to reload the models list from the server.

#### 3. T5 Model Training Tab

**⭐ NEW FEATURE**: GUI for training the T5 NL2SPARQL model

Access: Settings → T5 Model Training

See detailed documentation in [T5 Model Training Guide](./t5_training_guide.md)

**Quick Overview:**
- Add training examples (question + SPARQL + sensors)
- Train T5 model incrementally
- Monitor training progress with real-time updates
- Deploy trained models to production
- Test translations with the T5 playground

### Log Console

The compact log window at the bottom shows real-time output from:
- Training jobs (Rasa model training)
- Server startup
- Model activation
- Error messages

**Features:**
- **Auto-scroll**: Automatically scrolls to latest entry
- **Copy All**: Copy entire log to clipboard
- **Clear**: Reset log window
- **Append/Replace Toggle**: Choose log accumulation behavior

### Progress Indicators

Visual feedback throughout the workflow:

**Training Badge:**
- 🔵 `idle`: Ready to start
- 🟡 `starting`, `preparing_data`, `training_core`, `training_nlu`, `packaging`: In progress
- 🟢 `done`: Completed successfully
- 🔴 `error`: Failed (check logs)

**Start Badge:**
- 🔵 `idle`: Not started
- 🟡 `starting`: Server initializing
- 🟢 `healthy`: Running and ready
- 🔴 `error`: Failed to start

## Health Monitoring

Access: `http://localhost:3000/health`

### Features

Monitor the health status of all OntoBot services:

**Service Categories:**
- Data & Semantics (Fuseki, GraphDB)
- IoT Platform (ThingsBoard, pgAdmin)
- Microservices (Analytics, File Server, NL2SPARQL)
- Conversational Stack (Rasa, Duckling)
- AI Services (Ollama, Jupyter)

**Status Indicators:**
- ✅ **Healthy**: Service responding
- ⚠️ **Warning**: Slow response
- ❌ **Error**: Service unreachable
- ⏳ **Checking**: Status pending

**Health Check Actions:**
- **Check All**: Test all services simultaneously
- **Individual Check**: Test specific service
- **Auto-refresh**: Toggle automatic status updates
- **Open Service**: Direct link to service URL

### Health Endpoint Details

Each service's health check uses its specific endpoint:
- `/health`: Standard health endpoint (most services)
- `/$/ping`: Jena Fuseki
- `/version`: Rasa
- `/`: Homepage check (ThingsBoard, pgAdmin, etc.)

## Editor Interface

Access: `http://localhost:3000/editor` or via Rasa Editor service

### Features

Integrated editor for modifying Rasa project files:

**File Management:**
- Browse project structure
- Create new files
- Delete existing files
- Organize into folders

**Code Editor:**
- Syntax highlighting for:
  - YAML (domain, config, rules, stories)
  - Python (actions)
  - Markdown (documentation)
- Line numbers
- Auto-indentation
- Search and replace

**Supported File Types:**
- `domain.yml`: Intents, entities, responses, forms
- `config.yml`: Pipeline configuration
- `nlu.yml`: Training examples
- `rules.yml`: Conversation rules
- `stories.yml`: Dialogue flows
- `actions.py`: Custom action code

**Safety Features:**
- Automatic backup before saving
- Syntax validation
- Confirmation for destructive actions

## Responsive Design

The frontend is fully responsive and works on:
- Desktop browsers (recommended)
- Tablets
- Mobile devices (limited features)

**Optimal Experience:**
- Screen resolution: 1920x1080 or higher
- Browser: Chrome, Firefox, Edge (latest versions)
- JavaScript: Required
- Cookies: Required for authentication

## Keyboard Shortcuts

### Chat Interface
- `Enter`: Send message
- `Shift+Enter`: New line in message
- `Ctrl+K`: Clear chat
- `Ctrl+C`: Copy last response

### Settings Page
- `Ctrl+T`: Start training
- `Ctrl+R`: Refresh models
- `Ctrl+L`: Clear logs

### Editor
- `Ctrl+S`: Save file
- `Ctrl+F`: Find
- `Ctrl+H`: Find and replace
- `Ctrl+Z`: Undo
- `Ctrl+Y`: Redo

## Troubleshooting

### Common Issues

**1. "Cannot connect to backend"**
- Verify all services are running: `docker ps`
- Check port 6001 (microservices) is accessible
- Clear browser cache and reload

**2. "Model training stuck"**
- Check logs for error messages
- Ensure sufficient disk space (>2GB)
- Verify Rasa container has enough memory (>4GB)

**3. "Sensor dropdown empty"**
- Port 6001 must be accessible (not port 6000)
- Chrome blocks port 6000 as unsafe
- Restart microservices container

**4. "Chat not responding"**
- Verify Rasa server is healthy (Step 3 checkbox)
- Check Rasa logs in Settings
- Ensure model is trained and activated

### Browser Console

For debugging, open browser console:
- Chrome/Edge: `F12` or `Ctrl+Shift+I`
- Firefox: `F12` or `Ctrl+Shift+K`

Look for:
- Network errors (red in Network tab)
- JavaScript errors (red in Console tab)
- Failed API calls (check URL and response)

## Advanced Configuration

### Environment Variables

### Environment and CORS (.env)

When running with Docker Compose, the frontend and backend coordinate CORS and cookies using values from the repository's `.env` file.

1) Create your local `.env` from the template

```powershell
Copy-Item -Path .env.example -Destination .env
# Edit .env and replace placeholder values with your local credentials
```

2) Set frontend-related variables in `.env`

- FRONTEND_ORIGIN=http://localhost:3000
- ALLOWED_ORIGINS=http://localhost:3000
- JWT_SECRET=change_me_in_prod

Notes
- FRONTEND_ORIGIN and ALLOWED_ORIGINS are used by the File Server and Rasa Editor to allow cross-origin requests from the UI.
- Keep both values aligned with the actual UI URL (default http://localhost:3000). If you change the UI port, update both.
- JWT_SECRET secures session cookies sent by the File Server. Use a strong value in non-dev environments.

3) Validate your compose configuration (optional but recommended)

```powershell
docker compose --env-file .env -f docker-compose.bldg1.yml config
# Or validate the stack you plan to run, e.g. bldg2/bldg3 with extras overlay
# docker compose --env-file .env -f docker-compose.bldg2.yml config
# docker compose --env-file .env -f docker-compose.bldg3.yml -f docker-compose.extras.yml config
```

If you see warnings like "The \"PG_THINGSBOARD_DB\" variable is not set.", add the missing variable to `.env` and re-run the command.

4) Start the stack

```powershell
docker compose --env-file .env -f docker-compose.bldg1.yml up -d --build
```

### React app environment (advanced)

Configure frontend behavior via environment variables:

```bash
# React app environment
REACT_APP_RASA_URL=http://localhost:5005
REACT_APP_FILE_SERVER_URL=http://localhost:8080
REACT_APP_MICROSERVICES_URL=http://localhost:6001
REACT_APP_EDITOR_URL=http://localhost:6080
```

### Custom Styling

Override default styles in `src/custom.css`:

```css
/* Example: Change primary color */
:root {
  --primary-color: #007bff;
  --secondary-color: #6c757d;
}
```

### API Integration

Frontend connects to multiple backend services:

| Service | Port | Purpose |
|---------|------|---------|
| Rasa | 5005 | Conversational AI |
| File Server | 8080 | Artifacts & training |
| Microservices | 6001 | Analytics & sensors |
| Editor | 6080 | File management |

All API calls use:
- **Credentials**: `include` (cookies)
- **Content-Type**: `application/json`
- **CORS**: Enabled on all services

## Next Steps

- [Backend Services Documentation](./backend_services.md)
- [Multi-Building Guide](./multi_building.md)
- [T5 Training Guide](./t5_training_guide.md)
- [API Reference](./api_reference.md)
