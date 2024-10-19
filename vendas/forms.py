from django import forms
from .models import Venda, Vendedor, Veiculo


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
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'})
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