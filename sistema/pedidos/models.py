from django.db import models
from decimal import Decimal


class Pedido(models.Model):
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Entregue', 'Entregue'),
        ('Cancelado', 'Cancelado'),
    ]

    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE)
    produto = models.ForeignKey('produtos.Produto', on_delete=models.CASCADE)
    kg = models.FloatField()
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pendente')
    criado_em = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Converte kg para Decimal antes de multiplicar
        self.valor = self.produto.preco * Decimal(str(self.kg))
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Pedido #{self.id} - {self.cliente} - {self.produto}'