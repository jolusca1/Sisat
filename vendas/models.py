from django.db import models


class Vendedor(models.Model):
    nome = models.CharField(max_length=150)
    
    def __str__(self):
        return self.nome
    
class Veiculo(models.Model):
    modelo = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.modelo

class Venda(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    data_venda = models.DateField(auto_now_add=True)
    quantidade = models.PositiveIntegerField(default=1)
    
    @property
    def valor_total(self):
        return self.quantidade * self.carro.valor
    
    def __str__(self):
        return f"{self.vendedor.nome} - {self.carro.modelo} - {self.data_venda}"