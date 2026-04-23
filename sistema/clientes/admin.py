from django.contrib import admin
from .models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email', 'criado_em')
    search_fields = ('nome', 'email', 'telefone')
    ordering = ('nome',)