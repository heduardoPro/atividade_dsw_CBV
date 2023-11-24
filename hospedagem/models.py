from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    
class Quarto(models.Model):
    apartamento = models.IntegerField()
    valor = models.FloatField()

    def __str__(self):
        return str(self.apartamento)
    
class Hospedagem(models.Model):
    data_entrada = models.DateField()
    data_saida = models.DateField()
    valor = models.FloatField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.cliente} - {self.quarto}'
    
class Consumo(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    valor = models.FloatField()
    hospedagem = models.ForeignKey(Hospedagem, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome