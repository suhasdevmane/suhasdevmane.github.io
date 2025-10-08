---
layout: post
title: Troubleshooting & FAQ
date: 2025-10-08
categories: support
---

# Troubleshooting & FAQ

Comprehensive troubleshooting guide for OntoBot covering common issues across all buildings and services.

## Table of Contents

- [Docker & Compose Issues](#docker--compose-issues)
- [Database Problems](#database-problems)
- [Service Health Issues](#service-health-issues)
- [Building-Specific Issues](#building-specific-issues)
- [Performance Problems](#performance-problems)
- [Development Issues](#development-issues)
- [FAQ](#faq)

---

## Docker & Compose Issues

### Problem: Containers fail to start

**Symptoms:**
- `docker-compose up` exits with errors
- Services show "Exited (1)" status
- Port binding errors

**Solutions:**

```powershell
# Check Docker is running
docker --version
docker ps

# Check port conflicts
netstat -ano | findstr "5005"  # Windows
lsof -i :5005                   # Mac/Linux

# Stop conflicting services
docker-compose down
docker-compose -f docker-compose.bldg1.yml down
docker-compose -f docker-compose.bldg2.yml down
docker-compose -f docker-compose.bldg3.yml down

# Clean up and restart
docker system prune -f
docker-compose -f docker-compose.bldg1.yml up --build
```

### Problem: Out of memory errors

**Symptoms:**
- Services crash randomly
- "Cannot allocate memory" errors
- Slow performance

**Solutions:**

```
Docker Desktop → Settings → Resources
- Memory: Increase to 8GB minimum (16GB recommended)
- CPUs: Allocate 4+ cores
- Disk: Ensure 50GB+ free space
```

### Problem: Volume mount issues (Windows)

**Symptoms:**
- Files not updating in containers
- Permission denied errors
- Empty volumes

**Solutions:**

```powershell
# Enable file sharing
Docker Desktop → Settings → Resources → File Sharing
Add: C:\Users\<username>\Documents\GitHub\OntoBot

# Reset Docker
Docker Desktop → Troubleshoot → Reset to factory defaults

# Use WSL2 backend (recommended)
Docker Desktop → Settings → General → Use WSL2 based engine
```

### Problem: Network connectivity between containers

**Symptoms:**
- Services can't reach each other
- Connection refused errors
- DNS resolution failures

**Solutions:**

```yaml
# Ensure all services use same network
networks:
  ontobot_network:
    driver: bridge

# Use service names (not localhost) in URLs
ANALYTICS_URL: http://microservices:6000  # ✅ Correct
ANALYTICS_URL: http://localhost:6001      # ❌ Wrong
```

---

## Database Problems

### MySQL (Building 1)

**Problem: MySQL container fails to start**

```powershell
# Check logs
docker-compose -f docker-compose.bldg1.yml logs mysqlserver

# Common causes:
# 1. Corrupted data volume
docker-compose -f docker-compose.bldg1.yml down -v
docker volume rm ontobot_mysql_data
docker-compose -f docker-compose.bldg1.yml up -d mysqlserver

# 2. Port conflict (3307 in use)
netstat -ano | findstr "3307"
# Kill conflicting process or change port

# 3. Insufficient memory
# Increase Docker memory to 8GB+
```

**Problem: Slow queries**

```sql
-- Enable slow query log
SET GLOBAL slow_query_log = 'ON';
SET GLOBAL long_query_time = 2;

-- Check slow queries
SELECT * FROM mysql.slow_log;

-- Add missing indexes
EXPLAIN SELECT * FROM sensor_readings WHERE sensor_uuid = 'uuid-123';
CREATE INDEX idx_missing ON sensor_readings(sensor_uuid, timestamp);

-- Optimize table
OPTIMIZE TABLE sensor_readings;
ANALYZE TABLE sensor_readings;
```

**Problem: Connection timeouts**

```python
# Increase connection timeout
import mysql.connector

config = {
    'host': 'mysqlserver',
    'user': 'root',
    'password': 'password',
    'database': 'telemetry',
    'connect_timeout': 60,      # Increase from default 10
    'connection_timeout': 60
}
```

### TimescaleDB (Building 2)

**Problem: TimescaleDB extension not loaded**

```sql
-- Check if extension is loaded
SELECT extversion FROM pg_extension WHERE extname = 'timescaledb';

-- If not loaded, load it
CREATE EXTENSION IF NOT EXISTS timescaledb;

-- Verify hypertables
SELECT * FROM timescaledb_information.hypertables;
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

-- Enable compression if not already
ALTER TABLE sensor_readings SET (timescaledb.compress);

-- Manually compress chunks
SELECT compress_chunk(i) FROM show_chunks('sensor_readings') i;

-- Adjust retention policy
SELECT remove_retention_policy('sensor_readings');
SELECT add_retention_policy('sensor_readings', INTERVAL '6 months');
```

**Problem: Continuous aggregate not updating**

```sql
-- Check continuous aggregate status
SELECT * FROM timescaledb_information.continuous_aggregates;

-- Manually refresh
CALL refresh_continuous_aggregate('sensor_readings_hourly', NULL, NULL);

-- Check refresh policy
SELECT * FROM timescaledb_information.jobs
WHERE application_name LIKE 'Continuous%';

-- Re-create refresh policy
SELECT remove_continuous_aggregate_policy('sensor_readings_hourly');
SELECT add_continuous_aggregate_policy('sensor_readings_hourly',
    start_offset => INTERVAL '3 hours',
    end_offset => INTERVAL '1 hour',
    schedule_interval => INTERVAL '1 hour');
```

### Cassandra (Building 3)

**Problem: Cassandra fails to start**

```powershell
# Check logs
docker-compose -f docker-compose.bldg3.yml logs cassandra

# Common causes:
# 1. Insufficient memory (needs 4GB+ heap)
# Increase Docker memory to 16GB total

# 2. Port conflict (9042 in use)
netstat -ano | findstr "9042"

# 3. Corrupted data
docker-compose -f docker-compose.bldg3.yml down -v
docker volume rm ontobot_cassandra_data
docker-compose -f docker-compose.bldg3.yml up -d cassandra

# Wait for Cassandra to start (3-5 minutes)
Start-Sleep -Seconds 300
```

**Problem: Slow queries**

```bash
# Check node status
docker-compose -f docker-compose.bldg3.yml exec cassandra nodetool status

# Monitor compaction
docker-compose -f docker-compose.bldg3.yml exec cassandra nodetool compactionstats

# Force compaction
docker-compose -f docker-compose.bldg3.yml exec cassandra nodetool compact telemetry_bldg3 sensor_data

# Check if compression enabled
# Change compaction strategy if needed
ALTER TABLE sensor_data
WITH compaction = {
    'class': 'TimeWindowCompactionStrategy',
    'compaction_window_unit': 'HOURS',
    'compaction_window_size': '24'
};
```

**Problem: Write timeouts**

```python
# Increase timeouts in client
from cassandra.cluster import Cluster
from cassandra.policies import ExponentialReconnectionPolicy

cluster = Cluster(
    ['cassandra'],
    reconnection_policy=ExponentialReconnectionPolicy(1, 60),
    protocol_version=4,
    connect_timeout=30,
    control_connection_timeout=30
)

# Use prepared statements
prepare = session.prepare("""
    INSERT INTO sensor_data (sensor_uuid, timestamp, value)
    VALUES (?, ?, ?)
""")
session.execute(prepare, (uuid, timestamp, value))

# Use batch for bulk inserts
from cassandra.query import BatchStatement, BatchType
batch = BatchStatement(batch_type=BatchType.UNLOGGED)
```

---

## Service Health Issues

### Rasa Core (5005)

**Problem: Rasa fails to start or crashes**

```powershell
# Check logs
docker-compose -f docker-compose.bldg1.yml logs rasa

# Common causes:
# 1. Model not found
docker-compose -f docker-compose.bldg1.yml exec rasa rasa train
docker-compose -f docker-compose.bldg1.yml restart rasa

# 2. Invalid domain.yml or config.yml
docker-compose -f docker-compose.bldg1.yml exec rasa rasa data validate

# 3. Port conflict
netstat -ano | findstr "5005"
```

**Problem: NLU not detecting intents**

```powershell
# Test NLU
docker-compose -f docker-compose.bldg1.yml exec rasa rasa shell nlu

# Retrain model
docker-compose -f docker-compose.bldg1.yml exec rasa rasa train nlu --force

# Check intent examples
docker-compose -f docker-compose.bldg1.yml exec rasa rasa data validate --domain domain.yml
```

### Action Server (5055)

**Problem: Action server not responding**

```powershell
# Check health
curl http://localhost:5055/health

# Check logs
docker-compose -f docker-compose.bldg1.yml logs actions

# Common causes:
# 1. Database connection failure
# Check DB_HOST, DB_PORT, DB_PASSWORD environment variables

# 2. Missing dependencies
docker-compose -f docker-compose.bldg1.yml exec actions pip list

# 3. Python syntax errors in actions.py
docker-compose -f docker-compose.bldg1.yml exec actions python -m py_compile /app/actions/actions.py
```

**Problem: Custom actions failing**

```python
# Add logging to actions
import logging
logger = logging.getLogger(__name__)

class ActionQueryCO2(Action):
    def run(self, dispatcher, tracker, domain):
        try:
            # Your code here
            logger.info("Action executed successfully")
        except Exception as e:
            logger.error(f"Action failed: {str(e)}")
            dispatcher.utter_message(text="Sorry, something went wrong")
        return []
```

### Analytics Microservice (6001)

**Problem: Analytics service not starting**

```powershell
# Check logs
docker-compose -f docker-compose.bldg1.yml logs microservices

# Check dependencies
docker-compose -f docker-compose.bldg1.yml exec microservices pip list

# Common causes:
# 1. Import errors
docker-compose -f docker-compose.bldg1.yml exec microservices python -c "import pandas, numpy, sklearn"

# 2. Port conflict
netstat -ano | findstr "6001"
```

**Problem: Analytics requests timing out**

```python
# Increase timeout in requests
import requests

response = requests.post(
    'http://localhost:6001/analytics/run',
    json={...},
    timeout=300  # Increase from default 30s
)

# Check analytics logs for errors
docker-compose -f docker-compose.bldg1.yml logs -f microservices
```

### Frontend (3000)

**Problem: Frontend not loading**

```powershell
# Check if running
curl http://localhost:3000

# Rebuild frontend
docker-compose -f docker-compose.bldg1.yml up --build frontend

# Check logs
docker-compose -f docker-compose.bldg1.yml logs frontend

# Common causes:
# 1. Node modules not installed
docker-compose -f docker-compose.bldg1.yml exec frontend npm install

# 2. Environment variables missing
# Check REACT_APP_RASA_URL, REACT_APP_FILE_SERVER_URL
```

**Problem: Frontend can't connect to Rasa**

```javascript
// Check CORS settings in rasa/credentials.yml
socketio:
  user_message_evt: user_uttered
  bot_message_evt: bot_uttered
  session_persistence: true
  cors: ["*"]  # Or specific origin: ["http://localhost:3000"]

// Check environment variables
console.log(process.env.REACT_APP_RASA_URL);
```

---

## Building-Specific Issues

### Building 1 (ABACWS) - MySQL

**Problem: No sensor data**

```sql
-- Check if data exists
SELECT COUNT(*) FROM sensor_readings;
SELECT COUNT(*) FROM sensors;

-- Check latest readings
SELECT * FROM sensor_readings ORDER BY timestamp DESC LIMIT 10;

-- If empty, check data ingestion
-- Verify ThingsBoard or data pipeline is running
```

**Problem: Missing zones**

```sql
-- List all zones
SELECT DISTINCT zone_id FROM sensors;

-- Add missing zones
INSERT INTO zones (zone_id, floor, building, description)
VALUES ('5.12', 5, 'Building1', 'Zone 5.12');
```

### Building 2 (Office) - TimescaleDB

**Problem: Hypertable not created**

```sql
-- Check if table is a hypertable
SELECT * FROM timescaledb_information.hypertables;

-- If not, convert to hypertable
SELECT create_hypertable('sensor_readings', 'time');

-- Verify
\d+ sensor_readings
```

**Problem: No HVAC data**

```sql
-- Check equipment IDs
SELECT DISTINCT equipment_id FROM sensor_readings;

-- Check sensor types
SELECT DISTINCT sensor_type, COUNT(*) FROM sensor_readings GROUP BY sensor_type;

-- Verify data pipeline for AHU, Chiller, Boiler data
```

### Building 3 (Data Center) - Cassandra

**Problem: No telemetry data**

```cql
-- Check keyspace
DESCRIBE KEYSPACES;
USE telemetry_bldg3;

-- Check tables
DESCRIBE TABLES;

-- Count records
SELECT COUNT(*) FROM sensor_data;  -- Note: Expensive on Cassandra

-- Check recent data
SELECT * FROM sensor_data LIMIT 10;
```

**Problem: Alarm table empty**

```cql
-- Verify alarm table exists
DESCRIBE TABLE alarms;

-- Check if data ingestion is working
-- Alarms should be generated by monitoring service
```

---

## Performance Problems

### Slow Dashboard Loading

```
1. Check database query performance (see database sections above)
2. Verify Analytics service is responsive
3. Check network latency between services
4. Review frontend console for errors (F12 in browser)
5. Consider caching frequently accessed data
```

### High CPU Usage

```powershell
# Check container resource usage
docker stats

# Identify problematic container
# Common culprits:
# - Rasa (model loading, NLU processing)
# - Analytics (heavy computation)
# - Cassandra (compaction)

# Allocate more resources in docker-compose.yml
services:
  rasa:
    deploy:
      resources:
        limits:
          cpus: '2.0'
          memory: 4G
```

### Memory Leaks

```powershell
# Monitor memory usage over time
docker stats --no-stream

# Restart leaking containers
docker-compose -f docker-compose.bldg1.yml restart <service>

# Check for connection leaks in custom code
# Always close database connections:
cursor.close()
conn.close()
```

---

## Development Issues

### Code Changes Not Reflecting

```powershell
# For action server (live reload enabled)
docker-compose -f docker-compose.bldg1.yml restart actions

# For frontend (should auto-reload)
docker-compose -f docker-compose.bldg1.yml restart frontend

# Force rebuild if needed
docker-compose -f docker-compose.bldg1.yml up --build <service>
```

### Python Import Errors

```powershell
# Check installed packages
docker-compose -f docker-compose.bldg1.yml exec actions pip list

# Install missing packages
docker-compose -f docker-compose.bldg1.yml exec actions pip install <package>

# Or add to requirements.txt and rebuild
docker-compose -f docker-compose.bldg1.yml up --build actions
```

### Training Fails

```powershell
# Validate data
docker-compose -f docker-compose.bldg1.yml exec rasa rasa data validate

# Check for duplicate stories
# Check for conflicting intents
# Review domain.yml for syntax errors

# Train with debug output
docker-compose -f docker-compose.bldg1.yml exec rasa rasa train --debug
```

---

## FAQ

### Q: How do I switch between buildings?

```powershell
# Stop current building
docker-compose -f docker-compose.bldg1.yml down

# Start different building
docker-compose -f docker-compose.bldg2.yml up -d

# Or use specific services
docker-compose -f docker-compose.bldg3.yml up -d rasa actions frontend
```

### Q: How do I reset everything?

```powershell
# Stop all containers
docker-compose down
docker-compose -f docker-compose.bldg1.yml down
docker-compose -f docker-compose.bldg2.yml down
docker-compose -f docker-compose.bldg3.yml down

# Remove volumes (WARNING: deletes all data)
docker-compose down -v

# Remove all OntoBot images
docker images | grep ontobot | awk '{print $3}' | xargs docker rmi

# Clean Docker system
docker system prune -a -f --volumes
```

### Q: How do I backup my data?

```powershell
# MySQL
docker-compose -f docker-compose.bldg1.yml exec mysqlserver mysqldump -u root -ppassword telemetry > backup.sql

# PostgreSQL/TimescaleDB
docker-compose -f docker-compose.bldg2.yml exec timescale pg_dump -U postgres telemetry_bldg2 > backup.sql

# Cassandra
docker-compose -f docker-compose.bldg3.yml exec cassandra nodetool snapshot telemetry_bldg3
```

### Q: How do I restore data?

```powershell
# MySQL
docker-compose -f docker-compose.bldg1.yml exec -T mysqlserver mysql -u root -ppassword telemetry < backup.sql

# PostgreSQL/TimescaleDB
docker-compose -f docker-compose.bldg2.yml exec -T timescale psql -U postgres telemetry_bldg2 < backup.sql

# Cassandra
# 1. Stop Cassandra
# 2. Copy snapshot files to data directory
# 3. Start Cassandra
# 4. Run: nodetool refresh telemetry_bldg3 sensor_data
```

### Q: How do I update Rasa or other services?

```yaml
# Update image version in docker-compose.yml
services:
  rasa:
    image: rasa/rasa:3.6.12-full  # Change version here

# Then rebuild
docker-compose -f docker-compose.bldg1.yml up --build rasa
```

### Q: How do I add a new sensor?

```sql
-- MySQL (Building 1)
INSERT INTO sensors (uuid, name, zone_id, sensor_type, unit, brick_class)
VALUES ('new-uuid', 'New Sensor', '5.25', 'Temperature', '°C', 'brick:Temperature_Sensor');

-- PostgreSQL/TimescaleDB (Building 2)
-- Just insert readings; sensor metadata can be in separate table or JSON

-- Cassandra (Building 3)
-- Insert readings directly; no separate sensor table needed
INSERT INTO sensor_data (sensor_uuid, timestamp, value, unit, sensor_type)
VALUES (uuid(), toTimestamp(now()), 22.5, '°C', 'Temperature');
```

### Q: How do I monitor system health?

```powershell
# All services status
docker-compose -f docker-compose.bldg1.yml ps

# Health checks
curl http://localhost:5005/version        # Rasa
curl http://localhost:5055/health         # Actions
curl http://localhost:8080/health         # File Server
curl http://localhost:6001/health         # Analytics
curl http://localhost:6009/health         # Decider

# Database connectivity
# MySQL
docker-compose -f docker-compose.bldg1.yml exec mysqlserver mysql -u root -ppassword -e "SELECT 1"

# TimescaleDB
docker-compose -f docker-compose.bldg2.yml exec timescale pg_isready

# Cassandra
docker-compose -f docker-compose.bldg3.yml exec cassandra nodetool status
```

### Q: How do I enable debug logging?

```yaml
# In docker-compose.yml, add environment variables
services:
  rasa:
    environment:
      - LOG_LEVEL=DEBUG
  
  actions:
    environment:
      - LOG_LEVEL=DEBUG
      - PYTHONUNBUFFERED=1

# Or in code (actions.py)
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
```

---

## Getting Help

### Logs to Check

```powershell
# All services
docker-compose -f docker-compose.bldg1.yml logs

# Specific service
docker-compose -f docker-compose.bldg1.yml logs rasa
docker-compose -f docker-compose.bldg1.yml logs actions
docker-compose -f docker-compose.bldg1.yml logs microservices

# Follow logs in real-time
docker-compose -f docker-compose.bldg1.yml logs -f

# Last 100 lines
docker-compose -f docker-compose.bldg1.yml logs --tail=100
```

### Diagnostic Commands

```powershell
# Docker info
docker info
docker version

# Network inspection
docker network ls
docker network inspect ontobot_default

# Volume inspection
docker volume ls
docker volume inspect ontobot_mysql_data

# Container inspection
docker inspect ontobot_rasa_1
```

### Support Resources

- **GitHub Issues**: [OntoBot Issues](https://github.com/suhasdevmane/OntoBot/issues)
- **Documentation**: [OntoBot GitHub Pages](https://suhasdevmane.github.io/)
- **Rasa Community**: [forum.rasa.com](https://forum.rasa.com/)
- **Docker Documentation**: [docs.docker.com](https://docs.docker.com/)

---

**Still having issues?** Create a GitHub issue with:
1. Error message (full stack trace)
2. Docker logs (`docker-compose logs`)
3. System info (`docker info`, OS version)
4. Steps to reproduce
5. Expected vs actual behavior
