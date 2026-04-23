from django.urls import path
from . import views

app_name = 'pedidos'

urlpatterns = [
    path('', views.home, name='home'),
    path('excluir/<int:pk>/', views.excluir, name='excluir'),
    path('status/<int:pk>/', views.alterar_status, name='alterar_status'),
]