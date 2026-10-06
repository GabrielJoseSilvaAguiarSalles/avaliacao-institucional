from django.db import models

class Avaliacoes(models.Model):
    nome = models.CharField(max_length=100)
    nota = models.CharField(max_length=4)

    def __str__(self):
        return self.nome