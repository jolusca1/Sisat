from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator


from django.core.validators import RegexValidator
from django.db import models

class Vendedor(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(
        max_length=11, 
        unique=True, 
        validators=[RegexValidator(r'^\d{11}$', 'Digite um CPF válido com 11 dígitos.')]
    )
    email = models.EmailField(max_length=255, unique=True)
    telefone = models.CharField(
        max_length=15, 
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', 'Digite um número de telefone válido.')]
    )
    data_contratacao = models.DateField()
    endereco = models.CharField(max_length=255, null=True, blank=True)
    ativo = models.BooleanField(default=True)
    
    def clean(self):
        """Remove qualquer pontuação do CPF antes de salvar."""
        self.cpf = self.cpf.replace('.', '').replace('-', '')

    def __str__(self):
        return f"{self.nome} ({self.cpf})"


class Veiculo(models.Model):
    MODELO_CHOICES = [
        ('Sedan', 'Sedan'),
        ('Hatch', 'Hatch'),
        ('SUV', 'SUV'),
        ('Caminhão', 'Caminhão'),
        ('Moto', 'Moto'),
    ]

    modelo = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    ano_fabricacao = models.PositiveIntegerField()
    ano_modelo = models.PositiveIntegerField()
    placa = models.CharField(max_length=7, unique=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2) 
    cor = models.CharField(max_length=50, null=True, blank=True)
    tipo_combustivel = models.CharField(max_length=20, choices=[('Gasolina', 'Gasolina'), ('Diesel', 'Diesel'), ('Etanol', 'Etanol'), ('Elétrico', 'Elétrico'), ('Híbrido', 'Híbrido')])
    quilometragem = models.PositiveIntegerField(default=0)
    chassi = models.CharField(max_length=17, unique=True)
    categoria = models.CharField(max_length=20, choices=MODELO_CHOICES, null=True, blank=True)

    def __str__(self):
        return f"{self.fabricante} {self.modelo} - {self.placa} ({self.ano_modelo})"


from django.db import models
from django.core.validators import MinValueValidator


class Venda(models.Model):
    vendedor = models.ForeignKey('Vendedor', on_delete=models.CASCADE)
    veiculo = models.ForeignKey('Veiculo', on_delete=models.CASCADE)
    data_venda = models.DateField()
    quantidade = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    concluida = models.BooleanField(default=True)
    observacoes = models.TextField(null=True, blank=True)

    @property
    def valor_total(self):
        return self.quantidade * self.valor_unitario
    
    def save(self, *args, **kwargs):
        self.valor_unitario = self.veiculo.valor
        super(Venda, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.vendedor.nome} - {self.veiculo.modelo} - {self.data_venda}"
