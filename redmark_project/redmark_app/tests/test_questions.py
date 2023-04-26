from ..models import Question
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from ..models import User, UserProfile


class QuestionTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser",
                                             first_name="testfirstname",
                                             last_name="testlastname",
                                             email="test@email.com",
                                             password="testpassword")
        UserProfile.objects.create(user=self.user)
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_all_questions(self):
        url = reverse('question')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
