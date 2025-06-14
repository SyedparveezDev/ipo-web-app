# ipo_app/urls.py

from django.urls import path
from .views import IPOListAPIView

urlpatterns = [
    path('api/ipo/', IPOListAPIView.as_view(), name='ipo-list'),
]
