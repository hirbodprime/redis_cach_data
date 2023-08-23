# celery.py
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'redis_fake_data_get.settings')

app = Celery('redis_fake_data_get')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bing=True)
def debug_task(self):
    print('request: {0!r}'.format(self.request))

app.conf.beat_schedule = {
    'fetch-fake-data-every-1-minute': {
        'task': 'get_data.tasks.cache_fake_data',
        'schedule': 60.0,  # 1 minute in seconds
    },
    # Add more periodic tasks here if needed
}

app.conf.timezone = 'UTC'
