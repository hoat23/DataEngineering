# CELERY

### Celery in an Application

#### Proyect Layout

```python
proj/__init__.py
    /celery.py
    /tasks.py
```

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
```

##### Execute Celery Server
```
celery -A proj worker -l INFO
```
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
