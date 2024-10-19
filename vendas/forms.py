from django import forms
from .models import Venda


class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['vendedor', 'veiculo', 'quantidade']
        widgets = {
            'vendedor': forms.Select(attrs={'class': 'form-control'}),
            'veiculo': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
        }