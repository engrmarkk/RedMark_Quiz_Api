from ...models import UserProfile, User
from ...serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist


class GetUsers(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class EachUser(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response({"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            if "username" in serializer.validated_data:
                user.username = serializer.validated_data["username"]
            if "email" in serializer.validated_data:
                user.email = serializer.validated_data["email"]
            if "password" in serializer.validated_data:
                user.password = serializer.validated_data["password"]
            user.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        user = User.objects.get(id=pk)
        user.delete()
        return Response({"message": "User deleted successfully"})
