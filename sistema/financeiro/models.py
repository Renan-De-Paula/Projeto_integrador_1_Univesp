from django.db import models

# O app Financeiro não possui model próprio.
# Ele lê os dados diretamente do model Pedido (app pedidos).
# Toda lógica financeira é calculada na view financeiro/views.py.