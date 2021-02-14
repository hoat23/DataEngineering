# REDIS

## Redis Python Connector for Read, Write, and Updae Redis with Python

### Instalation Redis-Python Connector 
- https://www.cdata.com/drivers/redis/python/

### Features
- Compatible with Redis and Redis Enterprise
- Seamlessly convert key-value stores into relational tables.
- Enables SQL-92 capabilities on Redis No-SQL data.
- Connect to live Redis data, for real-time access
- Full support for data aggregation and complex JOINS in SQL query.
- Secure connectivity through modern cryptography, including TLS 1.2, SHA-256, ECC, etc.
- Seamless integration with leading BI, reporting, and ETL tools and with custom applications.


### Examples

#### Connecting Redis in Python
```python
import cdata.redis as mod
conn = mod.connect("User=user@domain.com; Password=password;")
 
#Create cursor and iterate over results
cur = conn.cursor()
cur.execute("SELECT * FROM RedisCache")
 
rs = cur.fetchall()
 
for row in rs:
print(row)
```

## Intallation  Redis on Windows

- https://riptutorial.com/redis/example/29962/installing-and-running-redis-server-on-windows

## Redis CLI

```
127.0.0.1:6379> dbsize
(integer) 3
```

```
> redis-cli --bigkeys
```

### Connecting to redis in another ip
```bash
> redis-cli -h 192.168.43.103
```
Disable protected-mode
```bash
C:\Users\Hoat23>redis-cli
127.0.0.1:6379> CONFIG SET protected-mode no
```
### PubSub on Redis

#### Creating a Channel in Redis-CLI
```
127.0.0.1:6379> subscribe MyChannel
```
#### Publishing message on Channel
```
127.0.0.1:6379> PUBLISH MyChannel 'Hola mundo'
```
## Python

```python
import redis
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool = pool)
r.mset({'Croatia': 'zagreb', 'Bahamas': 'nassau'})
r.mget('Bahamas')
r.keys()
r.flushdb()
```
