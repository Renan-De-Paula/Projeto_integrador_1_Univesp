from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Produto


def home(request):
    """Lista produtos e processa criação via POST."""
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        recheio = request.POST.get('recheio', '').strip()
        categoria = request.POST.get('categoria', '').strip()
        preco = request.POST.get('preco', '').strip()

        if nome and categoria and preco:
            try:
                Produto.objects.create(
                    nome=nome,
                    recheio=recheio,
                    categoria=categoria,
                    preco=float(preco),
                )
                messages.success(request, f'Produto "{nome}" cadastrado com sucesso!')
            except ValueError:
                messages.error(request, 'Preço inválido. Use formato: 50.00')
        else:
            messages.error(request, 'Preencha nome, categoria e preço.')

        return redirect('produtos:home')

    produtos = Produto.objects.all()
    return render(request, 'produtos/home.html', {'produtos': produtos})


def excluir(request, pk):
    """Exclui um produto pelo ID."""
    produto = get_object_or_404(Produto, pk=pk)
    nome = produto.nome
    produto.delete()
    messages.success(request, f'Produto "{nome}" removido.')
    return redirect('produtos:home')


def editar(request, pk):
    """Edita dados de um produto existente."""
    produto = get_object_or_404(Produto, pk=pk)

    if request.method == 'POST':
        produto.nome = request.POST.get('nome', '').strip()
        produto.recheio = request.POST.get('recheio', '').strip()
        produto.categoria = request.POST.get('categoria', '').strip()
        preco = request.POST.get('preco', '').strip()

        try:
            produto.preco = float(preco)
            produto.save()
            messages.success(request, 'Produto atualizado com sucesso!')
            return redirect('produtos:home')
        except ValueError:
            messages.error(request, 'Preço inválido.')

    return render(request, 'produtos/editar.html', {'produto': produto})