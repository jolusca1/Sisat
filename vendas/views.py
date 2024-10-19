from django.shortcuts import render, redirect
from django.db.models import Sum, F, FloatField
from django.contrib import messages
from .models import Vendedor, Veiculo, Venda
from .forms import VendaForm, VendedorForm, VeiculoForm


def index(request):
    return render(request, 'vendas/index.html')

def list_vendedores(request):
    vendedores = Vendedor.objects.all()
    return render(request, 'vendas/list_vendedores.html', {'vendedores': vendedores})

def add_vendedor(request):
    if request.method == 'POST':
        form = VendedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vendedor adicionado com sucesso!')
            return redirect('vendas:list_vendedores')
    else:
        form = VendedorForm()
    return render(request, 'vendas/add_vendedor.html', {'form': form})
        

def list_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'vendas/list_veiculos.html', {'veiculos': veiculos})

def add_veiculo(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Veículo adicionado com sucesso!')
            return redirect('vendas:list_veiculos')
    else:
        form = VeiculoForm()
    return render(request, 'vendas/add_veiculo.html', {'form': form})
        

def list_vendas(request):
    vendas = Venda.objects.select_related('vendedor', 'veiculo').all()
    return render(request, 'vendas/list_vendas.html', {'vendas': vendas})

def add_venda(request):
    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Venda adicionada com sucesso!')
            return redirect('vendas:list_vendas')
    else:
        form = VendaForm()
    return render(request, 'vendas/add_venda.html', {'form': form})
        