# Generated by Django 5.1.1 on 2024-10-07 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0003_pedido_numeropedido_pedido_produto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='preco_total',
            new_name='precototal',
        ),
    ]
