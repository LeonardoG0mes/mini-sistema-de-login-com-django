from django.contrib import admin
from .models import PerfilUsuario

class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ['user', 'codigo_autenticacao']
    list_filter = ['codigo_autenticacao']
    search_fields = ['user__username', 'user__email']

# Registre o modelo Usuario com a classe de admin personalizada
admin.site.register(PerfilUsuario, PerfilUsuarioAdmin)
