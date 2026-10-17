"""
Admin
"""
from django.contrib import admin
from .models import WhatsAppConfig

# Register your models here.
@admin.register(WhatsAppConfig)
class WhatsAppConfigAdmin(admin.ModelAdmin):
    """
    Administrador
    """
    list_display = ('__str__', 'telefono', 'clics')
    readonly_fields = ('clics', 'fecha_creacion')

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return True

    def has_delete_permission(self, request, obj = None):
        return False
