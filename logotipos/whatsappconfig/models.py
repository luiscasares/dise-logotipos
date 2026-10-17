"""
Modelo de WhatsApp
"""
from django.db import models
from urllib.parse import quote

# Create your models here.
class WhatsAppConfig(models.Model):
    """
    Modelo para WhatsApp
    """
    telefono = models.CharField(max_length=12, help_text="Incluye el código de país sin el signo de +, ej: 52729123456", verbose_name="Teléfono")
    mensaje = models.CharField(max_length=255, help_text="Mensaje predeterminado", verbose_name="Mensaje")
    clics = models.PositiveIntegerField(default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Configuración de WhatsApp"
        verbose_name_plural = "Configuracion de WhatsApp"

    def save(self, *args, **kwargs):
        self.pk = 1
        super(WhatsAppConfig, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    def get_whatsapp_url(self):
        mensaje_condificado = quote(self.mensaje if self.mensaje else "")
        return f"https://wa.me/{self.telefono}?text=={mensaje_condificado}"

    def __str__(self):
        return "Ajustes del Widget de WhatsApp"
