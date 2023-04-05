from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Question


class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        return Response("Hello, world. You're at the polls index.")

class QuestionView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Question.objects.all()
        question = qs.first()
        return Response(question)
