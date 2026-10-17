from django.shortcuts import render
from .models import Service

# Create your views here.
def servicios(request):
    """Función del servicios"""
    services = Service.objects.all()
    return render(request, "services/servicios.html", {'services':services})
