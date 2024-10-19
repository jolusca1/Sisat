from django import forms
from .models import Venda, Vendedor, Veiculo
import re


class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['vendedor', 'veiculo', 'quantidade', 'data_venda']
        widgets = {
            'vendedor': forms.Select(attrs={'class': 'form-control'}),
            'veiculo': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'data_venda': forms.DateInput(attrs={'class': 'form-control'}),
        }
        
class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = ['nome', 'cpf', 'email', 'telefone', 'data_contratacao', 'endereco', 'ativo']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o CPF'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite o e-mail'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o telefone'}),
            'data_contratacao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o endereço'}),
            'ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        
class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['modelo', 'fabricante', 'valor']
        widgets = {
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'fabricante': forms.TextInput(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        
    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        cpf = re.sub(r'\D', '', cpf)

        if len(cpf) != 11:
            raise forms.ValidationError("Digite um CPF válido.")

        return cpf