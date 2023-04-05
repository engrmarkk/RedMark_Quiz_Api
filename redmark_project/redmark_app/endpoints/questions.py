from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Question
from ..serializers import QuestionSerializer


class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        return Response("Hello, world. You're at the polls index.")


class QuestionView(APIView):

    def get(self, request, *args, **kwargs):
        qs = Question.objects.all()
        # question = qs.first()
        serializer = QuestionSerializer(qs, many=True)
        # if not question:
        #     return Response("No questions found")
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
