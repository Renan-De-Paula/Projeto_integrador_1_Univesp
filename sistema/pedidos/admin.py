from django.contrib import admin
from .models import Pedido


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'produto', 'kg', 'valor', 'status', 'criado_em')
    list_filter = ('status',)
    search_fields = ('cliente__nome', 'produto__nome')
    ordering = ('-criado_em',)
    readonly_fields = ('valor',)