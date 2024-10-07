from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
     path('produtos/', include('produtos.urls')),
     path('clientes/', include('clientes.urls')),
     path('pedidos/', include('pedidos.urls')),
     path('pagamentos/', include('pagamentos.urls')),
]
