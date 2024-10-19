from django.shortcuts import render, redirect
from django.db.models import Sum, F, FloatField
from .models import Vendedor, Veiculo, Venda
from .forms import VendaForm


def index(request):
    return render(request, 'vendas/index.html')

def list_vendedores(request):
    vendedores = Vendedor.objects.all()
    return render(request, 'vendas/list_vendedores.html', {'vendedores': vendedores})

def list_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'vendas/list_carros.html', {'veiculos': veiculos})

def list_vendas(request):
    vendas = Venda.objects.select_related('vendedor', 'carro').all()
    return render(request, 'vendas/list_vendas.html', {'vendas': vendas})

def add_venda(request):
    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendas:list_vendas')
    else:
        form = VendaForm()
    return render(request, 'vendas/add_venda.html', {'form': form})
        