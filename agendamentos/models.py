from django.db import models

class Agendamento(models.Model):
    nome_cliente = models.CharField(max_length=100)
    data = models.DateField()
    horario = models.TimeField()
    servico = models.CharField(max_length=100)

    class Meta:
        unique_together = ('data' , 'horario')

    def __str__(self):
       return f"{self.nome_cliente} - {self.data} - {self.horario} - {self.servico}"