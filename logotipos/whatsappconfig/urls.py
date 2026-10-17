"""
URLS
"""
from django.urls import path
from . import views

app_name = 'whatsappconfig'

urlpatterns = [
    path('track-click/', views.registrar_clic_whatsapp, name='track_click'),
]
