from rest_framework import serializers

from .models import *

# class CorpusSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Corpus
#         fields = ('name',)

# class CsrfSerializ(serializers.Serializer):
#     csrf = 


class AuditorSerializer(serializers.ModelSerializer):
    corpus = serializers.CharField(source="corpus.name")
    class Meta:
        model = Auditor
        fields = ('__all__')


class BronSerializer(serializers.ModelSerializer):
    auditor = AuditorSerializer()
    # csrf = CsrfSerializ()
    class Meta:
        model = Bron
        fields = ('__all__')


