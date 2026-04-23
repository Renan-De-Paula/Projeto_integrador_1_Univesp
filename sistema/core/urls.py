from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('clientes/', include('clientes.urls')),
    path('produtos/', include('produtos.urls')),
    path('pedidos/', include('pedidos.urls')),
    path('financeiro/', include('financeiro.urls')),
    path('admin/', admin.site.urls),
]