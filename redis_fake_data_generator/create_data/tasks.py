# tasks.py
import random
from faker import Faker
from celery import shared_task
import redis

@shared_task
def generate_and_store_fake_data():
    fake = Faker()
    r = redis.Redis(host='localhost', port=6379, db=0)

    light_module_temperature_choices = ('1', '2', '3', '4')
    internal_temp_choices = ('1', '2', '3', '4', '5')
    module_status_choices = ('ON', 'OFF')  

    fake_data = {
        "light_module_temperature": random.choice(light_module_temperature_choices),
        "internal_temperature": random.choice(internal_temp_choices),
        "fan_status": random.choice(fan_status_choices),
        "module_status": random.choice(module_status_choices),
    }

    r.hmset("fake_data", fake_data)

