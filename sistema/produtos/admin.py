from django.contrib import admin
from .models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'recheio', 'preco')
    list_filter = ('categoria',)
    search_fields = ('nome', 'recheio')
    ordering = ('categoria', 'nome')