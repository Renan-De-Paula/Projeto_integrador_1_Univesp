from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    telefone = models.CharField(max_length=20, verbose_name='Telefone')
    email = models.EmailField(verbose_name='E-mail')
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name='Cadastrado em')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nome']

    def __str__(self):
        return self.nome