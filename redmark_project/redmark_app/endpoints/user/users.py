from ...models import UserProfile
from ...serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class GetUsers(APIView):
    def get(self, request, *args, **kwargs):
        users = UserProfile.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class EachUser(APIView):
    def get(self, request, pk):
        user = UserProfile.objects.get(id=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = UserProfile.objects.get(id=pk)
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
        user = UserProfile.objects.get(id=pk)
        user.delete()
        return Response({"message": "User deleted successfully"})
