# REDIS

# Intallation on Windows

- https://riptutorial.com/redis/example/29962/installing-and-running-redis-server-on-windows

## Redis CLI

```
127.0.0.1:6379> dbsize
(integer) 3
```

```
> redis-cli --bigkeys
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
