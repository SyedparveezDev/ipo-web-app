# ipo_app/urls.py

from django.urls import path
from .views import IPOListAPIView

# ipo_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/ipo/', IPOListAPIView.as_view(), name='ipo-list'),
    path('admin/', admin.site.urls),
    path('', include('ipo_app.urls')), 
]


