#from proj.celery import app
import celery
from .celery import app
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@app.task(bind=True)
def add(self,x,y):
	logger.info("task.id.add  [{0}]".format(self.request.id))
	logger.info("{0} + {1} = {2}".format(x,y,x+y))
	return x+y

@app.task(bind=True)
def mult(self,x,y):
	logger.info("task.id.mult [{0}]".format(self.request.id))
	logger.info("{0} + {1} = {2}".format(x,y,x*y))
	return x*y

@app.task(bind=True)
def sum(self,numbers):
	logger.info("task.id.mult [{0}]".format(self.request.id))
	logger.info("sum of numbers")
	return sum(numbers)
