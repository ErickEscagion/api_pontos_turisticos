from rest_framework.serializers import ModelSerializer
from avaliacoes.models import Avalicao

class AvalicaoSerializer(ModelSerializer):
    class Meta:
        model = Avalicao
        fields = ('user','comentario','nota','data')