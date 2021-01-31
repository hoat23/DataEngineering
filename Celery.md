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

## Documentation
- https://docs.celeryproject.org/en/stable/getting-started/next-steps.html#project-layout
