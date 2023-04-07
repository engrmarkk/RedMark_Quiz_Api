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
    def post(self, request, question_id):
        question = Question.objects.get(id=question_id)
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


class EachAnswerView(APIView):
    def get(self, pk):
        answer = get_object_or_404(Answer, id=pk)
        question = Question.objects.filter(question_text=answer.question).first()
        return Response(
            {
                "id": answer.id,
                "answer": answer.answer,
                "question": question.question_text
            }
        )

    def put(self, request, pk):
        answer = get_object_or_404(Answer, id=pk)
        serializer = AnswerSerializer(answer, data=request.data, partial=True)
        if serializer.is_valid():
            if "answer" in serializer.validated_data:
                answer.answer = serializer.validated_data["answer"]
            answer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, pk):
        answer = get_object_or_404(Answer, id=pk)
        answer.delete()
        return Response({"message": "Answer deleted successfully"})
