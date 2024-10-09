from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
     path('admin/', admin.site.urls),
     path('clientes/', include('clientes.urls')),
     path('pedidos/', include('pedidos.urls')),
     path('pagamentos/', include('pagamentos.urls')),
     path('produtos/', include('produtos.urls')),
     path('', lambda request: redirect('produto_list'))
]
