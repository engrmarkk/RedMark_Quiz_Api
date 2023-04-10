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
    class Meta:
        model = UserProfile
        fields = ('id', 'first_name', 'last_name', 'email', 'password')
        # this is to make sure that the password is not returned in the response
        extra_kwargs = {'password': {'write_only': True}}

    # this is to make sure that the password is hashed
    # when a user is created
    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user
