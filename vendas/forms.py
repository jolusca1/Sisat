from django import forms
from .models import Venda, Vendedor, Veiculo
import re


class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['vendedor', 'veiculo', 'quantidade', 'data_venda', 'concluida', 'observacoes']
        labels = {
            'vendedor': 'Selecione o Vendedor',
            'veiculo': 'Selecione o Veículo',
            'quantidade': 'Quantidade',
            'data_venda': 'Data da Venda',
            'concluida': 'Venda Concluída?',
            'observacoes': 'Observações (opcional)',
        }
        widgets = {
            'vendedor': forms.Select(attrs={'class': 'form-control'}),
            'veiculo': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Digite a quantidade',
                'min': '1'  # Para garantir que o usuário insira pelo menos 1
            }),
            'data_venda': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Selecione a data da venda',
                'type': 'date'  # Isso garante um seletor de data no HTML5
            }),
            'concluida': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'observacoes': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Observações sobre a venda (opcional)',
                'rows': 3  # Para tornar o campo de observações mais amigável
            }),
        }
        
class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = ['nome', 'cpf', 'email', 'telefone', 'data_contratacao', 'endereco', 'ativo']
        labels = {
            'nome': "Nome do vendedor",
            'cpf': "CPF",
            'email': "E-mail",
            'telefone': "Telefone",
            'data_contratacao': "Data de contratação (admissão)",
            'endereco': "Endereço",
            'ativo': 'Ativo?'
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o CPF'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite o e-mail'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o telefone'}),
            'data_contratacao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o endereço'}),
            'ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        
    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        cpf = re.sub(r'\D', '', cpf)

        if len(cpf) != 11:
            raise forms.ValidationError("Digite um CPF válido.")

        return cpf
        
class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = [
            'modelo', 'fabricante', 'ano_fabricacao', 'ano_modelo', 'placa', 
            'valor', 'cor', 'tipo_combustivel', 'quilometragem', 'chassi', 'categoria'
        ]
        labels = {
            'modelo': "Modelo do veículo",
            'fabricante': "Fabricante",
            'ano_fabricacao': "Ano de fabricação",
            'ano_modelo': "Ano do modelo",
            'placa': "Placa",
            'valor': "Valor do veículo",
            'cor': "Cor do veículo",
            'tipo_combustivel': "Tipo de combustível",
            'quilometragem': "Quilometragem",
            'chassi': "Chassi",
            'categoria': "Categoria do veículo"
        }
        widgets = {
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o modelo'}),
            'fabricante': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite a fabricante'}),
            'ano_fabricacao': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ano de Fabricação'}),
            'ano_modelo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ano do Modelo'}),
            'placa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite a placa'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite o valor'}),
            'cor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite a cor'}),
            'tipo_combustivel': forms.Select(attrs={'class': 'form-control'}),
            'quilometragem': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite a quilometragem'}),
            'chassi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o número do chassi'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }
        