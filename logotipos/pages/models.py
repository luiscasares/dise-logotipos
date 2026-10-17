"""
Modelos
"""
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    """
    Modelo de la clase pages
    """
    title = models.CharField(max_length=200, verbose_name="Título")
    content = RichTextField(verbose_name="Contenido", help_text="Editor de texto avanzado")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        """
        Meta
        """
        verbose_name = "Página"
        verbose_name_plural = "Páginas"
        ordering = ['order','title']
    def __str__(self):
        return str(self.title)
