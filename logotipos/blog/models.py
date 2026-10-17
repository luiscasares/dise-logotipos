"""
Modelos del blog
"""
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Category(models.Model):
    """
    Categorías
    """
    name = models.CharField(max_length=100, verbose_name="Nombre", help_text="Nombre categoría Blogs")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        """
        Meta datos categorías
        """
        verbose_name = "categoría"
        verbose_name_plural = "categorías"

    def __str__(self):
        return str(self.name)


class Post(models.Model):
    """
    Clase entradas de blog
    """
    title = models.CharField(max_length=200, verbose_name="Título", help_text="Título de la entrada")
    content = models.TextField(verbose_name="Contenido", help_text="Contenido de la entrada")
    published = models.DateTimeField(default=now, verbose_name="Fecha de publicación")
    image = models.ImageField(upload_to="blog", null=True, blank=True, verbose_name="Imagen")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    categories = models.ManyToManyField(Category, verbose_name="Categorías",related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        """
        Meta datos de Entrada
        """
        verbose_name = "entrada"
        verbose_name_plural = "entradas"

    def __str__(self):
        return str(self.title)
