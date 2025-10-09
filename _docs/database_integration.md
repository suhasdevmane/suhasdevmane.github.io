---
layout: post
title: Database Integration Guide
date: 2025-10-08
categories: technical
---

# Database Integration Guide

OntoBot supports three different database systems, each optimized for specific building types and use cases. This guide covers MySQL, TimescaleDB, and Cassandra integration.

## Overview

| Database | Building | Use Case | Strengths | Best For |
|----------|----------|----------|-----------|----------|
| **MySQL 8.0** | Building 1 | Traditional relational | ACID compliance, mature tooling | Structured data, joins, transactions |
| **TimescaleDB 2.11** | Building 2 | Time-series | Automatic partitioning, compression | HVAC analytics, energy monitoring |
| **Cassandra 4.1** | Building 3 | Distributed NoSQL | High availability, write throughput | Critical infrastructure, scalability |

---

## MySQL Integration (Building 1)

### Configuration

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
  command: --default-authentication-plugin=mysql_native_password
```

### Schema Design

```sql
-- Create telemetry database
CREATE DATABASE IF NOT EXISTS telemetry
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE telemetry;

-- Sensor readings (time-series data)
CREATE TABLE sensor_readings (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    sensor_uuid VARCHAR(36) NOT NULL,
    sensor_name VARCHAR(255),
    zone_id VARCHAR(10),
    timestamp DATETIME(6) NOT NULL,
    value DOUBLE NOT NULL,
    unit VARCHAR(20),
    sensor_type VARCHAR(50),
    quality_flag TINYINT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    INDEX idx_sensor_time (sensor_uuid, timestamp),
    INDEX idx_zone_time (zone_id, timestamp),
    INDEX idx_type_time (sensor_type, timestamp),
    INDEX idx_timestamp (timestamp)
) ENGINE=InnoDB 
  ROW_FORMAT=COMPRESSED
  COMMENT='Time-series sensor telemetry data';

-- Sensor metadata
CREATE TABLE sensors (
    uuid VARCHAR(36) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    zone_id VARCHAR(10) NOT NULL,
    sensor_type VARCHAR(50) NOT NULL,
    unit VARCHAR(20),
    location_description TEXT,
    brick_class VARCHAR(100),
    metadata JSON,
    last_reading DATETIME(6),
    last_value DOUBLE,
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    UNIQUE KEY unique_name (name),
    INDEX idx_zone (zone_id),
    INDEX idx_type (sensor_type),
    INDEX idx_active (active)
) ENGINE=InnoDB;

-- Zone information
CREATE TABLE zones (
    zone_id VARCHAR(10) PRIMARY KEY,
    floor INT NOT NULL,
    building VARCHAR(50) NOT NULL DEFAULT 'Building1',
    zone_type VARCHAR(50),
    area_sqm DOUBLE,
    occupancy_capacity INT,
    description TEXT,
    metadata JSON,
    
    INDEX idx_floor (floor),
    INDEX idx_building (building)
) ENGINE=InnoDB;

-- Alarm history
CREATE TABLE alarm_history (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    alarm_id VARCHAR(36) NOT NULL,
    sensor_uuid VARCHAR(36),
    timestamp DATETIME(6) NOT NULL,
    severity ENUM('INFO', 'WARNING', 'CRITICAL') NOT NULL,
    message TEXT,
    acknowledged BOOLEAN DEFAULT FALSE,
    acknowledged_by VARCHAR(100),
    acknowledged_at DATETIME(6),
    
    INDEX idx_sensor_time (sensor_uuid, timestamp),
    INDEX idx_timestamp (timestamp),
    INDEX idx_severity (severity),
    INDEX idx_acknowledged (acknowledged)
) ENGINE=InnoDB;
```

### Python Client

```python
# mysql_client.py
import mysql.connector
from mysql.connector import pooling
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import os

