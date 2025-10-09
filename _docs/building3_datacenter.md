---
layout: post
title: Building 3 - Data Center
date: 2025-10-08
categories: buildings
---

# Building 3 - Synthetic Data Center

**Rasa Conversational AI Stack for Building 3**

## Overview

Building 3 is a synthetic critical infrastructure data center focused on cooling systems, power distribution, and alarm monitoring with high-availability Cassandra storage.

### Key Specifications

| Property | Details |
|----------|---------|
| **Building Type** | Synthetic Critical Infrastructure |
| **Purpose** | Data Center Operations & Monitoring |
| **Sensor Coverage** | 597 sensors across multiple zones |
| **Focus Area** | Cooling Systems, Power Distribution & Alarms |
| **Database** | Cassandra (port 9042) - Distributed NoSQL |
| **Metadata Store** | PostgreSQL (port 5434) - ThingsBoard entities |
| **Knowledge Graph** | Brick Schema 1.3 via Jena Fuseki (port 3030) |
| **Compose File** | `docker-compose.bldg3.yml` |
| **Technology Stack** | Rasa 3.6.12, Python 3.10, Docker, Cassandra 4.1 |

## Critical Infrastructure Monitoring

### Equipment Coverage (597 Sensors)

**CRAC Units (Computer Room Air Conditioning):**
- Supply/Return Air Temperature sensors
- Airflow Rate & Pressure monitoring
- Cooling Capacity measurement
- Efficiency metrics
- Alarm status indicators
- **Total CRAC Sensors**: ~150

**UPS Systems (Uninterruptible Power Supply):**
- Input/Output Voltage monitoring
- Battery Charge Level & Health
- Power Load & Capacity tracking
- Alarm Conditions
- Runtime on battery
- **Total UPS Sensors**: ~120

**PDUs (Power Distribution Units):**
- Phase Voltages (L1, L2, L3)
- Current Draw per Phase
- Power Factor measurement
- Circuit Breaker Status
- Branch circuit monitoring
- **Total PDU Sensors**: ~180

**Rack-Level Monitoring:**
- Inlet/Outlet Temperature per rack
- Humidity sensors
- Hot Aisle/Cold Aisle Temperature
- Power Consumption per Rack
- Airflow sensors
- **Total Rack Sensors**: ~120

**Alarm Systems:**
- Environmental Alarms
- Equipment Failure Alerts
- Threshold Violations
- Critical System Warnings
- **Total Alarm Points**: ~27

### Data Center Metrics

**PUE (Power Usage Effectiveness):**
```
PUE = Total Facility Power / IT Equipment Power
Target: < 1.5 (Excellent), < 2.0 (Good)
```

**DCiE (Data Center Infrastructure Efficiency):**
```
DCiE = 1 / PUE × 100%
Target: > 67% (Excellent), > 50% (Good)
```

**Other Metrics:**
- Cooling efficiency (kW per ton)
- Server inlet temperature
- Return temperature index (RTI)
- Cooling capacity utilization
- Power capacity utilization

## Cassandra Database Architecture

### Why Cassandra?

Cassandra is a distributed NoSQL database ideal for mission-critical data:

**Benefits:**
- ✅ **High Availability** - No single point of failure
- ✅ **Linear Scalability** - Add nodes without downtime
- ✅ **Write Performance** - Millions of writes/second
- ✅ **Geographic Distribution** - Multi-datacenter replication
- ✅ **Tunable Consistency** - Balance between consistency & availability
- ✅ **Time-Series Optimized** - Perfect for sensor data

### Database Configuration

```yaml
# docker-compose.bldg3.yml
cassandra:
  image: cassandra:4.1
  ports:
    - "9042:9042"
  environment:
    CASSANDRA_CLUSTER_NAME: "DataCenter-Cluster"
    CASSANDRA_DC: "DC1"
    CASSANDRA_ENDPOINT_SNITCH: "GossipingPropertyFileSnitch"
    MAX_HEAP_SIZE: "4G"
    HEAP_NEWSIZE: "800M"
  volumes:
    - cassandra_data:/var/lib/cassandra
```

### Cassandra Schema

