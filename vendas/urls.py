from django.urls import path
from . import views


app_name = 'vendas'

urlpatterns = [
    path('', views.index, name='index'),
    path('vendedores/', views.list_vendedores, name='list_vendedores'),
    path('vendedores/adicionar', views.add_vendedor, name='add_vendedor'),
    path('veiculos/', views.list_veiculos, name='list_veiculos'),
    path('veiculos/adicionar', views.add_veiculo, name='add_veiculo'),
    path('vendas/', views.list_vendas, name='list_vendas'),
    path('vendas/adicionar/', views.add_venda, name='add_venda'),
    # path('relatorios/', views.relatorios, name='relatorios'),
]
