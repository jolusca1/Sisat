from django.core.management.base import BaseCommand
import os
import django
from faker import Faker
from random import choice
from vendas.models import Vendedor


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'seu_projeto.settings')
django.setup()

def criar_vendedores(n):
    fake = Faker('pt_BR')
    for _ in range(n):
        nome = fake.name()
        cpf = fake.unique.random_int(min=10000000000, max=99999999999)
        email = fake.unique.email()
        telefone = fake.phone_number()
        data_contratacao = fake.date_this_decade()
        endereco = fake.address()
        ativo = choice([True, False])

        vendedor = Vendedor(
            nome=nome,
            cpf=str(cpf),
            email=email,
            telefone=telefone,
            data_contratacao=data_contratacao,
            endereco=endereco,
            ativo=ativo
        )
        vendedor.save()
        print(f'Vendedor {nome} adicionado.')


class Command(BaseCommand):
    help = 'Popula a tabela de vendedores com dados fake'

    def handle(self, *args, **kwargs):
        criar_vendedores(100)  # Altere o número para quantos vendedores deseja adicionar
