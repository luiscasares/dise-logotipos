"""
Procesadores de contexto
"""
from .models import WhatsAppConfig

def whatsapp_widget(request):
    """
    Configuracion de app de WhatsApp
    """
    return{
        'whatsapp_config':WhatsAppConfig.load()
    }
