"""
Vistas
"""
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import WhatsAppConfig

# Create your views here.
@require_POST
def registrar_clic_whatsapp(request):
    """
    Metodo para contabilizar WhatsApp
    """
    config = WhatsAppConfig.load()
    config.clics += 1
    config.save(update_fields=['clics'])
    return JsonResponse({'status':'ok', 'clics':config.clics})