class MySQLClient:
    def __init__(self):
        self.config = {
            'host': os.getenv('DB_HOST', 'mysqlserver'),
            'port': int(os.getenv('DB_PORT', 3306)),
            'database': os.getenv('DB_NAME', 'telemetry'),
            'user': os.getenv('DB_USER', 'root'),
            'password': os.getenv('DB_PASSWORD', 'password'),
            'pool_name': 'ontobot_pool',
            'pool_size': 10,
            'pool_reset_session': True
        }
        self.pool = mysql.connector.pooling.MySQLConnectionPool(**self.config)
    
    def get_connection(self):
        """Get connection from pool"""
        return self.pool.get_connection()
    
    def get_recent_reading(self, sensor_uuid: str) -> Optional[Dict]:
        """Get most recent reading for a sensor"""
        conn = self.get_connection()
        cursor = conn.cursor(dictionary=True)
        
        query = """
            SELECT sr.timestamp, sr.value, sr.unit, s.name, s.zone_id
            FROM sensor_readings sr
            JOIN sensors s ON sr.sensor_uuid = s.uuid
            WHERE sr.sensor_uuid = %s
            ORDER BY sr.timestamp DESC
            LIMIT 1
        """
        cursor.execute(query, (sensor_uuid,))
        result = cursor.fetchone()
        
        cursor.close()
        conn.close()
        return result
    
    def get_time_series(
        self, 
        sensor_uuid: str, 
        start_time: datetime, 
        end_time: datetime,
        aggregation: Optional[str] = None
    ) -> List[Dict]:
        """Get time-series data with optional aggregation"""
        conn = self.get_connection()
        cursor = conn.cursor(dictionary=True)
        
        if aggregation:
            # Aggregated query (e.g., '1h', '15m', '1d')
            query = f"""
                SELECT 
                    DATE_FORMAT(timestamp, %s) AS time_bucket,
                    AVG(value) AS avg_value,
                    MIN(value) AS min_value,
                    MAX(value) AS max_value,
                    COUNT(*) AS count
                FROM sensor_readings
                WHERE sensor_uuid = %s
                  AND timestamp BETWEEN %s AND %s
                GROUP BY time_bucket
                ORDER BY time_bucket
            """
            time_format = self._get_mysql_time_format(aggregation)
            cursor.execute(query, (time_format, sensor_uuid, start_time, end_time))
        else:
            # Raw data
            query = """
                SELECT timestamp, value, unit
                FROM sensor_readings
                WHERE sensor_uuid = %s
                  AND timestamp BETWEEN %s AND %s
                ORDER BY timestamp
            """
            cursor.execute(query, (sensor_uuid, start_time, end_time))
        
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results
    
    def get_zone_statistics(self, zone_id: str, sensor_type: str, hours: int = 24) -> Dict:
        """Get aggregated statistics for a zone"""
        conn = self.get_connection()
        cursor = conn.cursor(dictionary=True)
        
        query = """
            SELECT 
                s.zone_id,
                COUNT(DISTINCT sr.sensor_uuid) AS sensor_count,
                AVG(sr.value) AS avg_value,
                MIN(sr.value) AS min_value,
                MAX(sr.value) AS max_value,
                STDDEV(sr.value) AS stddev_value,
                MAX(sr.timestamp) AS last_updated
            FROM sensor_readings sr
            JOIN sensors s ON sr.sensor_uuid = s.uuid
            WHERE s.zone_id = %s
              AND s.sensor_type = %s
              AND sr.timestamp >= DATE_SUB(NOW(), INTERVAL %s HOUR)
            GROUP BY s.zone_id
        """
        cursor.execute(query, (zone_id, sensor_type, hours))
        result = cursor.fetchone()
        
        cursor.close()
        conn.close()
        return result or {}
    
    def insert_reading(self, sensor_uuid: str, value: float, timestamp: datetime = None):
        """Insert new sensor reading"""
        if timestamp is None:
            timestamp = datetime.now()
        
        conn = self.get_connection()
        cursor = conn.cursor()
        
        query = """
            INSERT INTO sensor_readings (sensor_uuid, timestamp, value)
            VALUES (%s, %s, %s)
        """
        cursor.execute(query, (sensor_uuid, timestamp, value))
        
        # Update sensor metadata
        update_query = """
            UPDATE sensors 
            SET last_reading = %s, last_value = %s 
            WHERE uuid = %s
        """
        cursor.execute(update_query, (timestamp, value, sensor_uuid))
        
        conn.commit()
        cursor.close()
        conn.close()
    
    def _get_mysql_time_format(self, aggregation: str) -> str:
        """Convert aggregation string to MySQL DATE_FORMAT"""
        formats = {
            '1m': '%Y-%m-%d %H:%i:00',
            '5m': '%Y-%m-%d %H:%i:00',
            '15m': '%Y-%m-%d %H:%i:00',
            '1h': '%Y-%m-%d %H:00:00',
            '1d': '%Y-%m-%d 00:00:00'
        }
        return formats.get(aggregation, '%Y-%m-%d %H:%i:00')
