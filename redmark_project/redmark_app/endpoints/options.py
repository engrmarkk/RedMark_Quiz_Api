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


class PostOptionView(APIView):
    def post(self, request, question_id):
        question = Question.objects.filter(id=question_id).first()
        if not question:
            raise ValidationError({"error": "Question does not exist."})
        # question = Question.objects.get(pk=pk)
        option = Options.objects.filter(question=question).first()
        if option:
            raise ValidationError({"error": "Options to this question has already been posted."})
        serializer = OptionsSerializerQuestionID(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['question'] = question
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class EachOptionView(APIView):
    def get(self, request, pk):
        option = get_object_or_404(Options, id=pk)
        serializer = OptionsSerializerQuestionID(option)
        return Response(serializer.data)

    def put(self, request, pk):
        option = get_object_or_404(Options, id=pk)
        serializer = OptionsSerializerQuestionID(option, data=request.data, partial=True)
        if serializer.is_valid():
            if "a" in serializer.validated_data:
                option.a = serializer.validated_data["a"]
            if "b" in serializer.validated_data:
                option.b = serializer.validated_data["b"]
            if "c" in serializer.validated_data:
                option.c = serializer.validated_data["c"]
            if "d" in serializer.validated_data:
                option.d = serializer.validated_data["d"]
            if "e" in serializer.validated_data:
                option.e = serializer.validated_data["e"]

            option.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, pk):
        option = get_object_or_404(Options, id=pk)
        option.delete()
        return Response({"message": "Option deleted successfully"})
