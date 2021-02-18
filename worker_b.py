from celery import Celery

# Celery configuration
CELERY_BROKER_URL = 'amqp://guest:guest@tfcd_rabbit:5672/'
CELERY_RESULT_BACKEND = 'rpc://'

# Initialize Celery
celery = Celery('worker_b',
                broker=CELERY_BROKER_URL,
                backend=CELERY_RESULT_BACKEND)

@celery.task()
def sub_nums(a, b):
   result = a - b
   print(f'\nsub_nums({a}, {b}): {result}')
   return result
