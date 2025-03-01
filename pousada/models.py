# Create your models here.
from django.core.exceptions import ValidationError
from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome






class Comodo(models.Model):
    numero = models.CharField(max_length=10)
    tipo = models.CharField(max_length=50)
    descricao = models.TextField(blank=True)
    preco_diaria = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=10, choices=[('livre', 'Livre'), ('ocupado', 'Ocupado'), ('manutencao', 'Em manutenção')])

    def __str__(self):
        return f"{self.numero} - {self.tipo}"

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    comodo = models.ForeignKey(Comodo, on_delete=models.CASCADE)
    data_entrada = models.DateField()
    data_saida = models.DateField()
    status = models.CharField(max_length=20, choices=[('confirmada', 'Confirmada'), ('cancelada', 'Cancelada')])


    def clean(self):
        """
        Valida que a data de saída seja posterior à data de entrada.
        """
        if self.data_saida <= self.data_entrada:
            raise ValidationError("A data de saída deve ser posterior à data de entrada.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Reserva de {self.cliente.nome} no cômodo {self.comodo.numero}"


