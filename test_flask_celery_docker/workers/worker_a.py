from celery import Celery

# Celery configuration
CELERY_BROKER_URL = 'amqp://guest:guest@tfcd_rabbit:5672//'
CELERY_RESULT_BACKEND = 'rpc://'

# Initialize Celery
celery = Celery('tfcd.workers.worker_a',  # celery name
                broker=CELERY_BROKER_URL,
                backend=CELERY_RESULT_BACKEND)

celery.conf.broker_transport_options = {
    'max_retries': 3,
    'interval_start': 0,
    'interval_step': 0.2,
    'interval_max': 0.5
}

@celery.task(queue='worker_a', name='tfcd.workers.worker_a.add_nums')
def add_nums(a, b):
   result = a + b
   print(f'\nadd_nums({a}, {b}): {result}\n')
   return result
