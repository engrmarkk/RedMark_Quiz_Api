from ...models import User, UserProfile
from ...serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from ...utils import validate_email


class RegisterView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['email'] = serializer.validated_data['email'].lower()
            serializer.validated_data['username'] = serializer.validated_data['username'].lower()
            serializer.validated_data['first_name'] = serializer.validated_data['first_name'].lower()
            serializer.validated_data['last_name'] = serializer.validated_data['last_name'].lower()
            if not validate_email(serializer.validated_data['email']):
                return Response({"message": "Invalid email"}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            UserProfile.objects.create(user=User.objects.get(email=serializer.validated_data['email']))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        request.data['email'] = request.data['email'].lower()
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key,
                         'email': user.email
                         })
