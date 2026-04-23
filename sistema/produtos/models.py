from django.db import models


class Produto(models.Model):
    CATEGORIAS = [
        ('Bolo', 'Bolo'),
        ('Doce', 'Doce'),
        ('Torta', 'Torta'),
        ('Cupcake', 'Cupcake'),
        ('Outro', 'Outro'),
    ]

    nome = models.CharField(max_length=100, verbose_name='Nome')
    recheio = models.CharField(max_length=100, blank=True, verbose_name='Recheio')
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, verbose_name='Categoria')
    preco = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Preço por KG (R$)')
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['nome']

    def __str__(self):
        return f'{self.nome} ({self.categoria})'