```

### Optimization Tips

```sql
-- Partition by month for large tables
ALTER TABLE sensor_readings
PARTITION BY RANGE (YEAR(timestamp) * 100 + MONTH(timestamp)) (
    PARTITION p202310 VALUES LESS THAN (202311),
    PARTITION p202311 VALUES LESS THAN (202312),
    PARTITION p202312 VALUES LESS THAN (202401),
    PARTITION p_future VALUES LESS THAN MAXVALUE
);

-- Add covering indexes
CREATE INDEX idx_covering ON sensor_readings(sensor_uuid, timestamp) 
INCLUDE (value, unit);

-- Enable query cache (if appropriate)
SET GLOBAL query_cache_type = 1;
SET GLOBAL query_cache_size = 268435456;  -- 256MB

-- Optimize table regularly
OPTIMIZE TABLE sensor_readings;

-- Analyze for better query plans
ANALYZE TABLE sensor_readings;
```

---

## TimescaleDB Integration (Building 2)

### Configuration

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
  command: postgres -c shared_preload_libraries=timescaledb -c max_connections=200
```

### Schema Design

```sql
-- Create database
CREATE DATABASE telemetry_bldg2;
\c telemetry_bldg2

-- Enable TimescaleDB
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
    quality_flag INTEGER DEFAULT 0,
    metadata JSONB
);

-- Convert to hypertable (partitioned by time)
SELECT create_hypertable('sensor_readings', 'time', chunk_time_interval => INTERVAL '1 day');

-- Create indexes
CREATE INDEX idx_sensor_time ON sensor_readings (sensor_id, time DESC);
CREATE INDEX idx_zone_time ON sensor_readings (zone_id, time DESC) WHERE zone_id IS NOT NULL;
CREATE INDEX idx_equipment_time ON sensor_readings (equipment_id, time DESC) WHERE equipment_id IS NOT NULL;
CREATE INDEX idx_type_time ON sensor_readings (sensor_type, time DESC);

-- Enable compression (90%+ savings)
ALTER TABLE sensor_readings SET (
    timescaledb.compress,
    timescaledb.compress_segmentby = 'sensor_id, sensor_type',
    timescaledb.compress_orderby = 'time DESC'
);

-- Add compression policy (compress after 7 days)
SELECT add_compression_policy('sensor_readings', INTERVAL '7 days');

-- Add retention policy (drop after 1 year)
SELECT add_retention_policy('sensor_readings', INTERVAL '1 year');

-- Create continuous aggregates (pre-computed rollups)
CREATE MATERIALIZED VIEW sensor_readings_hourly
WITH (timescaledb.continuous) AS
SELECT 
    time_bucket('1 hour', time) AS bucket,
    sensor_id,
    sensor_type,
    zone_id,
    equipment_id,
    AVG(value) AS avg_value,
    MIN(value) AS min_value,
    MAX(value) AS max_value,
    STDDEV(value) AS stddev_value,
    COUNT(*) AS reading_count
FROM sensor_readings
GROUP BY bucket, sensor_id, sensor_type, zone_id, equipment_id;

-- Refresh policy for continuous aggregate
SELECT add_continuous_aggregate_policy('sensor_readings_hourly',
    start_offset => INTERVAL '3 hours',
    end_offset => INTERVAL '1 hour',
    schedule_interval => INTERVAL '1 hour');
```

