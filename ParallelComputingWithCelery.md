# CELERY

### Celery in an Application

#### Proyect Layout

```python
proj/__init__.py
    /celery.py
    /tasks.py
first_app.py
```
Documentation
- https://medium.com/analytics-vidhya/asynchronous-tasks-in-python-with-celery-e6a9d7e3b33d
#### proj/celery.py
```python
from celery import Celery
app = Celery('proj', 
             broker = 'amqp://',
             backend = 'rpc://',
             include = ['proj.tasks'])
# Optional configuration, see the application user guide
app.conf.update( 
  result_expires=3600,
)

if __name__=='__main__':
   app.start()
```

#### proj/tasks.py
```python
#from proj.celery import app
import celery
from .celery import app
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@app.task(bind=True)
def add(x,y):
	logger.info("{0} + {1} = {2}".format(x,y,x+y))
	return x+y

@app.task(bind=True)
def mult(x,y):
	logger.info("{0} + {1} = {2}".format(x,y,x*y))
	return x*y

@app.task(bind=True)
def sum(numbers):
	logger.info("sum of numbers")
	return sum(numbers)
```

#### Runing tasks

```python
from proj.tasks import add

# Asyncronous
rpt = add.delay(3,4) 
print(rpt.id) # print task id
print( rpt.get(timeout=1) )

# Syncronous
rpt = add(3,4)
print(rpt)

# Get status
# happy track   : "PENDING -> STARTED -> SUCCESS"
# not so happy  : "PENDING -> STARTED -> RETRY -> STARTED -> RETRY -> STARTED -> SUCCESS"
while a.state!='SUCCESS':
   # code here!
   ...

# Runing by steps
## Normal
s1 = add.s(2, 2)
res = s1.delay()
res.get()

## Special
# incomplete partial: add(?, 2)
s2 = add.s(2)
# resolves the partial: add(8, 2)
res = s2.delay(8)
res.get()

```
## Commands Line

##### Execute Celery Server
```
celery -A proj worker -l INFO
```

##### Monitoring tasks and workers
Enable monitoring
```
celery -A proj control1 enable_event
```
See the workers are doing
```
# events
celery -A proj events
# dumps
celery -A proj events --dump
```
Disable monitoring
```
celery -A proj control disable_event
```

##### 


Options:
-  -A, --app APPLICATION
-  -b, --broker TEXT
-  --result-backend TEXT
-  --loader TEXT
-  --config TEXT
-  --workdir PATH
-  -C, --no-color
-  -q, --quiet
-  --version
-  --help

## Documentation
- https://docs.celeryproject.org/en/stable/getting-started/next-steps.html#project-layout
- https://www.impactian.com/python/ray-vs-dask-vs-celery-the-road-to-parallel-computing (*)
