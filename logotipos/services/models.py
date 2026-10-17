from django.db import models

# Create your models here.
# Modelo de la descripcióin de servicio
class Service(models.Model):
    """
    Modelo para los servicios
    """
    title = models.CharField(max_length=150, verbose_name="Título")
    subtitle = models.CharField(max_length=150, verbose_name="Subtítulo")
    content = models.TextField(max_length=300, verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen", upload_to="services/images/%Y/%m/%d/" )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        """
        Meta datos
        """
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ['-created']

    def __str__(self):
        return str(self.title)
