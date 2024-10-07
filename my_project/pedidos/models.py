from django.db import  models
from django.urls import reverse

class Pedido(models.Model):
    numeropedido = models.IntegerField(default=0)
    name = models.CharField(max_length=200, default=" ")
    produto = models.CharField(max_length=200, default=" ")
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    # precototal = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pedido_edit', kwargs={'pk': self.pk})