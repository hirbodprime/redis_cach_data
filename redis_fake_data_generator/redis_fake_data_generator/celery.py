# celery.py

import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'redis_fake_data_generator.settings')

app = Celery('redis_fake_data_generator')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


app.conf.beat_schedule = {
    'generate-fake-data-every-2-minutes': {
        'task': 'redis_fake_data_generator.tasks.generate_and_store_fake_data',
        'schedule': 120.0,  # 2 minutes in seconds
    },
    # Add more periodic tasks here if needed
}

app.conf.timezone = 'UTC'
