from django.core.management.base import BaseCommand
import os
import django
import django
import random
from vendas.models import Veiculo


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vendas.settings')
django.setup()


def criar_veiculos(n):
    fabricantes = ['Toyota', 'Ford', 'Volkswagen', 'Honda', 'Chevrolet']
    modelos = ['Corolla', 'Civic', 'Fusca', 'Onix', 'Hilux', 'Focus', 'A5', 'C4', 'X5']
    cores = ['Preto', 'Branco', 'Prata', 'Vermelho', 'Azul', 'Verde', 'Amarelo']
    tipos_combustivel = ['Gasolina', 'Diesel', 'Etanol', 'Elétrico', 'Híbrido']
    
    for _ in range(n):
        modelo = random.choice(modelos)
        fabricante = random.choice(fabricantes)
        ano_fabricacao = random.randint(2000, 2023)
        ano_modelo = ano_fabricacao  # ou um ano aleatório entre 2000 e 2023
        placa = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=7)).upper()
        valor = round(random.uniform(20000, 200000), 2)  # Valor entre 20.000 e 200.000
        cor = random.choice(cores)
        tipo_combustivel = random.choice(tipos_combustivel)
        quilometragem = random.randint(0, 200000)  # Quilometragem entre 0 e 200.000 km
        chassi = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=17)).upper()
        categoria = random.choice([choice[0] for choice in Veiculo.MODELO_CHOICES])  # Escolher aleatoriamente da categoria

        veiculo = Veiculo(
            modelo=modelo,
            fabricante=fabricante,
            ano_fabricacao=ano_fabricacao,
            ano_modelo=ano_modelo,
            placa=placa,
            valor=valor,
            cor=cor,
            tipo_combustivel=tipo_combustivel,
            quilometragem=quilometragem,
            chassi=chassi,
            categoria=categoria
        )
        
        veiculo.save()
        print(f"Veículo {modelo} {fabricante} adicionado com sucesso.")

class Command(BaseCommand):
    help = 'Popula a tabela de vendedores com dados fake'

    def handle(self, *args, **kwargs):
        criar_veiculos(100)