```cql
-- Create keyspace with replication
CREATE KEYSPACE IF NOT EXISTS telemetry_bldg3
WITH replication = {
    'class': 'SimpleStrategy',
    'replication_factor': 3  -- For production cluster
};

USE telemetry_bldg3;

-- Sensor readings table (time-series)
CREATE TABLE IF NOT EXISTS sensor_data (
    sensor_uuid UUID,
    timestamp TIMESTAMP,
    value DOUBLE,
    unit TEXT,
    zone TEXT,
    equipment_type TEXT,
    equipment_id TEXT,
    sensor_type TEXT,
    PRIMARY KEY ((sensor_uuid), timestamp)
) WITH CLUSTERING ORDER BY (timestamp DESC)
  AND compaction = {
      'class': 'TimeWindowCompactionStrategy',
      'compaction_window_unit': 'HOURS',
      'compaction_window_size': '24'
  };

-- Alarms table
CREATE TABLE IF NOT EXISTS alarms (
    alarm_id UUID,
    timestamp TIMESTAMP,
    severity TEXT,
    equipment_id TEXT,
    equipment_type TEXT,
    message TEXT,
    acknowledged BOOLEAN,
    acknowledged_by TEXT,
    acknowledged_at TIMESTAMP,
    PRIMARY KEY ((equipment_id), timestamp)
) WITH CLUSTERING ORDER BY (timestamp DESC);

-- Equipment status table
CREATE TABLE IF NOT EXISTS equipment_status (
    equipment_id TEXT,
    equipment_type TEXT,
    zone TEXT,
    status TEXT,
    last_updated TIMESTAMP,
    metadata MAP<TEXT, TEXT>,
    PRIMARY KEY (equipment_id)
);

-- Aggregated metrics (rollups)
CREATE TABLE IF NOT EXISTS hourly_aggregates (
    sensor_uuid UUID,
    hour TIMESTAMP,
    avg_value DOUBLE,
    min_value DOUBLE,
    max_value DOUBLE,
    sample_count INT,
    PRIMARY KEY ((sensor_uuid), hour)
) WITH CLUSTERING ORDER BY (hour DESC);
```

### CQL Query Examples

**Get Recent CRAC Temperature:**
```cql
SELECT timestamp, value, unit, equipment_id
FROM sensor_data
WHERE sensor_uuid = uuid-crac-001
  AND timestamp >= '2025-10-08 00:00:00'
  AND timestamp <= '2025-10-08 23:59:59'
ORDER BY timestamp DESC
LIMIT 100;
```

**Query Active Alarms:**
```cql
SELECT alarm_id, timestamp, severity, message
FROM alarms
WHERE equipment_id = 'CRAC-A-01'
  AND acknowledged = false
ORDER BY timestamp DESC;
```

**Get Hourly Averages:**
```cql
SELECT hour, avg_value, min_value, max_value
FROM hourly_aggregates
WHERE sensor_uuid = uuid-ups-battery-001
  AND hour >= '2025-10-01 00:00:00'
  AND hour <= '2025-10-08 00:00:00'
ORDER BY hour DESC;
```

### Python Client Integration

```python
# actions/cassandra_client.py
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from datetime import datetime, timedelta
import uuid

class CassandraClient:
    def __init__(self, hosts=['cassandra'], port=9042, keyspace='telemetry_bldg3'):
        self.cluster = Cluster(hosts, port=port)
        self.session = self.cluster.connect(keyspace)
    
    def get_sensor_data(self, sensor_uuid, hours_back=1):
        """Get recent sensor readings"""
        query = """
        SELECT timestamp, value, unit, equipment_id
        FROM sensor_data
        WHERE sensor_uuid = %s
          AND timestamp >= %s
        ORDER BY timestamp DESC
        """
        start_time = datetime.now() - timedelta(hours=hours_back)
        return self.session.execute(query, (uuid.UUID(sensor_uuid), start_time))
    
    def get_active_alarms(self, equipment_id=None, severity=None):
        """Get active (unacknowledged) alarms"""
        if equipment_id:
            query = """
            SELECT * FROM alarms
            WHERE equipment_id = %s
              AND acknowledged = false
            ORDER BY timestamp DESC
            """
            return self.session.execute(query, (equipment_id,))
        else:
            # Note: This requires ALLOW FILTERING or secondary index
            query = """
            SELECT * FROM alarms
            WHERE acknowledged = false
            ALLOW FILTERING
            """
            return self.session.execute(query)
    
    def calculate_pue(self, timestamp=None):
        """Calculate Power Usage Effectiveness"""
        if timestamp is None:
            timestamp = datetime.now()
        
        # Get total facility power
        total_power_query = """
        SELECT value FROM sensor_data
        WHERE sensor_uuid = %s
          AND timestamp <= %s
        ORDER BY timestamp DESC
        LIMIT 1
        """
        
        # Get IT equipment power
        it_power_query = """
        SELECT value FROM sensor_data
        WHERE sensor_uuid = %s
          AND timestamp <= %s
        ORDER BY timestamp DESC
        LIMIT 1
        """
        
        total_power_result = self.session.execute(
            total_power_query, 
            (uuid.UUID('total-facility-power-uuid'), timestamp)
        ).one()
        
        it_power_result = self.session.execute(
            it_power_query,
            (uuid.UUID('it-equipment-power-uuid'), timestamp)
        ).one()
        
        if total_power_result and it_power_result:
            total_power = total_power_result.value
            it_power = it_power_result.value
            pue = total_power / it_power if it_power > 0 else None
            return pue
        return None
    
    def insert_sensor_reading(self, sensor_uuid, value, unit, equipment_id, sensor_type):
        """Insert new sensor reading"""
        query = """
        INSERT INTO sensor_data (sensor_uuid, timestamp, value, unit, equipment_id, sensor_type)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        self.session.execute(
            query,
            (uuid.UUID(sensor_uuid), datetime.now(), value, unit, equipment_id, sensor_type)
        )
    
    def acknowledge_alarm(self, alarm_id, acknowledged_by):
        """Acknowledge an alarm"""
        query = """
        UPDATE alarms
        SET acknowledged = true,
            acknowledged_by = %s,
            acknowledged_at = %s
        WHERE alarm_id = %s
        """
        self.session.execute(query, (acknowledged_by, datetime.now(), uuid.UUID(alarm_id)))
```

