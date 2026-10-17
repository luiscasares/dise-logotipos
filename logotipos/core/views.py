"""
Vistas Generales
"""
from django.shortcuts import render

# Create your views here.
def home(request):
    """Función de saludo"""
    return render(request, "core/home.html")

def about(request):
    """Función de acerca"""
    return render(request, "core/acerca.html")

def portafolio(request):
    """Función de portafolio de proyectos"""
    return render(request, "core/portafolio.html")

