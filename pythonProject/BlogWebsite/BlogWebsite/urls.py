from django.contrib import admin
from django.urls import path, include  # Make sure to include 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Include your app's URLs here
    # Add more URL patterns as needed
]
