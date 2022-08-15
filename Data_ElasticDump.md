# ELASTICDUMP



## Input

### Basic auth
- If you need basic http auth, you can use it like this: ```--input=http://name:password@production.es.com:9200/my_index```
- TLS X509 client authentication (Check the docs)

### Limit download

- Max document by dowload. Example: ```--limit=10000```

## Output

### Saving in json format

```--output=Desktop/file.json```

- If you need save only data information add: ```--type=data```
 
## Comments

Something is need to add a flag lik : ```NODE_TLS_REJECT_UNAUTHORIZED=0```


### Documentation

- https://github.com/elasticsearch-dump/elasticsearch-dump 
- https://blog.logrocket.com/a-practical-guide-to-working-with-elasticdump/ 
