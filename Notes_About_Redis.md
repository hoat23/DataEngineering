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

### Download image

- https://github.com/MicrosoftArchive/redis/releases

### Restart service or set path.config
```bash
redis-cli.exe
shutdown
exit
redis-server.exe pathtoconfig
```

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

### Connecting a Redis-Server
#### Localhost
```
> redis-cli
```

#### External host
```
> redis-cli -h www.myredishost.com  -p 6379
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
## S-commands

### Adding registers
```bash
127.0.0.1:6379>sadd users_ip 10.0.0.1
127.0.0.1:6379>sadd users_ip 10.0.0.2 10.0.0.3 10.0.0.4
```
Adding other list of IP
```bash
127.0.0.1:6379>sadd yesterday_ip 10.0.0.2 10.0.0.6 10.0.0.4 10.0.0.2 10.0.0.3 10.0.0.4
```
### Showing all registers by key
```bash
127.0.0.1:6379>smembers users_ip
```
### Difference of registers
```bash
127.0.0.1:6379>sdiff yesterday_ip users_ip
```
### Checking if a registers in a key
```bash
127.0.0.1:6379>sismember yesterday_ip 10.0.0.2
(integer) 1
```
### Remove a registers
```bash
127.0.0.1:6379>srem yesterday_ip 10.0.0.1
```
### Remove all keys
```
127.0.0.1:6379> flushall
```
### Print keys created
```bash
127.0.0.1:6379>keys *
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
