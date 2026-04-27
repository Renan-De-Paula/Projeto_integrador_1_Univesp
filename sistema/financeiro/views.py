from django.shortcuts import render
from pedidos.models import Pedido
from django.db.models import Sum


def home(request):
    pedidos = Pedido.objects.select_related('cliente', 'produto').all()

    # CORREÇÃO: usa os nomes de status com maiúscula conforme MODEL CHOICES
    total_entradas = pedidos.filter(status='Entregue').aggregate(
        total=Sum('valor')
    )['total'] or 0

    total_pendente = pedidos.filter(status='Pendente').aggregate(
        total=Sum('valor')
    )['total'] or 0

    total_cancelado = pedidos.filter(status='Cancelado').aggregate(
        total=Sum('valor')
    )['total'] or 0

    # total_geral = entregues + pendentes (cancelados não contam)
    total_geral = total_entradas + total_pendente

    context = {
        'total_entradas': total_entradas,
        'total_pendente': total_pendente,
        'total_cancelado': total_cancelado,
        'total_geral': total_geral,
        'pedidos': pedidos,
    }

    return render(request, 'financeiro/home.html', context)