### Python Client

```python
# timescale_client.py
import psycopg2
from psycopg2.extras import RealDictCursor, execute_values
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import os

class TimescaleClient:
    def __init__(self):
        self.config = {
            'host': os.getenv('DB_HOST', 'timescale'),
            'port': int(os.getenv('DB_PORT', 5432)),
            'database': os.getenv('DB_NAME', 'telemetry_bldg2'),
            'user': os.getenv('DB_USER', 'postgres'),
            'password': os.getenv('DB_PASSWORD', 'postgres')
        }
        self.conn = None
    
    def connect(self):
        """Establish database connection"""
        if self.conn is None or self.conn.closed:
            self.conn = psycopg2.connect(**self.config)
        return self.conn
    
    def get_time_series(
        self,
        sensor_id: str,
        start_time: datetime,
        end_time: datetime,
        bucket_size: str = '1 hour'
    ) -> List[Dict]:
        """Get time-bucketed data"""
        conn = self.connect()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        query = """
            SELECT 
                time_bucket(%s, time) AS bucket,
                AVG(value) AS avg_value,
                MIN(value) AS min_value,
                MAX(value) AS max_value,
                COUNT(*) AS count
            FROM sensor_readings
            WHERE sensor_id = %s
              AND time BETWEEN %s AND %s
            GROUP BY bucket
            ORDER BY bucket
        """
        cursor.execute(query, (bucket_size, sensor_id, start_time, end_time))
        results = cursor.fetchall()
        cursor.close()
        return results
    
    def get_hvac_efficiency(
        self,
        equipment_id: str,
        hours: int = 24
    ) -> Dict:
        """Calculate HVAC equipment efficiency (COP/EER)"""
        conn = self.connect()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        query = """
            WITH equipment_data AS (
                SELECT 
                    time_bucket('15 minutes', time) AS bucket,
                    AVG(CASE WHEN sensor_type = 'CoolingOutput' THEN value END) AS cooling_kw,
                    AVG(CASE WHEN sensor_type = 'PowerInput' THEN value END) AS power_kw
                FROM sensor_readings
                WHERE equipment_id = %s
                  AND time >= NOW() - INTERVAL '%s hours'
                GROUP BY bucket
            )
            SELECT 
                bucket,
                cooling_kw,
                power_kw,
                CASE 
                    WHEN power_kw > 0 THEN cooling_kw / power_kw 
                    ELSE NULL 
                END AS cop
            FROM equipment_data
            WHERE cooling_kw IS NOT NULL AND power_kw IS NOT NULL
            ORDER BY bucket DESC
        """
        cursor.execute(query, (equipment_id, hours))
        results = cursor.fetchall()
        cursor.close()
        return results
    
    def get_thermal_comfort(self, zone_id: str, hours: int = 24) -> Dict:
        """Calculate thermal comfort metrics"""
        conn = self.connect()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        query = """
            SELECT 
                AVG(value) AS avg_temp,
                MIN(value) AS min_temp,
                MAX(value) AS max_temp,
                STDDEV(value) AS temp_variance,
                COUNT(*) FILTER (WHERE value < 20 OR value > 24) AS out_of_comfort_count,
                COUNT(*) AS total_readings
            FROM sensor_readings
            WHERE zone_id = %s
              AND sensor_type = 'ZoneTemp'
              AND time >= NOW() - INTERVAL '%s hours'
        """
        cursor.execute(query, (zone_id, hours))
        result = cursor.fetchone()
        cursor.close()
        return result or {}
    
    def bulk_insert(self, readings: List[Dict]):
        """Bulk insert sensor readings"""
        conn = self.connect()
        cursor = conn.cursor()
        
        query = """
            INSERT INTO sensor_readings 
            (time, sensor_id, sensor_type, zone_id, equipment_id, value, unit)
            VALUES %s
        """
        
        values = [
            (
                r.get('time', datetime.now()),
                r['sensor_id'],
                r['sensor_type'],
                r.get('zone_id'),
                r.get('equipment_id'),
                r['value'],
                r.get('unit')
            )
            for r in readings
        ]
        
        execute_values(cursor, query, values)
        conn.commit()
        cursor.close()
```

