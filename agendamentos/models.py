from django.db import models


class Agendamento(models.Model):
    nome_cliente = models.CharField(max_length=100)
    data = models.DateField()
    horario = models.TimeField()
    servico = models.CharField(max_length=100)

    class Meta:
         constraints = [
              models.UniqueConstraint(
                   fields=["data", "horario"],
                   name="agendamento_data_horario_unico",
              )
         ]

    def __str__(self):
        return (
            f"{self.nome_cliente} - "
            f"{self.data} - "
            f"{self.horario} - "
            f"{self.servico}"
        )