from django.shortcuts import render

def home(request):
    return render(request, 'clientes/home.html') # todo: verificar outra forma de retornar a pagina 
