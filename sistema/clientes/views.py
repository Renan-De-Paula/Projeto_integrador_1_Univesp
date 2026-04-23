from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Cliente


def home(request):
    """Lista clientes e processa criação via POST."""
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        telefone = request.POST.get('telefone', '').strip()
        email = request.POST.get('email', '').strip()

        if nome and telefone and email:
            Cliente.objects.create(nome=nome, telefone=telefone, email=email)
            messages.success(request, f'Cliente "{nome}" cadastrado com sucesso!')
        else:
            messages.error(request, 'Preencha todos os campos obrigatórios.')

        return redirect('clientes:home')

    clientes = Cliente.objects.all()
    return render(request, 'clientes/home.html', {'clientes': clientes})


def excluir(request, pk):
    """Exclui um cliente pelo ID."""
    cliente = get_object_or_404(Cliente, pk=pk)
    nome = cliente.nome
    cliente.delete()
    messages.success(request, f'Cliente "{nome}" removido.')
    return redirect('clientes:home')


def editar(request, pk):
    """Edita dados de um cliente existente."""
    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == 'POST':
        cliente.nome = request.POST.get('nome', '').strip()
        cliente.telefone = request.POST.get('telefone', '').strip()
        cliente.email = request.POST.get('email', '').strip()

        if cliente.nome and cliente.telefone and cliente.email:
            cliente.save()
            messages.success(request, 'Cliente atualizado com sucesso!')
            return redirect('clientes:home')
        else:
            messages.error(request, 'Preencha todos os campos.')

    return render(request, 'clientes/editar.html', {'cliente': cliente})