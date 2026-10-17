"""
Formularios de contacto
"""
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
# Create your views here.
def contacto(request):
    """Función de Contacto"""
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            nombre = contact_form.cleaned_data.get('nombre', '')
            email = contact_form.cleaned_data.get('email', '')
            asunto = contact_form.cleaned_data.get('asunto', '')
            mensaje = contact_form.cleaned_data.get('mensaje', '')
             # Creamos el correo
            email = EmailMessage(
                "Nuevo Mensaje Diseño Logotipos{}".format(asunto),
                "De {} <{}>\n\nEscribió:\n\n{}".format(nombre, email, mensaje),
                "no-reply@refillcreativo.com.mx",
                ["contacto@refillcreativo.com.mx"],
                reply_to=[email]
            )


            # Lo enviamos y redireccionamos
            try:
                email.send()
                # Todo ha ido bien, redireccionamos a OK
                return redirect(reverse('contact')+"?ok")
            except:
                # Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact')+"?fail")  
    return render(request, "contacto/contacto.html",{'form':contact_form})
