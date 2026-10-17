"""
Formulario de contacto general
"""
from django import forms

class ContactForm(forms.Form):
    """
    Clase y modelo del formulario de contacto
    """
    nombre = forms.CharField(label="Nombre", min_length=3, max_length=100, required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Escribe tu nombre', 'class':'form-control'}))
    email = forms.EmailField(label="Email", required=True, max_length=100,
                             widget=forms.EmailInput(attrs={'placeholder':'Escribe tu email', 'class':'form-control'}))
    asunto = forms.CharField(label="Asunto", required=True, min_length=10, max_length=40,
                             widget=forms.TextInput(attrs={'placeholder':'Asunto', 'class':'form-control'}))
    mensaje = forms.CharField(label="Contenido", required=True, min_length=10, max_length=200,
                               widget= forms.Textarea(attrs={'placeholder':'Describe tu proyecto','class':'form-control','rows':3}))
