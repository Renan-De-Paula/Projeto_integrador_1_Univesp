from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Pedido
from clientes.models import Cliente
from produtos.models import Produto


def home(request):
    """Lista pedidos e processa criação via POST."""
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente_id', '').strip()
        produto_id = request.POST.get('produto_id', '').strip()
        kg = request.POST.get('kg', '').strip()

        if cliente_id and produto_id and kg:
            try:
                cliente = Cliente.objects.get(pk=cliente_id)
                produto = Produto.objects.get(pk=produto_id)
                pedido = Pedido(cliente=cliente, produto=produto, kg=float(kg))
                pedido.save()  # save() calcula o valor automaticamente
                messages.success(request, f'Pedido #{pedido.pk} criado com sucesso!')
            except (Cliente.DoesNotExist, Produto.DoesNotExist):
                messages.error(request, 'Cliente ou Produto inválido.')
            except ValueError:
                messages.error(request, 'Quantidade inválida.')
        else:
            messages.error(request, 'Preencha todos os campos.')

        return redirect('pedidos:home')

    pedidos = Pedido.objects.select_related('cliente', 'produto').all()
    clientes = Cliente.objects.all()
    produtos = Produto.objects.all()

    return render(request, 'pedidos/home.html', {
        'pedidos': pedidos,
        'clientes': clientes,
        'produtos': produtos,
    })


def excluir(request, pk):
    """Exclui um pedido pelo ID."""
    pedido = get_object_or_404(Pedido, pk=pk)
    pedido.delete()
    messages.success(request, f'Pedido #{pk} removido.')
    return redirect('pedidos:home')


def alterar_status(request, pk):
    """Alterna o status do pedido entre Pendente e Entregue."""
    pedido = get_object_or_404(Pedido, pk=pk)

    if pedido.status == 'Pendente':
        pedido.status = 'Entregue'
        msg = f'Pedido #{pk} marcado como Entregue.'
    else:
        pedido.status = 'Pendente'
        msg = f'Pedido #{pk} marcado como Pendente.'

    pedido.save()
    messages.success(request, msg)
    return redirect('pedidos:home')