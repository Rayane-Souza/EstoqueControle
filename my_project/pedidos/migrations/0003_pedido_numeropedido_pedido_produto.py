# Generated by Django 5.1.1 on 2024-10-07 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_remove_pedido_cliente_remove_pedido_data_pedido_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='numeropedido',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pedido',
            name='produto',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]
