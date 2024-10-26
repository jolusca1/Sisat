from django.shortcuts import render, redirect
from django.db.models import Sum, F, FloatField
from django.contrib import messages
from .models import Vendedor, Veiculo, Venda
from .forms import VendaForm, VendedorForm, VeiculoForm
import pdb


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

    # Capturando os filtros da requisição
    fabricante = request.GET.get('fabricante')
    ano_fabricacao = request.GET.get('ano_fabricacao')
    tipo_combustivel = request.GET.get('tipo_combustivel')

    if fabricante:
        veiculos = veiculos.filter(fabricante__icontains=fabricante)
    
    if ano_fabricacao:
        veiculos = veiculos.filter(ano_fabricacao=ano_fabricacao)
    
    if tipo_combustivel:
        veiculos = veiculos.filter(tipo_combustivel=tipo_combustivel)

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
    vendas = Venda.objects.all()
    vendedores = Vendedor.objects.all()

    # Capturando os parâmetros de filtro
    vendedor = request.GET.get('vendedor')
    veiculo = request.GET.get('veiculo')
    data_venda = request.GET.get('data_venda')
    valor_min = request.GET.get('valor_min')
    valor_max = request.GET.get('valor_max')

    # Aplicando os filtros, se fornecidos
    if vendedor:
        vendas = vendas.filter(vendedor__id=vendedor)
    
    if veiculo:
        vendas = vendas.filter(veiculo__modelo__icontains=veiculo)

    if data_venda:
        vendas = vendas.filter(data_venda=data_venda)

    if valor_min:
        vendas = vendas.filter(valor_total__gte=valor_min)

    if valor_max:
        vendas = vendas.filter(valor_total__lte=valor_max)

    return render(request, 'vendas/list_vendas.html', {'vendas': vendas, 'vendedores': vendedores})

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
        