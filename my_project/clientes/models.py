from django.db import  models
from django.urls import reverse



class Cliente(models.Model):
    name = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20, default="")
    email = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cliente_edit', kwargs={'pk': self.pk})
