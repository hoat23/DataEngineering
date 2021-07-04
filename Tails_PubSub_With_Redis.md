# REDIS

## Redis Python Connector for Read, Write, and Updae Redis with Python


### Features
- Compatible with Redis and Redis Enterprise
- Seamlessly convert key-value stores into relational tables.
- Enables SQL-92 capabilities on Redis No-SQL data.
- Connect to live Redis data, for real-time access
- Full support for data aggregation and complex JOINS in SQL query.
- Secure connectivity through modern cryptography, including TLS 1.2, SHA-256, ECC, etc.
- Seamless integration with leading BI, reporting, and ETL tools and with custom applications.

## Intallation  Redis on Windows

- https://riptutorial.com/redis/example/29962/installing-and-running-redis-server-on-windows

## Installation Redis on Ubuntu
1. Installing redis-server
```
sudo apt update
sudo apt install redis-server
```
2. Open with nano ```sudo nano /etc/redis/redis.conf```
3. Find ```supervised``` and change ```no``` by ```systemd```
4. Exit and save changes.
5. Restart redis server ```sudo systemctl restart redis.service```
6. Check status with ```sudo systemctl status redis```

If want stop service use this command ```sudo systemctl disable redis```

### Check redis network
```
sudo netstat -lnp | grep redis
```

### More Documentation
- https://www.digitalocean.com/community/tutorials/como-instalar-y-proteger-redis-en-ubuntu-18-04-es

## Redis CLI Commands

### Start Redis-Server
#### On Windows
```
> redis-server
```

### Exploring DB
```
127.0.0.1:6379> dbsize
(integer) 3
```

```
> redis-cli --bigkeys
```
### Monitoring redis
Monitoring de commands
```bash
> redis-cli monitor
```
results:
```
OK
1460100081.165665 [0 127.0.0.1:51706] "set" "foo" "bar"
1460100083.053365 [0 127.0.0.1:51707] "get" "foo"
```

Monitoring latency to responses.
```bash
> redis-cli --latency
```
results:
```
min: 0, max: 1, avg: 0.19 (427 samples)
```

Monitoring latency in disk
```bash
> redis-cli --latency-dist
``` 

Monitoring latency history
```bash
> redis-cli --latency-history
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
## Pub-Sub Pattern on Redis

### in CLI

#### Creating a Channel in Redis-CLI
```
127.0.0.1:6379> subscribe MyChannel
```
#### Publishing message on Channel
```
127.0.0.1:6379> PUBLISH MyChannel 'Hola mundo'
```
## Python

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

### Put and Get data on Redis using Python
```python
import redis
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool = pool)
r.mset({'Croatia': 'zagreb', 'Bahamas': 'nassau'})
r.mget('Bahamas')
r.keys()
r.flushdb()
```

### Installation Redis-Python Connector 
- https://www.cdata.com/drivers/redis/python/

## Documentation

- https://tech.webinterpret.com/redis-notifications-python/
- https://itnext.io/event-data-pipelines-with-redis-pub-sub-async-python-and-dash-ab0a7bac63b0
- https://www.linuxtechi.com/install-redis-server-on-centos-8-rhel-8/
- https://redis.io/topics/rediscli
