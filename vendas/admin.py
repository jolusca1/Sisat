from django.contrib import admin
from .models import Venda, Vendedor, Veiculo


@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    
@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('id', 'modelo', 'valor')
    
@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ('id', 'vendedor', 'veiculo', 'quantidade', 'data_venda', 'valor_total')
    list_filter = ('data_venda', 'vendedor')
    search_fields = ('vendedor__nome', 'carro__modelo')