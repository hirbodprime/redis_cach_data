import redis
from celery import shared_task
from django.core.cache import cache

@shared_task
def cache_fake_data():
    print('data caching started')
    r = redis.Redis(host='localhost', port=6379, db=0)
    fake_data = r.hgetall("fake_data")
    print(fake_data)
    cache.set("cached_fake_data", fake_data) 