### Advanced Queries

```sql
-- Time-weighted average (accounts for irregular sampling)
SELECT 
    sensor_id,
    time_weight('average', time, value) AS weighted_avg
FROM sensor_readings
WHERE time >= NOW() - INTERVAL '24 hours'
GROUP BY sensor_id;

-- Gap filling (interpolate missing data)
SELECT 
    time_bucket_gapfill('5 minutes', time) AS bucket,
    sensor_id,
    AVG(value) AS avg_value,
    interpolate(AVG(value)) AS interpolated_value
FROM sensor_readings
WHERE time >= NOW() - INTERVAL '1 hour'
GROUP BY bucket, sensor_id;

-- First and last values in time range
SELECT 
    sensor_id,
    first(value, time) AS first_value,
    last(value, time) AS last_value,
    last(time, time) AS last_timestamp
FROM sensor_readings
WHERE time >= NOW() - INTERVAL '24 hours'
GROUP BY sensor_id;
```

---

## Cassandra Integration (Building 3)

### Configuration

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

### Schema Design

```cql
-- Create keyspace with replication
CREATE KEYSPACE IF NOT EXISTS telemetry_bldg3
WITH replication = {
    'class': 'SimpleStrategy',
    'replication_factor': 1  -- Change to 3 for production cluster
};

USE telemetry_bldg3;

-- Sensor readings (partition by sensor, cluster by time)
CREATE TABLE IF NOT EXISTS sensor_data (
    sensor_uuid UUID,
    timestamp TIMESTAMP,
    value DOUBLE,
    unit TEXT,
    zone TEXT,
    equipment_type TEXT,
    equipment_id TEXT,
    sensor_type TEXT,
    quality_flag INT,
    PRIMARY KEY ((sensor_uuid), timestamp)
) WITH CLUSTERING ORDER BY (timestamp DESC)
  AND compaction = {
      'class': 'TimeWindowCompactionStrategy',
      'compaction_window_unit': 'HOURS',
      'compaction_window_size': '24'
  }
  AND default_time_to_live = 31536000;  -- 1 year TTL

-- Alarms (partition by equipment, cluster by time)
CREATE TABLE IF NOT EXISTS alarms (
    alarm_id UUID,
    equipment_id TEXT,
    timestamp TIMESTAMP,
    severity TEXT,
    equipment_type TEXT,
    message TEXT,
    acknowledged BOOLEAN,
    acknowledged_by TEXT,
    acknowledged_at TIMESTAMP,
    PRIMARY KEY ((equipment_id), timestamp)
) WITH CLUSTERING ORDER BY (timestamp DESC);

-- Equipment status (single partition per equipment)
CREATE TABLE IF NOT EXISTS equipment_status (
    equipment_id TEXT PRIMARY KEY,
    equipment_type TEXT,
    zone TEXT,
    status TEXT,
    last_updated TIMESTAMP,
    metadata MAP<TEXT, TEXT>
);

-- Hourly aggregates (partition by sensor and day)
CREATE TABLE IF NOT EXISTS hourly_aggregates (
    sensor_uuid UUID,
    date DATE,
    hour TIMESTAMP,
    avg_value DOUBLE,
    min_value DOUBLE,
    max_value DOUBLE,
    sample_count INT,
    PRIMARY KEY ((sensor_uuid, date), hour)
) WITH CLUSTERING ORDER BY (hour DESC);

-- Zone rollups (partition by zone and day)
CREATE TABLE IF NOT EXISTS zone_rollups (
    zone TEXT,
    sensor_type TEXT,
    date DATE,
    hour TIMESTAMP,
    avg_value DOUBLE,
    min_value DOUBLE,
    max_value DOUBLE,
    PRIMARY KEY ((zone, sensor_type, date), hour)
) WITH CLUSTERING ORDER BY (hour DESC);
```

