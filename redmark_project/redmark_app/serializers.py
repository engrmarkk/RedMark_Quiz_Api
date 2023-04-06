from rest_framework import serializers
from .models import *


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('answer',)


class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = ('id', 'a', 'b', 'c', 'd', 'e')


class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(read_only=True, source='answer.answer')
    options = OptionsSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ("id", "question_text", "answer", "options")