## Usage Examples

### Cooling System Monitoring

```
"Show me CRAC unit 1 temperature trends"
"What's the cooling efficiency in zone A?"
"Alert me if any CRAC units have alarms"
"Compare supply vs return air temperatures"
"Display CRAC airflow rates"
```

### Power Distribution

```
"What's the current load on PDU 3?"
"Show UPS battery status for all units"
"What's our current PUE?"
"Display power consumption by rack"
"Show phase balance on PDU 1"
```

### Alarm Management

```
"Show all active alarms"
"What critical alarms were triggered today?"
"Display temperature threshold violations"
"Show equipment failure alerts"
"Acknowledge alarm [ID]"
```

### Environmental Monitoring

```
"Show hot aisle temperatures in zone B"
"What's the humidity in rack 15?"
"Display inlet/outlet temperature differential"
"Show me cooling load trends this week"
"Compare rack temperatures"
```

### Efficiency Metrics

```
"Calculate our DCiE for today"
"Show power usage effectiveness trend"
"What's the cooling efficiency?"
"Display energy consumption by zone"
"Show PUE history for the past month"
```

## High Availability Features

### Replication Strategy

**Production Setup (3+ nodes):**
```cql
CREATE KEYSPACE telemetry_bldg3
WITH replication = {
    'class': 'NetworkTopologyStrategy',
    'DC1': 3,  -- 3 replicas in datacenter 1
    'DC2': 2   -- 2 replicas in datacenter 2 (DR site)
};
```

**Consistency Levels:**
- **QUORUM** - Majority of replicas (recommended for critical data)
- **LOCAL_QUORUM** - Majority within local DC (better latency)
- **ALL** - All replicas (highest consistency, lowest availability)
- **ONE** - Single replica (best performance, lowest consistency)

### Multi-Datacenter Replication

```yaml
# docker-compose-prod.yml
cassandra-dc1-node1:
  image: cassandra:4.1
  environment:
    CASSANDRA_CLUSTER_NAME: "DataCenter-Cluster"
    CASSANDRA_DC: "DC1"
    CASSANDRA_SEEDS: "cassandra-dc1-node1,cassandra-dc2-node1"

cassandra-dc1-node2:
  image: cassandra:4.1
  environment:
    CASSANDRA_DC: "DC1"
    CASSANDRA_SEEDS: "cassandra-dc1-node1,cassandra-dc2-node1"

cassandra-dc2-node1:
  image: cassandra:4.1
  environment:
    CASSANDRA_DC: "DC2"
    CASSANDRA_SEEDS: "cassandra-dc1-node1,cassandra-dc2-node1"
```

### Backup & Recovery

```bash
# Create snapshot
docker-compose -f docker-compose.bldg3.yml exec cassandra nodetool snapshot telemetry_bldg3

# List snapshots
docker-compose -f docker-compose.bldg3.yml exec cassandra nodetool listsnapshots

# Export data
docker-compose -f docker-compose.bldg3.yml exec cassandra cqlsh -e "COPY telemetry_bldg3.sensor_data TO '/backup/sensor_data.csv'"

# Restore from snapshot
# 1. Stop Cassandra
# 2. Copy snapshot files to data directory
# 3. Start Cassandra
# 4. Run: nodetool refresh telemetry_bldg3 sensor_data
```

