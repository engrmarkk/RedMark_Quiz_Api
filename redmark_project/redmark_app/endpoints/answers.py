from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Answer, Question
from ..serializers import AnswerSerializer
from rest_framework.exceptions import ValidationError


class AnswerView(APIView):
    def get(self, request, *args, **kwargs):
        answer = Answer.objects.all()
        serializer = AnswerSerializer(answer, many=True)
        return Response(serializer.data)


class PostAnswerView(APIView):
    def post(self, request, pk):
        question = Question.objects.get(pk=pk)
        if not question:
            raise ValidationError({"error": "Question does not exist."})
        answer = Answer.objects.filter(question=question).first()
        if answer:
            raise ValidationError({"error": "Answer for this question has already been uploaded"})
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['question'] = question
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
