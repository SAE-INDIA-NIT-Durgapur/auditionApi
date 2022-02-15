from rest_framework import serializers
from .models import Question,Answer
from register.models import Profile

class answerSerializer(serializers.ModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(),many=False)
    class Meta:
        model=Answer
        fields=('question','profile','answer_text')


class questionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields='__all__'


