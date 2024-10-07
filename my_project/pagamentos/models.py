from django.db import models
from django.urls import reverse

class Pagamento(models.Model):
    numeropedido = models.IntegerField(default=0)
    metodo = models.CharField(max_length=30, default=" ")

    def __str__(self):
        return f"Pedido {self.numeropedido} - Pagamento {self.metodo.strip()}"

    def get_absolute_url(self):
        return reverse('pagamento_edit', kwargs={'pk': self.pk})
