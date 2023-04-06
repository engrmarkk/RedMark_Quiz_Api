from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Options, Question
from ..serializers import OptionsSerializerQuestionID


class OptionView(APIView):
    def get(self, request, *args, **kwargs):
        option = Options.objects.all()
        serializer = OptionsSerializerQuestionID(option, many=True)
        return Response(serializer.data)


class EachOptionView(APIView):
    def post(self, request, pk):
        question = Question.objects.filter(pk=pk).first()
        if not question:
            raise ValidationError({"error": "Question does not exist."})
        # question = Question.objects.get(pk=pk)
        option = Options.objects.filter(question=question).first()
        if option:
            raise ValidationError({"error": "Option already exists."})
        serializer = OptionsSerializerQuestionID(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['question'] = question
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
