import atracoes
from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avalicao

class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    cometarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avalicao)

    def __str__(self) -> str:
        return self.nome