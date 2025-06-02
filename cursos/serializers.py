from rest_framework import serializers
from django.db.models import Avg
from .models import Curso, Avaliacao

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = '__all__'


    def validate_avaliacao(self,valor):
        if valor in range (1,6):
            return valor
        else:
            raise serializers.ValidationError('A avaliação precisa ser entre 1 e 5')



class CursoSerializer(serializers.ModelSerializer):
    #avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    #avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')
    #avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #media_avaliacoes = serializers.SerializerMethodField()
    
    class Meta:
        model = Curso
        fields = '__all__'


    '''
    def get_media_avaliacoes(self,obj):
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')

        if media is None:
            return 0
        return round(media * 2) / 2
    '''