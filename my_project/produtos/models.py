from django.db import  models
from django.urls import reverse



class Produto(models.Model):
    name = models.CharField(max_length=200)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    categoria = models.CharField(max_length=100, default="")
    fornecedor = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('produto_edit', kwargs={'pk': self.pk})
