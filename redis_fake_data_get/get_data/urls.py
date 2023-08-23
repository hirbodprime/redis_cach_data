from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('cached-data/', views.show_cached_data, name='show_cached_data'),
]
