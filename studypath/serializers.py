from rest_framework import serializers
from .models import Word, Stage, GrammarType

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ["eng_word", "spa_word", "grammar_type", "stage", "date_created"]
        
class GrammarTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrammarType
        fields = ["type", "date_created"]