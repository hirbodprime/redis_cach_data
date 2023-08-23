from django.shortcuts import render
from django.core.cache import cache

def show_cached_data(request):
    cached_data = cache.get("cached_fake_data")  # Fetch cached data
    print(cached_data)
    return render(request, 'cacheddata.html', {'cached_data': cached_data})
