from rest_framework import serializers
from .models import *


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'answer',)


class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = ('id', 'a', 'b', 'c', 'd', 'e')


class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(read_only=True, source='question_answers.answer')
    options = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ("id", "question_text", "answer", "options")

    def get_options(self, obj):
        options = Options.objects.filter(question=obj).first()
        if not options:
            return {}
        return {
            'a': options.a,
            'b': options.b,
            'c': options.c,
            'd': options.d,
            'e': options.e
        }


class OptionsSerializerQuestionID(serializers.ModelSerializer):
    # question_id = serializers.ReadOnlyField(source='question.id')

    class Meta:
        model = Options
        fields = ('id', 'question_id', 'a', 'b', 'c', 'd', 'e')


# users serializers
class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150, required=True)
    email = serializers.EmailField(max_length=254, required=True)
    first_name = serializers.CharField(max_length=150, required=True)
    last_name = serializers.CharField(max_length=150, required=True)
    password = serializers.CharField(max_length=128, write_only=True)
    scores = serializers.CharField(source='userprofile.scores', read_only=True)
    taken = serializers.CharField(source='userprofile.taken', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name',
                  'scores', 'taken',
                  )

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
