from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('', views.home, name='home'),
    path('excluir/<int:pk>/', views.excluir, name='excluir'),
    path('editar/<int:pk>/', views.editar, name='editar'),
]