## Performance Optimization

### Compaction Strategy

For time-series data, use TimeWindowCompactionStrategy:

```cql
ALTER TABLE sensor_data
WITH compaction = {
    'class': 'TimeWindowCompactionStrategy',
    'compaction_window_unit': 'HOURS',
    'compaction_window_size': '24'
};
```

**Benefits:**
- Automatic cleanup of old SSTables
- Better read performance
- Efficient disk usage
- Time-based data organization

### Memory Settings

```yaml
# Production memory configuration
environment:
  MAX_HEAP_SIZE: "8G"      # 1/4 to 1/2 of available RAM
  HEAP_NEWSIZE: "2G"       # 1/4 of MAX_HEAP_SIZE
  CASSANDRA_MEMTABLE_HEAP_SPACE_IN_MB: "2048"
  CASSANDRA_MEMTABLE_OFFHEAP_SPACE_IN_MB: "2048"
```

### Monitoring Commands

```bash
# Cluster status
nodetool status

# Ring topology
nodetool ring

# Compaction statistics
nodetool compactionstats

# Table statistics
nodetool tablestats telemetry_bldg3.sensor_data

# Node info
nodetool info

# Performance stats
nodetool tpstats
```

## Analytics Integration

### Data Center-Specific Analytics

**Temperature Monitoring:**
- Time-series analysis of CRAC supply/return temperatures
- Hot aisle/cold aisle differential monitoring
- Rack-level thermal mapping
- Anomaly detection for temperature spikes

**Power Analysis:**
- UPS load trending
- PDU phase balance analysis
- PUE/DCiE calculation
- Power consumption forecasting
- Peak demand prediction

**Cooling Efficiency:**
- CRAC efficiency scoring
- Cooling capacity utilization
- Airflow optimization analysis
- Energy consumption per cooling ton
- Return Temperature Index (RTI)

**Alarm Analytics:**
- Alarm frequency analysis
- Root cause correlation
- Predictive maintenance triggers
- Threshold optimization
- Mean time between failures (MTBF)

### API Examples

```python
import requests

# Get CRAC temperature analysis
response = requests.post(
    'http://localhost:6001/analytics/run',
    json={
        'analysis_type': 'time_series',
        'sensor_id': 'CRAC-A-01-Supply-Temp',
        'start_time': '2025-10-01T00:00:00Z',
        'end_time': '2025-10-08T23:59:59Z',
        'aggregation': '1h'
    }
)

# Calculate PUE
response = requests.post(
    'http://localhost:6001/analytics/run',
    json={
        'analysis_type': 'pue_calculation',
        'building_id': 'bldg3',
        'timestamp': '2025-10-08T12:00:00Z'
    }
)

# Detect temperature anomalies
response = requests.post(
    'http://localhost:6001/analytics/run',
    json={
        'analysis_type': 'anomaly_detection',
        'sensor_id': 'CRAC-A-01-Supply-Temp',
        'method': 'isolation_forest',
        'sensitivity': 0.95
    }
)

# Alarm correlation analysis
response = requests.post(
    'http://localhost:6001/analytics/run',
    json={
        'analysis_type': 'alarm_correlation',
        'start_time': '2025-10-01T00:00:00Z',
        'end_time': '2025-10-08T23:59:59Z',
        'equipment_types': ['CRAC', 'UPS', 'PDU']
    }
)
```

## Development

### Custom Actions

```python
# actions/actions.py
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from .cassandra_client import CassandraClient

class ActionQueryCRACStatus(Action):
    def name(self) -> Text:
        return "action_query_crac_status"

    def run(
        self, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        
        equipment_id = tracker.get_slot("equipment_id")
        
        # Connect to Cassandra
        client = CassandraClient()
        
        # Get recent readings
        sensor_uuid = f"uuid-{equipment_id.lower()}-supply-temp"
        readings = client.get_sensor_data(sensor_uuid, hours_back=1)
        
        if readings:
            latest = list(readings)[0]
            message = f"{equipment_id} Supply Temperature: {latest.value:.1f} {latest.unit}"
        else:
            message = f"No data found for {equipment_id}"
        
        dispatcher.utter_message(text=message)
        return []

class ActionCalculatePUE(Action):
    def name(self) -> Text:
        return "action_calculate_pue"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        
        client = CassandraClient()
        pue = client.calculate_pue()
        
        if pue:
            dcit = (1 / pue) * 100
            message = f"Current PUE: {pue:.2f} (DCiE: {dcit:.1f}%)"
            
            if pue < 1.5:
                message += " - Excellent efficiency!"
            elif pue < 2.0:
                message += " - Good efficiency"
            else:
                message += " - Consider optimization"
        else:
            message = "Unable to calculate PUE at this time"
        
        dispatcher.utter_message(text=message)
        return []
```

