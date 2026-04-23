from django.db import models
from clientes.models import Cliente
from produtos.models import Produto


class Pedido(models.Model):
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Entregue', 'Entregue'),
        ('Cancelado', 'Cancelado'),
    ]

    # Relacionamento com Cliente (FK)
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        verbose_name='Cliente',
        related_name='pedidos',
    )

    # Relacionamento com Produto (FK)
    produto = models.ForeignKey(
        Produto,
        on_delete=models.PROTECT,
        verbose_name='Produto',
        related_name='pedidos',
    )

    kg = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Quantidade (KG)')
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor Total (R$)')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Pendente', verbose_name='Status')
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name='Data do Pedido')

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['-criado_em']

    def __str__(self):
        return f'Pedido #{self.pk} - {self.cliente.nome} ({self.status})'

    def save(self, *args, **kwargs):
        """Calcula automaticamente o valor total ao salvar."""
        self.valor = self.produto.preco * self.kg
        super().save(*args, **kwargs)