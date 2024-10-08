from django.urls import path
from . import views

urlpatterns = [
    path('', views.cliente_list, name='cliente_list'),
    path('view/<int:pk>', views.cliente_view, name='cliente_view'),
    path('new', views.cliente_create, name='cliente_new'),
    path('detail/<int:pk>', views.cliente_view, name='cliente_detail'),
    path('edit/<int:pk>', views.cliente_update, name='cliente_edit'),
    path('delete/<int:pk>', views.cliente_delete, name='cliente_delete'),
]