### Python Client

```python
# cassandra_client.py
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.query import SimpleStatement, BatchStatement, BatchType
from datetime import datetime, timedelta
import uuid
from typing import List, Dict, Optional
import os

class CassandraClient:
    def __init__(self):
        self.hosts = os.getenv('CASSANDRA_HOSTS', 'cassandra').split(',')
        self.port = int(os.getenv('CASSANDRA_PORT', 9042))
        self.keyspace = os.getenv('CASSANDRA_KEYSPACE', 'telemetry_bldg3')
        
        self.cluster = Cluster(self.hosts, port=self.port)
        self.session = self.cluster.connect(self.keyspace)
    
    def get_sensor_data(
        self,
        sensor_uuid: str,
        start_time: datetime,
        end_time: datetime
    ) -> List[Dict]:
        """Get sensor readings in time range"""
        query = """
            SELECT timestamp, value, unit, equipment_id
            FROM sensor_data
            WHERE sensor_uuid = ?
              AND timestamp >= ?
              AND timestamp <= ?
            ORDER BY timestamp DESC
        """
        statement = SimpleStatement(query, fetch_size=1000)
        rows = self.session.execute(statement, (uuid.UUID(sensor_uuid), start_time, end_time))
        return [dict(row) for row in rows]
    
    def get_active_alarms(
        self,
        equipment_id: Optional[str] = None,
        severity: Optional[str] = None
    ) -> List[Dict]:
        """Get active (unacknowledged) alarms"""
        if equipment_id:
            query = """
                SELECT * FROM alarms
                WHERE equipment_id = ?
                  AND acknowledged = false
                ORDER BY timestamp DESC
            """
            rows = self.session.execute(query, (equipment_id,))
        else:
            # Note: This requires ALLOW FILTERING or secondary index
            query = """
                SELECT * FROM alarms
                WHERE acknowledged = false
                ALLOW FILTERING
            """
            rows = self.session.execute(query)
        
        return [dict(row) for row in rows]
    
    def calculate_pue(self, timestamp: Optional[datetime] = None) -> Optional[float]:
        """Calculate Power Usage Effectiveness"""
        if timestamp is None:
            timestamp = datetime.now()
        
        # Get total facility power
        total_power = self._get_latest_reading('total-facility-power-uuid', timestamp)
        
        # Get IT equipment power
        it_power = self._get_latest_reading('it-equipment-power-uuid', timestamp)
        
        if total_power and it_power and it_power > 0:
            return total_power / it_power
        return None
    
    def _get_latest_reading(self, sensor_uuid: str, before: datetime) -> Optional[float]:
        """Get latest reading before timestamp"""
        query = """
            SELECT value FROM sensor_data
            WHERE sensor_uuid = ?
              AND timestamp <= ?
            ORDER BY timestamp DESC
            LIMIT 1
        """
        row = self.session.execute(query, (uuid.UUID(sensor_uuid), before)).one()
        return row.value if row else None
    
    def insert_reading(
        self,
        sensor_uuid: str,
        value: float,
        unit: str,
        equipment_id: str,
        sensor_type: str,
        timestamp: Optional[datetime] = None
    ):
        """Insert single sensor reading"""
        if timestamp is None:
            timestamp = datetime.now()
        
        query = """
            INSERT INTO sensor_data 
            (sensor_uuid, timestamp, value, unit, equipment_id, sensor_type)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        self.session.execute(
            query,
            (uuid.UUID(sensor_uuid), timestamp, value, unit, equipment_id, sensor_type)
        )
    
    def bulk_insert(self, readings: List[Dict]):
        """Bulk insert sensor readings using batch"""
        batch = BatchStatement(batch_type=BatchType.UNLOGGED)
        
        query = """
            INSERT INTO sensor_data 
            (sensor_uuid, timestamp, value, unit, equipment_id, sensor_type)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        
        for reading in readings:
            batch.add(query, (
                uuid.UUID(reading['sensor_uuid']),
                reading.get('timestamp', datetime.now()),
                reading['value'],
                reading.get('unit'),
                reading.get('equipment_id'),
                reading.get('sensor_type')
            ))
        
        self.session.execute(batch)
    
    def acknowledge_alarm(self, alarm_id: str, acknowledged_by: str):
        """Acknowledge an alarm"""
        query = """
            UPDATE alarms
            SET acknowledged = true,
                acknowledged_by = ?,
                acknowledged_at = ?
            WHERE alarm_id = ?
        """
        self.session.execute(
            query,
            (acknowledged_by, datetime.now(), uuid.UUID(alarm_id))
        )
    
    def close(self):
        """Close connection"""
        self.cluster.shutdown()
```