### Data Center-Specific Intents

```yaml
# data/nlu.yml
- intent: query_crac_status
  examples: |
    - show me [CRAC unit 1](equipment_id) status
    - what's the temperature of [CRAC-A-01](equipment_id)
    - display cooling efficiency for [zone A](zone_name)
    - how is [CRAC unit 3](equipment_id) performing

- intent: query_ups_status
  examples: |
    - show UPS battery levels
    - what's the status of [UPS 2](equipment_id)
    - display power load on [UPS-B-01](equipment_id)
    - how much charge does [UPS 1](equipment_id) have

- intent: query_alarms
  examples: |
    - show all active alarms
    - what [critical](alarm_severity) alarms do we have
    - display [temperature](alarm_type) alarms
    - show me equipment failure alerts

- intent: calculate_pue
  examples: |
    - what's our PUE
    - calculate power usage effectiveness
    - show me energy efficiency
    - what's the DCiE
```

## Testing & Monitoring

### Health Checks

```powershell
# Check Cassandra status
docker-compose -f docker-compose.bldg3.yml exec cassandra nodetool status

# Check connectivity
docker-compose -f docker-compose.bldg3.yml exec cassandra cqlsh -e "DESCRIBE KEYSPACES"

# Verify data
docker-compose -f docker-compose.bldg3.yml exec cassandra cqlsh -e "SELECT COUNT(*) FROM telemetry_bldg3.sensor_data"

# Check PostgreSQL (ThingsBoard metadata)
docker-compose -f docker-compose.bldg3.yml exec tb-postgres pg_isready
```

### Performance Testing

```bash
# Cassandra stress test
docker-compose -f docker-compose.bldg3.yml exec cassandra cassandra-stress write n=1000000 -rate threads=50

# Monitor performance
docker-compose -f docker-compose.bldg3.yml exec cassandra nodetool tpstats
docker-compose -f docker-compose.bldg3.yml exec cassandra nodetool proxyhistograms
```

## Troubleshooting

### Common Issues

**Problem: Cassandra fails to start**
```bash
# Check logs
docker-compose -f docker-compose.bldg3.yml logs cassandra

# Common causes:
# - Insufficient memory (increase Docker RAM to 8GB+)
# - Port conflict on 9042
# - Corrupted data volume

# Solution: Reset Cassandra
docker-compose -f docker-compose.bldg3.yml down -v
docker volume rm ontobot_cassandra_data
docker-compose -f docker-compose.bldg3.yml up -d cassandra
```

**Problem: Slow queries**
```bash
# Check node status
nodetool status

# Monitor compaction
nodetool compactionstats

# Optimize table
nodetool compact telemetry_bldg3 sensor_data
```

**Problem: High disk usage**
```bash
# Check disk usage
nodetool tablestats telemetry_bldg3.sensor_data

# Clear old snapshots
nodetool clearsnapshot

# Adjust retention (if using TTL)
# Data expires automatically with TTL set
```

## Related Documentation

- [Building 1 - ABACWS](/docs/building1_abacws/) - Real university testbed
- [Building 2 - Office](/docs/building2_office/) - HVAC optimization
- [Cassandra Integration Guide](/docs/cassandra_integration/) - Detailed database guide
- [Data Center Best Practices](/docs/datacenter_best_practices/) - Operations guide
- [Multi-Building Support](/docs/multi_building/) - Switching between buildings

## Support & Resources

- **Cassandra Documentation**: [cassandra.apache.org](https://cassandra.apache.org/doc/)
- **Data Center Standards**: [Uptime Institute](https://uptimeinstitute.com/)
- **PUE Guidelines**: [The Green Grid](https://www.thegreengrid.org/)
- **ThingsBoard Documentation**: [thingsboard.io/docs](https://thingsboard.io/docs/)

---

**Building 3 (Data Center)** represents critical infrastructure with:
- ✅ 597 sensors (CRAC, UPS, PDU, Racks, Alarms)
- ✅ Cassandra high-availability storage
- ✅ Real-time alarm monitoring
- ✅ Cooling system optimization
- ✅ Power distribution tracking
- ✅ PUE/DCiE efficiency metrics
