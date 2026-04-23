from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Sum
from pedidos.models import Pedido


def home(request):
    """Exibe resumo financeiro baseado nos pedidos."""
    pedidos = Pedido.objects.select_related('cliente', 'produto').all()

    # Cálculos financeiros
    total_entradas = pedidos.filter(status='Entregue').aggregate(
        total=Sum('valor')
    )['total'] or 0

    total_pendentes = pedidos.filter(status='Pendente').aggregate(
        total=Sum('valor')
    )['total'] or 0

    total_geral = total_entradas + total_pendentes

    return render(request, 'financeiro/home.html', {
        'pedidos': pedidos,
        'total_entradas': f'{total_entradas:.2f}',
        'total_pendentes': f'{total_pendentes:.2f}',
        'total_geral': f'{total_geral:.2f}',
    })