### Performance Tuning

```cql
-- Change compaction strategy for time-series
ALTER TABLE sensor_data
WITH compaction = {
    'class': 'TimeWindowCompactionStrategy',
    'compaction_window_unit': 'HOURS',
    'compaction_window_size': '24'
};

-- Add TTL for automatic data expiration
ALTER TABLE sensor_data
WITH default_time_to_live = 31536000;  -- 1 year

-- Adjust read/write consistency
-- In Python client:
from cassandra import ConsistencyLevel
statement = SimpleStatement(query, consistency_level=ConsistencyLevel.LOCAL_QUORUM)
```

---

## Comparison & Best Practices

### When to Use Each Database

**MySQL:**
- ✅ Structured data with relationships
- ✅ ACID transactions required
- ✅ Complex joins and aggregations
- ✅ Mature ecosystem and tools
- ❌ Limited horizontal scalability
- ❌ Not optimized for time-series

**TimescaleDB:**
- ✅ Time-series data (sensor readings)
- ✅ Automatic partitioning by time
- ✅ 90%+ compression
- ✅ PostgreSQL compatibility
- ✅ Continuous aggregates
- ❌ Single-server (vertical scaling)

**Cassandra:**
- ✅ High availability required
- ✅ Massive write throughput
- ✅ Linear horizontal scalability
- ✅ Geographic distribution
- ✅ No single point of failure
- ❌ No joins or transactions
- ❌ Eventual consistency

### Connection Pooling

All clients should use connection pooling:

```python
# MySQL
from mysql.connector import pooling

pool = pooling.MySQLConnectionPool(
    pool_name="ontobot_pool",
    pool_size=10,
    **config
)

# PostgreSQL/TimescaleDB
from psycopg2 import pool

connection_pool = pool.SimpleConnectionPool(
    minconn=1,
    maxconn=10,
    **config
)

# Cassandra (built-in)
cluster = Cluster(hosts, port=port)
session = cluster.connect()
```

### Backup Strategies

```bash
# MySQL
mysqldump -u root -p telemetry > backup.sql

# PostgreSQL/TimescaleDB
pg_dump -U postgres telemetry_bldg2 > backup.sql

# Cassandra
nodetool snapshot telemetry_bldg3
```

---

## Related Documentation

- [Building 1 - ABACWS](/docs/building1_abacws/) - MySQL implementation
- [Building 2 - Office](/docs/building2_office/) - TimescaleDB implementation
- [Building 3 - Data Center](/docs/building3_datacenter/) - Cassandra implementation
- [Analytics API](/docs/analytics_api/) - Database queries via API
- [Multi-Building Support](/docs/multi_building/) - Switching databases

---

**Database Selection Matrix:**

| Requirement | MySQL | TimescaleDB | Cassandra |
|-------------|-------|-------------|-----------|
| Time-series optimization | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| High availability | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Write throughput | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Query flexibility | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Horizontal scalability | ⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| Operational complexity | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
