# celery.py in your second project
from celery import Celery
from celery.schedules import crontab

app = Celery('redis_fake_data_get')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'fetch-fake-data-every-1-minute': {
        'task': 'redis_fake_data_get.tasks.fetch_fake_data',
        'schedule': 60.0,  # 1 minute in seconds
    },
    # Add more periodic tasks here if needed
}

app.conf.timezone = 'UTC'
