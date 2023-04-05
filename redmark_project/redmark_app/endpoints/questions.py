from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Question
from ..serializers import QuestionSerializer


class QuestionView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Question.objects.all()
        serializer = QuestionSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class EachQuestionView(APIView):
    def get(self, request, pk):
        qs = get_object_or_404(Question, id=pk)
        serializer = QuestionSerializer(qs)
        return Response(serializer.data)

    def put(self, request, pk):
        qs = get_object_or_404(Question, id=pk)
        # this takes the question object and the data from the request and updates the question object
        serializer = QuestionSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        qs = get_object_or_404(Question, id=pk)
        qs.delete()
        return Response({"message": "Question deleted successfully"})
